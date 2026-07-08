
"""
univapay_client_sdk

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from __future__ import annotations

from typing import (
    Callable,
    ClassVar,
)

from apimatic_core.types.union_types.any_of import (
    AnyOf,
)
from apimatic_core.types.union_types.leaf_type import (
    LeafType,
)
from apimatic_core.types.union_types.one_of import (
    OneOf,
)
from apimatic_core.types.union_types.union_type_context import (
    UnionTypeContext as Context,
)

from univapayclientsdk.models.bank_transfer_status_webhook_callback import (
    BankTransferStatusWebhookCallback,
)
from univapayclientsdk.models.cancel_webhook_callback import (
    CancelWebhookCallback,
)
from univapayclientsdk.models.charge_finished_webhook_callback import (
    ChargeFinishedWebhookCallback,
)
from univapayclientsdk.models.charge_updated_webhook_callback import (
    ChargeUpdatedWebhookCallback,
)
from univapayclientsdk.models.customs_declaration_webhook_callback import (
    CustomsDeclarationWebhookCallback,
)
from univapayclientsdk.models.recurring_token_deleted_webhook_callback import (
    RecurringTokenDeletedWebhookCallback,
)
from univapayclientsdk.models.refund_webhook_callback import (
    RefundWebhookCallback,
)
from univapayclientsdk.models.subscription_canceled_webhook_callback import (
    SubscriptionCanceledWebhookCallback,
)
from univapayclientsdk.models.subscription_completed_webhook_callback import (
    SubscriptionCompletedWebhookCallback,
)
from univapayclientsdk.models.subscription_created_webhook_callback import (
    SubscriptionCreatedWebhookCallback,
)
from univapayclientsdk.models.subscription_failure_webhook_callback import (
    SubscriptionFailureWebhookCallback,
)
from univapayclientsdk.models.subscription_payment_webhook_callback import (
    SubscriptionPaymentWebhookCallback,
)
from univapayclientsdk.models.subscription_suspended_webhook_callback import (
    SubscriptionSuspendedWebhookCallback,
)
from univapayclientsdk.models.token_create_bank_transfer_data import (
    TokenCreateBankTransferData,
)
from univapayclientsdk.models.token_create_card_data import (
    TokenCreateCardData,
)
from univapayclientsdk.models.token_create_konbini_data import (
    TokenCreateKonbiniData,
)
from univapayclientsdk.models.token_create_online_data import (
    TokenCreateOnlineData,
)
from univapayclientsdk.models.token_created_webhook_callback import (
    TokenCreatedWebhookCallback,
)
from univapayclientsdk.models.token_cvv_auth_check_updated_webhook_callback import (
    TokenCvvAuthCheckUpdatedWebhookCallback,
)
from univapayclientsdk.models.token_cvv_auth_updated_webhook_callback import (
    TokenCvvAuthUpdatedWebhookCallback,
)
from univapayclientsdk.models.token_replaced_webhook_callback import (
    TokenReplacedWebhookCallback,
)
from univapayclientsdk.models.token_response_bank_transfer_data import (
    TokenResponseBankTransferData,
)
from univapayclientsdk.models.token_response_card_data import (
    TokenResponseCardData,
)
from univapayclientsdk.models.token_response_konbini_data import (
    TokenResponseKonbiniData,
)
from univapayclientsdk.models.token_response_online_data import (
    TokenResponseOnlineData,
)
from univapayclientsdk.models.token_three_ds_updated_webhook_callback import (
    TokenThreeDsUpdatedWebhookCallback,
)
from univapayclientsdk.models.token_updated_webhook_callback import (
    TokenUpdatedWebhookCallback,
)


class UnionTypeLookUp:
    """
    Provides lookup and factory methods for predefined union type templates.
    This class stores a mapping of template names to callables that construct
    union type instances. These templates are used to describe compatible
    data shapes by combining primitive or model-based types into a single
    resolved representation at runtime.

    Attributes:
        _templates (dict): A mapping of template names to factory callables
        that create configured union types.

    """

    _templates: ClassVar[dict[str, Callable]] = {
        "GenericMetadataValue": lambda: AnyOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(bool),
            ],
        ),
        "TransactionTokenCreateRequestData": lambda: AnyOf(
            [
                LeafType(TokenCreateCardData),
                LeafType(TokenCreateKonbiniData),
                LeafType(TokenCreateOnlineData),
                LeafType(TokenCreateBankTransferData),
            ],
        ),
        "TransactionTokenCreateMetadataProps": lambda: OneOf(
            [
                LeafType(str),
                LeafType(bool),
                LeafType(float),
            ],
        ),
        "TransactionTokenMetadataAdditionalProperties": lambda: AnyOf(
            [
                LeafType(str),
                LeafType(float),
                LeafType(bool),
            ],
            Context.create(
               is_dict=True,
               is_optional=True,
            ),
        ),
        "TransactionTokenData": lambda: AnyOf(
            [
                LeafType(TokenResponseCardData),
                LeafType(TokenResponseKonbiniData),
                LeafType(TokenResponseOnlineData),
                LeafType(TokenResponseBankTransferData),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "chargeUpdated": lambda: OneOf(
            [
                LeafType(ChargeUpdatedWebhookCallback,
                         Context.create(
                             discriminator_value="charge_updated",
                             discriminator="event",
                         )),
            ],
        ),
        "chargeFinished": lambda: OneOf(
            [
                LeafType(ChargeFinishedWebhookCallback,
                         Context.create(
                             discriminator_value="charge_finished",
                             discriminator="event",
                         )),
            ],
        ),
        "tokenCreated": lambda: OneOf(
            [
                LeafType(TokenCreatedWebhookCallback,
                         Context.create(
                             discriminator_value="token_created",
                             discriminator="event",
                         )),
            ],
        ),
        "tokenUpdated": lambda: OneOf(
            [
                LeafType(TokenUpdatedWebhookCallback,
                         Context.create(
                             discriminator_value="token_updated",
                             discriminator="event",
                         )),
            ],
        ),
        "tokenThreeDsUpdated": lambda: OneOf(
            [
                LeafType(TokenThreeDsUpdatedWebhookCallback,
                         Context.create(
                             discriminator_value="token_three_d_s_updated",
                             discriminator="event",
                         )),
            ],
        ),
        "tokenCvvAuthUpdated": lambda: OneOf(
            [
                LeafType(TokenCvvAuthUpdatedWebhookCallback,
                         Context.create(
                             discriminator_value="token_cvv_auth_updated",
                             discriminator="event",
                         )),
            ],
        ),
        "tokenCvvAuthCheckUpdated": lambda: OneOf(
            [
                LeafType(TokenCvvAuthCheckUpdatedWebhookCallback,
                         Context.create(
                             discriminator_value="token_cvv_auth_check_updated",
                             discriminator="event",
                         )),
            ],
        ),
        "tokenReplaced": lambda: OneOf(
            [
                LeafType(TokenReplacedWebhookCallback,
                         Context.create(
                             discriminator_value="token_replaced",
                             discriminator="event",
                         )),
            ],
        ),
        "recurringTokenDeleted": lambda: OneOf(
            [
                LeafType(RecurringTokenDeletedWebhookCallback,
                         Context.create(
                             discriminator_value="recurring_token_deleted",
                             discriminator="event",
                         )),
            ],
        ),
        "refund": lambda: OneOf(
            [
                LeafType(RefundWebhookCallback,
                         Context.create(
                             discriminator_value="refund_finished",
                             discriminator="event",
                         )),
            ],
        ),
        "cancel": lambda: OneOf(
            [
                LeafType(CancelWebhookCallback,
                         Context.create(
                             discriminator_value="cancel_finished",
                             discriminator="event",
                         )),
            ],
        ),
        "subscriptionCreated": lambda: OneOf(
            [
                LeafType(SubscriptionCreatedWebhookCallback,
                         Context.create(
                             discriminator_value="subscription_created",
                             discriminator="event",
                         )),
            ],
        ),
        "subscriptionPayment": lambda: OneOf(
            [
                LeafType(SubscriptionPaymentWebhookCallback,
                         Context.create(
                             discriminator_value="subscription_payment",
                             discriminator="event",
                         )),
            ],
        ),
        "subscriptionCompleted": lambda: OneOf(
            [
                LeafType(SubscriptionCompletedWebhookCallback,
                         Context.create(
                             discriminator_value="subscription_completed",
                             discriminator="event",
                         )),
            ],
        ),
        "subscriptionFailure": lambda: OneOf(
            [
                LeafType(SubscriptionFailureWebhookCallback,
                         Context.create(
                             discriminator_value="subscription_failure",
                             discriminator="event",
                         )),
            ],
        ),
        "subscriptionCanceled": lambda: OneOf(
            [
                LeafType(SubscriptionCanceledWebhookCallback,
                         Context.create(
                             discriminator_value="subscription_canceled",
                             discriminator="event",
                         )),
            ],
        ),
        "subscriptionSuspended": lambda: OneOf(
            [
                LeafType(SubscriptionSuspendedWebhookCallback,
                         Context.create(
                             discriminator_value="subscription_suspended",
                             discriminator="event",
                         )),
            ],
        ),
        "bank-transfer": lambda: OneOf(
            [
                LeafType(BankTransferStatusWebhookCallback,
                         Context.create(
                             discriminator_value="bank_transfer_status_updated",
                             discriminator="event",
                         )),
            ],
        ),
        "customs": lambda: OneOf(
            [
                LeafType(CustomsDeclarationWebhookCallback,
                         Context.create(
                             discriminator_value="customs_declaration_finished",
                             discriminator="event",
                         )),
            ],
        ),
    }

    @staticmethod
    def get(name):
        """
        Retrieve and construct a union type template by name.

        Args:
            name (str): The key identifying the template to resolve.

        Returns:
            Any: A new instance of the union type defined for the given name.

        Raises:
            KeyError: If no template exists for the specified name.

        """
        return UnionTypeLookUp._templates[name]()
