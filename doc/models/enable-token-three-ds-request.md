
# Enable Token Three Ds Request

Request payload for enabling 3DS on a recurring token. Both the body and `redirect_endpoint` are optional.

*This model accepts additional fields of type Any.*

## Structure

`EnableTokenThreeDsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `redirect_endpoint` | `str` | Optional | URL to redirect the customer to after 3DS authentication. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.enable_token_three_ds_request import EnableTokenThreeDsRequest

enable_token_three_ds_request = EnableTokenThreeDsRequest()
```

