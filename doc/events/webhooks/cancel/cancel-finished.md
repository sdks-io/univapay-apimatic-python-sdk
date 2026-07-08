
# Cancel Finished

Fired when a cancellation request reaches a terminal status (`successful`, `failed`, `error`). The `data` field contains the full Cancel object.

## Headers

This event's request contains the following headers.

| Name | Description |
|  --- | --- |
| Idempotency-Key | An optional idempotency key to prevent double charges and duplicate operations. We recommend a randomly generated UUID (v4). |
| Content-Type |  |

## Payload Type

This event's request payload is of type [CancelWebhookCallback](../../../../doc/models/cancel-webhook-callback.md).

## Payload Example

```json
{
  "id": "11ef0000-0000-4000-8000-000000000001",
  "event": "cancel_finished",
  "data": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "charge_id": "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98",
    "store_id": "76cf4a64-02bc-4cb3-9a28-74622e5928a1",
    "status": "successful",
    "error": null,
    "metadata": {
      "order_id": "order_12345"
    },
    "mode": "live",
    "created_on": "2026-04-09T07:35:50.000000Z",
    "updated_on": "2026-04-09T07:36:00.000000Z",
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
from univapayclientsdk.events.webhooks.cancel_handler import (
    CancelHandler,
)
from univapayclientsdk.models.cancel_webhook_callback import (
    CancelWebhookCallback,
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
    event = CancelHandler.parse_event(core_req)

    # Step 3: Pattern match for cancelFinished only.
    if (
        isinstance(event, CancelWebhookCallback) and
        getattr(event, "event", None) == "cancel_finished"
    ):
        print("cancelFinished received")
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

