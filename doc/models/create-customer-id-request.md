
# Create Customer Id Request

Request payload for deriving a deterministic customer ID.

*This model accepts additional fields of type Any.*

## Structure

`CreateCustomerIdRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Required | The merchant's own local identifier for the customer, used as the seed for a deterministic per-store UUID.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from univapayclientsdk.models.create_customer_id_request import CreateCustomerIdRequest

create_customer_id_request = CreateCustomerIdRequest(
    customer_id='local-customer-1902'
)
```

