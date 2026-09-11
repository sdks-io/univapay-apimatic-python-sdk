
# Online Transaction Token

Stored transaction token resource for an `online` payment type.

*This model accepts additional fields of type Any.*

## Structure

`OnlineTransactionToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `email` | `str` | Optional | Customer email address. |
| `active` | `bool` | Optional | Whether the resource is active. |
| `mode` | [`TransactionTokenMode`](../../doc/models/transaction-token-mode.md) | Optional | Transaction Token Mode schema. |
| `mtype` | [`TransactionTokenType`](../../doc/models/transaction-token-type.md) | Optional | Transaction Token Type schema. |
| `usage_limit` | `str` | Optional | Usage limit applied to the token. |
| `confirmed` | `bool` | Optional | Whether the token has been confirmed. |
| `metadata` | Dict[str, str \| None \| int \| float \| bool \| List[str \| None \| int \| float \| bool]] | Optional | Alias of GenericMetadataValue, retained because this schema name is part of the published SDK surface. Do not narrow it — see GenericMetadataValue for the contract. |
| `created_on` | `datetime` | Optional | Timestamp when the resource was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the resource was last updated. |
| `last_used_on` | `datetime` | Optional | Timestamp when the token was last used. |
| `payment_type` | `str` | Required, Constant | Payment method type. Always `online` for this variant.<br><br>**Value**: `"online"` |
| `data` | [`TokenResponseOnlineData`](../../doc/models/token-response-online-data.md) | Required | Token Response Online Data schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.base_online_data_brand import BaseOnlineDataBrand
from univapayclientsdk.models.base_online_data_call_method import BaseOnlineDataCallMethod
from univapayclientsdk.models.base_online_data_os_type import BaseOnlineDataOsType
from univapayclientsdk.models.base_online_data_user_identifier_source import BaseOnlineDataUserIdentifierSource
from univapayclientsdk.models.online_transaction_token import OnlineTransactionToken
from univapayclientsdk.models.token_response_online_data import TokenResponseOnlineData
from univapayclientsdk.models.transaction_token_mode import TransactionTokenMode
from univapayclientsdk.models.transaction_token_type import TransactionTokenType

online_transaction_token = OnlineTransactionToken(
    data=TokenResponseOnlineData(
        brand=BaseOnlineDataBrand.WE_CHAT_ONLINE,
        call_method=BaseOnlineDataCallMethod.WEB,
        os_type=BaseOnlineDataOsType.ANDROID,
        user_identifier='wechat_open_id_12345',
        user_identifier_source=BaseOnlineDataUserIdentifierSource.PROVIDED,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

