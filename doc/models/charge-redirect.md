
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
from univapayclientsdk.models.charge_redirect import ChargeRedirect

charge_redirect = ChargeRedirect()
```

