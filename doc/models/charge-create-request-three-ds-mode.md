
# Charge Create Request Three Ds Mode

3D-Secure authentication type. App Token Secret is required to use 'skip'.

## Enumeration

`ChargeCreateRequestThreeDsMode`

## Fields

| Name |
|  --- |
| `NORMAL` |
| `REQUIRE` |
| `FORCE` |
| `SKIP` |

## Example

```python
from univapayclientsdk.models.charge_create_request_three_ds_mode import ChargeCreateRequestThreeDsMode

charge_create_request_three_ds_mode = ChargeCreateRequestThreeDsMode.FORCE
```

