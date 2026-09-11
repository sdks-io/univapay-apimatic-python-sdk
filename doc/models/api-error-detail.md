
# Api Error Detail

Structured detail entry describing a single API validation or business error.

*This model accepts additional fields of type Any.*

## Structure

`ApiErrorDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | `str` | Optional | The field name of the parameter that caused the error (lower_snake_case). |
| `reason` | `str` | Optional | Detailed reason for the nested error (UPPER_SNAKE_CASE or English description). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.api_error_detail import ApiErrorDetail

api_error_detail = ApiErrorDetail(
    field='card_number',
    reason='INVALID_CARD_NUMBER'
)
```

