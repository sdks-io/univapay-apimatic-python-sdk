## Cancel Handler

Cancel lifecycle events.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [cancelFinished](../../../doc/events/webhooks/cancel/cancel-finished.md) | Fired when a cancellation request reaches a terminal status (`successful`, `failed`, `error`). The `data` field contains the full Cancel object. | cancel_finished |

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
def Webhooks():
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = CancelHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
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

