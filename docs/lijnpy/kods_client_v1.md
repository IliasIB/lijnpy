# KODSClientV1

[Lijnpy Index](../README.md#lijnpy-index) / [Lijnpy](./index.md#lijnpy) / KODSClientV1

> Auto-generated documentation for [lijnpy.kods_client_v1](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py) module.

- [KODSClientV1](#kodsclientv1)
  - [KODSClientV1](#kodsclientv1-1)
    - [KODSClientV1().get_color](#kodsclientv1()get_color)
    - [KODSClientV1().get_colors](#kodsclientv1()get_colors)
    - [KODSClientV1().get_detours](#kodsclientv1()get_detours)
    - [KODSClientV1().get_directions](#kodsclientv1()get_directions)
    - [KODSClientV1().get_disruptions](#kodsclientv1()get_disruptions)
    - [KODSClientV1().get_entities](#kodsclientv1()get_entities)
    - [KODSClientV1().get_entity](#kodsclientv1()get_entity)
    - [KODSClientV1().get_lines](#kodsclientv1()get_lines)
    - [KODSClientV1().get_lines_by_entity](#kodsclientv1()get_lines_by_entity)
    - [KODSClientV1().get_lines_by_transport_region](#kodsclientv1()get_lines_by_transport_region)
    - [KODSClientV1().get_municipalities](#kodsclientv1()get_municipalities)
    - [KODSClientV1().get_municipalities_by_entity](#kodsclientv1()get_municipalities_by_entity)
    - [KODSClientV1().get_municipality](#kodsclientv1()get_municipality)
    - [KODSClientV1().get_real_time_timetable](#kodsclientv1()get_real_time_timetable)
    - [KODSClientV1().get_stop](#kodsclientv1()get_stop)
    - [KODSClientV1().get_stops](#kodsclientv1()get_stops)
    - [KODSClientV1().get_stops_by_entity](#kodsclientv1()get_stops_by_entity)
    - [KODSClientV1().get_stops_in_vicinity](#kodsclientv1()get_stops_in_vicinity)
    - [KODSClientV1().get_timetable](#kodsclientv1()get_timetable)
    - [KODSClientV1().get_transport_region](#kodsclientv1()get_transport_region)
    - [KODSClientV1().get_transport_regions](#kodsclientv1()get_transport_regions)
    - [KODSClientV1().parse_api_call](#kodsclientv1()parse_api_call)

## KODSClientV1

[Show source in kods_client_v1.py:24](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L24)

#### Signature

```python
class KODSClientV1:
    def __init__(
        self,
        api_key: str = "",
        logger: Logger = Logger(__name__),
        http_client: RestAdapter | None = None,
    ): ...
```

### KODSClientV1().get_color

[Show source in kods_client_v1.py:78](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L78)

Get a color by its code

#### Arguments

- `color_code` *str* - The code of the color

#### Returns

- `LineColor` - The color with the given code

#### Signature

```python
async def get_color(self, color_code: str) -> LineColor: ...
```

#### See also

- [LineColor](./models.md#linecolor)

### KODSClientV1().get_colors

[Show source in kods_client_v1.py:67](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L67)

Get a list of all colors

#### Returns

- `list[LineColor]` - A list of all colors

#### Signature

```python
async def get_colors(self) -> list[LineColor]: ...
```

#### See also

- [LineColor](./models.md#linecolor)

### KODSClientV1().get_detours

[Show source in kods_client_v1.py:295](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L295)

Get the detours of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `list[Detour]` - The detours of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
async def get_detours(self, entity_number: int, stop_number: int) -> list[Detour]: ...
```

#### See also

- [Detour](./models.md#detour)

### KODSClientV1().get_directions

[Show source in kods_client_v1.py:273](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L273)

Get the directions of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `list[Direction]` - The directions of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
async def get_directions(
    self, entity_number: int, stop_number: int
) -> list[Direction]: ...
```

#### See also

- [Direction](./models.md#direction)

### KODSClientV1().get_disruptions

[Show source in kods_client_v1.py:336](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L336)

Get the directions of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `list[Disruption]` - The disruptions of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
async def get_disruptions(
    self, entity_number: int, stop_number: int
) -> list[Disruption]: ...
```

#### See also

- [Disruption](./models.md#disruption)

### KODSClientV1().get_entities

[Show source in kods_client_v1.py:90](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L90)

Get a list of all entities

#### Returns

- `list[Entity]` - A list of all entities

#### Signature

```python
async def get_entities(self) -> list[Entity]: ...
```

#### See also

- [Entity](./models.md#entity)

### KODSClientV1().get_entity

[Show source in kods_client_v1.py:100](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L100)

Get an entity by its number

#### Arguments

- `entity_number` *int* - The number of the entity

#### Returns

- `Entity` - The entity with the given number

#### Signature

```python
async def get_entity(self, entity_number: int) -> Entity: ...
```

#### See also

- [Entity](./models.md#entity)

### KODSClientV1().get_lines

[Show source in kods_client_v1.py:187](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L187)

Get a list of lines in a municipality

#### Arguments

- `municipality_number` *int* - The municipality number

#### Returns

- `list[Line]` - A list of lines in the municipality

#### Signature

```python
async def get_lines(self, municipality_number: int) -> list[Line]: ...
```

#### See also

- [Line](./models.md#line)

### KODSClientV1().get_lines_by_entity

[Show source in kods_client_v1.py:144](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L144)

Get a list of lines in Belgium for a given entity

#### Arguments

- `entity_number` *str* - The number of the entity

#### Returns

- `list[Line]` - A list of lines in Belgium for a given entity

#### Signature

```python
async def get_lines_by_entity(self, entity_number: int) -> list[Line]: ...
```

#### See also

- [Line](./models.md#line)

### KODSClientV1().get_lines_by_transport_region

[Show source in kods_client_v1.py:383](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L383)

Get a list of lines by transport region code

#### Arguments

- `transport_region_code` *str* - The code of the transport region

#### Returns

- `list[Line]` - A list of lines

#### Signature

```python
async def get_lines_by_transport_region(
    self, transport_region_code: str
) -> list[Line]: ...
```

#### See also

- [Line](./models.md#line)

### KODSClientV1().get_municipalities

[Show source in kods_client_v1.py:160](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L160)

Get a list of all municipalities in Belgium

#### Returns

- `list[Municipality]` - A list of all municipalities in Belgium

#### Signature

```python
async def get_municipalities(self) -> list[Municipality]: ...
```

#### See also

- [Municipality](./models.md#municipality)

### KODSClientV1().get_municipalities_by_entity

[Show source in kods_client_v1.py:111](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L111)

Get a list of municipalities in Belgium for a given entity

#### Arguments

- `entity_number` *str* - The number of the entity

#### Returns

- `list[Municipality]` - A list of municipalities in Belgium for a given entity

#### Signature

```python
async def get_municipalities_by_entity(
    self, entity_number: int
) -> list[Municipality]: ...
```

#### See also

- [Municipality](./models.md#municipality)

### KODSClientV1().get_municipality

[Show source in kods_client_v1.py:203](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L203)

Get a municipality by its number

#### Arguments

- `municipality_number` *int* - The number of the municipality

#### Returns

- `Municipality` - The municipality with the given number

#### Signature

```python
async def get_municipality(self, municipality_number: int) -> Municipality: ...
```

#### See also

- [Municipality](./models.md#municipality)

### KODSClientV1().get_real_time_timetable

[Show source in kods_client_v1.py:315](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L315)

Get the real-time arrivals of the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `RealTimeTimetable` - The real-time arrivals of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
async def get_real_time_timetable(
    self, entity_number: int, stop_number: int
) -> RealTimeTimetable: ...
```

#### See also

- [RealTimeTimetable](./models.md#realtimetimetable)

### KODSClientV1().get_stop

[Show source in kods_client_v1.py:239](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L239)

Get the stop with the given entity and stop number

#### Arguments

- `entity_number` *int* - The number of the entity
- `stop_number` *int* - The number of the stop

#### Returns

- `Stop` - The stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
async def get_stop(self, entity_number: int, stop_number: int) -> Stop: ...
```

#### See also

- [Stop](./models.md#stop)

### KODSClientV1().get_stops

[Show source in kods_client_v1.py:171](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L171)

Get a list of stops in a municipality

#### Arguments

- `municipality_number` *int* - The municipality number

#### Returns

- `list[Stop]` - A list of stops in the municipality

#### Signature

```python
async def get_stops(self, municipality_number: int) -> list[Stop]: ...
```

#### See also

- [Stop](./models.md#stop)

### KODSClientV1().get_stops_by_entity

[Show source in kods_client_v1.py:128](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L128)

Get a list of stops in Belgium for a given entity

#### Arguments

- `entity_number` *str* - The number of the entity

#### Returns

- `list[Stop]` - A list of stops in Belgium for a given entity

#### Signature

```python
async def get_stops_by_entity(self, entity_number: int) -> list[Stop]: ...
```

#### See also

- [Stop](./models.md#stop)

### KODSClientV1().get_stops_in_vicinity

[Show source in kods_client_v1.py:217](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L217)

Get a list of all available stops in the neighbourhood of the given geo-coordinates

#### Arguments

- `geo_coordinate` *GeoCoordinate* - The geo-coordinates to search around

#### Returns

- `list[StopInVicinity]` - A list of all available stops in the neighbourhood of the given geo-coordinates

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
async def get_stops_in_vicinity(
    self, geo_coordinate: GeoCoordinate
) -> list[StopInVicinity]: ...
```

#### See also

- [GeoCoordinate](./models.md#geocoordinate)
- [StopInVicinity](./models.md#stopinvicinity)

### KODSClientV1().get_timetable

[Show source in kods_client_v1.py:258](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L258)

Get the schedule of the stop with the given entity and stop number

#### Returns

- `Timetable` - The schedule of the stop with the given entity and stop number

#### Raises

- `DeLijnAPIException` - If the API request fails

#### Signature

```python
async def get_timetable(self, entity_number: int, stop_number: int) -> Timetable: ...
```

#### See also

- [Timetable](./models.md#timetable)

### KODSClientV1().get_transport_region

[Show source in kods_client_v1.py:368](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L368)

Get a transport region by code

#### Arguments

- `transport_region_code` *str* - The code of the transport region

#### Returns

- `TransportRegion` - The transport region

#### Signature

```python
async def get_transport_region(self, transport_region_code: str) -> TransportRegion: ...
```

#### See also

- [TransportRegion](./models.md#transportregion)

### KODSClientV1().get_transport_regions

[Show source in kods_client_v1.py:357](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L357)

Get a list of all transport regions

#### Returns

- `list[TransportRegion]` - A list of all transport regions

#### Signature

```python
async def get_transport_regions(self) -> list[TransportRegion]: ...
```

#### See also

- [TransportRegion](./models.md#transportregion)

### KODSClientV1().parse_api_call

[Show source in kods_client_v1.py:40](https://github.com/IliasIB/lijnpy/blob/main/lijnpy/kods_client_v1.py#L40)

Parses result of API path and returns a model

#### Arguments

- `path` *str* - The path to call on the API
- `cls` *type[T]* - Class to validate the result of the API to
mapper (Callable[[dict], dict | list[dict]], optional): Mapper to extract
value from the return value

#### Returns

- `T` - A model validated from the result of the given path on the API

#### Signature

```python
async def parse_api_call(
    self,
    path: str,
    cls: type[T],
    mapper: Callable[[dict], dict | list[dict]] | None = None,
) -> T: ...
```