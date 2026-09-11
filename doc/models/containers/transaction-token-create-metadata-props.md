
# Transaction Token Create Metadata Props

Alias of GenericMetadataValue, retained because this schema name is part of the published SDK surface. Do not narrow it — see GenericMetadataValue for the contract.

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

