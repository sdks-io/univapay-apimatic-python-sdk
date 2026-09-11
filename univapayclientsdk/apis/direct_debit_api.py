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
from univapayclientsdk.models.direct_debit_bank_account import (
    DirectDebitBankAccount,
)
from univapayclientsdk.models.direct_debit_bank_account_list import (
    DirectDebitBankAccountList,
)
from univapayclientsdk.models.direct_debit_bank_transfer import (
    DirectDebitBankTransfer,
)
from univapayclientsdk.models.direct_debit_bank_transfer_list import (
    DirectDebitBankTransferList,
)
from univapayclientsdk.models.direct_debit_merchant_configuration import (
    DirectDebitMerchantConfiguration,
)
from univapayclientsdk.models.direct_debit_notification_configuration import (
    DirectDebitNotificationConfiguration,
)
from univapayclientsdk.models.direct_debit_schedule import (
    DirectDebitSchedule,
)


class DirectDebitApi(BaseApi):
    """A Controller to access Endpoints in the univapayclientsdk API."""

    def __init__(self, config):
        """Initialize DirectDebitApi object."""
        super(DirectDebitApi, self).__init__(config)

    def get_direct_debit_configuration(self,
                                       merchant_id):
        """Perform a GET request to /merchants/{merchantId}/configuration.

        Retrieves the merchant's direct debit configuration — whether direct debit is
        enabled and which monthly debit cycle applies.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Direct Debit
                Configuration

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/configuration")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitMerchantConfiguration.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
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

    def get_direct_debit_notification_configuration(self,
                                                    merchant_id):
        """Perform a GET request to
        /merchants/{merchantId}/notification-configuration.

        Retrieves which direct debit email notifications the merchant has opted into.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Notification
                Configuration

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/notification-configuration")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitNotificationConfiguration.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
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

    def get_direct_debit_current_schedule(self,
                                          merchant_id):
        """Perform a GET request to /merchants/{merchantId}/schedules/current.

        Retrieves the key dates for the debit cycle currently in progress, based on
        the merchant's configured cycle. Compare
        `merchant_bank_transfer_upload_deadline` against today to decide whether
        transfers can still be registered or edited this month.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Current Debit Cycle

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/schedules/current")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitSchedule.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
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

    def list_direct_debit_bank_accounts(self,
                                        merchant_id,
                                        limit=10,
                                        cursor=None,
                                        cursor_direction="desc",
                                        user_number=None,
                                        bank_account_id=None,
                                        bank_code=None,
                                        bank_name=None,
                                        branch_code=None,
                                        bank_account_type=None,
                                        bank_account_number=None,
                                        bank_account_name=None,
                                        registration_origin=None,
                                        bank_account_status=None,
                                        mfrom=None,
                                        to=None):
        """Perform a GET request to /merchants/{merchantId}/bank-accounts.

        Lists the consumer bank accounts registered for direct debit under this
        merchant.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.
            user_number (str, optional): Filter by the merchant's own membership
                number for the consumer (会員番号).
            bank_account_id (str, optional): Filter by a single bank account ID.
            bank_code (str, optional): Filter by the 4-digit bank code (銀行コード).
            bank_name (str, optional): Filter by bank name in half-width katakana
                (銀行名).
            branch_code (str, optional): Filter by the 3-digit branch code (支店コード).
            bank_account_type (DirectDebitBankAccountType, optional): Filter by
                deposit account type (預金種類).
            bank_account_number (str, optional): Filter by the 7-digit account number
                (口座番号).
            bank_account_name (str, optional): Filter by account holder name in
                half-width katakana (口座名義).
            registration_origin (DirectDebitRegistrationOrigin, optional): Filter by
                where the bank account was registered from.
            bank_account_status (DirectDebitBankAccountStatus, optional): Filter by
                bank account status. Omit to return every status.
            mfrom (str, optional): Show bank accounts created on or after this date
                (ISO-8601).
            to (str, optional): Show bank accounts created before this date
                (ISO-8601).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of Bank Accounts

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-accounts")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
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
                .key("user_number")
                .value(user_number))
            .query_param(Parameter()
                .key("bank_account_id")
                .value(bank_account_id))
            .query_param(Parameter()
                .key("bank_code")
                .value(bank_code))
            .query_param(Parameter()
                .key("bank_name")
                .value(bank_name))
            .query_param(Parameter()
                .key("branch_code")
                .value(branch_code))
            .query_param(Parameter()
                .key("bank_account_type")
                .value(bank_account_type))
            .query_param(Parameter()
                .key("bank_account_number")
                .value(bank_account_number))
            .query_param(Parameter()
                .key("bank_account_name")
                .value(bank_account_name))
            .query_param(Parameter()
                .key("registration_origin")
                .value(registration_origin))
            .query_param(Parameter()
                .key("bank_account_status")
                .value(bank_account_status))
            .query_param(Parameter()
                .key("from")
                .value(mfrom))
            .query_param(Parameter()
                .key("to")
                .value(to))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitBankAccountList.from_dictionary)
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

    def create_direct_debit_bank_account(self,
                                         merchant_id,
                                         body,
                                         idempotency_key=None):
        """Perform a POST request to /merchants/{merchantId}/bank-accounts.

        Registers a consumer bank account for direct debit. The account is created
        and then verified against the bank, so it starts out unusable — poll its
        `status` until it becomes `active` (or `registration_failed`) before
        scheduling transfers against it.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            body (DirectDebitBankAccountCreateRequest): Request payload for
                registering a consumer bank account.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Account Registered

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-accounts")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
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
            .deserialize_into(DirectDebitBankAccount.from_dictionary)
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

    def get_direct_debit_bank_account(self,
                                      merchant_id,
                                      bank_account_id):
        """Perform a GET request to
        /merchants/{merchantId}/bank-accounts/{bankAccountId}.

        Retrieves a single registered bank account, including its current
        verification status.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_account_id (str): The unique identifier of the direct debit bank
                account.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Account

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-accounts/{bankAccountId}")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankAccountId")
                .value(bank_account_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitBankAccount.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
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

    def update_direct_debit_bank_account(self,
                                         merchant_id,
                                         bank_account_id,
                                         body,
                                         idempotency_key=None):
        """Perform a PATCH request to
        /merchants/{merchantId}/bank-accounts/{bankAccountId}.

        Updates a registered bank account. Changing bank details re-triggers
        verification with the bank. Transfers already registered keep the details
        they were created with.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_account_id (str): The unique identifier of the direct debit bank
                account.
            body (DirectDebitBankAccountUpdateRequest): Request payload for updating
                a registered bank account.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Account Updated

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-accounts/{bankAccountId}")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankAccountId")
                .value(bank_account_id)
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
            .deserialize_into(DirectDebitBankAccount.from_dictionary)
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

    def deactivate_direct_debit_bank_account(self,
                                             merchant_id,
                                             bank_account_id):
        """Perform a DELETE request to
        /merchants/{merchantId}/bank-accounts/{bankAccountId}.

        Deactivates a bank account so no further transfers can be registered against
        it. The record is retained (status becomes `inactive`) rather than deleted,
        and can be re-enabled later.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_account_id (str): The unique identifier of the direct debit bank
                account.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Account Deactivated

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-accounts/{bankAccountId}")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankAccountId")
                .value(bank_account_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitBankAccount.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
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

    def reenable_direct_debit_bank_account(self,
                                           merchant_id,
                                           bank_account_id,
                                           idempotency_key=None):
        """Perform a POST request to
        /merchants/{merchantId}/bank-accounts/{bankAccountId}/re-enable.

        Returns a deactivated bank account to `active` so transfers can be registered
        against it again. The account must currently be `inactive`.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_account_id (str): The unique identifier of the direct debit bank
                account.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Account Re-enabled

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-accounts/{bankAccountId}/re-enable")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankAccountId")
                .value(bank_account_id)
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
            .deserialize_into(DirectDebitBankAccount.from_dictionary)
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

    def create_direct_debit_bank_transfer(self,
                                          merchant_id,
                                          bank_account_id,
                                          body,
                                          idempotency_key=None):
        """Perform a POST request to
        /merchants/{merchantId}/bank-accounts/{bankAccountId}/bank-transfers.

        Schedules a pull of funds from an active bank account. The transfer is queued
        for the merchant's next debit cycle and stays editable until that cycle's
        upload deadline passes.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_account_id (str): The unique identifier of the direct debit bank
                account.
            body (DirectDebitBankTransferCreateRequest): Request payload for
                scheduling a transfer, in JPY.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Transfer Scheduled

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-accounts/{bankAccountId}/bank-transfers")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankAccountId")
                .value(bank_account_id)
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
            .deserialize_into(DirectDebitBankTransfer.from_dictionary)
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

    def list_direct_debit_bank_transfers(self,
                                         merchant_id,
                                         limit=10,
                                         cursor=None,
                                         cursor_direction="desc",
                                         bank_transfer_id=None,
                                         bank_transfer_start=None,
                                         bank_transfer_end=None,
                                         debit_date=None,
                                         user_number=None,
                                         bank_account_number=None,
                                         bank_account_name=None,
                                         lock_status=None,
                                         bank_transfer_status=None):
        """Perform a GET request to /merchants/{merchantId}/bank-transfers.

        Lists the direct debit transfers registered under this merchant, across all
        bank accounts.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.
            bank_transfer_id (str, optional): Filter by a single bank transfer ID.
            bank_transfer_start (str, optional): Start of the year-month range in
                which the transfer is scheduled to occur.
            bank_transfer_end (str, optional): End of the year-month range in which
                the transfer is scheduled to occur.
            debit_date (DirectDebitDebitDate, optional): Filter by monthly debit
                cycle.
            user_number (str, optional): Filter by the merchant's own membership
                number for the consumer (会員番号).
            bank_account_number (str, optional): Filter by the 7-digit account number
                (口座番号).
            bank_account_name (str, optional): Filter by account holder name in
                half-width katakana (口座名義).
            lock_status (DirectDebitBankTransferLock, optional): Filter by lock
                status. Omit to return both locked and unlocked transfers.
            bank_transfer_status (DirectDebitBankTransferStatus, optional): Filter by
                transfer status. Omit to return every status.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. List of Bank Transfers

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-transfers")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
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
                .key("bank_transfer_id")
                .value(bank_transfer_id))
            .query_param(Parameter()
                .key("bank_transfer_start")
                .value(bank_transfer_start))
            .query_param(Parameter()
                .key("bank_transfer_end")
                .value(bank_transfer_end))
            .query_param(Parameter()
                .key("debit_date")
                .value(debit_date))
            .query_param(Parameter()
                .key("user_number")
                .value(user_number))
            .query_param(Parameter()
                .key("bank_account_number")
                .value(bank_account_number))
            .query_param(Parameter()
                .key("bank_account_name")
                .value(bank_account_name))
            .query_param(Parameter()
                .key("lock_status")
                .value(lock_status))
            .query_param(Parameter()
                .key("bank_transfer_status")
                .value(bank_transfer_status))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitBankTransferList.from_dictionary)
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

    def get_direct_debit_bank_transfer(self,
                                       merchant_id,
                                       bank_transfer_id):
        """Perform a GET request to
        /merchants/{merchantId}/bank-transfers/{bankTransferId}.

        Retrieves a single transfer. Poll this after the cycle's result registration
        date to pick up the outcome and, on failure, the bank's reason.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_transfer_id (str): The unique identifier of the direct debit bank
                transfer.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Transfer

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-transfers/{bankTransferId}")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankTransferId")
                .value(bank_transfer_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DirectDebitBankTransfer.from_dictionary)
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
            .local_error_template("429",
                "HTTP 429 Rate Limited: {$response.body#/code}",
                ApiException)
            .local_error_template("400",
                "HTTP 400 Bad Request: {$response.body#/code}",
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

    def update_direct_debit_bank_transfer(self,
                                          merchant_id,
                                          bank_transfer_id,
                                          body,
                                          idempotency_key=None):
        """Perform a PATCH request to
        /merchants/{merchantId}/bank-transfers/{bankTransferId}.

        Changes a scheduled transfer's amount. Only permitted while the transfer is
        `unlocked` — once its cycle's upload deadline passes the amount is fixed.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_transfer_id (str): The unique identifier of the direct debit bank
                transfer.
            body (DirectDebitBankTransferPatchRequest): Request payload for changing
                the transfer amount.
            idempotency_key (str, optional): An optional idempotency key to prevent
                double charges and duplicate operations. We recommend a randomly
                generated UUID (v4).

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Transfer Updated

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-transfers/{bankTransferId}")
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankTransferId")
                .value(bank_transfer_id)
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
            .deserialize_into(DirectDebitBankTransfer.from_dictionary)
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

    def delete_direct_debit_bank_transfer(self,
                                          merchant_id,
                                          bank_transfer_id):
        """Perform a DELETE request to
        /merchants/{merchantId}/bank-transfers/{bankTransferId}.

        Cancels a scheduled transfer so it is not sent to the bank. Only permitted
        while the transfer is `unlocked`.

        Args:
            merchant_id (uuid|str): The unique identifier of the merchant.
            bank_transfer_id (str): The unique identifier of the direct debit bank
                transfer.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Bank Transfer Deleted.
                Returns no content.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DIRECTDEBIT)
            .path("/merchants/{merchantId}/bank-transfers/{bankTransferId}")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("merchantId")
                .value(merchant_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("bankTransferId")
                .value(bank_transfer_id)
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
