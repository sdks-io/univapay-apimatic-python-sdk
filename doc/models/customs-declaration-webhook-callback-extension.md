
# Customs Declaration Webhook Callback Extension

Customs-declaration-specific webhook payload extension.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationWebhookCallbackExtension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`CustomsDeclarationWebhookData`](../../doc/models/customs-declaration-webhook-data.md) | Optional | Customs declaration payload delivered in `customs_declaration_finished` webhooks. Platform-level deliveries may include `platform_id` and `updated_on`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.customs_declaration_webhook_callback_extension import CustomsDeclarationWebhookCallbackExtension
from univapayclientsdk.models.customs_declaration_webhook_data import CustomsDeclarationWebhookData
from univapayclientsdk.models.customs_declaration_webhook_declaration import CustomsDeclarationWebhookDeclaration
from univapayclientsdk.models.customs_declaration_webhook_result import CustomsDeclarationWebhookResult
from univapayclientsdk.models.customs_declaration_webhook_status import CustomsDeclarationWebhookStatus

customs_declaration_webhook_callback_extension = CustomsDeclarationWebhookCallbackExtension(
    data=CustomsDeclarationWebhookData(
        id='11ef0000-0000-4000-8000-000000000040',
        charge_id='11ef0000-0000-4000-8000-000000000001',
        merchant_id='11ef0000-0000-4000-8000-000000000020',
        store_id='11ef0000-0000-4000-8000-000000000022',
        platform_id='00000550-0000-0000-0000-000000000000',
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
        created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

