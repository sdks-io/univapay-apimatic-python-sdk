
# Webhook List

Paginated list of webhooks.

*This model accepts additional fields of type Any.*

## Structure

`WebhookList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[Webhook]`](../../doc/models/webhook.md) | Optional | List of resources. |
| `has_more` | `bool` | Optional | Whether more results are available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.webhook import Webhook
from univapayclientsdk.models.webhook_list import WebhookList
from univapayclientsdk.models.webhook_trigger import WebhookTrigger

webhook_list = WebhookList(
    items=[
        Webhook(
            id='d3e4f5a6-b7c8-9012-def0-123456789abc',
            store_id='76cf4a64-02bc-4cb3-9a28-74622e5928a1',
            merchant_id='01234567-89ab-cdef-0123-456789abcdef',
            triggers=[
                WebhookTrigger.CHARGE_FINISHED,
                WebhookTrigger.REFUND_FINISHED
            ],
            url='https://example.com/webhooks/payments',
            auth_token='my-secret-token',
            active=True,
            is_integration=False,
            created_on=dateutil.parser.parse('2026-04-01T00:00:00.000000Z'),
            updated_on=dateutil.parser.parse('2026-04-02T00:00:00.000000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Webhook(
            id='e4f5a6b7-c8d9-0123-ef01-23456789abcd',
            store_id='76cf4a64-02bc-4cb3-9a28-74622e5928a1',
            merchant_id='01234567-89ab-cdef-0123-456789abcdef',
            triggers=[
                WebhookTrigger.SUBSCRIPTION_PAYMENT,
                WebhookTrigger.SUBSCRIPTION_FAILURE
            ],
            url='https://example.com/webhooks/subscriptions',
            auth_token=None,
            active=True,
            is_integration=False,
            created_on=dateutil.parser.parse('2026-04-03T08:30:00.000000Z'),
            updated_on=dateutil.parser.parse('2026-04-03T08:30:00.000000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

