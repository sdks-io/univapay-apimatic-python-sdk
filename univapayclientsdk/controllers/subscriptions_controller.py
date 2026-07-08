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
from univapayclientsdk.models.charge import (
    Charge,
)
from univapayclientsdk.models.charge_list import (
    ChargeList,
)
from univapayclientsdk.models.subscription import (
    Subscription,
)
from univapayclientsdk.models.subscription_list import (
    SubscriptionList,
)
from univapayclientsdk.models.subscription_payment import (
    SubscriptionPayment,
)
from univapayclientsdk.models.subscription_payment_list import (
    SubscriptionPaymentList,
)


class SubscriptionsController(BaseController):
    """A Controller to access Endpoints in the univapayclientsdk API."""

    def __init__(self, config):
        """Initialize SubscriptionsController object."""
        super(SubscriptionsController, self).__init__(config)

    def create_subscription(self,
                            idempotency_key=None,
                            body=None):
        """Perform a POST request to /subscriptions.

        Creates a new subscription.

        Args:
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (SubscriptionCreateRequest, optional): Create Subscription request

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription Created

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/subscriptions")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .header_param(Parameter()
                .key("Idempotency-Key")
                .value(idempotency_key))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Subscription.from_dictionary)
            .is_api_response(True)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiException)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiException)
            .local_error_template("403",
                "HTTP 403 Forbidden: {$response.body#/code}",
                ApiException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
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

    def list_all_subscriptions(self,
                               limit=10,
                               cursor=None,
                               cursor_direction="desc"):
        """Perform a GET request to /subscriptions.

        Lists all subscriptions across all stores.

        Args:
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of Subscriptions

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/subscriptions")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("limit")
                .value(limit))
            .query_param(Parameter()
                .key("cursor")
                .value(cursor))
            .query_param(Parameter()
                .key("cursor_direction")
                .value(cursor_direction))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionList.from_dictionary)
            .is_api_response(True)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiException)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiException)
            .local_error_template("403",
                "HTTP 403 Forbidden: {$response.body#/code}",
                ApiException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
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

    def list_store_subscriptions(self,
                                 store_id,
                                 search=None,
                                 status=None,
                                 mode=None,
                                 limit=10,
                                 cursor=None,
                                 cursor_direction="desc"):
        """Perform a GET request to /stores/{storeId}/subscriptions.

        Lists all subscriptions for a specific store.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            search (str, optional): Search by metadata values.
            status (SubscriptionStatus, optional): Filter subscriptions by current
                status.
            mode (ChargeMode, optional): Filter subscriptions by processing mode.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of subscriptions
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .query_param(Parameter()
                .key("search")
                .value(search))
            .query_param(Parameter()
                .key("status")
                .value(status))
            .query_param(Parameter()
                .key("mode")
                .value(mode))
            .query_param(Parameter()
                .key("limit")
                .value(limit))
            .query_param(Parameter()
                .key("cursor")
                .value(cursor))
            .query_param(Parameter()
                .key("cursor_direction")
                .value(cursor_direction))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionList.from_dictionary)
            .is_api_response(True)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiException)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiException)
            .local_error_template("403",
                "HTTP 403 Forbidden: {$response.body#/code}",
                ApiException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
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

    def get_subscription(self,
                         store_id,
                         id,
                         polling=None):
        """Perform a GET request to /stores/{storeId}/subscriptions/{id}.

        Retrieves the details of an existing subscription.  Supports internal polling
        to wait for status changes.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The Subscription ID.
            polling (bool, optional): If set to true, instructs the API to internally
                poll the subscription  status until it changes from 'unverified' (the
                initial status) to  another status.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription Details
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{id}")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
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
            .deserialize_into(Subscription.from_dictionary)
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

    def update_subscription(self,
                            store_id,
                            id,
                            idempotency_key=None,
                            body=None):
        """Perform a PATCH request to /stores/{storeId}/subscriptions/{id}.

        Updates the configuration, payment method, or schedule of a specific
        subscription.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (SubscriptionUpdateRequest, optional): Properties to update on the
                subscription.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription Updated
                successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{id}")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
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
            .header_param(Parameter()
                .key("Idempotency-Key")
                .value(idempotency_key))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Subscription.from_dictionary)
            .is_api_response(True)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("401",
                "HTTP 401 Unauthorized: {$response.body#/code}",
                ApiErrorException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
                ApiErrorException)
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

    def cancel_subscription(self,
                            store_id,
                            id):
        """Perform a DELETE request to /stores/{storeId}/subscriptions/{id}.

        Cancels an existing subscription. The subscription status will be
        permanently changed to `canceled` and it cannot be resumed.  Please proceed
        with caution.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription
                successfully canceled. No content.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{id}")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
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

    def list_subscription_payments(self,
                                   store_id,
                                   subscription_id,
                                   limit=10,
                                   cursor=None,
                                   cursor_direction="desc"):
        """Perform a GET request to
        /stores/{storeId}/subscriptions/{subscriptionId}/payments.

        Retrieves a list of all historical and scheduled payments for a  specific
        subscription.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of subscription
                payments retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/payments")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
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
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionPaymentList.from_dictionary)
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

    def get_subscription_payment(self,
                                 store_id,
                                 subscription_id,
                                 payment_id):
        """Perform a GET request to
        /stores/{storeId}/subscriptions/{subscriptionId}/payments/{paymentId}.

        Retrieves the details of an individual payment associated with a specific
        subscription.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            payment_id (uuid|str): The unique identifier of the scheduled payment of
                a subscription

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription Payment
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/payments/{paymentId}")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("paymentId")
                .value(payment_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionPayment.from_dictionary)
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

    def update_subscription_payment(self,
                                    store_id,
                                    subscription_id,
                                    payment_id,
                                    body,
                                    idempotency_key=None):
        """Perform a PATCH request to
        /stores/{storeId}/subscriptions/{subscriptionId}/payments/{paymentId}.

        Updates properties of a specific scheduled payment for a subscription. Can be
        used to change the due date when permitted, mark the payment as paid,
        schedule a termination status, or set a retry interval.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            payment_id (uuid|str): The unique identifier of the scheduled payment of
                a subscription
            body (SubscriptionPatchPaymentRequest): Request payload for updating a
                scheduled subscription payment.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Scheduled payment
                updated successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/payments/{paymentId}")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("paymentId")
                .value(payment_id)
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
            .deserialize_into(SubscriptionPayment.from_dictionary)
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

    def get_subscription_latest_charge(self,
                                       store_id,
                                       subscription_id):
        """Perform a GET request to
        /stores/{storeId}/subscriptions/{subscriptionId}/charges/latest.

        Retrieves the most recent charge created for a specific subscription. Returns
        404 if no charges have been attempted yet.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Latest charge retrieved
                successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/charges/latest")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Charge.from_dictionary)
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

    def list_subscription_charges(self,
                                  merchant_id,
                                  store_id,
                                  subscription_id,
                                  limit=10,
                                  cursor=None,
                                  cursor_direction="desc"):
        """Perform a GET request to
        /merchants/{merchantId}/stores/{storeId}/subscriptions/{subscriptionId}/charges
        .

        Retrieves a paginated list of charges linked to a subscription. Backend
        search uses the same charge search surface as normal charge listing and adds
        a subscription filter for the requested subscription.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription charges
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/merchants/{merchantId}/stores/{storeId}/subscriptions/{subscriptionId}/charges")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
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
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ChargeList.from_dictionary)
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

    def list_charges_for_subscription_payment(self,
                                              store_id,
                                              subscription_id,
                                              payment_id,
                                              limit=10,
                                              cursor=None,
                                              cursor_direction="desc"):
        """Perform a GET request to
        /stores/{storeId}/subscriptions/{subscriptionId}/payments/{paymentId}/charges.

        Retrieves a paginated list of all charge attempts made for a specific
        scheduled payment of a subscription. Useful for inspecting retry history.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            payment_id (uuid|str): The unique identifier of the scheduled payment of
                a subscription
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of charges for the
                scheduled payment retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/payments/{paymentId}/charges")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("paymentId")
                .value(payment_id)
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
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ChargeList.from_dictionary)
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

    def suspend_subscription(self,
                             store_id,
                             subscription_id,
                             idempotency_key=None,
                             body=None):
        """Perform a PATCH request to
        /stores/{storeId}/subscriptions/{subscriptionId}/suspend.

        Suspends a subscription that is currently `current` or `unpaid`. The
        `termination_mode` controls when the suspension takes effect: `immediate`
        (default) suspends right away, `on_next_payment` waits until the next
        scheduled payment date before suspending.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (SubscriptionSuspendRequest, optional): Request payload for
                suspending a subscription.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription suspended
                successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/suspend")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .header_param(Parameter()
                .key("Idempotency-Key")
                .value(idempotency_key))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Subscription.from_dictionary)
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

    def unsuspend_subscription(self,
                               store_id,
                               subscription_id,
                               idempotency_key=None):
        """Perform a PATCH request to
        /stores/{storeId}/subscriptions/{subscriptionId}/unsuspend.

        Resumes a subscription that is currently `suspended`, setting its status back
        to `unpaid` and rescheduling the next payment. No request body is required.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription
                unsuspended successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/unsuspend")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Idempotency-Key")
                .value(idempotency_key))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Subscription.from_dictionary)
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

    def update_subscription_token(self,
                                  store_id,
                                  subscription_id,
                                  body,
                                  idempotency_key=None):
        """Perform a PATCH request to
        /stores/{storeId}/subscriptions/{subscriptionId}/token.

        Replaces the payment method (transaction token) used for a subscription.
        Useful when a card expires or a customer wants to switch payment methods. The
        new token must belong to the same store, be active, and match the
        subscription's processing mode (live/test). One-time tokens are not accepted;
        use a recurring or subscription token.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            subscription_id (uuid|str): The unique identifier of the subscription.
            body (SubscriptionPatchTokenRequest): Request payload for replacing a
                subscription payment token.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Subscription token
                updated successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/subscriptions/{subscriptionId}/token")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("subscriptionId")
                .value(subscription_id)
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
            .deserialize_into(Subscription.from_dictionary)
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
