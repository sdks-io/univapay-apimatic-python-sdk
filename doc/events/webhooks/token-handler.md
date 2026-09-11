## Token Handler

Transaction token lifecycle events.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [tokenCreated](../../../doc/events/webhooks/token/token-created.md) | Fired when a new transaction token is created. The `data` field contains the full TransactionToken object. | token_created |
| [tokenUpdated](../../../doc/events/webhooks/token/token-updated.md) | Fired when a transaction token is updated (e.g., metadata change). The `data` field contains the full TransactionToken object. | token_updated |
| [tokenThreeDsUpdated](../../../doc/events/webhooks/token/token-three-ds-updated.md) | Fired when the 3-D Secure data associated with a token is updated. The `data` field contains the full TransactionToken object. | token_three_d_s_updated |
| [tokenCvvAuthUpdated](../../../doc/events/webhooks/token/token-cvv-auth-updated.md) | Fired when the CVV authorization result for a token is updated. The `data` field contains the full TransactionToken object. | token_cvv_auth_updated |
| [tokenCvvAuthCheckUpdated](../../../doc/events/webhooks/token/token-cvv-auth-check-updated.md) | Fired when the CVV auth check status for a token changes. The `data` field contains the full TransactionToken object. | token_cvv_auth_check_updated |
| [tokenReplaced](../../../doc/events/webhooks/token/token-replaced.md) | Fired when a transaction token is replaced by a new token (e.g., after card update). The `data` field contains the replacement TransactionToken object. | token_replaced |
| [recurringTokenDeleted](../../../doc/events/webhooks/token/recurring-token-deleted.md) | Fired when a recurring transaction token is deleted. The `data` field contains the deleted TransactionToken object. | recurring_token_deleted |

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
from univapayclientsdk.events.webhooks.token_handler import (
    TokenHandler,
)
from univapayclientsdk.models.token_webhook_event import (
    TokenWebhookEvent,
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
    event = TokenHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if (
        isinstance(event, TokenWebhookEvent) and
        getattr(event, "event", None) == "token_created"
    ):
        print("tokenCreated received")
        # TODO: add handling logic
    elif (
        isinstance(event, TokenWebhookEvent) and
        getattr(event, "event", None) == "token_updated"
    ):
        print("tokenUpdated received")
        # TODO: add handling logic
    elif (
        isinstance(event, TokenWebhookEvent) and
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

