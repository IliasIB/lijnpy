# Models

[Lijnpy Index](../../../../README.md#lijnpy-index) / [Lijnpy](../../../index.md#lijnpy) / [Kods](../../index.md#kods) / [Api](../index.md#api) / [V1](./index.md#v1) / Models

> Auto-generated documentation for [lijnpy.kods.api.v1.models](../../../../../lijnpy/kods/api/v1/models.py) module.

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
  - [RealTimeTimetable](#realtimetimetable)
  - [RideNote](#ridenote)
  - [Stop](#stop)
  - [StopInVicinity](#stopinvicinity)
  - [Timetable](#timetable)
  - [TransportRegion](#transportregion)

## Detour

[Show source in models.py:280](../../../../../lijnpy/kods/api/v1/models.py#L280)

Represents a detour of a line

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

[Show source in models.py:30](../../../../../lijnpy/kods/api/v1/models.py#L30)

Represents a period of a detour of a line

#### Attributes

- `start_date` *datetime* - The start date of the period
- `end_date` *datetime, optional* - The end date of the period. Defaults to None.

#### Signature

```python
class DetourPeriod(BaseModel): ...
```



## Direction

[Show source in models.py:264](../../../../../lijnpy/kods/api/v1/models.py#L264)

Represents a direction of a line

#### Attributes

- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *str* - The direction of the line
- `description` *str* - The description of the direction

#### Signature

```python
class Direction(BaseModel): ...
```



## Disruption

[Show source in models.py:344](../../../../../lijnpy/kods/api/v1/models.py#L344)

Represents a disruption

#### Attributes

- `id` *int* - The id of the disruption
- `title` *str* - The title of the disruption
- `description` *str* - The description of the disruption
- `start_date` *str* - The start date of the disruption
- `end_date` *str* - The end date of the disruption

#### Signature

```python
class Disruption(BaseModel): ...
```



## Entity

[Show source in models.py:100](../../../../../lijnpy/kods/api/v1/models.py#L100)

Represents a response from the entity API

#### Attributes

- `number` *int* - The number of the entity
- `code` *str* - The code of the entity
- `description` *str* - The description of the entity

#### Signature

```python
class Entity(BaseModel): ...
```



## GeoCoordinate

[Show source in models.py:18](../../../../../lijnpy/kods/api/v1/models.py#L18)

Represents a geographical coordinate

#### Attributes

- `latitude` *Latitude* - The latitude of the coordinate
- `longitude` *Longitude* - The longitude of the coordinate

#### Signature

```python
class GeoCoordinate(Coordinate): ...
```



## Line

[Show source in models.py:72](../../../../../lijnpy/kods/api/v1/models.py#L72)

Represents a response from the lines API

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

[Show source in models.py:114](../../../../../lijnpy/kods/api/v1/models.py#L114)

Represents a response from the color API

#### Attributes

- `code` *str* - The code of the color
- `description` *str* - The description of the color
- `rgb` *RGB* - The RGB values of the color
- `hex` *str* - The hexadecimal value of the color

#### Signature

```python
class LineColor(BaseModel): ...
```



## Municipality

[Show source in models.py:129](../../../../../lijnpy/kods/api/v1/models.py#L129)

Represents a response from the municipality API

#### Attributes

- `number` *int* - The number of the municipality
- `description` *str* - The description of the municipality
main_municipality (Municipality | None, optional): The main municipality of the municipality. Defaults to None.

#### Signature

```python
class Municipality(BaseModel): ...
```



## Passage

[Show source in models.py:162](../../../../../lijnpy/kods/api/v1/models.py#L162)

Represents a passage of a schedule

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

[Show source in models.py:224](../../../../../lijnpy/kods/api/v1/models.py#L224)

Represents a note of a passage

#### Attributes

- `id` *int* - The id of the note
- `title` *str* - The title of the note
- `ride_number` *int* - The number of the ride
- `stop_number` *int* - The number of the stop
- `description` *str* - The description of the note
- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *str* - The direction of the line

#### Signature

```python
class PassageNote(BaseModel): ...
```



## RealTimePassage

[Show source in models.py:300](../../../../../lijnpy/kods/api/v1/models.py#L300)

Represents a real-time passage of a stop

#### Attributes

- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *str* - The direction of the line
- `ride_number` *int* - The number of the ride
- `destination` *str* - The destination of the ride
- `vias` *list[str], optional* - The vias of the ride. Defaults to None.
- `timetable_timestamp` *str* - The timestamp of the timetable
- `real_time_timestamp` *str* - The timestamp of the real-time
- `vrtnum` *int* - The number of the real-time
- `prediction_statuses` *list[str]* - The statuses of the prediction

#### Signature

```python
class RealTimePassage(BaseModel): ...
```



## RealTimeTimetable

[Show source in models.py:328](../../../../../lijnpy/kods/api/v1/models.py#L328)

Represents the real-time arrivals of a stop

#### Attributes

- `passages` *list[RealTimePassageStopResponse]* - The real-time arrivals of the stop
- `passage_notes` *list[PassageNoteResponse]* - The notes of the passages
- `ride_notes` *list[RideNoteResponse]* - The notes of the rides
- `detours` *list[DetourResponse]* - The detours of the stop

#### Signature

```python
class RealTimeTimetable(BaseModel): ...
```



## RideNote

[Show source in models.py:200](../../../../../lijnpy/kods/api/v1/models.py#L200)

Represents a note of a ride

#### Attributes

- `id` *int* - The id of the note
- `title` *str* - The title of the note
- `ride_number` *int* - The number of the ride
- `stop_number` *int* - The number of the stop
- `description` *str* - The description of the note
- `entity_number` *int* - The number of the entity
- `line_number` *int* - The number of the line
- `direction` *str* - The direction of the line

#### Signature

```python
class RideNote(BaseModel): ...
```



## Stop

[Show source in models.py:42](../../../../../lijnpy/kods/api/v1/models.py#L42)

Represents a response from the stop API

#### Attributes

- `entity_number` *int* - The number of the entity
- `number` *int* - The number of the stop
- `description` *str* - The description of the stop
- `description_long` *str* - The long description of the stop
- `language` *str* - The language of the stop
- `municipality_number` *int* - The number of the municipality
- `omschrijving_gemeente` *str* - The description of the municipality
- `geo_coordinate` *GeoCoordinate* - The geographical coordinate of the stop
- `accessibilities` *list[str]* - The accessibilities of the stop
- `is_main` *bool* - Whether the stop is main

#### Signature

```python
class Stop(BaseModel): ...
```



## StopInVicinity

[Show source in models.py:145](../../../../../lijnpy/kods/api/v1/models.py#L145)

Represents a response from the stops in vicinity API

#### Attributes

- `id` *int* - The id of the stop
- `name` *str* - The name of the stop
- `distance` *int* - The distance of the stop
- `geo_coordinate` *GeoCoordinate* - The geographical coordinate of the stop

#### Signature

```python
class StopInVicinity(BaseModel): ...
```



## Timetable

[Show source in models.py:248](../../../../../lijnpy/kods/api/v1/models.py#L248)

Represents a schedule

#### Attributes

- `passages` *list[Passage]* - The passages of the schedule
- `passage_notes` *list[PassageNote]* - The notes of the passages
- `ride_notes` *list[RideNote]* - The notes of the rides
- `detours` *list[Detour]* - The detours of the schedule

#### Signature

```python
class Timetable(BaseModel): ...
```



## TransportRegion

[Show source in models.py:186](../../../../../lijnpy/kods/api/v1/models.py#L186)

Represents a transport region in Belgium

#### Attributes

- `code` *str* - The code of the transport region
- `name` *str* - The name of the transport region
- `number` *str* - The number of the transport region

#### Signature

```python
class TransportRegion(BaseModel): ...
```