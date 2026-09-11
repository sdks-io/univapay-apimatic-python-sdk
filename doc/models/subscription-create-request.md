
# Subscription Create Request

Request payload for creating a subscription.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_token_id` | `uuid\|str` | Required | Transaction token ID authorized for recurring payments. |
| `amount` | `int` | Required | Amount to be charged in each cycle. |
| `currency` | `str` | Required | ISO-4217 currency code. |
| `initial_amount` | `int` | Optional | Optional different amount for the first charge. |
| `period` | [`SubscriptionPeriod`](../../doc/models/subscription-period.md) | Optional | Subscription Period schema. |
| `cyclical_period` | `str` | Optional | ISO-8601 Duration for custom frequency (e.g., P3D, P2M).  Cannot be used if 'period' is specified. |
| `schedule_settings` | [`SubscriptionScheduleSettings`](../../doc/models/subscription-schedule-settings.md) | Optional | Schedule settings applied to a subscription. |
| `installment_plan` | [`SubscriptionInstallmentPlan`](../../doc/models/subscription-installment-plan.md) | Optional | Configuration for credit card company side installments. |
| `subscription_plan` | [`SubscriptionPlanSettings`](../../doc/models/subscription-plan-settings.md) | Optional | Configuration for limited-cycle subscriptions (Univapay side). |
| `first_charge_authorization_only` | `bool` | Optional | If true, the first charge will only be an authorization (Hold).<br><br>**Default**: `False` |
| `first_charge_capture_after` | `str` | Optional | ISO-8601 Duration for auto-capture if authorization only is true.  Allowed days: P1D to P6D. |
| `metadata` | [`GenericMetadata`](../../doc/models/generic-metadata.md) | Optional | A free-form dictionary for custom metadata. |
| `three_ds` | [`ChargeCreateRequestThreeDs`](../../doc/models/charge-create-request-three-ds.md) | Optional | Charge Create Request Three Ds schema. Either supply `mode` (and optionally `redirect_endpoint`) to have Univapay run 3DS, or supply all six external-MPI fields (`authentication_value` through `transaction_status`) when 3DS authentication was already completed outside of Univapay — in that case `mode` is set to `provided` automatically and must not be sent. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.subscription_create_request import SubscriptionCreateRequest
from univapayclientsdk.models.subscription_period import SubscriptionPeriod

subscription_create_request = SubscriptionCreateRequest(
    transaction_token_id='11ef32a7-3a71-8662-803f-1bc27702eeec',
    amount=1250,
    currency='USD',
    period=SubscriptionPeriod.MONTHLY
)
```

