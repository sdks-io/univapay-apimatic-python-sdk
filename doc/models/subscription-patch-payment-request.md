
# Subscription Patch Payment Request

Request body for updating a scheduled payment. All fields are optional. Omitted fields are left unchanged.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionPatchPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `due_date` | `date` | Optional | New due date for this payment (YYYY-MM-DD).  Only available to merchants with permission to edit payment dates. |
| `is_paid` | `bool` | Optional | Mark this payment as paid. Setting to `true` will trigger scheduling  of the next payment in the cycle. |
| `terminate_with_status` | [`SubscriptionTerminateWithStatus`](../../doc/models/subscription-terminate-with-status.md) | Optional | Schedule a status transition on a payment's due date. Set to `suspended` or `canceled` to schedule termination. Send `null` to cancel a previously scheduled transition. |
| `retry_interval` | `str` | Optional | ISO-8601 Duration override for the retry interval on a scheduled payment (for example `P3D`). Send `null` to clear. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.subscription_patch_payment_request import SubscriptionPatchPaymentRequest

subscription_patch_payment_request = SubscriptionPatchPaymentRequest(
    due_date=dateutil.parser.parse('2026-09-01').date(),
    is_paid=False,
    terminate_with_status=None,
    retry_interval='P3D',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

