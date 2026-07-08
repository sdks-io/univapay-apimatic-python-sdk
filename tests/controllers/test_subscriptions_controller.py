
"""
univapay_client_sdk

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291, W293, E501
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)

from tests.controllers.controller_test_base import (
    ControllerTestBase,
)
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.subscription_create_request import (
    SubscriptionCreateRequest,
)
from univapayclientsdk.models.subscription_patch_payment_request import (
    SubscriptionPatchPaymentRequest,
)
from univapayclientsdk.models.subscription_patch_token_request import (
    SubscriptionPatchTokenRequest,
)
from univapayclientsdk.models.subscription_suspend_request import (
    SubscriptionSuspendRequest,
)
from univapayclientsdk.models.subscription_update_request import (
    SubscriptionUpdateRequest,
)


class SubscriptionsControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.subscriptions
        cls.response_catcher = cls.controller.http_call_back

    def test_create_subscription(self):
        """
        Creates a new subscription.
        """
        # Parameters for the API call
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"
        body = APIHelper.json_deserialize(
            "{\"transaction_token_id\":\"11ef32a7-3a71-8662-803f-1bc27702eeec\",\"amo"
            "unt\":1000,\"currency\":\"JPY\",\"period\":\"monthly\"}",
            SubscriptionCreateRequest.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.create_subscription(
            idempotency_key,
            body,
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
            "{\"id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"store_id\":\"11edf541"
            "-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11ef32a7-3a71-"
            "8662-803f-1bc27702eeec\",\"amount\":1250,\"currency\":\"USD\",\"amount_f"
            "ormatted\":12.5,\"initial_amount\":1000,\"initial_amount_formatted\":10."
            "0,\"subsequent_cycles_start\":null,\"only_direct_currency\":false,\"firs"
            "t_charge_authorization_only\":false,\"status\":\"current\",\"metadata\":"
            "{\"order_id\":\"ORD-987\"},\"mode\":\"live\",\"created_on\":\"2024-06-26"
            "T01:51:28.627023Z\",\"period\":\"monthly\",\"next_payment\":{\"id\":\"11"
            "ef3360-1f9a-c54a-8313-7f9847da313b\",\"due_date\":\"2024-07-26\",\"zone_"
            "id\":\"Asia/Tokyo\",\"amount\":1250,\"currency\":\"USD\",\"amount_format"
            "ted\":12.5,\"is_paid\":false}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_all_subscriptions(self):
        """
        Lists all subscriptions across all stores.
        """
        # Parameters for the API call
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_all_subscriptions(
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
            "{\"items\":[{\"id\":\"11ef3410-aaaa-4bcd-8e1f-1a2b3c4d5e60\",\"store_id"
            "\":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"1"
            "1ef3413-dddd-4ef0-b142-4d5e6f809193\",\"amount\":1250,\"currency\":\"USD"
            "\",\"amount_formatted\":12.5,\"status\":\"current\",\"merchant_name\":\""
            "管理画面ガイド\",\"store_name\":\"管理画面ガイド_TEST店舗\",\"payment_type\":\"card\",\""
            "next_payment_date\":\"2024-07-26\",\"user_data\":{\"type\":\"charge\",\""
            "cardholder_name\":\"taro yamada\",\"email\":\"taro@test.com\",\"brand\":"
            "\"visa\"}},{\"id\":\"11ef3411-bbbb-4cde-9f20-2b3c4d5e6f71\",\"store_id\""
            ":\"22af6520-d53e-764d-9d4e-ef01b66fa6d1\",\"transaction_token_id\":\"11e"
            "f3414-eeee-4f01-c253-5e6f80919204\",\"amount\":3000,\"currency\":\"JPY\""
            ",\"amount_formatted\":3000,\"status\":\"current\",\"merchant_name\":\"管理"
            "画面ガイド\",\"store_name\":\"管理画面ガイド_Online店舗\",\"payment_type\":\"card\",\""
            "next_payment_date\":\"2024-08-10\",\"user_data\":{\"type\":\"charge\",\""
            "cardholder_name\":\"hanako suzuki\",\"email\":\"hanako@test.com\",\"bran"
            "d\":\"mastercard\"}},{\"id\":\"11ef3412-cccc-4def-a031-3c4d5e6f8082\",\""
            "store_id\":\"33af7631-e64f-875e-ae5f-f012c77fb7e2\",\"transaction_token_"
            "id\":\"11ef3415-ffff-4012-d364-6f8091920315\",\"amount\":9800,\"currency"
            "\":\"JPY\",\"amount_formatted\":9800,\"status\":\"suspended\",\"merchant"
            "_name\":\"管理画面ガイド\",\"store_name\":\"管理画面ガイド_Osaka店舗\",\"payment_type\":"
            "\"card\",\"next_payment_date\":\"2024-09-15\",\"user_data\":{\"type\":\""
            "charge\",\"cardholder_name\":\"jiro tanaka\",\"email\":\"jiro@test.com\""
            ",\"brand\":\"jcb\"}}],\"has_more\":false,\"total_hits\":3}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_store_subscriptions(self):
        """
        Lists all subscriptions for a specific store.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        search = "order_id:12345"
        status = "current"
        mode = "live"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_store_subscriptions(
            store_id,
            search,
            status,
            mode,
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
            "{\"items\":[{\"id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"store_id"
            "\":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"1"
            "1ef32a7-3a71-8662-803f-1bc27702eeec\",\"amount\":1250,\"currency\":\"USD"
            "\",\"amount_formatted\":12.5,\"status\":\"current\",\"merchant_name\":\""
            "管理画面ガイド\",\"store_name\":\"管理画面ガイド_TEST店舗\",\"payment_type\":\"card\",\""
            "next_payment_date\":\"2024-07-26\",\"user_data\":{\"type\":\"charge\",\""
            "cardholder_name\":\"taro yamada\",\"email\":\"test@test.com\",\"brand\":"
            "\"visa\"}},{\"id\":\"11ef3401-1a2b-4c3d-8e4f-5a6b7c8d9e0f\",\"store_id\""
            ":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11e"
            "f3402-2b3c-4d5e-9f60-6b7c8d9e0f11\",\"amount\":5000,\"currency\":\"JPY\""
            ",\"amount_formatted\":5000,\"status\":\"current\",\"merchant_name\":\"管理"
            "画面ガイド\",\"store_name\":\"管理画面ガイド_TEST店舗\",\"payment_type\":\"card\",\"ne"
            "xt_payment_date\":\"2024-08-01\",\"user_data\":{\"type\":\"charge\",\"ca"
            "rdholder_name\":\"hanako suzuki\",\"email\":\"hanako@test.com\",\"brand"
            "\":\"mastercard\"}},{\"id\":\"11ef3403-3c4d-5e6f-a071-7c8d9e0f1122\",\"s"
            "tore_id\":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_i"
            "d\":\"11ef3404-4d5e-6f70-b182-8d9e0f112233\",\"amount\":9800,\"currency"
            "\":\"JPY\",\"amount_formatted\":9800,\"status\":\"suspended\",\"merchant"
            "_name\":\"管理画面ガイド\",\"store_name\":\"管理画面ガイド_TEST店舗\",\"payment_type\":"
            "\"card\",\"next_payment_date\":\"2024-09-15\",\"user_data\":{\"type\":\""
            "charge\",\"cardholder_name\":\"jiro tanaka\",\"email\":\"jiro@test.com\""
            ",\"brand\":\"jcb\"}}],\"has_more\":false,\"total_hits\":3}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_subscription(self):
        """
        Retrieves the details of an existing subscription.  Supports internal polling
        to wait for status changes.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "11ef335e-9aa5-c54a-8313-7f9847da313a"
        polling = True

        # Perform the API call through the SDK function
        result = self.controller.get_subscription(
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
            "{\"id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"store_id\":\"11edf541"
            "-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11ef32a7-3a71-"
            "8662-803f-1bc27702eeec\",\"amount\":1250,\"currency\":\"USD\",\"amount_f"
            "ormatted\":12.5,\"initial_amount\":null,\"initial_amount_formatted\":nul"
            "l,\"subsequent_cycles_start\":null,\"schedule_settings\":{\"start_on\":"
            "\"2024-07-01\",\"zone_id\":\"Asia/Tokyo\",\"preserve_end_of_month\":fals"
            "e,\"retry_interval\":\"P7D\",\"termination_mode\":\"immediate\"},\"only_"
            "direct_currency\":false,\"first_charge_capture_after\":null,\"first_char"
            "ge_authorization_only\":false,\"status\":\"current\",\"metadata\":{\"ord"
            "er_id\":\"12345\"},\"mode\":\"test\",\"created_on\":\"2024-06-26T01:51:2"
            "8.627023Z\",\"period\":\"monthly\",\"next_payment\":{\"id\":\"11ef335e-9"
            "ae2-8322-8e79-e7ba4b56234e\",\"due_date\":\"2024-07-26\",\"zone_id\":\"A"
            "sia/Tokyo\",\"amount\":1250,\"currency\":\"USD\",\"amount_formatted\":12"
            ".5,\"is_paid\":false,\"is_last_payment\":false,\"created_on\":\"2024-06-"
            "26T01:51:29.025129Z\",\"updated_on\":\"2024-06-26T01:51:29.025129Z\",\"r"
            "etry_date\":null}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_subscription(self):
        """
        Updates the configuration, payment method, or schedule of a specific
        subscription.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"
        body = APIHelper.json_deserialize(
            "{\"metadata\":{\"order_id\":\"12345\"},\"schedule_settings\":{\"terminat"
            "ion_mode\":\"on_next_payment\"}}",
            SubscriptionUpdateRequest.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.update_subscription(
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
            "{\"id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"store_id\":\"11edf541"
            "-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11ef3362-3700-"
            "c54a-9baa-6f7e6527c9d9\",\"amount\":1250,\"currency\":\"USD\",\"amount_f"
            "ormatted\":12.5,\"initial_amount\":null,\"initial_amount_formatted\":nul"
            "l,\"subsequent_cycles_start\":null,\"schedule_settings\":{\"start_on\":"
            "\"2024-07-01\",\"zone_id\":\"Asia/Tokyo\",\"preserve_end_of_month\":fals"
            "e,\"retry_interval\":\"P7D\",\"termination_mode\":\"on_next_payment\"},"
            "\"only_direct_currency\":false,\"first_charge_capture_after\":null,\"fir"
            "st_charge_authorization_only\":false,\"status\":\"current\",\"metadata\""
            ":{\"order_id\":\"12345\"},\"mode\":\"test\",\"created_on\":\"2024-06-26T"
            "01:51:28.627023Z\",\"period\":\"monthly\",\"next_payment\":{\"id\":\"11e"
            "f335e-9ae2-8322-8e79-e7ba4b56234e\",\"due_date\":\"2030-01-01\",\"zone_i"
            "d\":\"Asia/Tokyo\",\"amount\":1250,\"currency\":\"USD\",\"amount_formatt"
            "ed\":12.5,\"is_paid\":false,\"is_last_payment\":false,\"created_on\":\"2"
            "024-06-26T01:51:29.025129Z\",\"updated_on\":\"2024-06-26T01:51:29.025129"
            "Z\",\"retry_date\":null}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_cancel_subscription(self):
        """
        Cancels an existing subscription. The subscription status will be  permanently
        changed to `canceled` and it cannot be resumed.  Please proceed with caution.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"

        # Perform the API call through the SDK function
        self.controller.cancel_subscription(
            store_id,
            id,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 204

    def test_list_subscription_payments(self):
        """
        Retrieves a list of all historical and scheduled payments for a  specific
        subscription.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "25d0fb2c-18ef-11e7-9dd3-db8fb7b820e7"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_subscription_payments(
            store_id,
            subscription_id,
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
            "{\"items\":[{\"id\":\"11e89a0a-8cee-d660-b984-3fcaaed46e7c\",\"due_date"
            "\":\"2018-08-21\",\"zone_id\":\"Asia/Tokyo\",\"amount\":10000,\"currency"
            "\":\"JPY\",\"amount_formatted\":10000,\"is_paid\":false,\"is_last_paymen"
            "t\":false,\"created_on\":\"2018-08-07T06:24:33.961256Z\",\"updated_on\":"
            "\"2018-08-07T06:24:33.961256Z\"},{\"id\":\"11e89a0a-8cc5-2662-9460-2b14b"
            "1a601ba\",\"due_date\":\"2018-08-07\",\"zone_id\":\"Asia/Tokyo\",\"amoun"
            "t\":1000,\"currency\":\"JPY\",\"amount_formatted\":1000,\"is_paid\":true"
            ",\"is_last_payment\":false,\"created_on\":\"2018-08-07T06:24:33.646223Z"
            "\",\"updated_on\":\"2018-08-07T06:24:33.887760Z\"}],\"has_more\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_subscription_payment(self):
        """
        Retrieves the details of an individual payment associated with a specific
        subscription.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "25d0fb2c-18ef-11e7-9dd3-db8fb7b820e7"
        payment_id = "11e89a0a-8cee-d660-b984-3fcaaed46e7c"

        # Perform the API call through the SDK function
        result = self.controller.get_subscription_payment(
            store_id,
            subscription_id,
            payment_id,
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
            "{\"id\":\"11e89a0a-8cee-d660-b984-3fcaaed46e7c\",\"due_date\":\"2018-08-"
            "21\",\"zone_id\":\"Asia/Tokyo\",\"amount\":10000,\"currency\":\"JPY\",\""
            "amount_formatted\":10000,\"is_paid\":false,\"is_last_payment\":false,\"c"
            "reated_on\":\"2018-08-07T06:24:33.961256Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_subscription_payment(self):
        """
        Updates properties of a specific scheduled payment for a subscription. Can be
        used to change the due date when permitted, mark the payment as paid, schedule
        a termination status, or set a retry interval.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "25d0fb2c-18ef-11e7-9dd3-db8fb7b820e7"
        payment_id = "11e89a0a-8cee-d660-b984-3fcaaed46e7c"
        body = APIHelper.json_deserialize(
            "{\"due_date\":\"2026-09-01\",\"is_paid\":false}",
            SubscriptionPatchPaymentRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.update_subscription_payment(
            store_id,
            subscription_id,
            payment_id,
            body,
            idempotency_key,
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
            "{\"id\":\"11e89a0a-8cee-d660-b984-3fcaaed46e7c\",\"due_date\":\"2026-09-"
            "01\",\"zone_id\":\"Asia/Tokyo\",\"amount\":10000,\"currency\":\"JPY\",\""
            "amount_formatted\":10000,\"is_paid\":false,\"is_last_payment\":false,\"c"
            "reated_on\":\"2018-08-07T06:24:33.961256Z\",\"updated_on\":\"2026-04-22T"
            "06:00:00.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_subscription_latest_charge(self):
        """
        Retrieves the most recent charge created for a specific subscription. Returns
        404 if no charges have been attempted yet.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "25d0fb2c-18ef-11e7-9dd3-db8fb7b820e7"

        # Perform the API call through the SDK function
        result = self.controller.get_subscription_latest_charge(
            store_id,
            subscription_id,
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
            "{\"id\":\"6efb4e5c-690a-40f3-a4f1-0e19c5f84e98\",\"store_id\":\"11edf541"
            "-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11ef32a7-3a71-"
            "8662-803f-1bc27702eeec\",\"transaction_token_type\":\"recurring\",\"subs"
            "cription_id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"requested_amoun"
            "t\":1250,\"requested_currency\":\"USD\",\"requested_amount_formatted\":1"
            "2.5,\"charged_amount\":1250,\"charged_currency\":\"USD\",\"charged_amoun"
            "t_formatted\":12.5,\"only_direct_currency\":false,\"status\":\"successfu"
            "l\",\"error\":null,\"mode\":\"test\",\"created_on\":\"2024-06-26T01:51:3"
            "0.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_subscription_charges(self):
        """
        Retrieves a paginated list of charges linked to a subscription. Backend search
        uses the same charge search surface as normal charge listing and adds a
        subscription filter for the requested subscription.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "25d0fb2c-18ef-11e7-9dd3-db8fb7b820e7"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_subscription_charges(
            merchant_id,
            store_id,
            subscription_id,
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
            "{\"items\":[{\"id\":\"6efb4e5c-690a-40f3-a4f1-0e19c5f84e98\",\"store_id"
            "\":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"1"
            "1ef32a7-3a71-8662-803f-1bc27702eeec\",\"transaction_token_type\":\"recur"
            "ring\",\"subscription_id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"re"
            "quested_amount\":1250,\"requested_currency\":\"USD\",\"requested_amount_"
            "formatted\":12.5,\"charged_amount\":1250,\"charged_currency\":\"USD\",\""
            "charged_amount_formatted\":12.5,\"only_direct_currency\":false,\"status"
            "\":\"successful\",\"error\":{},\"mode\":\"test\",\"created_on\":\"2024-0"
            "6-26T01:51:30.000000Z\"}],\"has_more\":false,\"total_hits\":1}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_charges_for_subscription_payment(self):
        """
        Retrieves a paginated list of all charge attempts made for a specific
        scheduled payment of a subscription. Useful for inspecting retry history.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "25d0fb2c-18ef-11e7-9dd3-db8fb7b820e7"
        payment_id = "11e89a0a-8cee-d660-b984-3fcaaed46e7c"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_charges_for_subscription_payment(
            store_id,
            subscription_id,
            payment_id,
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
            "{\"items\":[{\"id\":\"6efb4e5c-690a-40f3-a4f1-0e19c5f84e98\",\"store_id"
            "\":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"1"
            "1ef32a7-3a71-8662-803f-1bc27702eeec\",\"transaction_token_type\":\"recur"
            "ring\",\"subscription_id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"re"
            "quested_amount\":1250,\"requested_currency\":\"USD\",\"requested_amount_"
            "formatted\":12.5,\"charged_amount\":1250,\"charged_currency\":\"USD\",\""
            "charged_amount_formatted\":12.5,\"only_direct_currency\":false,\"status"
            "\":\"successful\",\"error\":{},\"mode\":\"test\",\"created_on\":\"2024-0"
            "6-26T01:51:30.000000Z\"}],\"has_more\":false,\"total_hits\":1}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_suspend_subscription(self):
        """
        Suspends a subscription that is currently `current` or `unpaid`. The
        `termination_mode` controls when the suspension takes effect: `immediate`
        (default) suspends right away, `on_next_payment` waits until the next
        scheduled payment date before suspending.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "11ef335e-9aa5-c54a-8313-7f9847da313a"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"
        body = APIHelper.json_deserialize(
            "{\"schedule_settings\":{\"termination_mode\":\"on_next_payment\"}}",
            SubscriptionSuspendRequest.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.suspend_subscription(
            store_id,
            subscription_id,
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
            "{\"id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"store_id\":\"11edf541"
            "-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11ef32a7-3a71-"
            "8662-803f-1bc27702eeec\",\"amount\":1250,\"currency\":\"USD\",\"amount_f"
            "ormatted\":12.5,\"status\":\"suspended\",\"mode\":\"test\",\"created_on"
            "\":\"2024-06-26T01:51:28.627023Z\",\"period\":\"monthly\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_unsuspend_subscription(self):
        """
        Resumes a subscription that is currently `suspended`, setting its status back
        to `unpaid` and rescheduling the next payment. No request body is required.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "11ef335e-9aa5-c54a-8313-7f9847da313a"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.unsuspend_subscription(
            store_id,
            subscription_id,
            idempotency_key,
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
            "{\"id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"store_id\":\"11edf541"
            "-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11ef32a7-3a71-"
            "8662-803f-1bc27702eeec\",\"amount\":1250,\"currency\":\"USD\",\"amount_f"
            "ormatted\":12.5,\"status\":\"unpaid\",\"mode\":\"test\",\"created_on\":"
            "\"2024-06-26T01:51:28.627023Z\",\"period\":\"monthly\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_subscription_token(self):
        """
        Replaces the payment method (transaction token) used for a subscription.
        Useful when a card expires or a customer wants to switch payment methods. The
        new token must belong to the same store, be active, and match the
        subscription's processing mode (live/test). One-time tokens are not accepted;
        use a recurring or subscription token.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        subscription_id = "11ef335e-9aa5-c54a-8313-7f9847da313a"
        body = APIHelper.json_deserialize(
            "{\"transaction_token_id\":\"11ef3362-3700-c54a-9baa-6f7e6527c9d9\"}",
            SubscriptionPatchTokenRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.update_subscription_token(
            store_id,
            subscription_id,
            body,
            idempotency_key,
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
            "{\"id\":\"11ef335e-9aa5-c54a-8313-7f9847da313a\",\"store_id\":\"11edf541"
            "-c42d-653c-8c3d-dfe0a55f95c0\",\"transaction_token_id\":\"11ef3362-3700-"
            "c54a-9baa-6f7e6527c9d9\",\"amount\":1250,\"currency\":\"USD\",\"amount_f"
            "ormatted\":12.5,\"status\":\"current\",\"mode\":\"test\",\"created_on\":"
            "\"2024-06-26T01:51:28.627023Z\",\"period\":\"monthly\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

