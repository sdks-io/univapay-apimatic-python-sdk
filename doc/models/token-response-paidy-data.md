
# Token Response Paidy Data

Token Response Paidy Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponsePaidyData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paidy_token` | `str` | Required | One-time token issued by the Paidy SDK/widget on the client side. |
| `phone_number` | `str` | Optional | Consumer phone number in Japanese format. |
| `shipping_address` | [`TokenResponsePaidyDataShippingAddress`](../../doc/models/token-response-paidy-data-shipping-address.md) | Optional | Shipping address returned for a Paidy token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_response_paidy_data import TokenResponsePaidyData
from univapayclientsdk.models.token_response_paidy_data_shipping_address import TokenResponsePaidyDataShippingAddress

token_response_paidy_data = TokenResponsePaidyData(
    paidy_token='paidy-token-abc123',
    phone_number='08012341234',
    shipping_address=TokenResponsePaidyDataShippingAddress(
        zip='105-0011',
        line_1='1-1-1',
        city='Minato',
        state='Tokyo'
    )
)
```

