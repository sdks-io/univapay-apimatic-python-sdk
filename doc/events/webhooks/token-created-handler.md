## Token Created Handler

Token created event.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [tokenCreated](../../../doc/events/webhooks/token_created/token-created.md) | Fired when a new transaction token is created. The `data` field contains the full TransactionToken object. | token_created |

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
from univapayclientsdk.events.webhooks.token_created_handler import (
    TokenCreatedHandler,
)
from univapayclientsdk.models.token_created_webhook_callback import (
    TokenCreatedWebhookCallback,
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
    event = TokenCreatedHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if (
        isinstance(event, TokenCreatedWebhookCallback) and
        getattr(event, "event", None) == "token_created"
    ):
        print("tokenCreated received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

