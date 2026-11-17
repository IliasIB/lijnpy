# lijnpy

[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![Tests](https://github.com/IliasIB/lijnpy/actions/workflows/main.yml/badge.svg)](https://github.com/IliasIB/lijnpy/actions/workflows/main.yml)
[![Documentation](https://github.com/IliasIB/lijnpy/actions/workflows/docs.yml/badge.svg)](https://iliasib.github.io/lijnpy/)
[![PyPI - Version](https://img.shields.io/pypi/v/lijnpy)](https://pypi.org/project/lijnpy/)

lijnpy is een asynchrone Python-wrapper voor de [open data API van De Lijn](https://data.delijn.be). Alle aanroepen zijn coroutines en geven gevalideerde [pydantic](https://docs.pydantic.dev)-modellen terug.

## Functies

- Entiteiten, gemeenten, vervoerregio's en lijnkleuren opvragen.
- Haltes en lijnen opvragen per entiteit of per gemeente, en haltes in de buurt van een coördinaat zoeken.
- Alle lijnen opvragen, en per lijn de details, kleuren, richtingen en gemeenten.
- Per halte de details, richtingen, dienstregeling, real-time doorkomsten, omleidingen en storingen opvragen.

Niet alle endpoints van de API worden al ondersteund (bijvoorbeeld de dienstregeling en haltes per lijnrichting, en `omleidingen` en `storingen` als zelfstandige lijsten). Zie de [issues](https://github.com/IliasIB/lijnpy/issues) voor wat nog ontbreekt.

## Installatie

```sh
pip install lijnpy
```

Vereist Python 3.12 of hoger.

## API-sleutel

De API heeft een sleutel nodig. Maak een account aan op het [open data-portaal van De Lijn](https://data.delijn.be), abonneer je op de Kern Open Data Services en kopieer je sleutel. Zet hem niet in je code of in git, maar bijvoorbeeld in een omgevingsvariabele:

```sh
export DELIJN_API_KEY="<jouw sleutel>"
```

De bibliotheek leest die variabele niet zelf: je geeft de sleutel altijd expliciet mee aan de client via `api_key` (zie hieronder). `DELIJN_API_KEY` is de naam die ook de tests en de scripts in deze repository gebruiken.

## Gebruik

```python
import asyncio
import os

from lijnpy import KODSClientV1


async def main():
    async with KODSClientV1(api_key=os.environ["DELIJN_API_KEY"]) as client:
        # Antwerpen Groenplaats: entiteit 1, halte 102675
        stop = await client.get_stop(1, 102675)
        print(stop.description_long)

        timetable = await client.get_real_time_timetable(1, 102675)
        print(f"{len(timetable.passages)} komende doorkomsten")


asyncio.run(main())
```

- Veel methodes hebben optionele argumenten voor de query-parameters van de API, bijvoorbeeld `get_timetable(1, 102675, day=date(2026, 11, 20))` of `get_stops_in_vicinity(locatie, radius=500, max_stops=10)`. Een `datetime` moet zonder tijdzone zijn, in Belgische lokale tijd.
- `KODSClientV1` en `DeLijnAPIException` importeer je rechtstreeks uit `lijnpy`. Modellen en enums staan in `lijnpy.models` en `lijnpy.enums`.
- De client houdt één HTTP-sessie open. Gebruik `async with` of roep `await client.close()` aan als je klaar bent.
- Een client hoort bij één event loop: gebruik hem niet over meerdere `asyncio.run`-aanroepen heen.
- Fouten van de API (een statuscode buiten 200-299, ongeldige JSON, een verbindingsfout of een antwoord dat niet bij de modellen past) geven een `DeLijnAPIException`.

## Documentatie

De volledige API-documentatie staat op <https://iliasib.github.io/lijnpy/lijnpy.html>. Wijzigingen per versie staan in de [CHANGELOG](CHANGELOG.md).

## Bijdragen

Hoe je de tests draait en de testdata vernieuwt staat in [tests/README.md](tests/README.md), hoe een release werkt in [RELEASING.md](RELEASING.md), en de OpenAPI-specificatie van De Lijn (met de verschillen met de echte API) staat in [docs/openapi/](docs/openapi/README.md).

## Licentie

MIT
