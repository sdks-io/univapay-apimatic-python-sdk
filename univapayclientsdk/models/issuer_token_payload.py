"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class IssuerTokenPayload(object):
    """Implementation of the 'IssuerTokenPayload' model.

    A dictionary containing necessary key-value pairs for sending the request.

    Attributes:
        request_data (str): Generic payload key used by most payment providers.
        s_spcd (str): d-barai payment service code.
        s_cptok (str): d-barai coupon token.
        s_terkn (str): d-barai terminal key.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_data": "request_data",
        "s_spcd": "sSpcd",
        "s_cptok": "sCptok",
        "s_terkn": "sTerkn",
    }

    _optionals = [
        "request_data",
        "s_spcd",
        "s_cptok",
        "s_terkn",
    ]

    def __init__(
        self,
        request_data=APIHelper.SKIP,
        s_spcd=APIHelper.SKIP,
        s_cptok=APIHelper.SKIP,
        s_terkn=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a IssuerTokenPayload instance."""
        # Initialize members of the class
        if request_data is not APIHelper.SKIP:
            self.request_data = request_data
        if s_spcd is not APIHelper.SKIP:
            self.s_spcd = s_spcd
        if s_cptok is not APIHelper.SKIP:
            self.s_cptok = s_cptok
        if s_terkn is not APIHelper.SKIP:
            self.s_terkn = s_terkn

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
        request_data =\
            dictionary.get("request_data")\
            if dictionary.get("request_data")\
                else APIHelper.SKIP
        s_spcd =\
            dictionary.get("sSpcd")\
            if dictionary.get("sSpcd")\
                else APIHelper.SKIP
        s_cptok =\
            dictionary.get("sCptok")\
            if dictionary.get("sCptok")\
                else APIHelper.SKIP
        s_terkn =\
            dictionary.get("sTerkn")\
            if dictionary.get("sTerkn")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(request_data,
                   s_spcd,
                   s_cptok,
                   s_terkn,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _request_data=(
            self.request_data
            if hasattr(self, "request_data")
            else None
        )
        _s_spcd=(
            self.s_spcd
            if hasattr(self, "s_spcd")
            else None
        )
        _s_cptok=(
            self.s_cptok
            if hasattr(self, "s_cptok")
            else None
        )
        _s_terkn=(
            self.s_terkn
            if hasattr(self, "s_terkn")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"request_data={_request_data!r}, "
            f"s_spcd={_s_spcd!r}, "
            f"s_cptok={_s_cptok!r}, "
            f"s_terkn={_s_terkn!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _request_data=(
            self.request_data
            if hasattr(self, "request_data")
            else None
        )
        _s_spcd=(
            self.s_spcd
            if hasattr(self, "s_spcd")
            else None
        )
        _s_cptok=(
            self.s_cptok
            if hasattr(self, "s_cptok")
            else None
        )
        _s_terkn=(
            self.s_terkn
            if hasattr(self, "s_terkn")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"request_data={_request_data!s}, "
            f"s_spcd={_s_spcd!s}, "
            f"s_cptok={_s_cptok!s}, "
            f"s_terkn={_s_terkn!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
