"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenCreatePaidyDataShippingAddress(object):
    """Implementation of the 'TokenCreatePaidyDataShippingAddress' model.

    Shipping address for a Paidy token. `zip` is required; the server additionally
    requires at least one of `line1`, `line2`, `city`, or `state` to be present (not
    enforceable at the schema level).

    Attributes:
        zip (str): Japanese postal code (e.g., '105-0011').
        line_1 (str): Primary street address line.
        line_2 (str): Secondary street address line.
        city (str): City or locality.
        state (str): State or prefecture.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "zip": "zip",
        "line_1": "line1",
        "line_2": "line2",
        "city": "city",
        "state": "state",
    }

    _optionals = [
        "line_1",
        "line_2",
        "city",
        "state",
    ]

    def __init__(
        self,
        zip=None,
        line_1=APIHelper.SKIP,
        line_2=APIHelper.SKIP,
        city=APIHelper.SKIP,
        state=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenCreatePaidyDataShippingAddress instance."""
        # Initialize members of the class
        self.zip = zip
        if line_1 is not APIHelper.SKIP:
            self.line_1 = line_1
        if line_2 is not APIHelper.SKIP:
            self.line_2 = line_2
        if city is not APIHelper.SKIP:
            self.city = city
        if state is not APIHelper.SKIP:
            self.state = state

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
        zip =\
            dictionary.get("zip")\
            if dictionary.get("zip")\
                else None
        line_1 =\
            dictionary.get("line1")\
            if dictionary.get("line1")\
                else APIHelper.SKIP
        line_2 =\
            dictionary.get("line2")\
            if dictionary.get("line2")\
                else APIHelper.SKIP
        city =\
            dictionary.get("city")\
            if dictionary.get("city")\
                else APIHelper.SKIP
        state =\
            dictionary.get("state")\
            if dictionary.get("state")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(zip,
                   line_1,
                   line_2,
                   city,
                   state,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                    value=dictionary.zip,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        str,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("zip"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    str,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _zip=self.zip
        _line_1=(
            self.line_1
            if hasattr(self, "line_1")
            else None
        )
        _line_2=(
            self.line_2
            if hasattr(self, "line_2")
            else None
        )
        _city=(
            self.city
            if hasattr(self, "city")
            else None
        )
        _state=(
            self.state
            if hasattr(self, "state")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"zip={_zip!r}, "
            f"line_1={_line_1!r}, "
            f"line_2={_line_2!r}, "
            f"city={_city!r}, "
            f"state={_state!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _zip=self.zip
        _line_1=(
            self.line_1
            if hasattr(self, "line_1")
            else None
        )
        _line_2=(
            self.line_2
            if hasattr(self, "line_2")
            else None
        )
        _city=(
            self.city
            if hasattr(self, "city")
            else None
        )
        _state=(
            self.state
            if hasattr(self, "state")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"zip={_zip!s}, "
            f"line_1={_line_1!s}, "
            f"line_2={_line_2!s}, "
            f"city={_city!s}, "
            f"state={_state!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
