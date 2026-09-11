
# Token Create Qr Scan Data

Token Create Qr Scan Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenCreateQrScanData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scanned_qr` | `str` | Required | The QR/barcode payload scanned from the customer's payment app (Customer-Presented Mode). Only valid when `type` is `one_time` — the server rejects `subscription`/`recurring` token types for this payment type. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.token_create_qr_scan_data import TokenCreateQrScanData

token_create_qr_scan_data = TokenCreateQrScanData(
    scanned_qr='091234567890123456789012345'
)
```

