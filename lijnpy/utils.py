def clean_halte(halte: dict) -> dict:
    """Clean the stop data

    Args:
        halte (dict): The stop data

    Returns:
        dict: The cleaned stop data
    """
    return {
        "entiteitnummer": halte["entiteitnummer"],
        "haltenummer": halte["haltenummer"],
        "omschrijving": halte["omschrijving"],
        "omschrijving_lang": halte["omschrijvingLang"],
        "taal": halte["taal"],
        "gemeentenummer": halte["gemeentenummer"],
        "omschrijving_gemeente": halte["omschrijvingGemeente"],
        "geo_coordinaat": halte["geoCoordinaat"],
        "halte_toegankelijkheden": halte["halteToegankelijkheden"],
        "hoofd_halte": halte["hoofdHalte"],
        "links": halte["links"],
    }


def clean_lijn(lijn: dict) -> dict:
    """Clean the line data

    Args:
        lijn (dict): The line data

    Returns:
        dict: The cleaned line data
    """
    return {
        "entiteitnummer": lijn["entiteitnummer"],
        "lijnnummer": lijn["lijnnummer"],
        "lijnnummer_publiek": lijn["lijnnummerPubliek"],
        "omschrijving": lijn["omschrijving"],
        "vervoer_regio_code": lijn["vervoerRegioCode"],
        "publiek": lijn["publiek"],
        "vervoertype": lijn["vervoertype"],
        "bedieningtype": lijn["bedieningtype"],
        "lijn_geldig_van": lijn["lijnGeldigVan"],
        "lijn_geldig_tot": lijn["lijnGeldigTot"],
        "links": lijn["links"],
    }
