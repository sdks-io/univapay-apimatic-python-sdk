
# Base Online Data

Base Online Data schema.

*This model accepts additional fields of type Any.*

## Structure

`BaseOnlineData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | [`BaseOnlineDataBrand`](../../doc/models/base-online-data-brand.md) | Optional | Base Online Data Brand schema. `alipay_china`, `alipay_hk`, `gcash`, `dana`, `truemoney`, `kakaopay`, `tng`, `rabbit_line_pay`, `bpi`, `boost`, `tinaba`, `naver_pay`, `toss_pay`, `maya`, `grab_sg`, `kredivo_id`, `k_plus`, and `kaspi_kz` are Alipay+ regional wallets routed through the `alipay_plus_online` gateway family. |
| `call_method` | [`BaseOnlineDataCallMethod`](../../doc/models/base-online-data-call-method.md) | Optional | Base Online Data Call Method schema. |
| `os_type` | [`BaseOnlineDataOsType`](../../doc/models/base-online-data-os-type.md) | Optional | Base Online Data Os Type schema. |
| `user_identifier` | `str` | Optional | Consumer specific identifier required by some gateways for fraud prevention. |
| `user_identifier_source` | [`BaseOnlineDataUserIdentifierSource`](../../doc/models/base-online-data-user-identifier-source.md) | Optional | The source of the user identifier |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.base_online_data import BaseOnlineData

base_online_data = BaseOnlineData()
```

