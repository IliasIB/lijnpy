# Change Log

## [Unreleased]

### Changed

- **Breaking:** `Language` now matches the values the De Lijn API returns
  (`NEDERLANDS`, `FRANS`, `TWEETALIG`). The members `NL`, `FR`, `EN` and `DE`
  are replaced by `DUTCH`, `FRENCH` and `BILINGUAL`.
- `Line.transport_region_code` is now optional (`None` when the API does not
  return a region for a line).

### Added

- `OperationType.TECHNICAL`, `OperationType.CALL_BUS` and `OperationType.FLEX`
- `TransportType.METRO`, `TransportType.TRAIN` and `TransportType.ALL`

### Fixed

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
