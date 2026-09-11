
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
from univapayclientsdk.models.charge_create_request_redirect import ChargeCreateRequestRedirect

charge_create_request_redirect = ChargeCreateRequestRedirect()
```

