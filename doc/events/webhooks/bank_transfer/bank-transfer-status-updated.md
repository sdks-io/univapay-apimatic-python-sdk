
# Bank Transfer Status Updated

Fired when the payment status of a bank transfer charge changes (e.g., when a deposit is received and matched against the expected amount). The `data` field contains a `BankTransferStatusData` object with the extension record, deposit amounts, and originating charge/token metadata.

## Headers

This event's request contains the following headers.

| Name | Description |
|  --- | --- |
| Idempotency-Key | An optional idempotency key to prevent double charges and duplicate operations. We recommend a randomly generated UUID (v4). |
| Content-Type |  |

## Payload Type

This event's request payload is of type [BankTransferStatusWebhookCallback](../../../../doc/models/bank-transfer-status-webhook-callback.md).

## Payload Example

```json
{
  "id": "11ef0000-0000-4000-8000-000000000001",
  "event": "bank_transfer_status_updated",
  "data": {
    "id": "11ef0000-0000-4000-8000-000000000002",
    "charge_id": "11ef0000-0000-4000-8000-000000000001",
    "payment_status": "exact",
    "latest_deposit_date": "2026-04-09T07:35:50.000000Z",
    "created_on": "2026-04-09T07:35:50.000000Z",
    "latest_deposit_amount": 1000,
    "balance": 0,
    "currency": "JPY",
    "amount": 1000,
    "amount_difference": 0,
    "token_metadata": {
      "order_id": "12345"
    },
    "charge_metadata": {
      "order_id": "order_12345"
    },
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
from univapayclientsdk.events.webhooks.bank_transfer_handler import (
    BankTransferHandler,
)
from univapayclientsdk.models.bank_transfer_status_webhook_callback import (
    BankTransferStatusWebhookCallback,
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
    event = BankTransferHandler.parse_event(core_req)

    # Step 3: Pattern match for bankTransferStatusUpdated only.
    if (
        isinstance(event, BankTransferStatusWebhookCallback) and
        getattr(event, "event", None) == "bank_transfer_status_updated"
    ):
        print("bankTransferStatusUpdated received")
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

