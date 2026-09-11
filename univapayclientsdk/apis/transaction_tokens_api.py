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
from univapayclientsdk.apis.base_api import (
    BaseApi,
)
from univapayclientsdk.configuration import (
    Server,
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
from univapayclientsdk.models.three_ds_issuer_token import (
    ThreeDsIssuerToken,
)
from univapayclientsdk.models.transaction_token_list import (
    TransactionTokenList,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)


class TransactionTokensApi(BaseApi):
    """A Controller to access Endpoints in the univapayclientsdk API."""

    def __init__(self, config):
        """Initialize TransactionTokensApi object."""
        super(TransactionTokensApi, self).__init__(config)

    def create_transaction_token(self,
                                 body,
                                 idempotency_key=None):
        """Perform a POST request to /tokens.

        Exchange raw payment data for a secure token. **PCI DSS Compliance Required**
        if sending raw card numbers.

        Args:
            body (TransactionTokenCreateRequest): Request payload for creating a
                transaction token.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Token Created

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/tokens")
            .http_method(HttpMethodEnum.POST)
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
            .deserializer(lambda value: APIHelper.deserialize_union_type(
                 UnionTypeLookUp
                 .get("TransactionToken"), value))
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
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

    def list_all_transaction_tokens(self,
                                    search=None,
                                    customer_id=None,
                                    mtype=None,
                                    mode=None,
                                    active="active",
                                    limit=10,
                                    cursor=None,
                                    cursor_direction="desc"):
        """Perform a GET request to /tokens.

        Lists all transaction tokens across all stores.

        Args:
            search (str, optional): Case-insensitive free-text search.
            customer_id (uuid|str, optional): Filter by customer ID.
            mtype (TransactionTokenListType, optional): Filter by token type.
                `one_time` tokens are excluded from listings and cannot be filtered
                on; filtering to `recurring` requires the App Token Secret.
            mode (ModeQuery, optional): Filter by environment mode.
            active (TransactionTokenActiveFilter, optional): Filter recurring tokens
                by whether they are still active.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of Tokens

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/tokens")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("search")
                .value(search))
            .query_param(Parameter()
                .key("customer_id")
                .value(customer_id))
            .query_param(Parameter()
                .key("type")
                .value(mtype))
            .query_param(Parameter()
                .key("mode")
                .value(mode))
            .query_param(Parameter()
                .key("active")
                .value(active))
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
            .deserialize_into(TransactionTokenList.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
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

    def list_store_transaction_tokens(self,
                                      store_id,
                                      search=None,
                                      customer_id=None,
                                      mtype=None,
                                      mode=None,
                                      active="active",
                                      limit=10,
                                      cursor=None,
                                      cursor_direction="desc"):
        """Perform a GET request to /stores/{storeId}/tokens.

        Lists all transaction tokens for a specific store.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            search (str, optional): Case-insensitive free-text search.
            customer_id (uuid|str, optional): Filter by customer ID.
            mtype (TransactionTokenListType, optional): Filter by token type.
                `one_time` tokens are excluded from listings and cannot be filtered
                on; filtering to `recurring` requires the App Token Secret.
            mode (ModeQuery, optional): Filter by environment mode.
            active (TransactionTokenActiveFilter, optional): Filter recurring tokens
                by whether they are still active.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of Tokens

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/tokens")
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
                .key("customer_id")
                .value(customer_id))
            .query_param(Parameter()
                .key("type")
                .value(mtype))
            .query_param(Parameter()
                .key("mode")
                .value(mode))
            .query_param(Parameter()
                .key("active")
                .value(active))
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
            .deserialize_into(TransactionTokenList.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("404",
                "HTTP 404 Not Found: {$response.body#/code}",
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

    def get_transaction_token(self,
                              store_id,
                              id,
                              polling=None):
        """Perform a GET request to /stores/{storeId}/tokens/{id}.

        Retrieves the details of an existing transaction token.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.
            polling (bool, optional): If set to true, instructs the API to internally
                poll the token's 3DS or CVV authorization sub-status until it
                transitions to another status, or until the ~3 second server-side
                timeout is reached.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Token Details

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/tokens/{id}")
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
            .deserializer(lambda value: APIHelper.deserialize_union_type(
                 UnionTypeLookUp
                 .get("TransactionToken"), value))
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

    def update_transaction_token(self,
                                 store_id,
                                 id,
                                 idempotency_key=None,
                                 body=None):
        """Perform a PATCH request to /stores/{storeId}/tokens/{id}.

        ⚠️ **LEGACY WARNING: Discouraged Operation**
        While it is technically possible to update a transaction token, this practice
        is highly discouraged and is maintained solely for legacy reasons.
        **Updating raw card details requires your server environment to be fully PCI
        DSS compliant.**
        **Recommended Approach:** Instead of updating an existing token, it is best
        practice to create an entirely new transaction token using Univapay's
        frontend integrations (**Link Form**, **Widget**, or **Inline Form**). This
        allows Univapay to securely handle the customer's payment data without it
        ever touching your servers.
        --- **Legacy Usage:** Updates CVV, Address, Email, or Card Details.  *Note:
        If updating only the CVV to resolve a `RECURRING_USAGE_REQUIRES_CVV` error,
        the application token secret is not required.*

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (TransactionTokenUpdateRequest, optional): Request payload for
                updating a transaction token.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Token Updated
                Successfully

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/tokens/{id}")
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
            .deserializer(lambda value: APIHelper.deserialize_union_type(
                 UnionTypeLookUp
                 .get("TransactionToken"), value))
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

    def delete_transaction_token(self,
                                 store_id,
                                 id):
        """Perform a DELETE request to /stores/{storeId}/tokens/{id}.

        Deletes a specific transaction token.
        ⚠️ **WARNING: Breaks Linked Subscriptions**
        Please note that deleting a transaction token will immediately prevent any
        linked recurring charges or subscriptions from being processed. Proceed with
        caution.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Token successfully
                deleted. No content.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/tokens/{id}")
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

    def enable_token_three_ds(self,
                              store_id,
                              id,
                              idempotency_key=None,
                              body=None):
        """Perform a POST request to /stores/{storeId}/tokens/{id}/three_ds.

        Enables 3-D Secure on an existing `recurring` transaction token that was
        created without it. Only applies to `recurring` tokens; returns an error if
        3DS is already enabled. After calling this endpoint, poll the token until
        `data.three_ds.status` becomes `awaiting`, then use the token 3DS issuer
        token endpoint to complete authentication.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (EnableTokenThreeDsRequest, optional): Optional request payload.
                Omit entirely, or omit `redirect_endpoint`, if no redirect is needed.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. 3DS enabled
                successfully. Returns the updated token.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/tokens/{id}/three_ds")
            .http_method(HttpMethodEnum.POST)
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
            .deserializer(lambda value: APIHelper.deserialize_union_type(
                 UnionTypeLookUp
                 .get("TransactionToken"), value))
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

    def disable_token_three_ds(self,
                               store_id,
                               id):
        """Perform a DELETE request to /stores/{storeId}/tokens/{id}/three_ds.

        Disables 3-D Secure on an existing `recurring` transaction token. Only
        applies to `recurring` tokens.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. 3DS disabled
                successfully. Returns the updated token.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/tokens/{id}/three_ds")
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
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(lambda value: APIHelper.deserialize_union_type(
                 UnionTypeLookUp
                 .get("TransactionToken"), value))
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

    def get_token_three_ds_issuer_token(self,
                                        store_id,
                                        id):
        """Perform a GET request to
        /stores/{storeId}/tokens/{id}/three_ds/issuer_token.

        Retrieves the information required to execute 3-D Secure authentication when
        creating a recurring transaction token.
        **⚠️ Important Notes:** 1. **PCI DSS Compliance:** This endpoint is only
        available to PCI DSS compliant merchants who are authorized to send raw card
        data directly via the API to create tokens. 2. **Target Tokens:** This only
        applies to tokens where `type` is `recurring`. For `one_time` or
        `subscription` tokens, 3-D Secure is requested during charge creation, not
        token creation. 3. **Execution Flow:**
           - After creating the token, poll the token object until
        `data.three_ds.status` becomes `awaiting`.
           - Once `awaiting`, use this endpoint to fetch the issuer token details.
           - Format the returned `payload` according to the `content_type` (e.g.,
        URL-encoded) and execute an `http_post` request from the consumer's browser
        to the `issuer_token` URL.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. 3-D Secure
                authentication details retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/tokens/{id}/three_ds/issuer_token")
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
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ThreeDsIssuerToken.from_dictionary)
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
