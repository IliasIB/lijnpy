# Tests

```sh
uv run pytest                       # offline tests, the same as CI
DELIJN_API_KEY=... uv run pytest -m live   # smoke test against the real API
```

Coverage of the `lijnpy` package must stay at or above 95% (`fail_under` in
`pyproject.toml`). Check it locally with:

```sh
uv run coverage run -m pytest && uv run coverage report
```

CI shows the same table in the job summary of each run.

The offline tests read the recorded responses in `inputs/kods_client/v1/`.
The live tests (`test_live.py`) call every client method once and are
deselected by default and skipped when `DELIJN_API_KEY` is not set.

## Refreshing the fixtures

When the API changes, or a client method is added, record the fixtures again:

```sh
DELIJN_API_KEY=... uv run python tests/record_fixtures.py
```

The script calls every method listed in `live_calls.py`, validates each
response against the models, and writes the raw JSON to `inputs/`, with every
list cut down to 5 entries. The key is read from the environment only; API
responses do not contain it. Review the diff before committing: recordings of
`detours` and `disruptions` depend on what is happening on the network that
day and may be empty.

Adding a client method makes `test_live_calls_cover_every_client_method` fail
until it has an entry in `live_calls.py`.
