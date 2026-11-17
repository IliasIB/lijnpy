"""Record live API responses into tests/inputs/kods_client/v1/.

Usage (from the repo root):
    DELIJN_API_KEY=... uv run python tests/record_fixtures.py [METHOD ...]

Without arguments every method is recorded; name methods (for example
`get_line`) to record only those, which keeps the diff small when you add an
endpoint.

Every KODSClientV1 method is called once. The raw JSON the API returns is
written to a fixture file, with every list cut down to MAX_ITEMS entries so the
fixtures stay small. The API key is only read from the environment and is never
written to disk (the API does not echo it back in its responses).
"""

import asyncio
import json
import logging
import sys
from pathlib import Path

from live_calls import API_KEY_VARIABLE, get_api_key, get_calls

from lijnpy._rest_adapter import Result
from lijnpy.kods_client_v1 import KODSClientV1

FIXTURE_DIRECTORY = Path(__file__).parent / "inputs" / "kods_client" / "v1"
MAX_ITEMS = 5


def truncate(value):
    """Cut every list, at any depth, down to MAX_ITEMS entries."""
    if isinstance(value, list):
        return [truncate(item) for item in value[:MAX_ITEMS]]
    if isinstance(value, dict):
        return {key: truncate(item) for key, item in value.items()}
    return value


async def main() -> int:
    api_key = get_api_key()
    if api_key is None:
        sys.exit(f"Set {API_KEY_VARIABLE} to record fixtures.")

    selected = sys.argv[1:]
    client = KODSClientV1(api_key=api_key, logger=logging.getLogger("record"))
    calls = get_calls(client)
    unknown = [name for name in selected if name not in calls]
    if unknown:
        sys.exit(f"Unknown method(s): {', '.join(unknown)}")

    # Keep the raw response of each call, so it is stored exactly as the API sent it.
    responses: list[dict] = []
    original_get = client.http_client.get

    async def recording_get(*args, **kwargs) -> Result:
        result = await original_get(*args, **kwargs)
        assert result.data is not None
        responses.append(result.data)
        return result

    client.http_client.get = recording_get  # type: ignore[method-assign]

    FIXTURE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    failed = 0
    try:
        for method, (fixture, call) in calls.items():
            if selected and method not in selected:
                continue
            responses.clear()
            try:
                await call()  # also validates the response against the models
            except Exception as error:
                failed += 1
                print(f"FAIL {method}: {error!r}"[:200])
                continue
            path = FIXTURE_DIRECTORY / f"{fixture}.json"
            path.write_text(json.dumps(truncate(responses[-1]), indent=4) + "\n")
            print(f"OK   {method:32} -> {path.name}")
    finally:
        await client.close()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
