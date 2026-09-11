
# Customs Declaration Webhook Result

Result payload returned by the customs declaration formatter.

*This model accepts additional fields of type Any.*

## Structure

`CustomsDeclarationWebhookResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `approving_authority` | `str` | Optional | Customs authority that approved the declaration. |
| `trade_id` | `str` | Optional | Gateway trade identifier. |
| `transaction_id` | `str` | Optional | Gateway transaction identifier for customs. |
| `charge_transaction_id` | `str` | Optional | Gateway charge transaction identifier linked to the declaration. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.customs_declaration_webhook_result import CustomsDeclarationWebhookResult

customs_declaration_webhook_result = CustomsDeclarationWebhookResult(
    approving_authority='TOKYO',
    trade_id='wx_trade_12345',
    transaction_id='wx_txn_12345',
    charge_transaction_id='wx_charge_12345'
)
```

