
# Token Response Card Data

Token Response Card Data schema.

*This model accepts additional fields of type Any.*

## Structure

`TokenResponseCardData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card` | [`TokenResponseCardDataCard`](../../doc/models/token-response-card-data-card.md) | Optional | Token Response Card Data Card schema. |
| `billing` | [`TokenResponseCardDataBilling`](../../doc/models/token-response-card-data-billing.md) | Optional | Token Response Card Data Billing schema. |
| `cvv_authorize` | [`TokenResponseCardDataCvvAuthorize`](../../doc/models/token-response-card-data-cvv-authorize.md) | Optional | Token Response Card Data Cvv Authorize schema. |
| `cvv_authorize_check` | [`TokenResponseCardDataCvvAuthorizeCheck`](../../doc/models/token-response-card-data-cvv-authorize-check.md) | Optional | Token Response Card Data Cvv Authorize Check schema. |
| `three_ds` | [`TokenResponseCardDataThreeDs`](../../doc/models/token-response-card-data-three-ds.md) | Optional | Token Response Card Data Three Ds schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.token_response_card_data import TokenResponseCardData
from univapayclientsdk.models.token_response_card_data_billing import TokenResponseCardDataBilling
from univapayclientsdk.models.token_response_card_data_card import TokenResponseCardDataCard
from univapayclientsdk.models.token_response_card_data_cvv_authorize import TokenResponseCardDataCvvAuthorize
from univapayclientsdk.models.token_response_card_data_cvv_authorize_check import TokenResponseCardDataCvvAuthorizeCheck
from univapayclientsdk.models.token_response_card_data_three_ds import TokenResponseCardDataThreeDs
from univapayclientsdk.models.token_response_card_data_three_ds_status import TokenResponseCardDataThreeDsStatus
from univapayclientsdk.models.token_response_phone_number import TokenResponsePhoneNumber

token_response_card_data = TokenResponseCardData(
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
            local_number='08012341234'
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
)
```

