
# Token Response Online Data

Token Response Online Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseOnlineData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand` | [`BaseOnlineDataBrand`](../../doc/models/base-online-data-brand.md) | Optional | Base Online Data Brand schema. |
| `call_method` | [`BaseOnlineDataCallMethod`](../../doc/models/base-online-data-call-method.md) | Optional | Base Online Data Call Method schema. |
| `os_type` | [`BaseOnlineDataOsType`](../../doc/models/base-online-data-os-type.md) | Optional | Base Online Data Os Type schema. |
| `user_identifier` | `str` | Optional | Consumer specific identifier required by some gateways for fraud prevention. |
| `user_identifier_source` | [`BaseOnlineDataUserIdentifierSource`](../../doc/models/base-online-data-user-identifier-source.md) | Optional | The source of the user identifier |
| `issuer_token` | `str` | Optional | Token provided by the issuer (if applicable). |
| `issuer_token_payload` | `str` | Optional | Additional payload from the issuer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.base_online_data_brand import BaseOnlineDataBrand
from univapayclientsdk.models.base_online_data_call_method import BaseOnlineDataCallMethod
from univapayclientsdk.models.base_online_data_os_type import BaseOnlineDataOsType
from univapayclientsdk.models.base_online_data_user_identifier_source import BaseOnlineDataUserIdentifierSource
from univapayclientsdk.models.token_response_online_data import TokenResponseOnlineData

token_response_online_data = TokenResponseOnlineData(
    brand=BaseOnlineDataBrand.WE_CHAT_ONLINE,
    call_method=BaseOnlineDataCallMethod.WEB,
    os_type=BaseOnlineDataOsType.ANDROID,
    user_identifier='wechat_open_id_12345',
    user_identifier_source=BaseOnlineDataUserIdentifierSource.PROVIDED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

