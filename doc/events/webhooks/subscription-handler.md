## Subscription Handler

Subscription lifecycle events.

Events in this group are uniquely identified by the `event` field.

## Events

Events available in this group. Subscribe to receive webhook notifications when these events occur.

| Name | Description | Event Identifier |
|  --- | --- | --- |
| [subscriptionCreated](../../../doc/events/webhooks/subscription/subscription-created.md) | Fired when a new subscription is created and its first payment has been initiated. The `data` field contains the full Subscription object. | subscription_created |
| [subscriptionPayment](../../../doc/events/webhooks/subscription/subscription-payment.md) | Fired when a scheduled subscription payment is successfully processed. The `data` field contains the full Subscription object. | subscription_payment |
| [subscriptionCompleted](../../../doc/events/webhooks/subscription/subscription-completed.md) | Fired when a subscription completes all of its scheduled payments. The `data` field contains the full Subscription object. | subscription_completed |
| [subscriptionFailure](../../../doc/events/webhooks/subscription/subscription-failure.md) | Fired when a scheduled subscription payment fails. The `data` field contains the full Subscription object. | subscription_failure |
| [subscriptionCanceled](../../../doc/events/webhooks/subscription/subscription-canceled.md) | Fired when a subscription is cancelled before all payments complete. The `data` field contains the full Subscription object. | subscription_canceled |
| [subscriptionSuspended](../../../doc/events/webhooks/subscription/subscription-suspended.md) | Fired when a subscription is suspended (paused). The `data` field contains the full Subscription object. | subscription_suspended |

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
from univapayclientsdk.events.webhooks.subscription_handler import (
    SubscriptionHandler,
)
from univapayclientsdk.models.subscription_webhook_event import (
    SubscriptionWebhookEvent,
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
    event = SubscriptionHandler.parse_event(core_req)

    # Step 3: Pattern match on the event type and handle it.
    if (
        isinstance(event, SubscriptionWebhookEvent) and
        getattr(event, "event", None) == "subscription_created"
    ):
        print("subscriptionCreated received")
        # TODO: add handling logic
    elif (
        isinstance(event, SubscriptionWebhookEvent) and
        getattr(event, "event", None) == "subscription_payment"
    ):
        print("subscriptionPayment received")
        # TODO: add handling logic
    elif (
        isinstance(event, SubscriptionWebhookEvent) and
        getattr(event, "event", None) == "subscription_completed"
    ):
        print("subscriptionCompleted received")
        # TODO: add handling logic
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    # Step 4: Return 200 OK to acknowledge receipt (adjust with other codes if needed).
    return Response(status=200)
```

