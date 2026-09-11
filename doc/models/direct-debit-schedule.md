
# Direct Debit Schedule

The key dates for one debit cycle. Use these to work out whether the current month's registration window is still open.

*This model accepts additional fields of type Any.*

## Structure

`DirectDebitSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_bank_account_transfer_date` | `date` | Optional | The date funds are pulled from consumer accounts (指定振替日). |
| `merchant_bank_account_registration_deadline` | `date` | Optional | The date by which the bank must receive the signed direct debit mandate (振替依頼書到着期限). |
| `merchant_bank_transfer_upload_deadline` | `date` | Optional | The last date transfers can be registered or edited for this cycle (振替データアップロード期限). After this, transfers lock. |
| `platform_result_registration_date` | `date` | Optional | The date transfer results are reflected on the platform (振替結果反映日). |
| `platform_scheduled_payout` | `date` | Optional | The date collected funds are paid out to the merchant (支払日). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.direct_debit_schedule import DirectDebitSchedule

direct_debit_schedule = DirectDebitSchedule(
    merchant_bank_account_transfer_date=dateutil.parser.parse('2026-03-14').date(),
    merchant_bank_account_registration_deadline=dateutil.parser.parse('2026-02-20').date(),
    merchant_bank_transfer_upload_deadline=dateutil.parser.parse('2026-03-04').date(),
    platform_result_registration_date=dateutil.parser.parse('2026-03-24').date(),
    platform_scheduled_payout=dateutil.parser.parse('2026-03-31').date(),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

