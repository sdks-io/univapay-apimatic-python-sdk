
# Token Create Paidy Data

Token Create Paidy Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreatePaidyData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paidy_token` | `str` | Required | One-time token issued by the Paidy SDK/widget on the client side. |
| `shipping_address` | [`TokenCreatePaidyDataShippingAddress`](../../doc/models/token-create-paidy-data-shipping-address.md) | Required | Shipping address for a Paidy token. `zip` is required; the server additionally requires at least one of `line1`, `line2`, `city`, or `state` to be present (not enforceable at the schema level). |
| `phone_number` | `str` | Optional | Consumer phone number in Japanese format (e.g., '08012341234'). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_create_paidy_data import TokenCreatePaidyData
from univapayclientsdk.models.token_create_paidy_data_shipping_address import TokenCreatePaidyDataShippingAddress

token_create_paidy_data = TokenCreatePaidyData(
    paidy_token='paidy-token-abc123',
    shipping_address=TokenCreatePaidyDataShippingAddress(
        zip='105-0011',
        line_1='1-1-1',
        city='Minato',
        state='Tokyo'
    ),
    phone_number='08012341234'
)
```

