
# Store List Item

Store row returned by store list queries.

*This model accepts additional fields of type Any.*

## Structure

`StoreListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Store identifier. |
| `name` | `str` | Optional | Store display name. |
| `merchant_name` | `str` | Optional | Merchant display name associated with the store row. |
| `created_on` | `datetime` | Optional | Timestamp when the store was created. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser

from univapayclientsdk.models.store_list_item import StoreListItem

store_list_item = StoreListItem(
    id='11ef0000-0000-4000-8000-000000000022',
    name='Tokyo Store',
    merchant_name='Example Merchant',
    created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z')
)
```

