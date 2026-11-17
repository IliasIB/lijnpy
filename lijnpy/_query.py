"""Formatting of optional query parameters for the De Lijn API."""

from datetime import date, datetime

# The API takes local (Belgian) wall-clock time without a UTC offset
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"


def format_datetime(value: datetime | date | None) -> str | None:
    """Format a moment as `yyyy-MM-dd'T'HH:mm:ss`; a plain date means midnight.

    Raises:
        ValueError: If the datetime has a time zone; pass local Belgian time
            without one, as the API does not accept an offset.
    """
    if value is None:
        return None
    if isinstance(value, datetime):
        if value.tzinfo is not None:
            raise ValueError(
                "Pass a naive datetime in local Belgian time: the API does not "
                "accept a UTC offset"
            )
        return value.strftime(DATETIME_FORMAT)
    return datetime(value.year, value.month, value.day).strftime(DATETIME_FORMAT)


def format_date(value: date | None) -> str | None:
    """Format a day as `yyyy-MM-dd` (the time of a datetime is dropped)."""
    return None if value is None else value.strftime(DATE_FORMAT)


def format_bool(value: bool | None) -> str | None:
    """Format a boolean the way the API expects it: `true` or `false`."""
    return None if value is None else str(value).lower()


def format_int(value: int | None) -> str | None:
    return None if value is None else str(value)
