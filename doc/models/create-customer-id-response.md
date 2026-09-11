
# Create Customer Id Response

Response payload returned after deriving a deterministic customer ID.

*This model accepts additional fields of type Any.*

## Structure

`CreateCustomerIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `uuid\|str` | Optional | Deterministic UUID derived from the store and the supplied local `customer_id`. Identical for repeated calls with the same inputs. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.create_customer_id_response import CreateCustomerIdResponse

create_customer_id_response = CreateCustomerIdResponse(
    customer_id='8a3f1b8e-2c1a-4b7a-9c2e-6f6b6f6e2b10'
)
```

