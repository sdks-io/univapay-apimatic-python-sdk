
# Generic Metadata

A free-form dictionary for custom metadata.

*This model accepts additional fields of type [str | None | int | float | bool | List[str | bool]](../../doc/models/containers/generic-metadata-value.md).*

## Structure

`GenericMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | Example of a custom metadata key. |
| `univapay_name` | `str` | Optional | Consumer name passed to payment processors that require it (e.g., konbini, bank transfer). |
| `univapay_phone_number` | `str` | Optional | Consumer phone number passed to payment processors that require it. |
| `additional_properties` | Dict[str, str \| None \| int \| float \| bool \| List[str \| bool]] | Optional | Allowed values for metadata properties. Values may be a string, number, boolean, null, or an array of any of the above — but not a nested object; the server rejects metadata whose direct property values are JSON objects. |

## Example

```python
from univapayclientsdk.models.generic_metadata import GenericMetadata

generic_metadata = GenericMetadata(
    order_id='12345'
)
```

