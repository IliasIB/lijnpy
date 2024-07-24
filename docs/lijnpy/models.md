# Models

[Lijnpy Index](../README.md#lijnpy-index) / [Lijnpy](./index.md#lijnpy) / Models

> Auto-generated documentation for [lijnpy.models](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py) module.

- [Models](#models)
  - [Detour](#detour)
  - [DetourPeriod](#detourperiod)
  - [Direction](#direction)
  - [Disruption](#disruption)
  - [Entity](#entity)
  - [GeoCoordinate](#geocoordinate)
  - [Line](#line)
  - [LineColor](#linecolor)
  - [Municipality](#municipality)
  - [Passage](#passage)
  - [PassageNote](#passagenote)
  - [RealTimePassage](#realtimepassage)
  - [RealTimeStopPassage](#realtimestoppassage)
  - [RealTimeTimetable](#realtimetimetable)
  - [RideNote](#ridenote)
  - [Stop](#stop)
  - [StopInVicinity](#stopinvicinity)
  - [Timetable](#timetable)
  - [TransportRegion](#transportregion)

## Detour

[Show source in models.py:291](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L291)

A detour of a line

#### Attributes

- `title` *str* - The title of the detour
- `description` *str* - The description of the detour
- `period` *DetourPeriod* - The period of the detour
- `directions` *list[Direction]* - The directions of the detour
- `detour_reference` *int* - The reference of the detour
- `detour_days` *list[str]* - The days of the detour

#### Signature

```python
class Detour(BaseModel): ...
```



## DetourPeriod

[Show source in models.py:32](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L32)

A period of a detour of a line

#### Attributes

- `start_date` *datetime* - The start date of the period
- `end_date` *datetime, optional* - The end date of the period. Defaults to None.

#### Signature

```python
class DetourPeriod(BaseModel): ...
```



## Direction

[Show source in models.py:275](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L275)

A direction of a line

#### Attributes

- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *LineDirection* - The direction of the line
- `description` *str* - The description of the direction

#### Signature

```python
class Direction(BaseModel): ...
```



## Disruption

[Show source in models.py:373](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L373)

A disruption of a line

#### Attributes

- `description` *str* - The description of the disruption
- `line_directions` *list[Direction]* - The directions of the line

#### Signature

```python
class Disruption(BaseModel): ...
```



## Entity

[Show source in models.py:102](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L102)

An entity

#### Attributes

- `number` *int* - The number of the entity
- `code` *str* - The code of the entity
- `description` *str* - The description of the entity

#### Signature

```python
class Entity(BaseModel): ...
```



## GeoCoordinate

[Show source in models.py:20](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L20)

A geographical coordinate with a latitude and longitude

#### Attributes

- `latitude` *Latitude* - The latitude of the coordinate
- `longitude` *Longitude* - The longitude of the coordinate

#### Signature

```python
class GeoCoordinate(Coordinate): ...
```



## Line

[Show source in models.py:74](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L74)

A bus line

#### Attributes

- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `line_number_public` *str* - The public number of the line
- `description` *str* - The description of the line
- `transport_region_code` *str* - The code of the transport region
- `is_public` *bool* - Whether the line is public
- `transport_type` *str* - The type of the transport
- `operation_type` *str* - The type of the operation
- `valid_from` *str* - The valid from date of the line
- `valid_to` *str, optional* - The valid to date of the line. Defaults to None.

#### Signature

```python
class Line(BaseModel): ...
```



## LineColor

[Show source in models.py:116](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L116)

A color of a bus line

#### Attributes

- `code` *str* - The code of the color
- `description` *str* - The description of the color
- `color` *Color* - The color of the line

#### Signature

```python
class LineColor(BaseModel): ...
```



## Municipality

[Show source in models.py:130](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L130)

A municipality in Belgium

#### Attributes

- `number` *int* - The number of the municipality
- `description` *str* - The description of the municipality
main_municipality (Municipality | None, optional): The main municipality of the municipality. Defaults to None.

#### Signature

```python
class Municipality(BaseModel): ...
```



## Passage

[Show source in models.py:165](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L165)

A passage of a bus line

#### Attributes

- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *str* - The direction of the line
- `ride_number` *int* - The number of the ride
- `destination` *str* - The destination of the ride
- `destination_place` *str* - The place of the destination
- `vias` *list[str], optional* - The vias of the ride. Defaults to None.
- `timetable_timestamp` *datetime* - The timestamp of the timetable

#### Signature

```python
class Passage(BaseModel): ...
```



## PassageNote

[Show source in models.py:227](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L227)

A note for a passage

#### Attributes

- `id` *int* - The id of the note
- `title` *str* - The title of the note
- `ride_number` *int* - The number of the ride
- `stop_number` *int* - The number of the stop
- `description` *str* - The description of the note
- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *LineDirection* - The direction of the line

#### Signature

```python
class PassageNote(BaseModel): ...
```



## RealTimePassage

[Show source in models.py:311](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L311)

A real-time passage of a bus line

#### Attributes

- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *LineDirection* - The direction of the line
- `ride_number` *int* - The number of the ride
- `destination` *str* - The destination of the ride
- `vias` *list[str], optional* - The vias of the ride. Defaults to None.
- `timetable_timestamp` *datetime* - The timestamp of the timetable
- `real_time_timestamp` *datetime* - The timestamp of the real-time
- `vrtnum` *int* - The number of the real-time
- `prediction_statuses` *list[str]* - The statuses of the prediction

#### Signature

```python
class RealTimePassage(BaseModel): ...
```



## RealTimeStopPassage

[Show source in models.py:339](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L339)

All real-time passages of a bus stop

#### Attributes

- `passages` *list[RealTimePassage]* - The real-time passages of a bus stop

#### Signature

```python
class RealTimeStopPassage(BaseModel): ...
```



## RealTimeTimetable

[Show source in models.py:349](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L349)

A real-time timetable of a stop

#### Attributes

- `passages` *list[RealTimePassage]* - The real-time arrivals of the stop
- `passage_notes` *list[PassageNote]* - The notes of the passages
- `ride_notes` *list[RideNote]* - The notes of the rides
- `detours` *list[Detour]* - The detours of the stop

#### Signature

```python
class RealTimeTimetable(BaseModel):
    def __init__(self, **kwargs): ...
```



## RideNote

[Show source in models.py:203](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L203)

A note for a ride

#### Attributes

- `id` *int* - The id of the note
- `title` *str* - The title of the note
- `ride_number` *int* - The number of the ride
- `stop_number` *int* - The number of the stop
- `description` *str* - The description of the note
- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *LineDirection* - The direction of the line

#### Signature

```python
class RideNote(BaseModel): ...
```



## Stop

[Show source in models.py:44](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L44)

A bus stop

#### Attributes

- `entity_number` *int* - The number of the entity
- `number` *int* - The number of the stop
- `description` *str, optional* - The description of the stop. Defaults to None.
- `description_long` *str* - The long description of the stop
- `municipality_number` *int* - The number of the municipality
- `municipality_description` *str* - The description of the municipality
- `geo_coordinate` *GeoCoordinate* - The geographical coordinate of the stop
- `accessibilities` *list[Accessibility]* - The accessibilities of the stop
- `is_main` *bool, optional* - Whether the stop is the main stop. Defaults to None.
- `language` *Language* - The language of the stop

#### Signature

```python
class Stop(BaseModel): ...
```



## StopInVicinity

[Show source in models.py:146](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L146)

A stop in the vicinity of a geographical coordinate

#### Attributes

- `type` *str* - The type of the stop
- `id` *int* - The id of the stop
- `name` *str* - The name of the stop
- `distance` *int* - The distance of the stop
- `geo_coordinate` *GeoCoordinate* - The geographical coordinate of the stop

#### Signature

```python
class StopInVicinity(BaseModel): ...
```



## Timetable

[Show source in models.py:251](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L251)

A timetable of a stop

#### Attributes

- `passages` *list[Passage]* - The passages of the schedule
- `passage_notes` *list[PassageNote]* - The notes of the passages
- `ride_notes` *list[RideNote]* - The notes of the rides
- `detours` *list[Detour]* - The detours of the schedule

#### Signature

```python
class Timetable(BaseModel):
    def __init__(self, **kwargs): ...
```



## TransportRegion

[Show source in models.py:189](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/models.py#L189)

A transport region in Belgium

#### Attributes

- `code` *str* - The code of the transport region
- `name` *str* - The name of the transport region
- `number` *str* - The number of the transport region

#### Signature

```python
class TransportRegion(BaseModel): ...
```