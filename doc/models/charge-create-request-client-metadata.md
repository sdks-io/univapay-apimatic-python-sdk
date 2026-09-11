
# Charge Create Request Client Metadata

Charge Create Request Client Metadata schema.

*This model accepts additional fields of type Any.*

## Structure

`ChargeCreateRequestClientMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | Consumer's IPv4 address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.charge_create_request_client_metadata import ChargeCreateRequestClientMetadata

charge_create_request_client_metadata = ChargeCreateRequestClientMetadata(
    ip_address='198.51.100.14'
)
```

