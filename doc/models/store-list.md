
# Store List

Paginated store search result.

*This model accepts additional fields of type Any.*

## Structure

`StoreList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[StoreListItem]`](../../doc/models/store-list-item.md) | Optional | Store rows matching the current filter set. |
| `has_more` | `bool` | Optional | Whether another page is available. |
| `total_hits` | `int` | Optional | Total number of matching stores when available. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from univapayclientsdk.models.store_list import StoreList
from univapayclientsdk.models.store_list_item import StoreListItem

store_list = StoreList(
    items=[
        StoreListItem(
            id='11ef0000-0000-4000-8000-000000000022',
            name='Tokyo Store',
            merchant_name='Example Merchant',
            created_on=dateutil.parser.parse('2026-04-09T07:35:50.000000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        StoreListItem(
            id='11ef0000-0000-4000-8000-000000000023',
            name='Osaka Store',
            merchant_name='Example Merchant',
            created_on=dateutil.parser.parse('2026-04-10T09:12:30.000000Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    has_more=False,
    total_hits=2,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

