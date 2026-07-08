
# Getting Started with Univapay Public API

## Introduction

OpenAPI specification for the Univapay Online Payment API.

### Authentication (JWT)

This API uses JWT (JSON Web Tokens) for authentication via the HTTP `Authorization` header. To authenticate, you must generate an **Application Token** in the Univapay dashboard.  This generates two components: 1. **Token (`{jwt}`)** 2. **Secret (`{secret}`)**

#### ⚠️ Security Warning

The **Secret** grants extensive privileges (e.g., creating charges, capturing authorized card charges, refunding).
**NEVER expose the `{secret}` in frontend application code** (e.g., consumer browsers) or public repositories. It is strictly for backend server-to-server communication.
*Univapay is not responsible for accidents caused by leaked secrets.*

#### Bearer Auth Formats

Depending on where you are calling the API from, the Bearer format changes:

* **Frontend / Browser (No Secret)**: `Bearer {jwt}`
  *(Used for Widgets or Inline Forms. You must register your allowed domains in the dashboard when creating the token).*
* **Backend / Server (With Secret)**: `Bearer {secret}.{jwt}`
  *(Required for all backend processing).*

We will assume that all requests are going to originate from a backend server thus, all requests will require the secret

#### Token Types

* **Store Token**: Grants full access to requests for that specific store.
* **Merchant Token**: Can't create transaction tokens but can access data from multiple stores.

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install univapay-apimatic-sdk==0.0.3
```

You can also view the package at:
https://pypi.python.org/pypi/univapay-apimatic-sdk/0.0.3

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands


pip install -r test-requirements.txt
pytest


## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| base_url | `str` | Base URL for the API<br>*Default*: `"https://api.univapay.com"` |
| environment | [`Environment`](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| bearer_auth_credentials | [`BearerAuthCredentials`](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/auth/oauth-2-bearer-token.md) | The credential object for OAuth 2 Bearer token |

The API client can be initialized as follows:

### Code-Based Client Initialization

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

### Environment-Based Client Initialization

```python
from univapayclientsdk.univapay_client_sdk_client import UnivapayClientSdkClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = UnivapayClientSdkClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| PRODUCTION | **Default** Production Server |

## Authorization

This API uses the following authentication schemes.

* [`JWT_TOKEN (OAuth 2 Bearer token)`](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/auth/oauth-2-bearer-token.md)

## List of APIs

* [Transaction Tokens](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/transaction-tokens.md)
* [Charges](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/charges.md)
* [Refunds](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/refunds.md)
* [Subscriptions](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/subscriptions.md)
* [Cancels](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/cancels.md)
* [Merchants](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/merchants.md)
* [Stores](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/stores.md)
* [Webhooks](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/controllers/webhooks.md)

## Webhooks

* [Charge Updated](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/charge-updated-handler.md)
* [Charge Finished](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/charge-finished-handler.md)
* [Token Created](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/token-created-handler.md)
* [Token Updated](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/token-updated-handler.md)
* [Token Three Ds Updated](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/token-three-ds-updated-handler.md)
* [Token Cvv Auth Updated](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/token-cvv-auth-updated-handler.md)
* [Token Cvv Auth Check Updated](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/token-cvv-auth-check-updated-handler.md)
* [Token Replaced](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/token-replaced-handler.md)
* [Recurring Token Deleted](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/recurring-token-deleted-handler.md)
* [Refund](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/refund-handler.md)
* [Cancel](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/cancel-handler.md)
* [Subscription Created](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/subscription-created-handler.md)
* [Subscription Payment](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/subscription-payment-handler.md)
* [Subscription Completed](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/subscription-completed-handler.md)
* [Subscription Failure](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/subscription-failure-handler.md)
* [Subscription Canceled](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/subscription-canceled-handler.md)
* [Subscription Suspended](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/subscription-suspended-handler.md)
* [Bank-Transfer](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/bank-transfer-handler.md)
* [Customs](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/events/webhooks/customs-handler.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/proxy-settings.md)
* [Environment-Based Client Initialization](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/environment-based-client-initialization.md)
* [AbstractLogger](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/abstract-logger.md)
* [LoggingConfiguration](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/http-request.md)
* [Request](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/request.md)

### Utilities

* [ApiResponse](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/api-response.md)
* [ApiHelper](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/sdks-io/univapay-apimatic-python-sdk/tree/0.0.3/doc/unix-date-time.md)

