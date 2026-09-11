"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class ChargeCreateRequestThreeDs(object):
    """Implementation of the 'ChargeCreateRequestThreeDs' model.

    Charge Create Request Three Ds schema. Either supply `mode` (and optionally
    `redirect_endpoint`) to have Univapay run 3DS, or supply all six external-MPI
    fields (`authentication_value` through `transaction_status`) when 3DS
    authentication was already completed outside of Univapay — in that case `mode` is
    set to `provided` automatically and must not be sent.

    Attributes:
        redirect_endpoint (str): URL to redirect the customer to after 3DS
            authentication.
        mode (ChargeCreateRequestThreeDsMode): 3D-Secure authentication type. App
            Token Secret is required to use 'skip'. `if_available` enforces 3DS only
            if credentials are available for the recurring token and it has not
            already completed 3DS. `provided` is set automatically by the server when
            external MPI authentication data (`authentication_value`, `eci`, etc.) is
            submitted on the request and cannot be set manually. When omitted, the
            store's default 3DS policy applies — do not assume 'normal'.
        authentication_value (str): External MPI: the cardholder authentication value
            (CAVV/AAV) returned by the 3-D Secure directory server. Submit together
            with `eci`, `ds_transaction_id`, `server_transaction_id`,
            `message_version`, and `transaction_status` to provide externally
            completed 3DS authentication data — either all six fields must be
            present, or none of them.
        eci (str): External MPI: the two-digit Electronic Commerce Indicator returned
            by the directory server. Submit together with the other external MPI
            fields.
        ds_transaction_id (str): External MPI: the directory server transaction ID.
            Submit together with the other external MPI fields.
        server_transaction_id (str): External MPI: the 3DS server transaction ID.
            Submit together with the other external MPI fields.
        message_version (str): External MPI: the 3-D Secure protocol message version
            (e.g., '2.1.0', '2.2.0'). Submit together with the other external MPI
            fields.
        transaction_status (str): External MPI: the 3-D Secure directory server
            transaction status. Only a successful authentication status is accepted.
            Submit together with the other external MPI fields.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "redirect_endpoint": "redirect_endpoint",
        "mode": "mode",
        "authentication_value": "authentication_value",
        "eci": "eci",
        "ds_transaction_id": "ds_transaction_id",
        "server_transaction_id": "server_transaction_id",
        "message_version": "message_version",
        "transaction_status": "transaction_status",
    }

    _optionals = [
        "redirect_endpoint",
        "mode",
        "authentication_value",
        "eci",
        "ds_transaction_id",
        "server_transaction_id",
        "message_version",
        "transaction_status",
    ]

    def __init__(
        self,
        redirect_endpoint=APIHelper.SKIP,
        mode=APIHelper.SKIP,
        authentication_value=APIHelper.SKIP,
        eci=APIHelper.SKIP,
        ds_transaction_id=APIHelper.SKIP,
        server_transaction_id=APIHelper.SKIP,
        message_version=APIHelper.SKIP,
        transaction_status=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ChargeCreateRequestThreeDs instance."""
        # Initialize members of the class
        if redirect_endpoint is not APIHelper.SKIP:
            self.redirect_endpoint = redirect_endpoint
        if mode is not APIHelper.SKIP:
            self.mode = mode
        if authentication_value is not APIHelper.SKIP:
            self.authentication_value = authentication_value
        if eci is not APIHelper.SKIP:
            self.eci = eci
        if ds_transaction_id is not APIHelper.SKIP:
            self.ds_transaction_id = ds_transaction_id
        if server_transaction_id is not APIHelper.SKIP:
            self.server_transaction_id = server_transaction_id
        if message_version is not APIHelper.SKIP:
            self.message_version = message_version
        if transaction_status is not APIHelper.SKIP:
            self.transaction_status = transaction_status

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
        redirect_endpoint =\
            dictionary.get("redirect_endpoint")\
            if dictionary.get("redirect_endpoint")\
                else APIHelper.SKIP
        mode =\
            dictionary.get("mode")\
            if dictionary.get("mode")\
                else APIHelper.SKIP
        authentication_value =\
            dictionary.get("authentication_value")\
            if dictionary.get("authentication_value")\
                else APIHelper.SKIP
        eci =\
            dictionary.get("eci")\
            if dictionary.get("eci")\
                else APIHelper.SKIP
        ds_transaction_id =\
            dictionary.get("ds_transaction_id")\
            if dictionary.get("ds_transaction_id")\
                else APIHelper.SKIP
        server_transaction_id =\
            dictionary.get("server_transaction_id")\
            if dictionary.get("server_transaction_id")\
                else APIHelper.SKIP
        message_version =\
            dictionary.get("message_version")\
            if dictionary.get("message_version")\
                else APIHelper.SKIP
        transaction_status =\
            dictionary.get("transaction_status")\
            if dictionary.get("transaction_status")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(redirect_endpoint,
                   mode,
                   authentication_value,
                   eci,
                   ds_transaction_id,
                   server_transaction_id,
                   message_version,
                   transaction_status,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _redirect_endpoint=(
            self.redirect_endpoint
            if hasattr(self, "redirect_endpoint")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _authentication_value=(
            self.authentication_value
            if hasattr(self, "authentication_value")
            else None
        )
        _eci=(
            self.eci
            if hasattr(self, "eci")
            else None
        )
        _ds_transaction_id=(
            self.ds_transaction_id
            if hasattr(self, "ds_transaction_id")
            else None
        )
        _server_transaction_id=(
            self.server_transaction_id
            if hasattr(self, "server_transaction_id")
            else None
        )
        _message_version=(
            self.message_version
            if hasattr(self, "message_version")
            else None
        )
        _transaction_status=(
            self.transaction_status
            if hasattr(self, "transaction_status")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_endpoint={_redirect_endpoint!r}, "
            f"mode={_mode!r}, "
            f"authentication_value={_authentication_value!r}, "
            f"eci={_eci!r}, "
            f"ds_transaction_id={_ds_transaction_id!r}, "
            f"server_transaction_id={_server_transaction_id!r}, "
            f"message_version={_message_version!r}, "
            f"transaction_status={_transaction_status!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _redirect_endpoint=(
            self.redirect_endpoint
            if hasattr(self, "redirect_endpoint")
            else None
        )
        _mode=(
            self.mode
            if hasattr(self, "mode")
            else None
        )
        _authentication_value=(
            self.authentication_value
            if hasattr(self, "authentication_value")
            else None
        )
        _eci=(
            self.eci
            if hasattr(self, "eci")
            else None
        )
        _ds_transaction_id=(
            self.ds_transaction_id
            if hasattr(self, "ds_transaction_id")
            else None
        )
        _server_transaction_id=(
            self.server_transaction_id
            if hasattr(self, "server_transaction_id")
            else None
        )
        _message_version=(
            self.message_version
            if hasattr(self, "message_version")
            else None
        )
        _transaction_status=(
            self.transaction_status
            if hasattr(self, "transaction_status")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"redirect_endpoint={_redirect_endpoint!s}, "
            f"mode={_mode!s}, "
            f"authentication_value={_authentication_value!s}, "
            f"eci={_eci!s}, "
            f"ds_transaction_id={_ds_transaction_id!s}, "
            f"server_transaction_id={_server_transaction_id!s}, "
            f"message_version={_message_version!s}, "
            f"transaction_status={_transaction_status!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
