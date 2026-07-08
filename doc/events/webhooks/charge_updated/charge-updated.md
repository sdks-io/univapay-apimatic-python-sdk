
# Charge Updated

Fired whenever a charge transitions to a new status (e.g., `pending` → `awaiting`). The `data` field contains the full Charge object at the time of the event.

## Headers

This event's request contains the following headers.

| Name | Description |
|  --- | --- |
| Idempotency-Key | An optional idempotency key to prevent double charges and duplicate operations. We recommend a randomly generated UUID (v4). |
| Content-Type |  |

## Payload Type

This event's request payload is of type [ChargeUpdatedWebhookCallback](../../../../doc/models/charge-updated-webhook-callback.md).

## Payload Example

```json
{
  "id": "11ef0000-0000-4000-8000-000000000001",
  "event": "charge_updated",
  "data": {
    "id": "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98",
    "store_id": "11edf541-c42d-653c-8c3d-dfe0a55f95c0",
    "transaction_token_id": "11ef32a7-3a71-8662-803f-1bc27702eeec",
    "transaction_token_type": "recurring",
    "subscription_id": "11ef335e-9aa5-c54a-8313-7f9847da313a",
    "requested_amount": 1250,
    "requested_currency": "USD",
    "requested_amount_formatted": 12.5,
    "charged_amount": 1250,
    "charged_currency": "USD",
    "charged_amount_formatted": 12.5,
    "only_direct_currency": false,
    "status": "successful",
    "error": null,
    "mode": "test",
    "created_on": "2024-06-26T01:51:30.000000Z",
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
from univapayclientsdk.events.webhooks.charge_updated_handler import (
    ChargeUpdatedHandler,
)
from univapayclientsdk.models.charge_updated_webhook_callback import (
    ChargeUpdatedWebhookCallback,
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
    event = ChargeUpdatedHandler.parse_event(core_req)

    # Step 3: Pattern match for chargeUpdated only.
    if (
        isinstance(event, ChargeUpdatedWebhookCallback) and
        getattr(event, "event", None) == "charge_updated"
    ):
        print("chargeUpdated received")
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

