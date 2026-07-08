## Charge Updated Handler

Charge updated event.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [chargeUpdated](../../../doc/events/webhooks/charge_updated/charge-updated.md) | Fired whenever a charge transitions to a new status (e.g., `pending` → `awaiting`). The `data` field contains the full Charge object at the time of the event. | charge_updated |

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
def Webhooks():
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = to_core_request(request)

    # Step 2: Parse the request into a typed event.
    event = ChargeUpdatedHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
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

