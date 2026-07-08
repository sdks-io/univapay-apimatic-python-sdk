## Bank-Transfer Handler

Bank transfer status update events.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [bankTransferStatusUpdated](../../../doc/events/webhooks/bank_transfer/bank-transfer-status-updated.md) | Fired when the payment status of a bank transfer charge changes (e.g., when a deposit is received and matched against the expected amount). The `data` field contains a `BankTransferStatusData` object with the extension record, deposit amounts, and originating charge/token metadata. | bank_transfer_status_updated |

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
def Webhooks():
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = BankTransferHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
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

