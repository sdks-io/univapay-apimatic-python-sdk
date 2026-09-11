
# Token Response Paidy Data Shipping Address

Shipping address returned for a Paidy token.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponsePaidyDataShippingAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `zip` | `str` | Optional | Japanese postal code. |
| `line_1` | `str` | Optional | Primary street address line. |
| `line_2` | `str` | Optional | Secondary street address line. |
| `city` | `str` | Optional | City or locality. |
| `state` | `str` | Optional | State or prefecture. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_response_paidy_data_shipping_address import TokenResponsePaidyDataShippingAddress

token_response_paidy_data_shipping_address = TokenResponsePaidyDataShippingAddress(
    zip='105-0011',
    line_1='1-1-1',
    city='Minato',
    state='Tokyo'
)
```

