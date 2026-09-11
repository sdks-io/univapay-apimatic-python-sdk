
# Generic Metadata Value

Allowed values for metadata properties. Values may be a string, number, boolean, null, or an array of any of the above — but not a nested object; the server rejects metadata whose direct property values are JSON objects.

## Data Type

`str | None | int | float | bool | List[str | bool]`

## Cases

| Type |
|  --- |
| `str` |
| `int` |
| `float` |
| `bool` |
| [`List[Any]`](../../../doc/models/containers/generic-metadata-array-item.md) |

## str

### Initialization Code

#### Example

```python
value = 'sale'
```

## int

### Initialization Code

#### Example

```python
value = 10
```

## float

### Initialization Code

#### Example

```python
value = 10.5
```

## bool

### Initialization Code

#### Example

```python
value = True
```

## List[Any]

### Initialization Code

#### Example

```python
value = [
    'sale',
    'promo'
]
```

