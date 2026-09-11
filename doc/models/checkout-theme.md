
# Checkout Theme

Widget theme applied to checkout.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutTheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `colors` | [`CheckoutThemeColors`](../../doc/models/checkout-theme-colors.md) | Optional | Hex colors applied to the checkout widget. Always resolves to the platform defaults shown here when not customized — never `null`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_theme import CheckoutTheme
from univapayclientsdk.models.checkout_theme_colors import CheckoutThemeColors

checkout_theme = CheckoutTheme(
    colors=CheckoutThemeColors(
        main_background='main_background8',
        secondary_background='secondary_background6',
        main_color='main_color0',
        main_text='main_text4',
        primary_text='primary_text8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

