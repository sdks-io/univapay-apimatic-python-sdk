
# Charge Create Request Redirect

Charge Create Request Redirect schema.

*This model accepts additional fields of type Any.*

## Structure

`ChargeCreateRequestRedirect`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `endpoint` | `str` | Optional | URL to redirect the customer to after payment completion. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.charge_create_request_redirect import ChargeCreateRequestRedirect

charge_create_request_redirect = ChargeCreateRequestRedirect(
    endpoint='endpoint6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

