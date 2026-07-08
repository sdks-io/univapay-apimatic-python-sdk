"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: D410, E501, E101, D206
from apimatic_core.authentication.multiple.single_auth import (
    Single,
)
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.configuration import (
    Server,
)
from univapayclientsdk.controllers.base_controller import (
    BaseController,
)
from univapayclientsdk.exceptions.api_error_exception import (
    ApiErrorException,
)
from univapayclientsdk.exceptions.api_exception import (
    ApiException,
)
from univapayclientsdk.http.http_method_enum import (
    HttpMethodEnum,
)
from univapayclientsdk.models.refund import (
    Refund,
)
from univapayclientsdk.models.refund_list import (
    RefundList,
)


class RefundsController(BaseController):
    """A Controller to access Endpoints in the univapayclientsdk API."""

    def __init__(self, config):
        """Initialize RefundsController object."""
        super(RefundsController, self).__init__(config)

    def list_refunds(self,
                     store_id,
                     charge_id,
                     limit=10,
                     cursor=None,
                     cursor_direction="desc",
                     metadata=None):
        """Perform a GET request to
        /stores/{storeId}/charges/{chargeId}/refunds.

        Retrieves a list of all refunds for a specific charge.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            charge_id (uuid|str): The unique identifier of the charge.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.
            metadata (str, optional): Filter refunds by metadata content.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of refunds
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{chargeId}/refunds")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("chargeId")
                .value(charge_id)
                .is_required(True)
                .should_encode(True))
            .query_param(Parameter()
                .key("limit")
                .value(limit))
            .query_param(Parameter()
                .key("cursor")
                .value(cursor))
            .query_param(Parameter()
                .key("cursor_direction")
                .value(cursor_direction))
            .query_param(Parameter()
                .key("metadata")
                .value(metadata))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RefundList.from_dictionary)
            .is_api_response(True)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("403",
                "HTTP 403 Forbidden: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiException)
            .local_error_template("409",
                "HTTP 409 Conflict: {$response.body#/code}",
                ApiException)
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("500",
                "HTTP 500 Server Error: {$response.body#/code}",
                ApiException)
            .local_error_template("503",
                "HTTP 503 Unavailable: {$response.body#/code}",
                ApiException)
            .local_error_template("504",
                "HTTP 504 Timeout: {$response.body#/code}",
                ApiException)
            .local_error_template("default",
                "HTTP {$statusCode}: {$response.body#/code}",
                ApiException),
        ).execute()

    def create_refund(self,
                      store_id,
                      charge_id,
                      body,
                      idempotency_key=None):
        """Perform a POST request to
        /stores/{storeId}/charges/{chargeId}/refunds.

        Creates a refund for a successful charge. The charge must have status
        `successful`. Konbini and bank transfer charges cannot be refunded. The
        refund is processed asynchronously — the initial status will be `pending`.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            charge_id (uuid|str): The unique identifier of the charge.
            body (RefundCreateRequest): Request payload for creating a refund.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Refund created
                successfully. Processing is asynchronous — poll or use webhooks to
                track completion.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{chargeId}/refunds")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("chargeId")
                .value(charge_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("Idempotency-Key")
                .value(idempotency_key))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Refund.from_dictionary)
            .is_api_response(True)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("403",
                "HTTP 403 Forbidden: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("409",
                "HTTP 409 Conflict: {$response.body#/code}",
                ApiException)
            .local_error_template("500",
                "HTTP 500 Server Error: {$response.body#/code}",
                ApiException)
            .local_error_template("503",
                "HTTP 503 Unavailable: {$response.body#/code}",
                ApiException)
            .local_error_template("504",
                "HTTP 504 Timeout: {$response.body#/code}",
                ApiException)
            .local_error_template("default",
                "HTTP {$statusCode}: {$response.body#/code}",
                ApiException),
        ).execute()

    def get_refund(self,
                   store_id,
                   charge_id,
                   id,
                   polling=None):
        """Perform a GET request to
        /stores/{storeId}/charges/{chargeId}/refunds/{id}.

        Retrieves the details of a specific refund. Supports long polling — set
        `polling=true` to wait until the refund status changes from `pending` to a
        terminal state (`successful`, `failed`, or `error`).

        Args:
            store_id (uuid|str): The unique identifier of the store.
            charge_id (uuid|str): The unique identifier of the charge.
            id (uuid|str): The unique identifier of the resource.
            polling (bool, optional): If `true`, the server holds the connection open
                until the refund status transitions from `pending` to a terminal
                state, or until the polling timeout is reached.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Refund details
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{chargeId}/refunds/{id}")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("chargeId")
                .value(charge_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .query_param(Parameter()
                .key("polling")
                .value(polling))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Refund.from_dictionary)
            .is_api_response(True)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiException)
            .local_error_template("403",
                "HTTP 403 Forbidden: {$response.body#/code}",
                ApiException)
            .local_error_template("409",
                "HTTP 409 Conflict: {$response.body#/code}",
                ApiException)
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("500",
                "HTTP 500 Server Error: {$response.body#/code}",
                ApiException)
            .local_error_template("503",
                "HTTP 503 Unavailable: {$response.body#/code}",
                ApiException)
            .local_error_template("504",
                "HTTP 504 Timeout: {$response.body#/code}",
                ApiException)
            .local_error_template("default",
                "HTTP {$statusCode}: {$response.body#/code}",
                ApiException),
        ).execute()

    def update_refund(self,
                      store_id,
                      charge_id,
                      id,
                      body,
                      idempotency_key=None):
        """Perform a PATCH request to
        /stores/{storeId}/charges/{chargeId}/refunds/{id}.

        Updates metadata, message, or reason on an existing refund.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            charge_id (uuid|str): The unique identifier of the charge.
            id (uuid|str): The unique identifier of the resource.
            body (RefundUpdateRequest): Request payload for updating refund metadata
                or reason.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Refund updated
                successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{chargeId}/refunds/{id}")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("chargeId")
                .value(charge_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body)
                .is_required(True))
            .header_param(Parameter()
                .key("Idempotency-Key")
                .value(idempotency_key))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Refund.from_dictionary)
            .is_api_response(True)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("403",
                "HTTP 403 Forbidden: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("409",
                "HTTP 409 Conflict: {$response.body#/code}",
                ApiException)
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("500",
                "HTTP 500 Server Error: {$response.body#/code}",
                ApiException)
            .local_error_template("503",
                "HTTP 503 Unavailable: {$response.body#/code}",
                ApiException)
            .local_error_template("504",
                "HTTP 504 Timeout: {$response.body#/code}",
                ApiException)
            .local_error_template("default",
                "HTTP {$statusCode}: {$response.body#/code}",
                ApiException),
        ).execute()
