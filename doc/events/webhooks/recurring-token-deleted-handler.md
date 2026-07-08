## Recurring Token Deleted Handler

Recurring token deleted event.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [recurringTokenDeleted](../../../doc/events/webhooks/recurring_token_deleted/recurring-token-deleted.md) | Fired when a recurring transaction token is deleted. The `data` field contains the deleted TransactionToken object. | recurring_token_deleted |

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
def Webhooks():
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = RecurringTokenDeletedHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
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

