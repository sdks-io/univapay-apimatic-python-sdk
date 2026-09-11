
"""
univapay_client_sdk

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291, W293, E501
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)

from tests.apis.api_test_base import ApiTestBase
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.enable_token_three_ds_request import (
    EnableTokenThreeDsRequest,
)
from univapayclientsdk.models.transaction_token_create_request import (
    TransactionTokenCreateRequest,
)
from univapayclientsdk.models.transaction_token_update_request import (
    TransactionTokenUpdateRequest,
)


class TransactionTokensApiTests(ApiTestBase):
    """
    Endpoint tests for validating the API behavior.

    Ensures controller methods execute correctly and produce the expected
    responses using the shared test client and response catcher.
    """

    controller = None

    @classmethod
    def setUpClass(cls):
        """
        Initialize the shared test client and controller for all test methods.
        """
        super().setUpClass()
        cls.controller = cls.client.transaction_tokens
        cls.response_catcher = cls.controller.http_call_back

    def test_create_transaction_token(self):
        """
        Exchange raw payment data for a secure token. **PCI DSS Compliance Required**
        if sending raw card numbers.
        """
        # Parameters for the API call
        body = APIHelper.json_deserialize(
            "{\"payment_type\":\"card\",\"type\":\"recurring\",\"email\":\"test@univa"
            "pay.com\",\"metadata\":{\"univapay-phone-number\":\"+81 08012341234\"},"
            "\"data\":{\"cardholder\":\"TEST TEST\",\"card_number\":\"424242424242424"
            "2\",\"exp_month\":\"09\",\"exp_year\":\"26\",\"cvv\":\"123\",\"phone_num"
            "ber\":{\"country_code\":\"81\",\"local_number\":\"08012341234\"},\"three"
            "_ds\":{\"redirect_endpoint\":\"https://univapay.com/redirect/index.html"
            "\"},\"cvv_authorize\":{\"enabled\":false,\"currency\":\"JPY\"}}}",
            TransactionTokenCreateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.create_transaction_token(
            body,
            idempotency_key,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 201
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"11f11e85-e9e9-b198-b990-c3a715943241\",\"store_id\":\"11f0e274"
            "-1e3b-4752-9513-33d3e07ede13\",\"email\":\"test@test.com\",\"payment_typ"
            "e\":\"card\",\"active\":true,\"mode\":\"live\",\"type\":\"recurring\",\""
            "usage_limit\":null,\"confirmed\":null,\"metadata\":{\"univapay-link-id\""
            ":\"11f11e85-1b45-dace-bf3d-cbcae52f65fc\",\"univapay-name\":\"test\",\"u"
            "nivapay-phone-number\":\"+81 08012341234\",\"items\":[\"productName: Che"
            "rry Ice Sandwich, price: 3080, quantity: 1\",\"productName: Shipping, pr"
            "ice: 200, quantity: 1\"],\"order_no\":1,\"note\":null},\"created_on\":\""
            "2026-03-13T02:39:52.908468Z\",\"updated_on\":\"2026-03-13T02:39:52.90846"
            "8Z\",\"last_used_on\":null,\"data\":{\"card\":{\"cardholder\":\"TEST TES"
            "T\",\"exp_month\":9,\"exp_year\":2026,\"card_bin\":\"424242\",\"last_fou"
            "r\":\"424242\",\"brand\":\"visa\",\"card_type\":\"credit\",\"country\":"
            "\"JP\",\"category\":\"standard\",\"issuer\":\"issuer\",\"sub_brand\":\"n"
            "one\"},\"billing\":{\"line1\":null,\"line2\":null,\"state\":null,\"city"
            "\":null,\"country\":null,\"zip\":null,\"phone_number\":{\"country_code\""
            ":81,\"local_number\":\"08012341234\"}},\"cvv_authorize\":{\"enabled\":fa"
            "lse,\"status\":null,\"charge_id\":null,\"credentials_id\":null,\"currenc"
            "y\":null},\"cvv_authorize_check\":{\"status\":null,\"charge_id\":null,\""
            "date\":null},\"three_ds\":{\"enabled\":true,\"status\":\"pending\",\"red"
            "irect_endpoint\":\"https://univapay.com/redirect/index.html\",\"error\":"
            "null,\"exempted\":false}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_all_transaction_tokens(self):
        """
        Lists all transaction tokens across all stores.
        """
        # Parameters for the API call
        search = "tokyo"
        customer_id = "8a3f1b8e-2c1a-4b7a-9c2e-6f6b6f6e2b10"
        mtype = "recurring"
        mode = "live"
        active = "active"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_all_transaction_tokens(
            search,
            customer_id,
            mtype,
            mode,
            active,
            limit,
            cursor,
            cursor_direction,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"items\":[{\"id\":\"2fe23e45-f95d-4c95-9963-739070096443\",\"store_id"
            "\":\"79e9504e-96d8-46ed-8d22-2e8b36238605\",\"merchant_name\":\"Test Mer"
            "chant\",\"store_name\":\"Tokyo Store\",\"email\":\"taro@example.com\",\""
            "payment_type\":\"card\",\"active\":true,\"mode\":\"live\",\"type\":\"rec"
            "urring\",\"created_on\":\"2026-04-09T07:35:50Z\",\"updated_on\":\"2026-0"
            "4-09T07:35:50Z\",\"user_data\":{\"cardholder_name\":\"TARO YAMADA\",\"em"
            "ail\":\"taro@example.com\"}},{\"id\":\"3af34f56-a06e-4d06-aa74-84a181107"
            "554\",\"store_id\":\"8bfa615f-a7e9-47fe-9e33-3f9c47349716\",\"merchant_n"
            "ame\":\"Test Merchant\",\"store_name\":\"Osaka Store\",\"email\":\"hanak"
            "o@example.com\",\"payment_type\":\"card\",\"active\":true,\"mode\":\"liv"
            "e\",\"type\":\"one_time\",\"created_on\":\"2026-04-10T10:20:11Z\",\"upda"
            "ted_on\":\"2026-04-10T10:20:11Z\",\"user_data\":{\"cardholder_name\":\"H"
            "ANAKO SUZUKI\",\"email\":\"hanako@example.com\"}},{\"id\":\"4bf45e67-b17"
            "f-4e17-bb85-95b292218665\",\"store_id\":\"79e9504e-96d8-46ed-8d22-2e8b36"
            "238605\",\"merchant_name\":\"Test Merchant\",\"store_name\":\"Tokyo Stor"
            "e\",\"email\":\"jiro@example.com\",\"payment_type\":\"card\",\"active\":"
            "false,\"mode\":\"live\",\"type\":\"subscription\",\"created_on\":\"2026-"
            "04-11T18:05:42Z\",\"updated_on\":\"2026-04-12T08:31:09Z\",\"user_data\":"
            "{\"cardholder_name\":\"JIRO TANAKA\",\"email\":\"jiro@example.com\"}}],"
            "\"has_more\":false,\"total_hits\":3}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_store_transaction_tokens(self):
        """
        Lists all transaction tokens for a specific store.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        search = "tokyo"
        customer_id = "8a3f1b8e-2c1a-4b7a-9c2e-6f6b6f6e2b10"
        mtype = "recurring"
        mode = "live"
        active = "active"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_store_transaction_tokens(
            store_id,
            search,
            customer_id,
            mtype,
            mode,
            active,
            limit,
            cursor,
            cursor_direction,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"items\":[{\"id\":\"2fe23e45-f95d-4c95-9963-739070096443\",\"store_id"
            "\":\"79e9504e-96d8-46ed-8d22-2e8b36238605\",\"merchant_name\":\"Test Mer"
            "chant\",\"store_name\":\"Tokyo Store\",\"email\":\"taro@example.com\",\""
            "payment_type\":\"card\",\"active\":true,\"mode\":\"live\",\"type\":\"rec"
            "urring\",\"created_on\":\"2026-04-09T07:35:50Z\",\"updated_on\":\"2026-0"
            "4-09T07:35:50Z\",\"user_data\":{\"cardholder_name\":\"TARO YAMADA\",\"em"
            "ail\":\"taro@example.com\"}},{\"id\":\"5cf56e78-c28a-4f28-cc96-06c303329"
            "776\",\"store_id\":\"79e9504e-96d8-46ed-8d22-2e8b36238605\",\"merchant_n"
            "ame\":\"Test Merchant\",\"store_name\":\"Tokyo Store\",\"email\":\"sabur"
            "o@example.com\",\"payment_type\":\"card\",\"active\":true,\"mode\":\"liv"
            "e\",\"type\":\"one_time\",\"created_on\":\"2026-04-10T12:14:00Z\",\"upda"
            "ted_on\":\"2026-04-10T12:14:00Z\",\"user_data\":{\"cardholder_name\":\"S"
            "ABURO KATO\",\"email\":\"saburo@example.com\"}},{\"id\":\"6df67e89-d39a-"
            "4039-dd07-17d414430887\",\"store_id\":\"79e9504e-96d8-46ed-8d22-2e8b3623"
            "8605\",\"merchant_name\":\"Test Merchant\",\"store_name\":\"Tokyo Store"
            "\",\"email\":\"shiro@example.com\",\"payment_type\":\"card\",\"active\":"
            "true,\"mode\":\"live\",\"type\":\"subscription\",\"created_on\":\"2026-0"
            "4-11T16:48:23Z\",\"updated_on\":\"2026-04-11T16:48:23Z\",\"user_data\":{"
            "\"cardholder_name\":\"SHIRO ITO\",\"email\":\"shiro@example.com\"}}],\"h"
            "as_more\":false,\"total_hits\":3}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_transaction_token(self):
        """
        Retrieves the details of an existing transaction token.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        polling = True

        # Perform the API call through the SDK function
        result = self.controller.get_transaction_token(
            store_id,
            id,
            polling,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"11f11e85-e9e9-b198-b990-c3a715943241\",\"store_id\":\"11f0e274"
            "-1e3b-4752-9513-33d3e07ede13\",\"email\":\"test@test.com\",\"payment_typ"
            "e\":\"card\",\"active\":true,\"mode\":\"live\",\"type\":\"recurring\",\""
            "usage_limit\":null,\"confirmed\":null,\"metadata\":{\"univapay-link-id\""
            ":\"11f11e85-1b45-dace-bf3d-cbcae52f65fc\",\"univapay-name\":\"test\",\"u"
            "nivapay-phone-number\":\"+81 08012341234\",\"items\":[\"productName: Che"
            "rry Ice Sandwich, price: 3080, quantity: 1\",\"productName: Shipping, pr"
            "ice: 200, quantity: 1\"],\"order_no\":1,\"note\":null},\"created_on\":\""
            "2026-03-13T02:39:52.908468Z\",\"updated_on\":\"2026-03-13T02:39:52.90846"
            "8Z\",\"last_used_on\":null,\"data\":{\"card\":{\"cardholder\":\"TEST TES"
            "T\",\"exp_month\":9,\"exp_year\":2026,\"card_bin\":\"424242\",\"last_fou"
            "r\":\"424242\",\"brand\":\"visa\",\"card_type\":\"credit\",\"country\":"
            "\"JP\",\"category\":\"standard\",\"issuer\":\"issuer\",\"sub_brand\":\"n"
            "one\"},\"billing\":{\"line1\":null,\"line2\":null,\"state\":null,\"city"
            "\":null,\"country\":null,\"zip\":null,\"phone_number\":{\"country_code\""
            ":81,\"local_number\":\"08012341234\"}},\"cvv_authorize\":{\"enabled\":fa"
            "lse,\"status\":null,\"charge_id\":null,\"credentials_id\":null,\"currenc"
            "y\":null},\"cvv_authorize_check\":{\"status\":null,\"charge_id\":null,\""
            "date\":null},\"three_ds\":{\"enabled\":true,\"status\":\"pending\",\"red"
            "irect_endpoint\":\"https://univapay.com/redirect/index.html\",\"error\":"
            "null,\"exempted\":false}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_transaction_token(self):
        """
        ⚠️ **LEGACY WARNING: Discouraged Operation**While it is technically possible
        to update a transaction token, this practice is highly discouraged and is
        maintained solely for legacy reasons. **Updating raw card details requires
        your server environment to be fully PCI DSS compliant.****Recommended
        Approach:** Instead of updating an existing token, it is best practice to
        create an entirely new transaction token using Univapay's frontend
        integrations (**Link Form**, **Widget**, or **Inline Form**). This allows
        Univapay to securely handle the customer's payment data without it ever
        touching your servers.--- **Legacy Usage:** Updates CVV, Address, Email, or
        Card Details.  *Note: If updating only the CVV to resolve a
        `RECURRING_USAGE_REQUIRES_CVV` error, the application token secret is not
        required.*.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"
        body = APIHelper.json_deserialize(
            "{\"email\":\"test.update@test.com\",\"data\":{\"cardholder\":\"TARO YAMA"
            "DA\",\"card_number\":\"4000020000000000\",\"exp_month\":12,\"exp_year\":"
            "2099,\"cvv\":\"123\",\"line1\":\"11111\",\"line2\":\"222\",\"state\":\"T"
            "okyo\",\"city\":\"テスト区一丁目\",\"country\":\"JP\",\"zip\":\"1234567\",\"pho"
            "ne_number\":{\"country_code\":\"81\",\"local_number\":\"08000000000\"}}}"
            "",
            TransactionTokenUpdateRequest.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.update_transaction_token(
            store_id,
            id,
            idempotency_key,
            body,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"11f11e85-e9e9-b198-b990-c3a715943241\",\"store_id\":\"11f0e274"
            "-1e3b-4752-9513-33d3e07ede13\",\"email\":\"test@test.com\",\"payment_typ"
            "e\":\"card\",\"active\":true,\"mode\":\"live\",\"type\":\"recurring\",\""
            "usage_limit\":null,\"confirmed\":null,\"metadata\":{\"univapay-link-id\""
            ":\"11f11e85-1b45-dace-bf3d-cbcae52f65fc\",\"univapay-name\":\"test\",\"u"
            "nivapay-phone-number\":\"+81 08012341234\",\"items\":[\"productName: Che"
            "rry Ice Sandwich, price: 3080, quantity: 1\",\"productName: Shipping, pr"
            "ice: 200, quantity: 1\"],\"order_no\":1,\"note\":null},\"created_on\":\""
            "2026-03-13T02:39:52.908468Z\",\"updated_on\":\"2026-03-13T02:39:52.90846"
            "8Z\",\"last_used_on\":null,\"data\":{\"card\":{\"cardholder\":\"TEST TES"
            "T\",\"exp_month\":9,\"exp_year\":2026,\"card_bin\":\"424242\",\"last_fou"
            "r\":\"424242\",\"brand\":\"visa\",\"card_type\":\"credit\",\"country\":"
            "\"JP\",\"category\":\"standard\",\"issuer\":\"issuer\",\"sub_brand\":\"n"
            "one\"},\"billing\":{\"line1\":null,\"line2\":null,\"state\":null,\"city"
            "\":null,\"country\":null,\"zip\":null,\"phone_number\":{\"country_code\""
            ":81,\"local_number\":\"08012341234\"}},\"cvv_authorize\":{\"enabled\":fa"
            "lse,\"status\":null,\"charge_id\":null,\"credentials_id\":null,\"currenc"
            "y\":null},\"cvv_authorize_check\":{\"status\":null,\"charge_id\":null,\""
            "date\":null},\"three_ds\":{\"enabled\":true,\"status\":\"pending\",\"red"
            "irect_endpoint\":\"https://univapay.com/redirect/index.html\",\"error\":"
            "null,\"exempted\":false}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_delete_transaction_token(self):
        """
        Deletes a specific transaction token. ⚠️ **WARNING: Breaks Linked
        Subscriptions**Please note that deleting a transaction token will immediately
        prevent any linked recurring charges or subscriptions from being processed.
        Proceed with caution.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"

        # Perform the API call through the SDK function
        self.controller.delete_transaction_token(
            store_id,
            id,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 204

    def test_enable_token_three_ds(self):
        """
        Enables 3-D Secure on an existing `recurring` transaction token that was
        created without it. Only applies to `recurring` tokens; returns an error if
        3DS is already enabled. After calling this endpoint, poll the token until
        `data.three_ds.status` becomes `awaiting`, then use the token 3DS issuer token
        endpoint to complete authentication.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"
        body = APIHelper.json_deserialize(
            "{\"redirect_endpoint\":\"https://univapay.com/3ds-redirect\"}",
            EnableTokenThreeDsRequest.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.enable_token_three_ds(
            store_id,
            id,
            idempotency_key,
            body,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"11f11e85-e9e9-b198-b990-c3a715943241\",\"store_id\":\"11f0e274"
            "-1e3b-4752-9513-33d3e07ede13\",\"email\":\"test@test.com\",\"payment_typ"
            "e\":\"card\",\"active\":true,\"mode\":\"live\",\"type\":\"recurring\",\""
            "usage_limit\":null,\"confirmed\":null,\"metadata\":{\"univapay-link-id\""
            ":\"11f11e85-1b45-dace-bf3d-cbcae52f65fc\",\"univapay-name\":\"test\",\"u"
            "nivapay-phone-number\":\"+81 08012341234\",\"items\":[\"productName: Che"
            "rry Ice Sandwich, price: 3080, quantity: 1\",\"productName: Shipping, pr"
            "ice: 200, quantity: 1\"],\"order_no\":1,\"note\":null},\"created_on\":\""
            "2026-03-13T02:39:52.908468Z\",\"updated_on\":\"2026-03-13T02:39:52.90846"
            "8Z\",\"last_used_on\":null,\"data\":{\"card\":{\"cardholder\":\"TEST TES"
            "T\",\"exp_month\":9,\"exp_year\":2026,\"card_bin\":\"424242\",\"last_fou"
            "r\":\"424242\",\"brand\":\"visa\",\"card_type\":\"credit\",\"country\":"
            "\"JP\",\"category\":\"standard\",\"issuer\":\"issuer\",\"sub_brand\":\"n"
            "one\"},\"billing\":{\"line1\":null,\"line2\":null,\"state\":null,\"city"
            "\":null,\"country\":null,\"zip\":null,\"phone_number\":{\"country_code\""
            ":81,\"local_number\":\"08012341234\"}},\"cvv_authorize\":{\"enabled\":fa"
            "lse,\"status\":null,\"charge_id\":null,\"credentials_id\":null,\"currenc"
            "y\":null},\"cvv_authorize_check\":{\"status\":null,\"charge_id\":null,\""
            "date\":null},\"three_ds\":{\"enabled\":true,\"status\":\"pending\",\"red"
            "irect_endpoint\":\"https://univapay.com/redirect/index.html\",\"error\":"
            "null,\"exempted\":false}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_disable_token_three_ds(self):
        """
        Disables 3-D Secure on an existing `recurring` transaction token. Only applies
        to `recurring` tokens.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"

        # Perform the API call through the SDK function
        result = self.controller.disable_token_three_ds(
            store_id,
            id,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"11f11e85-e9e9-b198-b990-c3a715943241\",\"store_id\":\"11f0e274"
            "-1e3b-4752-9513-33d3e07ede13\",\"email\":\"test@test.com\",\"payment_typ"
            "e\":\"card\",\"active\":true,\"mode\":\"live\",\"type\":\"recurring\",\""
            "usage_limit\":null,\"confirmed\":null,\"metadata\":{\"univapay-link-id\""
            ":\"11f11e85-1b45-dace-bf3d-cbcae52f65fc\",\"univapay-name\":\"test\",\"u"
            "nivapay-phone-number\":\"+81 08012341234\",\"items\":[\"productName: Che"
            "rry Ice Sandwich, price: 3080, quantity: 1\",\"productName: Shipping, pr"
            "ice: 200, quantity: 1\"],\"order_no\":1,\"note\":null},\"created_on\":\""
            "2026-03-13T02:39:52.908468Z\",\"updated_on\":\"2026-03-13T02:39:52.90846"
            "8Z\",\"last_used_on\":null,\"data\":{\"card\":{\"cardholder\":\"TEST TES"
            "T\",\"exp_month\":9,\"exp_year\":2026,\"card_bin\":\"424242\",\"last_fou"
            "r\":\"424242\",\"brand\":\"visa\",\"card_type\":\"credit\",\"country\":"
            "\"JP\",\"category\":\"standard\",\"issuer\":\"issuer\",\"sub_brand\":\"n"
            "one\"},\"billing\":{\"line1\":null,\"line2\":null,\"state\":null,\"city"
            "\":null,\"country\":null,\"zip\":null,\"phone_number\":{\"country_code\""
            ":81,\"local_number\":\"08012341234\"}},\"cvv_authorize\":{\"enabled\":fa"
            "lse,\"status\":null,\"charge_id\":null,\"credentials_id\":null,\"currenc"
            "y\":null},\"cvv_authorize_check\":{\"status\":null,\"charge_id\":null,\""
            "date\":null},\"three_ds\":{\"enabled\":true,\"status\":\"pending\",\"red"
            "irect_endpoint\":\"https://univapay.com/redirect/index.html\",\"error\":"
            "null,\"exempted\":false}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_token_three_ds_issuer_token(self):
        """
        Retrieves the information required to execute 3-D Secure authentication when
        creating a recurring transaction token.**⚠️ Important Notes:** 1. **PCI DSS
        Compliance:** This endpoint is only available to PCI DSS compliant merchants
        who are authorized to send raw card data directly via the API to create
        tokens. 2. **Target Tokens:** This only applies to tokens where `type` is
        `recurring`. For `one_time` or `subscription` tokens, 3-D Secure is requested
        during charge creation, not token creation. 3. **Execution Flow:**   - After
        creating the token, poll the token object until `data.three_ds.status` becomes
        `awaiting`.   - Once `awaiting`, use this endpoint to fetch the issuer token
        details.   - Format the returned `payload` according to the `content_type`
        (e.g., URL-encoded) and execute an `http_post` request from the consumer's
        browser to the `issuer_token` URL.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"

        # Perform the API call through the SDK function
        result = self.controller.get_token_three_ds_issuer_token(
            store_id,
            id,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"issuer_token\":\"http://test.com/action\",\"call_method\":\"http_post"
            "\",\"payload\":{\"request_data\":\"example_value\"},\"payment_type\":\"c"
            "ard\",\"content_type\":\"application/x-www-form-urlencoded; charset=UTF-"
            "8\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

