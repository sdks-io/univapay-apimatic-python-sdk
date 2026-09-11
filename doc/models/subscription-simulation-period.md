
# Subscription Simulation Period

Billing frequency for the simulated schedule. Includes `bimonthly`, which is not offered on `SubscriptionPeriod` for live subscription creation.

## Enumeration

`SubscriptionSimulationPeriod`

## Fields

| Name |
|  --- |
| `DAILY` |
| `WEEKLY` |
| `BIWEEKLY` |
| `MONTHLY` |
| `BIMONTHLY` |
| `QUARTERLY` |
| `SEMIANNUALLY` |
| `ANNUALLY` |

## Example

```python
from univapayclientsdk.models.subscription_simulation_period import SubscriptionSimulationPeriod

subscription_simulation_period = SubscriptionSimulationPeriod.DAILY
```

