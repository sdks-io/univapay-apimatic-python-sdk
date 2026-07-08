
# Charge Three Ds

Charge Three Ds schema.

*This model accepts additional fields of type Any.*

## Structure

`ChargeThreeDs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_endpoint` | `str` | Optional | Redirect endpoint URL. |
| `mode` | `str` | Optional | Processing mode for the resource. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.charge_three_ds import ChargeThreeDs

charge_three_ds = ChargeThreeDs(
    redirect_endpoint='redirect_endpoint4',
    mode='mode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

