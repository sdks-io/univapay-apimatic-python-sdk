"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CustomsDeclarationCreateRequest(object):
    """Implementation of the 'CustomsDeclarationCreateRequest' model.

    Request body for creating a customs declaration. Backend currently accepts this
    shape only for WeChat Online and WeChat MPM charges.

    Attributes:
        customs (str): WeChat customs authority code used for the declaration.
        merchant_customs_no (str): Merchant customs registration number.
        certificate_id (str): Customer certificate or passport identifier used by
            customs.
        certificate_name (str): Customer name exactly as shown on the certificate.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customs": "customs",
        "merchant_customs_no": "merchant_customs_no",
        "certificate_id": "certificate_id",
        "certificate_name": "certificate_name",
    }

    def __init__(
        self,
        customs=None,
        merchant_customs_no=None,
        certificate_id=None,
        certificate_name=None,
        additional_properties=None):
        """Initialize a CustomsDeclarationCreateRequest instance."""
        # Initialize members of the class
        self.customs = customs
        self.merchant_customs_no = merchant_customs_no
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name

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
        customs =\
            dictionary.get("customs")\
            if dictionary.get("customs")\
                else None
        merchant_customs_no =\
            dictionary.get("merchant_customs_no")\
            if dictionary.get("merchant_customs_no")\
                else None
        certificate_id =\
            dictionary.get("certificate_id")\
            if dictionary.get("certificate_id")\
                else None
        certificate_name =\
            dictionary.get("certificate_name")\
            if dictionary.get("certificate_name")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(customs,
                   merchant_customs_no,
                   certificate_id,
                   certificate_name,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _customs=self.customs
        _merchant_customs_no=self.merchant_customs_no
        _certificate_id=self.certificate_id
        _certificate_name=self.certificate_name
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customs={_customs!r}, "
            f"merchant_customs_no={_merchant_customs_no!r}, "
            f"certificate_id={_certificate_id!r}, "
            f"certificate_name={_certificate_name!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _customs=self.customs
        _merchant_customs_no=self.merchant_customs_no
        _certificate_id=self.certificate_id
        _certificate_name=self.certificate_name
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customs={_customs!s}, "
            f"merchant_customs_no={_merchant_customs_no!s}, "
            f"certificate_id={_certificate_id!s}, "
            f"certificate_name={_certificate_name!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
