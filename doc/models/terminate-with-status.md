
# Terminate with Status

The status the subscription would transition to on this payment's due date, if a termination is scheduled. `null` when no termination applies.

## Enumeration

`TerminateWithStatus`

## Fields

| Name |
|  --- |
| `SUSPENDED` |
| `CANCELED` |

## Example

```python
from univapayclientsdk.models.terminate_with_status import TerminateWithStatus

terminate_with_status = TerminateWithStatus.SUSPENDED
```

