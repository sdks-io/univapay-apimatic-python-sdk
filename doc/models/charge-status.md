
# Charge Status

Charge Status schema.

## Enumeration

`ChargeStatus`

## Fields

| Name |
|  --- |
| `PENDING` |
| `AWAITING` |
| `AUTHORIZED` |
| `SUCCESSFUL` |
| `FAILED` |
| `ERROR` |
| `CANCELED` |

## Example

```python
from univapayclientsdk.models.charge_status import ChargeStatus

charge_status = ChargeStatus.ERROR
```

