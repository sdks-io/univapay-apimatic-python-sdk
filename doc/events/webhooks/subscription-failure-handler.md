## Subscription Failure Handler

Subscription failure event.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [subscriptionFailure](../../../doc/events/webhooks/subscription_failure/subscription-failure.md) | Fired when a scheduled subscription payment fails. The `data` field contains the full Subscription object. | subscription_failure |

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
from univapayclientsdk.events.webhooks.subscription_failure_handler import (
    SubscriptionFailureHandler,
)
from univapayclientsdk.models.subscription_failure_webhook_callback import (
    SubscriptionFailureWebhookCallback,
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
    event = SubscriptionFailureHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if (
        isinstance(event, SubscriptionFailureWebhookCallback) and
        getattr(event, "event", None) == "subscription_failure"
    ):
        print("subscriptionFailure received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

