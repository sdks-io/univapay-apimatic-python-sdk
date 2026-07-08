"""
 univapay_client_sdk

 This file was automatically generated for Univapay by APIMATIC v3.0 (
https://www.apimatic.io ).
"""
# ruff: noqa: RET505

from fastapi import (
    FastAPI,
    Request,
)
from fastapi.responses import JSONResponse

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
    to_core_request_async,
)

app = FastAPI()

@app.post("/webhooks")
async def webhooks(request: Request) -> JSONResponse:
    """
     Process incoming `webhooks` requests.

    :param request: The incoming HTTP request.

    :return: A JSON response indicating the handling result.
    """
    # Step 1: Convert the incoming request using to_core_request (Django/Flask)
    #         or await to_core_request_async (FastAPI).
    core_req = await to_core_request_async(request)

    # Step 2: Parse the request into a typed event.
    event = ChargeUpdatedHandler.parse_event(core_req)

    # Step 3: Pattern match for chargeUpdated only.
    if (
        isinstance(event, ChargeUpdatedWebhookCallback) and
        getattr(event, "event", None) == "charge_updated"
    ):
        return JSONResponse(status_code=200, content={})
    elif isinstance(event, UnknownEvent):
        print("Unknown event")
        # TODO: add unknown event handling

    return JSONResponse(status_code=400, content={})
