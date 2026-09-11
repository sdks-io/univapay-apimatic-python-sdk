
# Card Transaction Token

Stored transaction token resource for a `card` payment type.

*This model accepts additional fields of type Any.*

## Structure

`CardTransactionToken`

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
| `payment_type` | `str` | Required, Constant | Payment method type. Always `card` for this variant.<br><br>**Value**: `"card"` |
| `data` | [`TokenResponseCardData`](../../doc/models/token-response-card-data.md) | Required | Token Response Card Data schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.card_transaction_token import CardTransactionToken
from univapayclientsdk.models.token_response_card_data import TokenResponseCardData
from univapayclientsdk.models.token_response_card_data_billing import TokenResponseCardDataBilling
from univapayclientsdk.models.token_response_card_data_card import TokenResponseCardDataCard
from univapayclientsdk.models.token_response_card_data_cvv_authorize import TokenResponseCardDataCvvAuthorize
from univapayclientsdk.models.token_response_card_data_cvv_authorize_check import TokenResponseCardDataCvvAuthorizeCheck
from univapayclientsdk.models.token_response_card_data_three_ds import TokenResponseCardDataThreeDs
from univapayclientsdk.models.token_response_card_data_three_ds_status import TokenResponseCardDataThreeDsStatus
from univapayclientsdk.models.token_response_phone_number import TokenResponsePhoneNumber
from univapayclientsdk.models.transaction_token_mode import TransactionTokenMode
from univapayclientsdk.models.transaction_token_type import TransactionTokenType

card_transaction_token = CardTransactionToken(
    data=TokenResponseCardData(
        card=TokenResponseCardDataCard(
            cardholder='TARO YAMADA',
            exp_month=12,
            exp_year=2026,
            card_bin='424242',
            last_four='4242',
            brand='visa',
            card_type='credit',
            country='JP',
            category='standard',
            issuer=None,
            sub_brand='none',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        billing=TokenResponseCardDataBilling(
            line_1='1-1-1',
            line_2='Shibakoen',
            state='Tokyo',
            city='Minato',
            country='JP',
            zip='105-0011',
            phone_number=TokenResponsePhoneNumber(
                country_code=81,
                local_number='08012341234',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        cvv_authorize=TokenResponseCardDataCvvAuthorize(
            enabled=True,
            status='successful',
            charge_id=None,
            credentials_id=None,
            currency='JPY',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        cvv_authorize_check=TokenResponseCardDataCvvAuthorizeCheck(
            status='successful',
            charge_id=None,
            date=dateutil.parser.parse('2026-04-09T07:35:50Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        three_ds=TokenResponseCardDataThreeDs(
            enabled=True,
            status=TokenResponseCardDataThreeDsStatus.SUCCESSFUL,
            redirect_endpoint=None,
            redirect_id=None,
            exempted=False,
            error=None,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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

