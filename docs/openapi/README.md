# De Lijn OpenAPI specification

`KernOpenDataServicesV1.json` is De Lijn's OpenAPI 3.0.1 definition of the
"Open Data V1 Core API" (version `v1`, base URL
`https://api.delijn.be/DLKernOpenData/api/v1`). It is kept here as a reference
while developing the client. It is committed unchanged, so a diff against a
newer download shows what De Lijn changed.

- **Obtained:** downloaded from De Lijn's open data portal
  (<https://data.delijn.be>) on 2026-11-15.
- **The live API is the source of truth, not the spec.** The spec is not fully
  accurate (see below). When they disagree, the client follows the live API and
  the fixtures in `tests/inputs/` are recorded from it.

## Differences between the spec and the live API

Checked on 2026-11-17 with `compare_with_live.py` (every GET path, once).

### Affects the client

| Where | Spec | Live API |
|---|---|---|
| `GET /kleuren` | response key `lijnkleuren` | key `kleuren` |
| `GET /haltes/indebuurt/{latlng}` | response key `punten` | key `haltes` |
| `GET /haltes/{e}/{h}/dienstregelingen` and `/real-time` | no `omleidingen` key | `omleidingen` is returned (the client's `Timetable` needs it) |
| `Lijn.vervoerRegioCode` | required | missing for 2 of 1112 lines (the client treats it as optional) |
| `Halte.taal`, `classificatie`, `bedieningsTypes` | enums are one malformed string, such as `"{NEDERLANDS,FRANS,TWEETALIG}"` | the individual values; see `lijnpy/enums.py` |
| `GET /berichten` and the four other `.../berichten` paths | documented | 404 |
| `GET /lijnen/{e}/{l}/lijnrichtingen/{richting}/rit/{ritnummer}` | documented | 404 for the trips tried (unverified: no valid trip number was found) |

### Does not affect the client (yet)

| Where | Spec | Live API |
|---|---|---|
| `GET /haltes/{e}/{h}` | has `districtCode` | not returned |
| `GET /kleuren/{code}` | only `code` and `omschrijving` | also `rgb`, `hex` and `links` |
| `GET /lijnen/{e}/{l}/lijnrichtingen/{richting}` | wrapped in `lijnLijnrichtingen` | the direction itself |
| `omleidingen` and `storingen` endpoints (also per line, per direction, and `GET /omleidingen`) | one shared schema containing both `omleidingen` and `storingen` | only the key that matches the endpoint |
| `dienstregelingen` and `real-time` endpoints | `dienstregelingNotas` | not returned |

`GET /vervoerregios/{code}/lijnen` is not in the spec either, which is why the
client method that called it was removed (it always returned 404).

## Keeping this up to date

```sh
DELIJN_API_KEY=... uv run python docs/openapi/compare_with_live.py
```

prints every path that does not return 200 or whose top-level keys differ from
the spec. Update the tables above when the output changes, and replace the JSON
file when De Lijn publishes a new definition (update the date above too).
