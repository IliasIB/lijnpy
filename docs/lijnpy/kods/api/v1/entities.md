# Entities

[Lijnpy Index](../../../../README.md#lijnpy-index) / [Lijnpy](../../../index.md#lijnpy) / [Kods](../../index.md#kods) / [Api](../index.md#api) / [V1](./index.md#v1) / Entities

> Auto-generated documentation for [lijnpy.kods.api.v1.entities](../../../../../lijnpy/kods/api/v1/entities.py) module.

- [Entities](#entities)
  - [get_entities](#get_entities)
  - [get_entity](#get_entity)
  - [get_lines](#get_lines)
  - [get_municipalities](#get_municipalities)
  - [get_stops](#get_stops)

## get_entities

[Show source in entities.py:14](../../../../../lijnpy/kods/api/v1/entities.py#L14)

Get a list of all entities

#### Returns

- `list[Entity]` - A list of all entities

#### Signature

```python
def get_entities() -> list[Entity]: ...
```

#### See also

- [Entity](./models.md#entity)



## get_entity

[Show source in entities.py:31](../../../../../lijnpy/kods/api/v1/entities.py#L31)

Get an entity by its number

#### Arguments

- `entity_number` *int* - The number of the entity

#### Returns

- `Entity` - The entity with the given number

#### Signature

```python
def get_entity(entity_number: int) -> Entity: ...
```

#### See also

- [Entity](./models.md#entity)



## get_lines

[Show source in entities.py:93](../../../../../lijnpy/kods/api/v1/entities.py#L93)

Get a list of lines in Belgium for a given entity

#### Arguments

- `entity_number` *str* - The number of the entity

#### Returns

- `list[Line]` - A list of lines in Belgium for a given entity

#### Signature

```python
def get_lines(entity_number: int) -> list[Line]: ...
```

#### See also

- [Line](./models.md#line)



## get_municipalities

[Show source in entities.py:51](../../../../../lijnpy/kods/api/v1/entities.py#L51)

Get a list of municipalities in Belgium for a given entity

#### Arguments

- `entity_number` *str* - The number of the entity

#### Returns

- `list[Municipality]` - A list of municipalities in Belgium for a given entity

#### Signature

```python
def get_municipalities(entity_number: int) -> list[Municipality]: ...
```

#### See also

- [Municipality](./models.md#municipality)



## get_stops

[Show source in entities.py:73](../../../../../lijnpy/kods/api/v1/entities.py#L73)

Get a list of stops in Belgium for a given entity

#### Arguments

- `entity_number` *str* - The number of the entity

#### Returns

- `list[Stop]` - A list of stops in Belgium for a given entity

#### Signature

```python
def get_stops(entity_number: int) -> list[Stop]: ...
```

#### See also

- [Stop](./models.md#stop)