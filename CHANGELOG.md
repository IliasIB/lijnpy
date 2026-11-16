# Change Log

## [Unreleased]

### Changed

- `RestAdapter` and `KODSClientV1` keep one `aiohttp` session for all requests
  instead of opening one per request. Close it with `await client.close()` or
  use the client as an async context manager (`async with KODSClientV1(...) as client`).
  Not closing it still works, but aiohttp warns about an unclosed session on exit.
- **Breaking:** `Language` now matches the values the De Lijn API returns
  (`NEDERLANDS`, `FRANS`, `TWEETALIG`). The members `NL`, `FR`, `EN` and `DE`
  are replaced by `DUTCH`, `FRENCH` and `BILINGUAL`.
- `Line.transport_region_code` is now optional (`None` when the API does not
  return a region for a line).

### Removed

- **Breaking:** `KODSClientV1.get_lines_by_transport_region`. The
  `/vervoerregios/{code}/lijnen` endpoint does not exist in the API and always
  returned 404.

### Added

- `OperationType.TECHNICAL`, `OperationType.CALL_BUS` and `OperationType.FLEX`
- `TransportType.METRO`, `TransportType.TRAIN` and `TransportType.ALL`

### Fixed

- API errors report the HTTP status first (`404: Not Found`), also when the
  error body is not JSON, instead of a generic "Request failed"
- Requests with query parameters no longer crash the request logging
- `KODSClientV1` uses `logging.getLogger("lijnpy.kods_client_v1")` by default, so
  it follows your logging configuration, instead of an unattached `Logger`
- A response without data raises `DeLijnAPIException` explicitly instead of
  relying on an `assert` (removed under `python -O`)
- Validation failures log one summary line (path, error count, first error)
  instead of one line per item
- Test fixtures are re-recorded from the live API and are about 70 times smaller.
  `tests/record_fixtures.py` refreshes them, and `pytest -m live` runs a smoke
  test against the real API (see `tests/README.md`)
- Stops no longer fail validation on `taal` values returned by the live API
- Lines no longer fail validation on the `FLEX` and `TECHNISCHE_LIJN` operation
  types, or when `vervoerRegioCode` is missing
- `get_real_time_timetable` calls `/real-time` instead of the removed
  `/real-time-doorkomsten` path, which returned 404

## [0.2.1] - 2024-03-14

### Added

- Automatic releases to PyPi

## [0.2.0] - 2024-03-14

Initial release

[Unreleased]: https://github.com/iliasib/lijnpy/compare/0.2.1...main
[0.2.1]: https://github.com/iliasib/lijnpy/releases/tag/0.2.1
[0.2.0]: https://github.com/iliasib/lijnpy/releases/tag/0.2.0
[0.1.0a1]: https://github.com/iliasib/lijnpy/releases/tag/0.1.0a1
[0.1.0a0]: https://github.com/iliasib/lijnpy/releases/tag/0.1.0a0
<!-- markdownlint-configure-file { "MD022": false, "MD024": false, "MD030": false, "MD032": false, "MD053": false} -->
