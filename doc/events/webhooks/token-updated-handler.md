## Token Updated Handler

Token updated event.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [tokenUpdated](../../../doc/events/webhooks/token_updated/token-updated.md) | Fired when a transaction token is updated (e.g., metadata change). The `data` field contains the full TransactionToken object. | token_updated |

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
from univapayclientsdk.events.webhooks.token_updated_handler import (
    TokenUpdatedHandler,
)
from univapayclientsdk.models.token_updated_webhook_callback import (
    TokenUpdatedWebhookCallback,
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
    event = TokenUpdatedHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if (
        isinstance(event, TokenUpdatedWebhookCallback) and
        getattr(event, "event", None) == "token_updated"
    ):
        print("tokenUpdated received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

