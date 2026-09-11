
# Transaction Token Update Request Data Phone Number

Transaction Token Update Request Data Phone Number schema.

*This model accepts additional fields of type Any.*

## Structure

`TransactionTokenUpdateRequestDataPhoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `str` | Optional | Telephone country code. |
| `local_number` | `str` | Optional | Local phone number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.transaction_token_update_request_data_phone_number import TransactionTokenUpdateRequestDataPhoneNumber

transaction_token_update_request_data_phone_number = TransactionTokenUpdateRequestDataPhoneNumber(
    country_code='81',
    local_number='08012341234'
)
```

