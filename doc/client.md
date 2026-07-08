
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| base_url | `str` | Base URL for the API<br>*Default*: `"https://api.univapay.com"` |
| environment | [`Environment`](../README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](../doc/logging-configuration.md) | The SDK logging configuration for API calls |
| bearer_auth_credentials | [`BearerAuthCredentials`](auth/oauth-2-bearer-token.md) | The credential object for OAuth 2 Bearer token |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
import logging

from univapayclientsdk.configuration import Environment
from univapayclientsdk.http.auth.oauth_2 import BearerAuthCredentials
from univapayclientsdk.logging.configuration.api_logging_configuration import LoggingConfiguration
from univapayclientsdk.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from univapayclientsdk.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from univapayclientsdk.univapay_client_sdk_client import UnivapayClientSdkClient

client = UnivapayClientSdkClient(
    bearer_auth_credentials=BearerAuthCredentials(
        access_token='AccessToken'
    ),
    environment=Environment.PRODUCTION,
    base_url='https://api.univapay.com',
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environment-Based Client Initialization

```python
from univapayclientsdk.univapay_client_sdk_client import UnivapayClientSdkClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = UnivapayClientSdkClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Univapay Public API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| charges | Gets ChargesController |
| transaction_tokens | Gets TransactionTokensController |
| refunds | Gets RefundsController |
| subscriptions | Gets SubscriptionsController |
| cancels | Gets CancelsController |
| merchants | Gets MerchantsController |
| stores | Gets StoresController |
| webhooks | Gets WebhooksController |

