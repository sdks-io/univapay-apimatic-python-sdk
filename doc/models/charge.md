
# Charge

Charge resource returned by the payments API.

*This model accepts additional fields of type Any.*

## Structure

`Charge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `transaction_token_id` | `uuid\|str` | Optional | Transaction token identifier. |
| `transaction_token_type` | [`ChargeTransactionTokenType`](../../doc/models/charge-transaction-token-type.md) | Optional | Charge Transaction Token Type schema. |
| `subscription_id` | `uuid\|str` | Optional | Subscription identifier. |
| `merchant_transaction_id` | `str` | Optional | Merchant-defined transaction identifier. |
| `requested_amount` | `int` | Optional | Requested amount in the smallest currency unit. |
| `requested_currency` | `str` | Optional | Requested ISO-4217 currency code. |
| `requested_amount_formatted` | `float` | Optional | Requested amount formatted for display. |
| `charged_amount` | `int` | Optional | Charged amount in the smallest currency unit. |
| `charged_currency` | `str` | Optional | Charged ISO-4217 currency code. |
| `charged_amount_formatted` | `float` | Optional | Charged amount formatted for display. |
| `fee_amount` | `int` | Optional | Fee amount in the smallest currency unit. |
| `fee_currency` | `str` | Optional | Fee ISO-4217 currency code. |
| `fee_amount_formatted` | `float` | Optional | Fee amount formatted for display. |
| `only_direct_currency` | `bool` | Optional | Whether only direct currency processing is allowed. |
| `capture_at` | `datetime` | Optional | Timestamp when capture should occur. |
| `descriptor` | `str` | Optional | Billing descriptor. |
| `descriptor_phone_number` | `str` | Optional | Billing descriptor phone number. |
| `status` | [`ChargeStatus`](../../doc/models/charge-status.md) | Optional | Charge Status schema. |
| `error` | [`PaymentError`](../../doc/models/payment-error.md) | Optional | Payment error details, or null if successful. |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `mode` | [`ChargeMode`](../../doc/models/charge-mode.md) | Optional | Charge Mode schema. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `merchant_name` | `str` | Optional | Merchant display name. |
| `store_name` | `str` | Optional | Store display name. |
| `redirect` | [`ChargeRedirect`](../../doc/models/charge-redirect.md) | Optional | Charge Redirect schema. |
| `three_ds` | [`ChargeThreeDs`](../../doc/models/charge-three-ds.md) | Optional | Charge Three Ds schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.charge import Charge
from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.charge_redirect import ChargeRedirect
from univapayclientsdk.models.charge_status import ChargeStatus
from univapayclientsdk.models.charge_three_ds import ChargeThreeDs
from univapayclientsdk.models.charge_transaction_token_type import ChargeTransactionTokenType
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.payment_error import PaymentError

charge = Charge(
    id='6efb4e5c-690a-40f3-a4f1-0e19c5f84e98',
    store_id='76cf4a64-02bc-4cb3-9a28-74622e5928a1',
    transaction_token_id='af834c88-7a8f-47ac-aee9-0386a0f98b0d',
    transaction_token_type=ChargeTransactionTokenType.ONE_TIME,
    subscription_id='11ef0000-0000-4000-8000-000000000001',
    merchant_transaction_id='ORD-998877',
    requested_amount=1000,
    requested_currency='JPY',
    requested_amount_formatted=1000,
    charged_amount=1000,
    charged_currency='JPY',
    charged_amount_formatted=1000,
    fee_amount=30,
    fee_currency='JPY',
    fee_amount_formatted=30,
    only_direct_currency=False,
    capture_at=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    descriptor='UNIVAPAY TEST',
    descriptor_phone_number='0312345678',
    status=ChargeStatus.PENDING,
    error=PaymentError(
        code=301,
        message='Card number error.',
        detail='The provided card number failed validation.',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    metadata=GenericMetadata(
        order_id='12345',
        univapay_name='univapay-name8',
        univapay_phone_number='univapay-phone-number2',
        additional_properties={
            'exampleAdditionalProperty': 'String4'
        }
    ),
    mode=ChargeMode.LIVE,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    merchant_name='Test Merchant',
    store_name='Tokyo Store',
    redirect=ChargeRedirect(
        endpoint='endpoint8',
        redirect_id='00000316-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    three_ds=ChargeThreeDs(
        redirect_endpoint='redirect_endpoint8',
        mode='mode2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

