
# Restrict Ip After Failed Charge Config

IP restriction policy applied after repeated failed charges.

*This model accepts additional fields of type Any.*

## Structure

`RestrictIpAfterFailedChargeConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Enables temporary IP restrictions after repeated failures. |
| `count` | `int` | Optional | Number of failed charges allowed before restriction starts. |
| `cooldown` | `str` | Optional | ISO-8601 duration that the IP restriction remains active. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.restrict_ip_after_failed_charge_config import RestrictIpAfterFailedChargeConfig

restrict_ip_after_failed_charge_config = RestrictIpAfterFailedChargeConfig(
    enabled=True,
    count=5,
    cooldown='PT1H',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

