# Colors

[Lijnpy Index](../../../../README.md#lijnpy-index) / [Lijnpy](../../../index.md#lijnpy) / [Kods](../../index.md#kods) / [Api](../index.md#api) / [V1](./index.md#v1) / Colors

> Auto-generated documentation for [lijnpy.kods.api.v1.colors](../../../../../lijnpy/kods/api/v1/colors.py) module.

- [Colors](#colors)
  - [get_color](#get_color)
  - [get_colors](#get_colors)

## get_color

[Show source in colors.py:26](../../../../../lijnpy/kods/api/v1/colors.py#L26)

Get a color by its code

#### Arguments

- `color_code` *str* - The code of the color

#### Returns

- `LineColor` - The color with the given code

#### Signature

```python
def get_color(color_code: str) -> LineColor: ...
```

#### See also

- [LineColor](./models.md#linecolor)



## get_colors

[Show source in colors.py:9](../../../../../lijnpy/kods/api/v1/colors.py#L9)

Get a list of all colors

#### Returns

- `list[Color]` - A list of all colors

#### Signature

```python
def get_colors() -> list[LineColor]: ...
```

#### See also

- [LineColor](./models.md#linecolor)