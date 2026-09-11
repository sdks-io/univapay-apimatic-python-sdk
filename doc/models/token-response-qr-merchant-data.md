
# Token Response Qr Merchant Data

Token Response Qr Merchant Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseQrMerchantData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `qr_image_url` | `str` | Required | QR code payload to be rendered by the consumer (content varies by brand — may be a URL or an opaque code). Some brands return an image URL; others (e.g. convenience-store QR brands) return an opaque numeric code with no URL structure. Populated asynchronously shortly after token/charge creation — `null` until then. |
| `brand` | `str` | Optional | The QR-MPM brand this code was generated for. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_response_qr_merchant_data import TokenResponseQrMerchantData

token_response_qr_merchant_data = TokenResponseQrMerchantData(
    qr_image_url='71001234567890202604141200450',
    brand='pay_pay_merchant'
)
```

