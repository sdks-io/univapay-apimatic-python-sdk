
# Subscription Suspended

Fired when a subscription is suspended (paused). The `data` field contains the full Subscription object.

## Headers

This event's request contains the following headers.

| Name | Description |
|  --- | --- |
| Idempotency-Key | An optional idempotency key to prevent double charges and duplicate operations. We recommend a randomly generated UUID (v4). |
| Content-Type |  |

## Payload Type

This event's request payload is of type [SubscriptionWebhookEvent](../../../../doc/models/subscription-webhook-event.md).

## Payload Example

```json
{
  "id": "11ef0000-0000-4000-8000-000000000001",
  "event": "subscription_suspended",
  "data": {
    "id": "11ef335e-9aa5-c54a-8313-7f9847da313a",
    "store_id": "11edf541-c42d-653c-8c3d-dfe0a55f95c0",
    "transaction_token_id": "11ef32a7-3a71-8662-803f-1bc27702eeec",
    "amount": 1250,
    "currency": "USD",
    "amount_formatted": 12.5,
    "schedule_settings": {
      "start_on": "2024-07-01",
      "zone_id": "Asia/Tokyo",
      "preserve_end_of_month": false,
      "retry_interval": "P7D",
      "termination_mode": "on_next_payment"
    },
    "only_direct_currency": false,
    "first_charge_authorization_only": false,
    "status": "current",
    "metadata": {
      "order_id": "12345"
    },
    "mode": "test",
    "created_on": "2024-06-26T01:51:28.627023Z",
    "period": "monthly",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "created_on": "2026-04-09T07:35:50.000000Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

## SDK Usage Example

```python
from flask import (
    Flask,
    Response,
    request,
)

from univapayclientsdk.events.unknown_event import (
    UnknownEvent,
)
from univapayclientsdk.events.webhooks.subscription_handler import (
    SubscriptionHandler,
)
from univapayclientsdk.models.subscription_webhook_event import (
    SubscriptionWebhookEvent,
)
from univapayclientsdk.utilities.request_adapter import (
    to_core_request,
)

app = Flask(__name__)

@app.route("/webhooks", methods=[
    "POST",
])
def Webhooks() -> Response:
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = SubscriptionHandler.parse_event(core_req)

    # Step 3: Pattern match for subscriptionSuspended only.
    if (
        isinstance(event, SubscriptionWebhookEvent) and
        getattr(event, "event", None) == "subscription_suspended"
    ):
        print("subscriptionSuspended received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

## Accepted Server Responses

The server should responds with one of the following status codes:

| Status Code | Description |
|  --- | --- |
| 200 | Return 200 to acknowledge receipt of the event. Returns an empty JSON object. |

