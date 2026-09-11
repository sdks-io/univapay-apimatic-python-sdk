
# Token Response Qr Scan Data

Token Response Qr Scan Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseQrScanData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | `str` | Required | QR-CPM brand detected from the scanned code (e.g. `pay_pay`, `we_chat`, `qq`, `line_pay`, `au_pay`, `alipay_china`). This is an open value set — new brands may appear without notice. Returned as `null` when the scanned code could not be parsed into a known brand. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_response_qr_scan_data import TokenResponseQrScanData

token_response_qr_scan_data = TokenResponseQrScanData(
    brand='pay_pay'
)
```

