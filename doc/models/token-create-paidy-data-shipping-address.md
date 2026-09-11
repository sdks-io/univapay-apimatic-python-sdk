
# Token Create Paidy Data Shipping Address

Shipping address for a Paidy token. `zip` is required; the server additionally requires at least one of `line1`, `line2`, `city`, or `state` to be present (not enforceable at the schema level).

*This model accepts additional fields of type Any.*

## Structure

`TokenCreatePaidyDataShippingAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `zip` | `str` | Required | Japanese postal code (e.g., '105-0011'). |
| `line_1` | `str` | Optional | Primary street address line. |
| `line_2` | `str` | Optional | Secondary street address line. |
| `city` | `str` | Optional | City or locality. |
| `state` | `str` | Optional | State or prefecture. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_create_paidy_data_shipping_address import TokenCreatePaidyDataShippingAddress

token_create_paidy_data_shipping_address = TokenCreatePaidyDataShippingAddress(
    zip='105-0011',
    line_1='1-1-1',
    city='Minato',
    state='Tokyo'
)
```

