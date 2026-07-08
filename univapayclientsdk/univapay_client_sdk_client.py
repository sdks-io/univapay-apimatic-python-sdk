"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from apimatic_core.configurations.global_configuration import (
    GlobalConfiguration,
)
from apimatic_core.decorators.lazy_property import (
    LazyProperty,
)

from univapayclientsdk.configuration import (
    Configuration,
    Environment,
)
from univapayclientsdk.controllers.base_controller import (
    BaseController,
)
from univapayclientsdk.controllers.cancels_controller import (
    CancelsController,
)
from univapayclientsdk.controllers.charges_controller import (
    ChargesController,
)
from univapayclientsdk.controllers.merchants_controller import (
    MerchantsController,
)
from univapayclientsdk.controllers.refunds_controller import (
    RefundsController,
)
from univapayclientsdk.controllers.stores_controller import (
    StoresController,
)
from univapayclientsdk.controllers.subscriptions_controller import (
    SubscriptionsController,
)
from univapayclientsdk.controllers.transaction_tokens_controller import (
    TransactionTokensController,
)
from univapayclientsdk.controllers.webhooks_controller import (
    WebhooksController,
)
from univapayclientsdk.http.auth.oauth_2 import (
    Oauth2,
)


class UnivapayClientSdkClient(object):
    """Client that provide access to the UnivapayClientSdkClient APIs."""

    @LazyProperty
    def charges(self):
        """Provide access to the ChargesController endpoints."""
        return ChargesController(self.global_configuration)

    @LazyProperty
    def transaction_tokens(self):
        """Provide access to the TransactionTokensController endpoints."""
        return TransactionTokensController(self.global_configuration)

    @LazyProperty
    def refunds(self):
        """Provide access to the RefundsController endpoints."""
        return RefundsController(self.global_configuration)

    @LazyProperty
    def subscriptions(self):
        """Provide access to the SubscriptionsController endpoints."""
        return SubscriptionsController(self.global_configuration)

    @LazyProperty
    def cancels(self):
        """Provide access to the CancelsController endpoints."""
        return CancelsController(self.global_configuration)

    @LazyProperty
    def merchants(self):
        """Provide access to the MerchantsController endpoints."""
        return MerchantsController(self.global_configuration)

    @LazyProperty
    def stores(self):
        """Provide access to the StoresController endpoints."""
        return StoresController(self.global_configuration)

    @LazyProperty
    def webhooks(self):
        """Provide access to the WebhooksController endpoints."""
        return WebhooksController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=30, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None, proxy_settings=None,
                 logging_configuration=None, environment=Environment.PRODUCTION,
                 base_url="https://api.univapay.com",
                 bearer_auth_credentials=None, config=None):
        """Initialize a new instance of UnivapayClientSdkClient."""
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            proxy_settings=proxy_settings,
            logging_configuration=logging_configuration,
            environment=environment, base_url=base_url,
            bearer_auth_credentials=bearer_auth_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(),
                BaseController.user_agent_parameters())

        self.auth_managers = {
            "JWT_TOKEN": Oauth2(self.config.bearer_auth_credentials),
        }
        self.global_configuration =\
            self.global_configuration.auth_managers(self.auth_managers)

    @classmethod
    def from_environment(cls, dotenv_path=None, **overrides):
        """Create a client instance using environment variables.

        Returns:
            UnivapayClientSdkClient instance.

        """
        return cls(config=Configuration
            .from_environment(dotenv_path=dotenv_path, **overrides))
