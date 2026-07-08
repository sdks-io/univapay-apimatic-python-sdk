
# Refund Reason Request

The reason for the refund (merchant-settable values). `duplicate`: A duplicate charge was made. `fraud`: The charge is fraudulent. `customer_request`: The customer requested the refund.

## Enumeration

`RefundReasonRequest`

## Fields

| Name |
|  --- |
| `DUPLICATE` |
| `FRAUD` |
| `CUSTOMER_REQUEST` |

## Example

```python
from univapayclientsdk.models.refund_reason_request import RefundReasonRequest

refund_reason_request = RefundReasonRequest.DUPLICATE
```

