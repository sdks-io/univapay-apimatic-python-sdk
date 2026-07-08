## Token Cvv Auth Check Updated Handler

Token CVV auth check updated event.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [tokenCvvAuthCheckUpdated](../../../doc/events/webhooks/token_cvv_auth_check_updated/token-cvv-auth-check-updated.md) | Fired when the CVV auth check status for a token changes. The `data` field contains the full TransactionToken object. | token_cvv_auth_check_updated |

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
from univapayclientsdk.events.webhooks.token_cvv_auth_check_updated_handler import (
    TokenCvvAuthCheckUpdatedHandler,
)
from univapayclientsdk.models.token_cvv_auth_check_updated_webhook_callback import (
    TokenCvvAuthCheckUpdatedWebhookCallback,
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
    event = TokenCvvAuthCheckUpdatedHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if (
        isinstance(event, TokenCvvAuthCheckUpdatedWebhookCallback) and
        getattr(event, "event", None) == "token_cvv_auth_check_updated"
    ):
        print("tokenCvvAuthCheckUpdated received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

