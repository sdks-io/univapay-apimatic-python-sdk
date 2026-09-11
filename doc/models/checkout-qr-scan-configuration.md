
# Checkout Qr Scan Configuration

QR-scan (CPM) payment settings applied to checkout.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutQrScanConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether QR-scan payments are enabled. |
| `forbidden_qr_scan_gateways` | `List[str]` | Optional | QR-scan gateways disabled for the merchant. Common values include `alipay`, `alipay_plus`, `pay_pay`, `we_chat`, `univapay`, and `test`. `null` when no gateway is forbidden. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_qr_scan_configuration import CheckoutQrScanConfiguration

checkout_qr_scan_configuration = CheckoutQrScanConfiguration(
    enabled=True,
    forbidden_qr_scan_gateways=[
        'forbidden_qr_scan_gateways7'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

