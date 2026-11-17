"""Compare the OpenAPI spec with the live De Lijn API.

Usage (from the repo root):
    DELIJN_API_KEY=... uv run python docs/openapi/compare_with_live.py

Calls every GET path of the spec once, with the example IDs below, and prints
the paths that do not return 200 or whose top-level JSON keys differ from the
spec. Paths without a difference are not printed. The result is the basis of
the list in README.md, which needs a manual update when this output changes.
Differences in `omleidingen`/`storingen`/`dienstregelingNotas` are expected:
the spec reuses one schema for several responses.
"""

import asyncio
import json
import os
import sys
from pathlib import Path

import aiohttp

SPEC = Path(__file__).with_name("KernOpenDataServicesV1.json")
EXAMPLES = {
    "entiteitnummer": "1",  # Antwerpen
    "gemeenteNummer": "482",
    "gemeenteNummers": "482",
    "latlng": "51.2194,4.4025",
    "haltesleutels": "1_102675",  # Antwerpen Groenplaats
    "haltenummer": "102675",
    "lijnnummer": "22",
    "lijnrichtingsleutels": "1_22_HEEN",
    "lijnsleutels": "1_22",
    "richting": "HEEN",
    "ritnummer": "7",
}

spec = json.loads(SPEC.read_text())


def resolve(reference: str) -> dict:
    node = spec
    for part in reference.lstrip("#/").split("/"):
        node = node[part]
    return node


def property_names(schema: dict) -> set[str]:
    if "$ref" in schema:
        schema = resolve(schema["$ref"])
    if schema.get("type") == "array":
        return property_names(schema["items"])
    return set(schema.get("properties", {}))


async def compare(session: aiohttp.ClientSession, path: str) -> tuple[int, str, str]:
    url = path
    for name, value in EXAMPLES.items():
        url = url.replace("{" + name + "}", value)
    url = url.replace("{code}", "TU" if path.startswith("/kleuren") else "AN")
    async with session.get(spec["servers"][0]["url"] + url) as response:
        status = response.status
        body = await response.json(content_type=None) if status == 200 else None
    schema = spec["paths"][path]["get"]["responses"]["200"]["content"]
    expected = property_names(schema["application/json"]["schema"])
    actual = set(body) if isinstance(body, dict) else set()
    detail = ""
    if status == 200 and expected != actual:
        detail = (
            f"only in spec: {sorted(expected - actual)}; "
            f"only live: {sorted(actual - expected)}"
        )
    return status, path, detail


async def main() -> None:
    key = os.environ.get("DELIJN_API_KEY")
    if not key:
        sys.exit("Set DELIJN_API_KEY.")
    async with aiohttp.ClientSession(
        headers={"Ocp-Apim-Subscription-Key": key}
    ) as session:
        for status, path, detail in await asyncio.gather(
            *(compare(session, path) for path in spec["paths"])
        ):
            if status != 200 or detail:
                print(status, path, detail)


asyncio.run(main())
