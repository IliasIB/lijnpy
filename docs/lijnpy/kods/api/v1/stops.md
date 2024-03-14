# Stops

[Lijnpy Index](../../../../README.md#lijnpy-index) / [Lijnpy](../../../index.md#lijnpy) / [Kods](../../index.md#kods) / [Api](../index.md#api) / [V1](./index.md#v1) / Stops

> Auto-generated documentation for [lijnpy.kods.api.v1.stops](../../../../../lijnpy/kods/api/v1/stops.py) module.

- [Stops](#stops)
  - [get_detours](#get_detours)
  - [get_directions](#get_directions)
  - [get_disruptions](#get_disruptions)
  - [get_real_time_timetable](#get_real_time_timetable)
  - [get_stop](#get_stop)
  - [get_stops_in_vicinity](#get_stops_in_vicinity)
  - [get_timetable](#get_timetable)

## get_detours

[Show source in stops.py:131](../../../../../lijnpy/kods/api/v1/stops.py#L131)

Get the detours of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `DetoursResponse` - The detours of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
def get_detours(entity_number: int, stop_number: int) -> list[Detour]: ...
```

#### See also

- [Detour](./models.md#detour)



## get_directions

[Show source in stops.py:105](../../../../../lijnpy/kods/api/v1/stops.py#L105)

Get the directions of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `DirectionsResponse` - The directions of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
def get_directions(entity_number: int, stop_number: int) -> list[Direction]: ...
```

#### See also

- [Direction](./models.md#direction)



## get_disruptions

[Show source in stops.py:191](../../../../../lijnpy/kods/api/v1/stops.py#L191)

Get the directions of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `DisruptionsResponse` - The disruptions of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
def get_disruptions(entity_number: int, stop_number: int) -> list[Disruption]: ...
```

#### See also

- [Disruption](./models.md#disruption)



## get_real_time_timetable

[Show source in stops.py:155](../../../../../lijnpy/kods/api/v1/stops.py#L155)

Get the real-time arrivals of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `RealTimePassagesResponse` - The real-time arrivals of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
def get_real_time_timetable(
    entity_number: int, stop_number: int
) -> RealTimeTimetable: ...
```

#### See also

- [RealTimeTimetable](./models.md#realtimetimetable)



## get_stop

[Show source in stops.py:49](../../../../../lijnpy/kods/api/v1/stops.py#L49)

Get the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `StopResponse` - The stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
def get_stop(entity_number: int, stop_number: int) -> Stop: ...
```

#### See also

- [Stop](./models.md#stop)



## get_stops_in_vicinity

[Show source in stops.py:22](../../../../../lijnpy/kods/api/v1/stops.py#L22)

Get a list of all available stops in the neighbourhood of the given geo-coordinates

#### Arguments

- `geo_coordinate` *GeoCoordinate* - The geo-coordinates to search around

#### Returns

- `StopsInVicinityResponse` - A list of all available stops in the neighbourhood of the given geo-coordinates

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
def get_stops_in_vicinity(geo_coordinate: GeoCoordinate) -> list[StopInVicinity]: ...
```

#### See also

- [GeoCoordinate](./models.md#geocoordinate)
- [StopInVicinity](./models.md#stopinvicinity)



## get_timetable

[Show source in stops.py:73](../../../../../lijnpy/kods/api/v1/stops.py#L73)

Get the schedule of the stop with the given entity and stop number

#### Returns

- `Timetable` - The schedule of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
def get_timetable(entity_number: int, stop_number: int) -> Timetable: ...
```

#### See also

- [Timetable](./models.md#timetable)