
# Recurring Token Deleted

Fired when a recurring transaction token is deleted. The `data` field contains the deleted TransactionToken object.

## Headers

This event's request contains the following headers.

| Name | Description |
|  --- | --- |
| Idempotency-Key | An optional idempotency key to prevent double charges and duplicate operations. We recommend a randomly generated UUID (v4). |
| Content-Type |  |

## Payload Type

This event's request payload is of type [RecurringTokenDeletedWebhookCallback](../../../../doc/models/recurring-token-deleted-webhook-callback.md).

## Payload Example

```json
{
  "id": "11ef0000-0000-4000-8000-000000000001",
  "event": "recurring_token_deleted",
  "data": {
    "id": "6426bbd2-17bd-41bf-883b-1fe970db48ee",
    "store_id": "fc264608-9a9e-495e-844e-a08129a81af4",
    "email": "test@univapay.com",
    "payment_type": "card",
    "active": true,
    "mode": "live",
    "type": "recurring",
    "confirmed": true,
    "metadata": {
      "customer_id": "cust_12345"
    },
    "created_on": "2026-04-09T07:35:50.000000Z",
    "updated_on": "2026-04-09T07:35:50.000000Z",
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
from univapayclientsdk.events.webhooks.recurring_token_deleted_handler import (
    RecurringTokenDeletedHandler,
)
from univapayclientsdk.models.recurring_token_deleted_webhook_callback import (
    RecurringTokenDeletedWebhookCallback,
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
    event = RecurringTokenDeletedHandler.parse_event(core_req)

    # Step 3: Pattern match for recurringTokenDeleted only.
    if (
        isinstance(event, RecurringTokenDeletedWebhookCallback) and
        getattr(event, "event", None) == "recurring_token_deleted"
    ):
        print("recurringTokenDeleted received")
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

