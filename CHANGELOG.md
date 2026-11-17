# Change Log

## [Unreleased]

### Changed

- The `requests` dependency is removed; it was never imported (the client uses
  `aiohttp`)
- Python 3.13, 3.14 and 3.15 are tested in CI (3.12 stays the minimum), and the
  oldest dependency versions the declared ranges allow are tested too

### Added

- Line endpoints: `get_all_lines`, `get_line`, `get_municipalities_by_line`,
  `get_line_colors`, `get_line_directions` and `get_line_direction`, all with
  the optional `valid_on` argument. New model `LineColorCodes`, and
  `Line.transport_layer` (`vervoerslaag`, `None` when the API has none).
- Optional keyword-only arguments for the query parameters of the API; leaving
  them out changes nothing:
  - `valid_on` (`geldigOp`, a `datetime` or `date`): `get_stop`, `get_stops`,
    `get_stops_by_entity`, `get_lines`, `get_lines_by_entity`, `get_directions`
  - `day` (`datum`, a `date`): `get_timetable`, `get_detours`, `get_disruptions`
  - `include_last_passage` (`inclusiefLaatsteDoorkomst`): `get_timetable`
  - `max_passages` (`maxAantalDoorkomsten`): `get_real_time_timetable`
  - `radius` and `max_stops` (`maxAantalHaltes`, at most 50): `get_stops_in_vicinity`

  A `datetime` must be naive, in local Belgian time: the API takes no UTC offset.
- `from lijnpy import KODSClientV1, DeLijnAPIException` now works
  (`lijnpy.__all__` is defined)

### Removed

- **Breaking:** `lijnpy.API_KEY`, which was never used by the library. Pass the
  key to `KODSClientV1(api_key=...)`; the README documents reading it from
  `DELIJN_API_KEY`.

## [2.0.0] - 2026-11-16

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

## [1.0.0] - 2024-07-24

### Changed

- **Breaking:** the whole API is asynchronous. The per-resource modules under
  `lijnpy.kods.api.v1` (`colors`, `entities`, `municipalities`, `stops`,
  `transport_regions`) are replaced by a single `KODSClientV1` class in
  `lijnpy.kods_client_v1` whose `get_*` methods are coroutines.
- **Breaking:** the separate list wrapper classes are removed; methods return
  plain lists of models.
- Models and enums moved to `lijnpy.models` and `lijnpy.enums`.

### Added

- `aiohttp` as a dependency
- `KODSClientV1.get_lines_by_transport_region` (removed again in the next
  release, as the endpoint does not exist)

## [0.2.1] - 2024-03-14

### Added

- Automatic releases to PyPi

## [0.2.0] - 2024-03-14

Refactored the models into one module, with clearer types.

## [0.1.0a1] - 2024-03-06

Added the municipalities, colors and transport regions endpoints.

## [0.1.0a0] - 2024-03-06

First pre-release.

[Unreleased]: https://github.com/iliasib/lijnpy/compare/2.0.0...main
[2.0.0]: https://github.com/iliasib/lijnpy/releases/tag/2.0.0
[1.0.0]: https://github.com/iliasib/lijnpy/releases/tag/1.0.0
[0.2.1]: https://github.com/iliasib/lijnpy/releases/tag/0.2.1
[0.2.0]: https://github.com/iliasib/lijnpy/releases/tag/0.2.0
[0.1.0a1]: https://github.com/iliasib/lijnpy/releases/tag/0.1.0a1
[0.1.0a0]: https://github.com/iliasib/lijnpy/releases/tag/0.1.0a0
<!-- markdownlint-configure-file { "MD022": false, "MD024": false, "MD030": false, "MD032": false, "MD053": false} -->
