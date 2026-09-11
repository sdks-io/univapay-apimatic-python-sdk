
# Subscription Simulation Payment

A single scheduled payment produced by the subscription plan simulation.

*This model accepts additional fields of type Any.*

## Structure

`SubscriptionSimulationPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `due_date` | `date` | Optional | Scheduled due date for this simulated payment (YYYY-MM-DD). |
| `zone_id` | `str` | Optional | IANA timezone identifier used to resolve the due date. |
| `amount` | `int` | Optional | Amount to be charged on this cycle, in the smallest currency unit.<br><br>**Constraints**: `>= 0` |
| `currency` | `str` | Optional | ISO-4217 currency code. |
| `is_paid` | `bool` | Optional | Always `false` for simulated payments — no real payment has been made. |
| `is_last_payment` | `bool` | Optional | Whether this is the final payment in the simulated schedule. |
| `successful_payment_date` | `date` | Optional | Always `null` for simulated payments — populated only once a real payment settles. |
| `terminate_with_status` | [`TerminateWithStatus`](../../doc/models/terminate-with-status.md) | Optional | The status the subscription would transition to on this payment's due date, if a termination is scheduled. `null` when no termination applies. |
| `retry_interval` | `str` | Optional | ISO-8601 Duration for the retry interval applied if this payment fails (e.g., P5D). `null` if no retry interval is configured. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.subscription_simulation_payment import SubscriptionSimulationPayment

subscription_simulation_payment = SubscriptionSimulationPayment()
```

