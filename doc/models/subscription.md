
# Subscription

The Subscription object represents a recurring payment schedule.

*This model accepts additional fields of type Any.*

## Structure

`Subscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `transaction_token_id` | `uuid\|str` | Optional | Transaction token identifier. |
| `amount` | `int` | Optional | Amount in the smallest currency unit. |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `amount_formatted` | `float` | Optional | Amount formatted for display. |
| `initial_amount` | `int` | Optional | Initial amount in the smallest currency unit. |
| `initial_amount_formatted` | `float` | Optional | Initial amount formatted for display. |
| `subsequent_cycles_start` | `datetime` | Optional | Timestamp when recurring cycles begin. |
| `schedule_settings` | [`SubscriptionScheduleSettings`](../../doc/models/subscription-schedule-settings.md) | Optional | Schedule settings applied to a subscription. |
| `only_direct_currency` | `bool` | Optional | Whether only direct currency processing is allowed. |
| `first_charge_capture_after` | `str` | Optional | ISO-8601 Duration (e.g., P3D). |
| `first_charge_authorization_only` | `bool` | Optional | Whether the first charge is authorization-only. |
| `status` | [`SubscriptionStatus`](../../doc/models/subscription-status.md) | Optional | Subscription Status schema. |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `mode` | [`ChargeMode`](../../doc/models/charge-mode.md) | Optional | Charge Mode schema. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `three_ds` | [`SubscriptionThreeDs`](../../doc/models/subscription-three-ds.md) | Optional | 3-D Secure configuration and redirect details applied to the subscription's payments. |
| `period` | [`SubscriptionPeriod`](../../doc/models/subscription-period.md) | Optional | Subscription Period schema. |
| `cyclical_period` | `str` | Optional | ISO-8601 Duration for a custom billing frequency (e.g., P3D, P1M), returned instead of `period` when the subscription uses a custom cycle length rather than one of the fixed period presets. Mutually exclusive with `period` — exactly one of the two is present. |
| `next_payment` | [`SubscriptionNextPayment`](../../doc/models/subscription-next-payment.md) | Optional | Next scheduled payment details for a subscription. |
| `cycles_left` | `int` | Optional | Number of remaining billing cycles before the subscription completes. Only present for cycle-limited plans (`subscription_plan` or `installment_plan`); `null` for indefinite subscriptions.<br><br>**Constraints**: `>= 0` |
| `subscription_plan` | [`SubscriptionPlanSettings`](../../doc/models/subscription-plan-settings.md) | Optional | Configuration for limited-cycle subscriptions (Univapay side). |
| `installment_plan` | [`SubscriptionInstallmentPlanResponse`](../../doc/models/subscription-installment-plan-response.md) | Optional | Installment plan applied to the subscription, as returned by the API. Covers both card-network installment plans (`revolving`, `fixed_cycles`) and legacy fixed-amount installment plans (`fixed_cycle_amount`). |
| `charge_id` | `uuid\|str` | Optional | Identifier of the charge associated with the subscription's installment plan. Only present when `installment_plan` is set. |
| `amount_left` | `int` | Optional | Remaining amount to be charged over the life of the plan, in the smallest currency unit. Only present for cycle-limited plans.<br><br>**Constraints**: `>= 0` |
| `amount_left_formatted` | `float` | Optional | `amount_left` formatted for display. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.charge_mode import ChargeMode
from univapayclientsdk.models.combined_installment_fixed_cycles import CombinedInstallmentFixedCycles
from univapayclientsdk.models.combined_plan_type import CombinedPlanType
from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.plan_settings_type import PlanSettingsType
from univapayclientsdk.models.subscription import Subscription
from univapayclientsdk.models.subscription_installment_plan_response import SubscriptionInstallmentPlanResponse
from univapayclientsdk.models.subscription_next_payment import SubscriptionNextPayment
from univapayclientsdk.models.subscription_period import SubscriptionPeriod
from univapayclientsdk.models.subscription_plan_settings import SubscriptionPlanSettings
from univapayclientsdk.models.subscription_schedule_settings import SubscriptionScheduleSettings
from univapayclientsdk.models.subscription_status import SubscriptionStatus
from univapayclientsdk.models.subscription_termination_mode import SubscriptionTerminationMode
from univapayclientsdk.models.subscription_three_ds import SubscriptionThreeDs
from univapayclientsdk.models.subscription_three_ds_mode import SubscriptionThreeDsMode

subscription = Subscription(
    id='11ef335e-9aa5-c54a-8313-7f9847da313a',
    store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
    transaction_token_id='11ef32a7-3a71-8662-803f-1bc27702eeec',
    amount=1250,
    currency='USD',
    amount_formatted=12.5,
    schedule_settings=SubscriptionScheduleSettings(
        start_on=dateutil.parser.parse('2016-03-13').date(),
        zone_id='zone_id8',
        preserve_end_of_month=False,
        retry_interval='retry_interval2',
        termination_mode=SubscriptionTerminationMode.IMMEDIATE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    only_direct_currency=False,
    first_charge_authorization_only=False,
    status=SubscriptionStatus.CURRENT,
    metadata=GenericMetadata(
        order_id='12345',
        univapay_name='univapay-name8',
        univapay_phone_number='univapay-phone-number2',
        additional_properties={
            'exampleAdditionalProperty': 'String4'
        }
    ),
    mode=ChargeMode.LIVE,
    created_on=dateutil.parser.parse('2024-06-26T01:51:28.627023Z'),
    three_ds=SubscriptionThreeDs(
        mode=SubscriptionThreeDsMode.NORMAL,
        redirect_endpoint='redirect_endpoint8',
        redirect_id='000023a4-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    period=SubscriptionPeriod.MONTHLY,
    next_payment=SubscriptionNextPayment(
        id='00000110-0000-0000-0000-000000000000',
        due_date=dateutil.parser.parse('2016-03-13').date(),
        zone_id='zone_id8',
        amount=126,
        currency='currency8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    subscription_plan=SubscriptionPlanSettings(
        plan_type=PlanSettingsType.FIXED_CYCLES,
        fixed_cycles=46,
        fixed_cycle_amount=112,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    installment_plan=SubscriptionInstallmentPlanResponse(
        plan_type=CombinedPlanType.FIXED_CYCLES,
        fixed_cycles=CombinedInstallmentFixedCycles.CYCLES_12,
        fixed_cycles_amount=198,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

