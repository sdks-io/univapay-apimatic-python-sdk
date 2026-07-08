
# Transaction Token Create Request Metadata

A free-form dictionary for custom metadata.

*This model accepts additional fields of type [str | bool | float](../../doc/models/containers/transaction-token-create-metadata-props.md).*

## Structure

`TransactionTokenCreateRequestMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `univapay_reference_id` | `str` | Optional | Any arbitrary value (Free format). |
| `univapay_customer_id` | `uuid\|str` | Optional | Customer ID. |
| `univapay_name` | `str` | Optional | Consumer name passed to payment processors that require it (e.g., konbini, bank transfer). |
| `univapay_phone_number` | `str` | Optional | Consumer phone number passed to payment processors that require it. |
| `additional_properties` | Dict[str, str \| bool \| float] | Optional | Transaction Token Create Metadata Props schema. |

## Example

```python
from univapayclientsdk.models.transaction_token_create_request_metadata import TransactionTokenCreateRequestMetadata

transaction_token_create_request_metadata = TransactionTokenCreateRequestMetadata(
    univapay_reference_id='ref-998877',
    univapay_customer_id='0fd29949-07d5-4a91-8eaf-fbce0897d944',
    univapay_name='univapay-name6',
    univapay_phone_number='univapay-phone-number0',
    additional_properties={
        'exampleAdditionalProperty': 'String8'
    }
)
```

