
# Transaction History User Data

Payment-type-specific details for this row. This is a single flat object covering every payment type — the fields actually populated depend on `payment_type` (documented per field below). Fields not applicable to a given payment type are omitted.

*This model accepts additional fields of type Any.*

## Structure

`TransactionHistoryUserData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TransactionHistoryType`](../../doc/models/transaction-history-type.md) | Optional | Whether this row represents a charge or a refund. |
| `cardholder_name` | `str` | Optional | Cardholder name. Present for `card` and `apple_pay` rows only. |
| `cardholder_email_address` | `str` | Optional | Cardholder/customer email address. Present for every payment type except `konbini`'s legacy alias fields; always non-null for `bank_transfer` rows, nullable for every other type. |
| `cardholder_phone_number` | `str` | Optional | Cardholder phone number. Present for `paidy` rows only. |
| `customer_name` | `str` | Optional | Customer name as entered at checkout. Present for `konbini` rows only (empty string when not provided). |
| `convenience_store` | `str` | Optional | Legacy duplicate of `brand`. Present for `konbini` rows only. |
| `brand` | `str` | Optional | Raw brand identifier for the payment method. Present for every payment type; the value set is payment-type-specific (e.g. card brands for `card`/`apple_pay`, QR brands for `qr_scan`/`qr_merchant`, online-wallet brands for `online`, convenience-store brands for `konbini`, `paidy` for `paidy` rows). Nullable for `qr_scan`, `qr_merchant`, and `online`; always non-null for the other types. |
| `gateway` | `str` | Optional | Raw gateway identifier that processed the payment. Present for every payment type. |
| `service_provider` | [`TransactionHistoryServiceProvider`](../../doc/models/transaction-history-service-provider.md) | Optional | Service provider, or `null` when not reported. |
| `refunds` | [`List[TransactionHistoryRefund]`](../../doc/models/transaction-history-refund.md) | Optional | Refunds issued against this charge. Present for charge rows only (`type: charge`); absent for refund rows. |
| `reason` | [`TransactionHistoryRefundReason`](../../doc/models/transaction-history-refund-reason.md) | Optional | Refund reason, or `null` when unset. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.transaction_history_refund import TransactionHistoryRefund
from univapayclientsdk.models.transaction_history_refund_status import TransactionHistoryRefundStatus
from univapayclientsdk.models.transaction_history_service_provider import TransactionHistoryServiceProvider
from univapayclientsdk.models.transaction_history_type import TransactionHistoryType
from univapayclientsdk.models.transaction_history_user_data import TransactionHistoryUserData

transaction_history_user_data = TransactionHistoryUserData(
    mtype=TransactionHistoryType.CHARGE,
    cardholder_name='Some Guy',
    cardholder_email_address='test4@univapay.com',
    brand='visa',
    gateway='test',
    service_provider=TransactionHistoryServiceProvider.CREDIT,
    refunds=[
        TransactionHistoryRefund(
            refund_id='11ef0000-0000-4000-8000-000000000010',
            amount=500,
            currency='JPY',
            amount_formatted=500,
            status=TransactionHistoryRefundStatus.SUCCESSFUL
        )
    ]
)
```

