
# Issuer Token Payload

A dictionary containing necessary key-value pairs for sending the request.

*This model accepts additional fields of type Any.*

## Structure

`IssuerTokenPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_data` | `str` | Optional | Generic payload key used by most payment providers. |
| `s_spcd` | `str` | Optional | d-barai payment service code. |
| `s_cptok` | `str` | Optional | d-barai coupon token. |
| `s_terkn` | `str` | Optional | d-barai terminal key. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.issuer_token_payload import IssuerTokenPayload

issuer_token_payload = IssuerTokenPayload(
    request_data='request_data0',
    s_spcd='sSpcd0',
    s_cptok='sCptok6',
    s_terkn='sTerkn0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

