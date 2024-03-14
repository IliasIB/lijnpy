# Transport Regions

[Lijnpy Index](../../../../README.md#lijnpy-index) / [Lijnpy](../../../index.md#lijnpy) / [Kods](../../index.md#kods) / [Api](../index.md#api) / [V1](./index.md#v1) / Transport Regions

> Auto-generated documentation for [lijnpy.kods.api.v1.transport_regions](../../../../../lijnpy/kods/api/v1/transport_regions.py) module.

- [Transport Regions](#transport-regions)
  - [get_lines](#get_lines)
  - [get_transport_region](#get_transport_region)
  - [get_transport_regions](#get_transport_regions)

## get_lines

[Show source in transport_regions.py:49](../../../../../lijnpy/kods/api/v1/transport_regions.py#L49)

Get a list of lines by transport region code

#### Arguments

- `transport_region_code` *str* - The code of the transport region

#### Returns

- `LinesResponse` - A list of lines

#### Signature

```python
def get_lines(transport_region_code: str) -> list[Line]: ...
```

#### See also

- [Line](./models.md#line)



## get_transport_region

[Show source in transport_regions.py:29](../../../../../lijnpy/kods/api/v1/transport_regions.py#L29)

Get a transport region by code

#### Arguments

- `transport_region_code` *str* - The code of the transport region

#### Returns

- `TransportRegion` - The transport region

#### Signature

```python
def get_transport_region(transport_region_code: str) -> TransportRegion: ...
```

#### See also

- [TransportRegion](./models.md#transportregion)



## get_transport_regions

[Show source in transport_regions.py:9](../../../../../lijnpy/kods/api/v1/transport_regions.py#L9)

Get a list of all transport regions

#### Returns

- `TransportRegionsResponse` - A list of all transport regions

#### Signature

```python
def get_transport_regions() -> list[TransportRegion]: ...
```

#### See also

- [TransportRegion](./models.md#transportregion)