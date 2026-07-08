
# Generic Metadata

A free-form dictionary for custom metadata.

*This model accepts additional fields of type [str | float | bool](../../doc/models/containers/generic-metadata-value.md).*

## Structure

`GenericMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | Example of a custom metadata key. |
| `univapay_name` | `str` | Optional | Consumer name passed to payment processors that require it (e.g., konbini, bank transfer). |
| `univapay_phone_number` | `str` | Optional | Consumer phone number passed to payment processors that require it. |
| `additional_properties` | Dict[str, str \| float \| bool] | Optional | Allowed values for metadata properties. |

## Example

```python
from univapayclientsdk.models.generic_metadata import GenericMetadata

generic_metadata = GenericMetadata(
    order_id='12345',
    univapay_name='univapay-name0',
    univapay_phone_number='univapay-phone-number4',
    additional_properties={
        'exampleAdditionalProperty': 'String4'
    }
)
```

