"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CheckoutThemeColors(object):
    """Implementation of the 'CheckoutThemeColors' model.

    Hex colors applied to the checkout widget. Always resolves to the platform
    defaults shown here when not customized — never `null`.

    Attributes:
        main_background (str): Main background color.
        secondary_background (str): Secondary background color.
        main_color (str): Main accent color.
        main_text (str): Main text color.
        primary_text (str): Primary text color.
        secondary_text (str): Secondary text color.
        base_text (str): Base text color.
        body_background (str): Body background color.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "main_background": "main_background",
        "secondary_background": "secondary_background",
        "main_color": "main_color",
        "main_text": "main_text",
        "primary_text": "primary_text",
        "secondary_text": "secondary_text",
        "base_text": "base_text",
        "body_background": "body_background",
    }

    _optionals = [
        "main_background",
        "secondary_background",
        "main_color",
        "main_text",
        "primary_text",
        "secondary_text",
        "base_text",
        "body_background",
    ]

    def __init__(
        self,
        main_background=APIHelper.SKIP,
        secondary_background=APIHelper.SKIP,
        main_color=APIHelper.SKIP,
        main_text=APIHelper.SKIP,
        primary_text=APIHelper.SKIP,
        secondary_text=APIHelper.SKIP,
        base_text=APIHelper.SKIP,
        body_background=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutThemeColors instance."""
        # Initialize members of the class
        if main_background is not APIHelper.SKIP:
            self.main_background = main_background
        if secondary_background is not APIHelper.SKIP:
            self.secondary_background = secondary_background
        if main_color is not APIHelper.SKIP:
            self.main_color = main_color
        if main_text is not APIHelper.SKIP:
            self.main_text = main_text
        if primary_text is not APIHelper.SKIP:
            self.primary_text = primary_text
        if secondary_text is not APIHelper.SKIP:
            self.secondary_text = secondary_text
        if base_text is not APIHelper.SKIP:
            self.base_text = base_text
        if body_background is not APIHelper.SKIP:
            self.body_background = body_background

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        main_background =\
            dictionary.get("main_background")\
            if dictionary.get("main_background")\
                else APIHelper.SKIP
        secondary_background =\
            dictionary.get("secondary_background")\
            if dictionary.get("secondary_background")\
                else APIHelper.SKIP
        main_color =\
            dictionary.get("main_color")\
            if dictionary.get("main_color")\
                else APIHelper.SKIP
        main_text =\
            dictionary.get("main_text")\
            if dictionary.get("main_text")\
                else APIHelper.SKIP
        primary_text =\
            dictionary.get("primary_text")\
            if dictionary.get("primary_text")\
                else APIHelper.SKIP
        secondary_text =\
            dictionary.get("secondary_text")\
            if dictionary.get("secondary_text")\
                else APIHelper.SKIP
        base_text =\
            dictionary.get("base_text")\
            if dictionary.get("base_text")\
                else APIHelper.SKIP
        body_background =\
            dictionary.get("body_background")\
            if dictionary.get("body_background")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(main_background,
                   secondary_background,
                   main_color,
                   main_text,
                   primary_text,
                   secondary_text,
                   base_text,
                   body_background,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _main_background=(
            self.main_background
            if hasattr(self, "main_background")
            else None
        )
        _secondary_background=(
            self.secondary_background
            if hasattr(self, "secondary_background")
            else None
        )
        _main_color=(
            self.main_color
            if hasattr(self, "main_color")
            else None
        )
        _main_text=(
            self.main_text
            if hasattr(self, "main_text")
            else None
        )
        _primary_text=(
            self.primary_text
            if hasattr(self, "primary_text")
            else None
        )
        _secondary_text=(
            self.secondary_text
            if hasattr(self, "secondary_text")
            else None
        )
        _base_text=(
            self.base_text
            if hasattr(self, "base_text")
            else None
        )
        _body_background=(
            self.body_background
            if hasattr(self, "body_background")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"main_background={_main_background!r}, "
            f"secondary_background={_secondary_background!r}, "
            f"main_color={_main_color!r}, "
            f"main_text={_main_text!r}, "
            f"primary_text={_primary_text!r}, "
            f"secondary_text={_secondary_text!r}, "
            f"base_text={_base_text!r}, "
            f"body_background={_body_background!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _main_background=(
            self.main_background
            if hasattr(self, "main_background")
            else None
        )
        _secondary_background=(
            self.secondary_background
            if hasattr(self, "secondary_background")
            else None
        )
        _main_color=(
            self.main_color
            if hasattr(self, "main_color")
            else None
        )
        _main_text=(
            self.main_text
            if hasattr(self, "main_text")
            else None
        )
        _primary_text=(
            self.primary_text
            if hasattr(self, "primary_text")
            else None
        )
        _secondary_text=(
            self.secondary_text
            if hasattr(self, "secondary_text")
            else None
        )
        _base_text=(
            self.base_text
            if hasattr(self, "base_text")
            else None
        )
        _body_background=(
            self.body_background
            if hasattr(self, "body_background")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"main_background={_main_background!s}, "
            f"secondary_background={_secondary_background!s}, "
            f"main_color={_main_color!s}, "
            f"main_text={_main_text!s}, "
            f"primary_text={_primary_text!s}, "
            f"secondary_text={_secondary_text!s}, "
            f"base_text={_base_text!s}, "
            f"body_background={_body_background!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
