
# Customs Declaration Webhook Data

Customs declaration payload delivered in `customs_declaration_finished` webhooks. Platform-level deliveries may include `platform_id` and `updated_on`.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationWebhookData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Customs declaration identifier. |
| `charge_id` | `uuid\|str` | Optional | Charge identifier associated with the declaration. |
| `merchant_id` | `uuid\|str` | Optional | Merchant identifier. |
| `store_id` | `uuid\|str` | Optional | Store identifier. |
| `platform_id` | `uuid\|str` | Optional | Platform identifier, included on platform-level deliveries. |
| `mode` | `str` | Optional | Processing mode. |
| `gateway` | `str` | Optional | Gateway that processed the declaration. |
| `declaration` | [`CustomsDeclarationWebhookDeclaration`](../../doc/models/customs-declaration-webhook-declaration.md) | Optional | WeChat customs declaration payload returned by the backend formatter. |
| `declaration_result` | [`CustomsDeclarationWebhookResult`](../../doc/models/customs-declaration-webhook-result.md) | Optional | Result payload returned by the customs declaration formatter. |
| `status` | [`CustomsDeclarationWebhookStatus`](../../doc/models/customs-declaration-webhook-status.md) | Optional | Customs declaration status returned by the backend. |
| `error` | [`CustomsDeclarationWebhookError`](../../doc/models/customs-declaration-webhook-error.md) | Optional | Error payload returned when customs declaration processing fails. |
| `created_on` | `datetime` | Optional | Timestamp when the declaration was created. |
| `updated_on` | `datetime` | Optional | Timestamp when the declaration was last updated, included on platform-level deliveries. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.customs_declaration_webhook_data import CustomsDeclarationWebhookData
from univapayclientsdk.models.customs_declaration_webhook_declaration import CustomsDeclarationWebhookDeclaration
from univapayclientsdk.models.customs_declaration_webhook_result import CustomsDeclarationWebhookResult
from univapayclientsdk.models.customs_declaration_webhook_status import CustomsDeclarationWebhookStatus

customs_declaration_webhook_data = CustomsDeclarationWebhookData(
    id='11ef0000-0000-4000-8000-000000000040',
    charge_id='11ef0000-0000-4000-8000-000000000001',
    merchant_id='11ef0000-0000-4000-8000-000000000020',
    store_id='11ef0000-0000-4000-8000-000000000022',
    platform_id='00001610-0000-0000-0000-000000000000',
    mode='test',
    gateway='wechat_online',
    declaration=CustomsDeclarationWebhookDeclaration(
        customs='TOKYO',
        merchant_customs_no='1234567890',
        certificate_id='AB1234567',
        certificate_name='TARO YAMADA'
    ),
    declaration_result=CustomsDeclarationWebhookResult(
        approving_authority='TOKYO',
        trade_id='wx_trade_12345',
        transaction_id='wx_txn_12345',
        charge_transaction_id='wx_charge_12345'
    ),
    status=CustomsDeclarationWebhookStatus.SUCCESSFUL,
    error=None,
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

