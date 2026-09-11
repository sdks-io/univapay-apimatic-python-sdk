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
from apimatic_core.types.array_serialization_format import (
    SerializationFormats,
)
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
from univapayclientsdk.models.transaction_history_list import (
    TransactionHistoryList,
)


class TransactionHistoryApi(BaseApi):
    """A Controller to access Endpoints in the univapayclientsdk API."""

    def __init__(self, config):
        """Initialize TransactionHistoryApi object."""
        super(TransactionHistoryApi, self).__init__(config)

    def list_transaction_history(self,
                                 mode=None,
                                 short_id=None,
                                 mfrom=None,
                                 to=None,
                                 status=None,
                                 mtype=None,
                                 search=None,
                                 email=None,
                                 id=None,
                                 metadata=None,
                                 card_exp=None,
                                 card_last_four=None,
                                 cardholder=None,
                                 card_brand=None,
                                 brand=None,
                                 brands=None,
                                 currency=None,
                                 service_provider=None,
                                 service_providers=None,
                                 gateway_transaction_id=None,
                                 bank_transfer_payment_statuses=None,
                                 bank_transfer_latest_deposit_date_from=None,
                                 bank_transfer_latest_deposit_date_to=None,
                                 limit=10,
                                 cursor=None,
                                 cursor_direction="desc"):
        """Perform a GET request to /transaction_history.

        Returns a paginated, searchable history of charges and refunds across all of
        the merchant's stores, combining both resource types into a single unified
        row shape.

        Args:
            mode (TransactionHistoryMode, optional): Filter by environment mode.
            short_id (str, optional): Filter by the last 6 characters of a resource's
                UUID. Must be exactly 6 characters.
            mfrom (str, optional): Show rows created on or after this date. Accepts
                epoch-millis or an ISO-8601 date-time. Must not be later than `to`.
            to (str, optional): Show rows created on or before this date. Accepts
                epoch-millis or an ISO-8601 date-time. Must not be earlier than
                `from`.
            status (TransactionHistoryStatus, optional): Filter by status. Accepts
                any charge or refund status value.
            mtype (TransactionHistoryType, optional): Filter by row type.
            search (str, optional): Free-text search across cardholder/customer name
                and email. Wrap a value in quotes (`"first last"`) for an
                exact-phrase match; an unquoted value matches partially.
            email (str, optional): Filter by email address.
            id (uuid|str, optional): Filter by exact charge or refund ID.
            metadata (str, optional): Filter by metadata.
            card_exp (str, optional): Filter by card expiration, in `yyyy-MM` format.
            card_last_four (str, optional): Filter by the last 4 digits of the card.
                Must be exactly 4 characters.
            cardholder (str, optional): Filter by cardholder name. Partial match by
                default; wrap in quotes for an exact-phrase match.
            card_brand (List[str], optional): Deprecated legacy alias of `brand`; use
                `brand` instead. Repeatable via the `[]` suffix (e.g.
                `card_brand[]=visa&card_brand[]=jcb`). Raw brand identifiers vary by
                payment type — see the `user_data.brand` field on this endpoint's
                response.
            brand (List[str], optional): Filter by brand. Repeatable via the `[]`
                suffix (e.g. `brand[]=visa&brand[]=jcb`). Raw brand identifiers vary
                by payment type — see the `user_data.brand` field on this endpoint's
                response.
            brands (List[str], optional): Deprecated legacy alias of `brand`; use
                `brand` instead. Repeatable via the `[]` suffix (e.g.
                `brands[]=visa&brands[]=jcb`). Raw brand identifiers vary by payment
                type — see the `user_data.brand` field on this endpoint's response.
            currency (str, optional): Filter by currency (ISO-4217).
            service_provider (TransactionHistoryServiceProvider, optional): Filter by
                service provider.
            service_providers (List[TransactionHistoryServiceProvider], optional):
                Filter by service provider. Repeatable via the `[]` suffix (e.g.
                `service_providers[]=credit&service_providers[]=paidy`). Must not be
                empty; duplicate values are deduplicated.
            gateway_transaction_id (str, optional): Filter by the gateway's own
                transaction ID (free text).
            bank_transfer_payment_statuses (List[BankTransferPaymentStatus],
                optional): Filter bank transfer rows by payment status. Repeatable
                via the `[]` suffix (e.g.
                `bank_transfer_payment_statuses[]=unpaid&bank_transfer_payment_statuse
                s[]=exact`).
            bank_transfer_latest_deposit_date_from (str, optional): Start of the
                range (inclusive) for `bank_transfer_latest_deposit_date`. Accepts
                epoch-millis or an ISO-8601 date-time.
            bank_transfer_latest_deposit_date_to (str, optional): End of the range
                (inclusive) for `bank_transfer_latest_deposit_date`. Accepts
                epoch-millis or an ISO-8601 date-time.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Paginated transaction
                history.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/transaction_history")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("mode")
                .value(mode))
            .query_param(Parameter()
                .key("short_id")
                .value(short_id))
            .query_param(Parameter()
                .key("from")
                .value(mfrom))
            .query_param(Parameter()
                .key("to")
                .value(to))
            .query_param(Parameter()
                .key("status")
                .value(status))
            .query_param(Parameter()
                .key("type")
                .value(mtype))
            .query_param(Parameter()
                .key("search")
                .value(search))
            .query_param(Parameter()
                .key("email")
                .value(email))
            .query_param(Parameter()
                .key("id")
                .value(id))
            .query_param(Parameter()
                .key("metadata")
                .value(metadata))
            .query_param(Parameter()
                .key("card_exp")
                .value(card_exp))
            .query_param(Parameter()
                .key("card_last_four")
                .value(card_last_four))
            .query_param(Parameter()
                .key("cardholder")
                .value(cardholder))
            .query_param(Parameter()
                .key("card_brand[]")
                .value(card_brand))
            .query_param(Parameter()
                .key("brand[]")
                .value(brand))
            .query_param(Parameter()
                .key("brands[]")
                .value(brands))
            .query_param(Parameter()
                .key("currency")
                .value(currency))
            .query_param(Parameter()
                .key("service_provider")
                .value(service_provider))
            .query_param(Parameter()
                .key("service_providers[]")
                .value(service_providers))
            .query_param(Parameter()
                .key("gateway_transaction_id")
                .value(gateway_transaction_id))
            .query_param(Parameter()
                .key("bank_transfer_payment_statuses[]")
                .value(bank_transfer_payment_statuses))
            .query_param(Parameter()
                .key("bank_transfer_latest_deposit_date.from")
                .value(bank_transfer_latest_deposit_date_from))
            .query_param(Parameter()
                .key("bank_transfer_latest_deposit_date.to")
                .value(bank_transfer_latest_deposit_date_to))
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
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionHistoryList.from_dictionary)
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

    def list_store_transaction_history(self,
                                       store_id,
                                       mode=None,
                                       short_id=None,
                                       mfrom=None,
                                       to=None,
                                       status=None,
                                       mtype=None,
                                       search=None,
                                       email=None,
                                       id=None,
                                       metadata=None,
                                       card_exp=None,
                                       card_last_four=None,
                                       cardholder=None,
                                       card_brand=None,
                                       brand=None,
                                       brands=None,
                                       currency=None,
                                       service_provider=None,
                                       service_providers=None,
                                       gateway_transaction_id=None,
                                       bank_transfer_payment_statuses=None,
                                       bank_transfer_latest_deposit_date_from=None,
                                       bank_transfer_latest_deposit_date_to=None,
                                       limit=10,
                                       cursor=None,
                                       cursor_direction="desc"):
        """Perform a GET request to /stores/{storeId}/transaction_history.

        Returns a paginated, searchable history of charges and refunds for a single
        store, combining both resource types into a single unified row shape.

        Args:
            store_id (uuid|str): The unique identifier of the store.
            mode (TransactionHistoryMode, optional): Filter by environment mode.
            short_id (str, optional): Filter by the last 6 characters of a resource's
                UUID. Must be exactly 6 characters.
            mfrom (str, optional): Show rows created on or after this date. Accepts
                epoch-millis or an ISO-8601 date-time. Must not be later than `to`.
            to (str, optional): Show rows created on or before this date. Accepts
                epoch-millis or an ISO-8601 date-time. Must not be earlier than
                `from`.
            status (TransactionHistoryStatus, optional): Filter by status. Accepts
                any charge or refund status value.
            mtype (TransactionHistoryType, optional): Filter by row type.
            search (str, optional): Free-text search across cardholder/customer name
                and email. Wrap a value in quotes (`"first last"`) for an
                exact-phrase match; an unquoted value matches partially.
            email (str, optional): Filter by email address.
            id (uuid|str, optional): Filter by exact charge or refund ID.
            metadata (str, optional): Filter by metadata.
            card_exp (str, optional): Filter by card expiration, in `yyyy-MM` format.
            card_last_four (str, optional): Filter by the last 4 digits of the card.
                Must be exactly 4 characters.
            cardholder (str, optional): Filter by cardholder name. Partial match by
                default; wrap in quotes for an exact-phrase match.
            card_brand (List[str], optional): Deprecated legacy alias of `brand`; use
                `brand` instead. Repeatable via the `[]` suffix (e.g.
                `card_brand[]=visa&card_brand[]=jcb`). Raw brand identifiers vary by
                payment type — see the `user_data.brand` field on this endpoint's
                response.
            brand (List[str], optional): Filter by brand. Repeatable via the `[]`
                suffix (e.g. `brand[]=visa&brand[]=jcb`). Raw brand identifiers vary
                by payment type — see the `user_data.brand` field on this endpoint's
                response.
            brands (List[str], optional): Deprecated legacy alias of `brand`; use
                `brand` instead. Repeatable via the `[]` suffix (e.g.
                `brands[]=visa&brands[]=jcb`). Raw brand identifiers vary by payment
                type — see the `user_data.brand` field on this endpoint's response.
            currency (str, optional): Filter by currency (ISO-4217).
            service_provider (TransactionHistoryServiceProvider, optional): Filter by
                service provider.
            service_providers (List[TransactionHistoryServiceProvider], optional):
                Filter by service provider. Repeatable via the `[]` suffix (e.g.
                `service_providers[]=credit&service_providers[]=paidy`). Must not be
                empty; duplicate values are deduplicated.
            gateway_transaction_id (str, optional): Filter by the gateway's own
                transaction ID (free text).
            bank_transfer_payment_statuses (List[BankTransferPaymentStatus],
                optional): Filter bank transfer rows by payment status. Repeatable
                via the `[]` suffix (e.g.
                `bank_transfer_payment_statuses[]=unpaid&bank_transfer_payment_statuse
                s[]=exact`).
            bank_transfer_latest_deposit_date_from (str, optional): Start of the
                range (inclusive) for `bank_transfer_latest_deposit_date`. Accepts
                epoch-millis or an ISO-8601 date-time.
            bank_transfer_latest_deposit_date_to (str, optional): End of the range
                (inclusive) for `bank_transfer_latest_deposit_date`. Accepts
                epoch-millis or an ISO-8601 date-time.
            limit (int, optional): Maximum number of resources to return in one page.
            cursor (uuid|str, optional): Cursor pointing to the resource after which
                pagination should continue.
            cursor_direction (CursorDirectionQuery, optional): Pagination direction
                relative to the supplied cursor.

        Returns:
            ApiResponse: An object with the response value as well as other useful
                information such as status codes and headers. Paginated transaction
                history for the store.

        Raises:
            ApiException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path("/stores/{storeId}/transaction_history")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("storeId")
                .value(store_id)
                .is_required(True)
                .should_encode(True))
            .query_param(Parameter()
                .key("mode")
                .value(mode))
            .query_param(Parameter()
                .key("short_id")
                .value(short_id))
            .query_param(Parameter()
                .key("from")
                .value(mfrom))
            .query_param(Parameter()
                .key("to")
                .value(to))
            .query_param(Parameter()
                .key("status")
                .value(status))
            .query_param(Parameter()
                .key("type")
                .value(mtype))
            .query_param(Parameter()
                .key("search")
                .value(search))
            .query_param(Parameter()
                .key("email")
                .value(email))
            .query_param(Parameter()
                .key("id")
                .value(id))
            .query_param(Parameter()
                .key("metadata")
                .value(metadata))
            .query_param(Parameter()
                .key("card_exp")
                .value(card_exp))
            .query_param(Parameter()
                .key("card_last_four")
                .value(card_last_four))
            .query_param(Parameter()
                .key("cardholder")
                .value(cardholder))
            .query_param(Parameter()
                .key("card_brand[]")
                .value(card_brand))
            .query_param(Parameter()
                .key("brand[]")
                .value(brand))
            .query_param(Parameter()
                .key("brands[]")
                .value(brands))
            .query_param(Parameter()
                .key("currency")
                .value(currency))
            .query_param(Parameter()
                .key("service_provider")
                .value(service_provider))
            .query_param(Parameter()
                .key("service_providers[]")
                .value(service_providers))
            .query_param(Parameter()
                .key("gateway_transaction_id")
                .value(gateway_transaction_id))
            .query_param(Parameter()
                .key("bank_transfer_payment_statuses[]")
                .value(bank_transfer_payment_statuses))
            .query_param(Parameter()
                .key("bank_transfer_latest_deposit_date.from")
                .value(bank_transfer_latest_deposit_date_from))
            .query_param(Parameter()
                .key("bank_transfer_latest_deposit_date.to")
                .value(bank_transfer_latest_deposit_date_to))
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
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single("JWT_TOKEN")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TransactionHistoryList.from_dictionary)
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
