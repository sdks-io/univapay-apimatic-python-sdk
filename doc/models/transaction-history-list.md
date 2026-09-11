
# Transaction History List

Paginated list of transaction history rows. Unlike other list responses in this API, `total_hits` is only present on the first page (no `cursor` supplied) or the last page, and `next_cursor` is only present while `has_more` is `true`.

*This model accepts additional fields of type Any.*

## Structure

`TransactionHistoryList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[TransactionHistoryItem]`](../../doc/models/transaction-history-item.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `total_hits` | `int` | Optional | Total number of matching resources. Present on the first page (no `cursor` supplied) or the last page; absent on intermediate pages while `has_more` is `true`. |
| `next_cursor` | `uuid\|str` | Optional | Cursor to pass as `cursor` to fetch the next page. Present only while `has_more` is `true`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.generic_metadata import GenericMetadata
from univapayclientsdk.models.transaction_history_charge_type import TransactionHistoryChargeType
from univapayclientsdk.models.transaction_history_item import TransactionHistoryItem
from univapayclientsdk.models.transaction_history_list import TransactionHistoryList
from univapayclientsdk.models.transaction_history_mode import TransactionHistoryMode
from univapayclientsdk.models.transaction_history_payment_type import TransactionHistoryPaymentType
from univapayclientsdk.models.transaction_history_refund import TransactionHistoryRefund
from univapayclientsdk.models.transaction_history_refund_reason import TransactionHistoryRefundReason
from univapayclientsdk.models.transaction_history_refund_status import TransactionHistoryRefundStatus
from univapayclientsdk.models.transaction_history_service_provider import TransactionHistoryServiceProvider
from univapayclientsdk.models.transaction_history_status import TransactionHistoryStatus
from univapayclientsdk.models.transaction_history_type import TransactionHistoryType
from univapayclientsdk.models.transaction_history_user_data import TransactionHistoryUserData

transaction_history_list = TransactionHistoryList(
    items=[
        TransactionHistoryItem(
            store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
            resource_id='11ef0000-0000-4000-8000-000000000070',
            charge_id=None,
            amount=1000,
            currency='JPY',
            amount_formatted=1000,
            mtype=TransactionHistoryType.CHARGE,
            status=TransactionHistoryStatus.SUCCESSFUL,
            metadata=GenericMetadata(
                order_id='order_id0',
                univapay_name='univapay-name8',
                univapay_phone_number='univapay-phone-number2',
                additional_properties={
                    'exampleAdditionalProperty': 'String4'
                }
            ),
            created_on=dateutil.parser.parse('2024-05-01T12:34:56.789Z'),
            mode=TransactionHistoryMode.TEST,
            merchant_name='Test merchant',
            store_name='Test store',
            payment_type=TransactionHistoryPaymentType.CARD,
            user_data=TransactionHistoryUserData(
                mtype=TransactionHistoryType.CHARGE,
                cardholder_name='Some Guy',
                cardholder_email_address='test4@univapay.com',
                cardholder_phone_number='cardholder_phone_number4',
                customer_name='customer_name8',
                brand='visa',
                gateway='test',
                service_provider=TransactionHistoryServiceProvider.CREDIT,
                refunds=[
                    TransactionHistoryRefund(
                        refund_id='11ef0000-0000-4000-8000-000000000010',
                        amount=500,
                        currency='JPY',
                        amount_formatted=500,
                        status=TransactionHistoryRefundStatus.SUCCESSFUL,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            bank_transfer_payment_status=None,
            bank_transfer_latest_deposit_date=None,
            mcp_token_id=None,
            charge_type=TransactionHistoryChargeType.NORMAL,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TransactionHistoryItem(
            store_id='11edf541-c42d-653c-8c3d-dfe0a55f95c0',
            resource_id='11ef0000-0000-4000-8000-000000000010',
            charge_id='11ef0000-0000-4000-8000-000000000070',
            amount=500,
            currency='JPY',
            amount_formatted=500,
            mtype=TransactionHistoryType.REFUND,
            status=TransactionHistoryStatus.SUCCESSFUL,
            metadata=GenericMetadata(
                order_id='order_id0',
                univapay_name='univapay-name8',
                univapay_phone_number='univapay-phone-number2',
                additional_properties={
                    'exampleAdditionalProperty': 'String4'
                }
            ),
            created_on=dateutil.parser.parse('2024-05-01T13:00:00.000000Z'),
            mode=TransactionHistoryMode.TEST,
            merchant_name='Test merchant',
            store_name='Test store',
            payment_type=TransactionHistoryPaymentType.CARD,
            user_data=TransactionHistoryUserData(
                mtype=TransactionHistoryType.REFUND,
                cardholder_name='cardholder_name8',
                cardholder_email_address='cardholder_email_address0',
                cardholder_phone_number='cardholder_phone_number4',
                customer_name='customer_name8',
                reason=TransactionHistoryRefundReason.CUSTOMER_REQUEST,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            bank_transfer_payment_status=None,
            bank_transfer_latest_deposit_date=None,
            mcp_token_id=None,
            charge_type=None,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    total_hits=2,
    next_cursor='11ef0000-0000-4000-8000-000000000071',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

