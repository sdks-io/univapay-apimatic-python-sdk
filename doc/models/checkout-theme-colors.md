
# Checkout Theme Colors

Hex colors applied to the checkout widget. Always resolves to the platform defaults shown here when not customized — never `null`.

*This model accepts additional fields of type Any.*

## Structure

`CheckoutThemeColors`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `main_background` | `str` | Optional | Main background color. |
| `secondary_background` | `str` | Optional | Secondary background color. |
| `main_color` | `str` | Optional | Main accent color. |
| `main_text` | `str` | Optional | Main text color. |
| `primary_text` | `str` | Optional | Primary text color. |
| `secondary_text` | `str` | Optional | Secondary text color. |
| `base_text` | `str` | Optional | Base text color. |
| `body_background` | `str` | Optional | Body background color. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from univapayclientsdk.models.checkout_theme_colors import CheckoutThemeColors

checkout_theme_colors = CheckoutThemeColors(
    main_background='#FFFFFF',
    secondary_background='#F5F8FC',
    main_color='#4C5F85',
    main_text='#FFFFFF',
    primary_text='#4C5F85',
    secondary_text='#4C5F85',
    base_text='#4C5F85',
    body_background='#FFFFFF',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

