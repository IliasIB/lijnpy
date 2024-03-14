# Municipalities

[Lijnpy Index](../../../../README.md#lijnpy-index) / [Lijnpy](../../../index.md#lijnpy) / [Kods](../../index.md#kods) / [Api](../index.md#api) / [V1](./index.md#v1) / Municipalities

> Auto-generated documentation for [lijnpy.kods.api.v1.municipalities](../../../../../lijnpy/kods/api/v1/municipalities.py) module.

- [Municipalities](#municipalities)
  - [get_lines](#get_lines)
  - [get_municipalities](#get_municipalities)
  - [get_municipality](#get_municipality)
  - [get_stops](#get_stops)

## get_lines

[Show source in municipalities.py:52](../../../../../lijnpy/kods/api/v1/municipalities.py#L52)

Get a list of lines in a municipality

#### Arguments

- `municipality_number` *int* - The municipality number

#### Returns

- `LinesResponse` - A list of lines in the municipality

#### Signature

```python
def get_lines(municipality_number: int) -> list[Line]: ...
```

#### See also

- [Line](./models.md#line)



## get_municipalities

[Show source in municipalities.py:13](../../../../../lijnpy/kods/api/v1/municipalities.py#L13)

Get a list of all municipalities in Belgium

#### Returns

- `MunicipalitiesResponse` - A list of all municipalities in Belgium

#### Signature

```python
def get_municipalities() -> list[Municipality]: ...
```

#### See also

- [Municipality](./models.md#municipality)



## get_municipality

[Show source in municipalities.py:72](../../../../../lijnpy/kods/api/v1/municipalities.py#L72)

Get a municipality by its number

#### Arguments

- `municipality_number` *int* - The number of the municipality

#### Returns

- `Municipality` - The municipality with the given number

#### Signature

```python
def get_municipality(municipality_number: int) -> Municipality: ...
```

#### See also

- [Municipality](./models.md#municipality)



## get_stops

[Show source in municipalities.py:32](../../../../../lijnpy/kods/api/v1/municipalities.py#L32)

Get a list of stops in a municipality

#### Arguments

- `municipality_number` *int* - The municipality number

#### Returns

- `StopsResponse` - A list of stops in the municipality

#### Signature

```python
def get_stops(municipality_number: int) -> list[Stop]: ...
```

#### See also

- [Stop](./models.md#stop)