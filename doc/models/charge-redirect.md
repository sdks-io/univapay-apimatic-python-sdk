
# Charge Redirect

Charge Redirect schema.

*This model accepts additional fields of type Any.*

## Structure

`ChargeRedirect`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `endpoint` | `str` | Optional | Endpoint value. |
| `redirect_id` | `uuid\|str` | Optional | Redirect identifier. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.charge_redirect import ChargeRedirect

charge_redirect = ChargeRedirect(
    endpoint='endpoint2',
    redirect_id='00001f64-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

