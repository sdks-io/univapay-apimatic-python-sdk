"""
 univapay_client_sdk

 This file was automatically generated for Univapay by APIMATIC v3.0 (
https://www.apimatic.io ).
"""
# ruff: noqa: RET505

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


def create_app() -> Flask:
    """
     Create and configure the Flask application.

    :return: A Flask application instance with the webhook route registered.
    """
    app = Flask(__name__)
    @app.route("/webhooks", methods=[
        "POST",
    ])
    def webhooks() -> Response:
        """
         Process incoming `webhooks` requests.

        :return: A response indicating the handling result.
        """
        # Step 1: Convert the incoming request using to_core_request (Django/Flask)
        #         or await to_core_request_async (FastAPI).
        core_req = to_core_request(request)

        # Step 2: Parse the request into a typed event.
        event = ChargeUpdatedHandler.parse_event(core_req)

        # Step 3: Pattern match for chargeUpdated only.
        if (
            isinstance(event, ChargeUpdatedWebhookCallback) and
            getattr(event, "event", None) == "charge_updated"
        ):
            return Response(status=200)
        elif isinstance(event, UnknownEvent):
            print("Unknown event")
            # TODO: add unknown event handling

        return Response(status=400)
    return app
