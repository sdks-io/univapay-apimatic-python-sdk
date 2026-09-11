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
from univapayclientsdk.models.bank_transfer_ledger_list import (
    BankTransferLedgerList,
)
from univapayclientsdk.models.charge import (
    Charge,
)
from univapayclientsdk.models.charge_list import (
    ChargeList,
)
from univapayclientsdk.models.customs_declaration_webhook_data import (
    CustomsDeclarationWebhookData,
)
from univapayclientsdk.models.issuer_token import (
    IssuerToken,
)
from univapayclientsdk.models.three_ds_issuer_token import (
    ThreeDsIssuerToken,
)


class ChargesApi(BaseApi):
    """A Controller to access Endpoints in the univapayclientsdk API."""

    def __init__(self, config):
        """Initialize ChargesApi object."""
        super(ChargesApi, self).__init__(config)

    def create_charge(self,
                      idempotency_key=None,
                      body=None):
        """Perform a POST request to /charges.

        Creates a charge on a payment instrument (e.g. transaction token).

        Args:
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (ChargeCreateRequest, optional): Request payload for creating a
                charge.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Charge Created

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/charges")
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
            .deserialize_into(Charge.from_dictionary)
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

    def list_all_charges(self,
                         limit=10,
                         cursor=None,
                         cursor_direction="desc",
                         last_four=None,
                         name=None,
                         exp_month=None,
                         exp_year=None,
                         mfrom=None,
                         to=None,
                         email=None,
                         phone=None,
                         amount_from=None,
                         amount_to=None,
                         currency=None,
                         mode=None,
                         metadata=None,
                         transaction_token_id=None):
        """Perform a GET request to /charges.

        Lists all charges across all stores for the authenticated user.

        Args:
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.
            last_four (str, optional): Filter by the last 4 digits of the card.
                **Note:** If specified, `name`, `exp_month`, and `exp_year` must also
                be included.
            name (str, optional): Filter by cardholder name.  **Note:** If specified,
                `last_four`, `exp_month`, and `exp_year` must also be included.
            exp_month (int, optional): Filter by expiration month.  **Note:** If
                specified, `last_four`, `name`, and `exp_year` must also be included.
            exp_year (int, optional): Filter by expiration year.  **Note:** If
                specified, `last_four`, `name`, and `exp_month` must also be included.
            mfrom (str, optional): Show charges created on or after this date
                (ISO-8601).
            to (str, optional): Show charges created before this date (ISO-8601).
            email (str, optional): Filter by email address.
            phone (str, optional): Filter by phone number.
            amount_from (int, optional): Show charges with an amount greater than or
                equal to this value.
            amount_to (int, optional): Show charges with an amount strictly less than
                this value.
            currency (str, optional): Filter by currency (ISO-4217).
            mode (ModeQuery, optional): Filter by environment mode.
            metadata (str, optional): Filter by metadata.
            transaction_token_id (uuid|str, optional): Filter by transaction token ID.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of Charges

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/charges")
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
            .query_param(Parameter()
                .key("last_four")
                .value(last_four))
            .query_param(Parameter()
                .key("name")
                .value(name))
            .query_param(Parameter()
                .key("exp_month")
                .value(exp_month))
            .query_param(Parameter()
                .key("exp_year")
                .value(exp_year))
            .query_param(Parameter()
                .key("from")
                .value(mfrom))
            .query_param(Parameter()
                .key("to")
                .value(to))
            .query_param(Parameter()
                .key("email")
                .value(email))
            .query_param(Parameter()
                .key("phone")
                .value(phone))
            .query_param(Parameter()
                .key("amount_from")
                .value(amount_from))
            .query_param(Parameter()
                .key("amount_to")
                .value(amount_to))
            .query_param(Parameter()
                .key("currency")
                .value(currency))
            .query_param(Parameter()
                .key("mode")
                .value(mode))
            .query_param(Parameter()
                .key("metadata")
                .value(metadata))
            .query_param(Parameter()
                .key("transaction_token_id")
                .value(transaction_token_id))
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

    def list_store_charges(self,
                           store_id,
                           limit=10,
                           cursor=None,
                           cursor_direction="desc",
                           last_four=None,
                           name=None,
                           exp_month=None,
                           exp_year=None,
                           mfrom=None,
                           to=None,
                           email=None,
                           phone=None,
                           amount_from=None,
                           amount_to=None,
                           currency=None,
                           mode=None,
                           metadata=None,
                           transaction_token_id=None):
        """Perform a GET request to /stores/{storeId}/charges.

        Lists all charges for a specific store.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.
            last_four (str, optional): Filter by the last 4 digits of the card.
                **Note:** If specified, `name`, `exp_month`, and `exp_year` must also
                be included.
            name (str, optional): Filter by cardholder name.  **Note:** If specified,
                `last_four`, `exp_month`, and `exp_year` must also be included.
            exp_month (int, optional): Filter by expiration month.  **Note:** If
                specified, `last_four`, `name`, and `exp_year` must also be included.
            exp_year (int, optional): Filter by expiration year.  **Note:** If
                specified, `last_four`, `name`, and `exp_month` must also be included.
            mfrom (str, optional): Show charges created on or after this date
                (ISO-8601).
            to (str, optional): Show charges created before this date (ISO-8601).
            email (str, optional): Filter by email address.
            phone (str, optional): Filter by phone number.
            amount_from (int, optional): Show charges with an amount greater than or
                equal to this value.
            amount_to (int, optional): Show charges with an amount strictly less than
                this value.
            currency (str, optional): Filter by currency (ISO-4217).
            mode (ModeQuery, optional): Filter by environment mode.
            metadata (str, optional): Filter by metadata.
            transaction_token_id (uuid|str, optional): Filter by transaction token ID.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of Charges

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
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
                .key("last_four")
                .value(last_four))
            .query_param(Parameter()
                .key("name")
                .value(name))
            .query_param(Parameter()
                .key("exp_month")
                .value(exp_month))
            .query_param(Parameter()
                .key("exp_year")
                .value(exp_year))
            .query_param(Parameter()
                .key("from")
                .value(mfrom))
            .query_param(Parameter()
                .key("to")
                .value(to))
            .query_param(Parameter()
                .key("email")
                .value(email))
            .query_param(Parameter()
                .key("phone")
                .value(phone))
            .query_param(Parameter()
                .key("amount_from")
                .value(amount_from))
            .query_param(Parameter()
                .key("amount_to")
                .value(amount_to))
            .query_param(Parameter()
                .key("currency")
                .value(currency))
            .query_param(Parameter()
                .key("mode")
                .value(mode))
            .query_param(Parameter()
                .key("metadata")
                .value(metadata))
            .query_param(Parameter()
                .key("transaction_token_id")
                .value(transaction_token_id))
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

    def get_charge(self,
                   store_id,
                   id,
                   polling=None):
        """Perform a GET request to /stores/{storeId}/charges/{id}.

        Retrieves the details of an existing charge.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.
            polling (bool, optional): If set to true, instructs the API to internally
                poll the charge status  until it changes from 'pending' (the initial
                status) to another status.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Charge Details

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{id}")
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
            .deserialize_into(Charge.from_dictionary)
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

    def update_charge(self,
                      store_id,
                      id,
                      idempotency_key=None,
                      body=None):
        """Perform a PATCH request to /stores/{storeId}/charges/{id}.

        Use this request to add or modify arbitrary metadata on an existing charge.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (ChargeUpdateRequest, optional): Request payload for updating charge
                metadata.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Updated Charge

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{id}")
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
            .deserialize_into(Charge.from_dictionary)
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

    def capture_charge(self,
                       store_id,
                       id,
                       idempotency_key=None,
                       body=None):
        """Perform a POST request to /stores/{storeId}/charges/{id}/capture.

        Captures a previously authorized charge (where `capture` was set to false
        during creation).  The capture amount must be less than or equal to the
        authorized amount, and the currency must match. The request body — and both
        of its fields — is optional: if omitted entirely, the full outstanding
        authorized amount (in the originally requested currency) is captured.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).
            body (ChargeCaptureRequest, optional): Optional request payload for
                capturing an authorized charge. Omit entirely to capture the full
                outstanding authorized amount.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Captured successfully.
                Returns an empty JSON object.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{id}/capture")
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
            .deserializer(APIHelper.json_deserialize)
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

    def get_charge_issuer_token(self,
                                store_id,
                                id):
        """Perform a GET request to
        /stores/{storeId}/charges/{id}/issuer_token.

        Retrieves the necessary payment execution URL (for online payments) or bank
        account details (for bank transfers).
        **⚠️ Prerequisite:** The charge `status` must be `awaiting` before requesting
        the issuer token.  If requested while the charge is in any other status, an
        error will be returned.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Issuer token or bank
                transfer instructions retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{id}/issuer_token")
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
            .deserialize_into(IssuerToken.from_dictionary)
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

    def get_charge_three_ds_issuer_token(self,
                                         store_id,
                                         id):
        """Perform a GET request to
        /stores/{storeId}/charges/{id}/three_ds/issuer_token.

        Retrieves the 3-D Secure issuer token details required to authenticate a card
        charge.
        **⚠️ Prerequisites:** 1. The charge must be created with `three_ds.mode` set
        to `normal` or `force`. 2. You must poll the charge until its `status`
        becomes `awaiting` before making this request.
        **Execution Flow:** Once retrieved, the client (browser) must execute an
        `http_post` request to the `issuer_token` URL.  The `payload` object must be
        formatted according to the `content_type` (e.g., URL-encoded) and sent in the
        body. You can execute this via a redirect or inside an iframe. If using an
        iframe, continue polling the charge status  in the background until it
        reaches `successful`, `failed`, or `error`.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. 3DS Redirect details
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{id}/three_ds/issuer_token")
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

    def list_bank_transfer_ledgers(self,
                                   store_id,
                                   id):
        """Perform a GET request to
        /stores/{storeId}/charges/{id}/bank_transfer_ledgers.

        Retrieves bank transfer ledger entries associated with a charge. This is an
        optional reconciliation endpoint — not part of the required
        create-charge-and-poll flow.
        **⚠️ Requires a merchant-level application token**, unlike the rest of the
        bank transfer flow. A store application token (`Bearer {secret}.{jwt}` scoped
        to a `store_id`) is not sufficient here, even though the path is store-scoped.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            id (uuid|str): The unique identifier of the resource.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Ledger entries
                (deposits/payments)

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{id}/bank_transfer_ledgers")
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
            .deserialize_into(BankTransferLedgerList.from_dictionary)
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

    def create_customs_declaration(self,
                                   store_id,
                                   charge_id,
                                   body,
                                   idempotency_key=None):
        """Perform a POST request to
        /stores/{storeId}/charges/{chargeId}/customs.

        Creates a customs declaration for a successful charge. Backend only accepts
        this request for WeChat Online and WeChat MPM charges. If a declaration
        already exists and is no longer pending, the backend updates its identity
        fields and restarts processing instead of creating a new record.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            charge_id (uuid|str): The unique identifier of the charge.
            body (CustomsDeclarationCreateRequest): Request payload for creating a
                customs declaration.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Existing customs
                declaration updated and resubmitted successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{chargeId}/customs")
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
            .deserialize_into(CustomsDeclarationWebhookData.from_dictionary)
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

    def get_customs_declaration(self,
                                store_id,
                                charge_id,
                                id,
                                polling=False):
        """Perform a GET request to
        /stores/{storeId}/charges/{chargeId}/customs/{id}.

        Retrieves a customs declaration for a charge. Supports long polling when
        `polling=true`, returning once the declaration leaves its current state or
        the polling timeout is reached.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            charge_id (uuid|str): The unique identifier of the charge.
            id (uuid|str): The unique identifier of the customs declaration.
            polling (bool, optional): Hold the request open while waiting for a
                status change.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Customs declaration
                retrieved successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{chargeId}/customs/{id}")
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
            .deserialize_into(CustomsDeclarationWebhookData.from_dictionary)
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

    def patch_customs_declaration(self,
                                  store_id,
                                  charge_id,
                                  id,
                                  body,
                                  idempotency_key=None):
        """Perform a PATCH request to
        /stores/{storeId}/charges/{chargeId}/customs/{id}.

        Updates a customs declaration and requeues processing. Backend patching
        preserves the original `customs`, `certificate_id`, and `certificate_name`
        values and only accepts a new `merchant_customs_no`. Pending declarations
        cannot be patched.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            charge_id (uuid|str): The unique identifier of the charge.
            id (uuid|str): The unique identifier of the customs declaration.
            body (CustomsDeclarationPatchRequest): Request payload for patching a
                customs declaration.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Customs declaration
                updated successfully.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/charges/{chargeId}/customs/{id}")
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
            .deserialize_into(CustomsDeclarationWebhookData.from_dictionary)
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
