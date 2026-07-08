## Token Three Ds Updated Handler

Token 3DS updated event.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [tokenThreeDsUpdated](../../../doc/events/webhooks/token_three_ds_updated/token-three-ds-updated.md) | Fired when the 3-D Secure data associated with a token is updated. The `data` field contains the full TransactionToken object. | token_three_d_s_updated |

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
from univapayclientsdk.events.webhooks.token_three_ds_updated_handler import (
    TokenThreeDsUpdatedHandler,
)
from univapayclientsdk.models.token_three_ds_updated_webhook_callback import (
    TokenThreeDsUpdatedWebhookCallback,
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
    event = TokenThreeDsUpdatedHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if (
        isinstance(event, TokenThreeDsUpdatedWebhookCallback) and
        getattr(event, "event", None) == "token_three_d_s_updated"
    ):
        print("tokenThreeDsUpdated received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

