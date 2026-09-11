
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
from univapayclientsdk.models.bank_transfer_transaction_token import (
    BankTransferTransactionToken,
)
from univapayclientsdk.models.cancel_webhook_callback import (
    CancelWebhookCallback,
)
from univapayclientsdk.models.card_transaction_token import (
    CardTransactionToken,
)
from univapayclientsdk.models.charge_webhook_event import (
    ChargeWebhookEvent,
)
from univapayclientsdk.models.customs_declaration_webhook_callback import (
    CustomsDeclarationWebhookCallback,
)
from univapayclientsdk.models.konbini_transaction_token import (
    KonbiniTransactionToken,
)
from univapayclientsdk.models.online_transaction_token import (
    OnlineTransactionToken,
)
from univapayclientsdk.models.paidy_transaction_token import (
    PaidyTransactionToken,
)
from univapayclientsdk.models.qr_merchant_transaction_token import (
    QrMerchantTransactionToken,
)
from univapayclientsdk.models.qr_scan_transaction_token import (
    QrScanTransactionToken,
)
from univapayclientsdk.models.refund_webhook_callback import (
    RefundWebhookCallback,
)
from univapayclientsdk.models.subscription_webhook_event import (
    SubscriptionWebhookEvent,
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
from univapayclientsdk.models.token_create_paidy_data import (
    TokenCreatePaidyData,
)
from univapayclientsdk.models.token_create_qr_merchant_data import (
    TokenCreateQrMerchantData,
)
from univapayclientsdk.models.token_create_qr_scan_data import (
    TokenCreateQrScanData,
)
from univapayclientsdk.models.token_webhook_event import (
    TokenWebhookEvent,
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
        "TransactionToken": lambda: OneOf(
            [
                LeafType(CardTransactionToken,
                         Context.create(
                             discriminator_value="card",
                             discriminator="payment_type",
                         )),
                LeafType(KonbiniTransactionToken,
                         Context.create(
                             discriminator_value="konbini",
                             discriminator="payment_type",
                         )),
                LeafType(OnlineTransactionToken,
                         Context.create(
                             discriminator_value="online",
                             discriminator="payment_type",
                         )),
                LeafType(BankTransferTransactionToken,
                         Context.create(
                             discriminator_value="bank_transfer",
                             discriminator="payment_type",
                         )),
                LeafType(PaidyTransactionToken,
                         Context.create(
                             discriminator_value="paidy",
                             discriminator="payment_type",
                         )),
                LeafType(QrScanTransactionToken,
                         Context.create(
                             discriminator_value="qr_scan",
                             discriminator="payment_type",
                         )),
                LeafType(QrMerchantTransactionToken,
                         Context.create(
                             discriminator_value="qr_merchant",
                             discriminator="payment_type",
                         )),
            ],
        ),
        "GenericMetadataArrayItem": lambda: AnyOf(
            [
                LeafType(str,
                         Context.create(
                             is_nullable=True,
                         )),
                LeafType(int),
                LeafType(float),
                LeafType(bool),
            ],
            Context.create(
               is_array=True,
            ),
        ),
        "GenericMetadataValue": lambda: AnyOf(
            [
                LeafType(str,
                         Context.create(
                             is_nullable=True,
                         )),
                LeafType(int),
                LeafType(float),
                LeafType(bool),
                AnyOf(
                    [
                        LeafType(str,
                                 Context.create(
                                     is_nullable=True,
                                 )),
                        LeafType(int),
                        LeafType(float),
                        LeafType(bool),
                    ],
                    Context.create(
                       is_array=True,
                    ),
                ),
            ],
        ),
        "TransactionTokenCreateRequestData": lambda: AnyOf(
            [
                LeafType(TokenCreateCardData),
                LeafType(TokenCreateKonbiniData),
                LeafType(TokenCreateOnlineData),
                LeafType(TokenCreateBankTransferData),
                LeafType(TokenCreatePaidyData),
                LeafType(TokenCreateQrScanData),
                LeafType(TokenCreateQrMerchantData),
            ],
        ),
        "TransactionTokenCreateMetadataProps": lambda: AnyOf(
            [
                LeafType(str,
                         Context.create(
                             is_nullable=True,
                         )),
                LeafType(int),
                LeafType(float),
                LeafType(bool),
                AnyOf(
                    [
                        LeafType(str,
                                 Context.create(
                                     is_nullable=True,
                                 )),
                        LeafType(int),
                        LeafType(float),
                        LeafType(bool),
                    ],
                    Context.create(
                       is_array=True,
                    ),
                ),
            ],
        ),
        "TransactionTokenMetadataAdditionalProperties": lambda: AnyOf(
            [
                LeafType(str,
                         Context.create(
                             is_nullable=True,
                         )),
                LeafType(int),
                LeafType(float),
                LeafType(bool),
                AnyOf(
                    [
                        LeafType(str,
                                 Context.create(
                                     is_nullable=True,
                                 )),
                        LeafType(int),
                        LeafType(float),
                        LeafType(bool),
                    ],
                    Context.create(
                       is_array=True,
                    ),
                ),
            ],
            Context.create(
               is_dict=True,
               is_optional=True,
            ),
        ),
        "TransactionToken2": lambda: OneOf(
            [
                LeafType(CardTransactionToken,
                         Context.create(
                             discriminator_value="card",
                             discriminator="payment_type",
                         )),
                LeafType(KonbiniTransactionToken,
                         Context.create(
                             discriminator_value="konbini",
                             discriminator="payment_type",
                         )),
                LeafType(OnlineTransactionToken,
                         Context.create(
                             discriminator_value="online",
                             discriminator="payment_type",
                         )),
                LeafType(BankTransferTransactionToken,
                         Context.create(
                             discriminator_value="bank_transfer",
                             discriminator="payment_type",
                         )),
                LeafType(PaidyTransactionToken,
                         Context.create(
                             discriminator_value="paidy",
                             discriminator="payment_type",
                         )),
                LeafType(QrScanTransactionToken,
                         Context.create(
                             discriminator_value="qr_scan",
                             discriminator="payment_type",
                         )),
                LeafType(QrMerchantTransactionToken,
                         Context.create(
                             discriminator_value="qr_merchant",
                             discriminator="payment_type",
                         )),
            ],
            Context.create(
               is_optional=True,
            ),
        ),
        "charge": lambda: OneOf(
            [
                LeafType(ChargeWebhookEvent,
                         Context.create(
                             discriminator_value="charge_updated",
                             discriminator="event",
                         )),
                LeafType(ChargeWebhookEvent,
                         Context.create(
                             discriminator_value="charge_finished",
                             discriminator="event",
                         )),
            ],
        ),
        "token": lambda: OneOf(
            [
                LeafType(TokenWebhookEvent,
                         Context.create(
                             discriminator_value="token_created",
                             discriminator="event",
                         )),
                LeafType(TokenWebhookEvent,
                         Context.create(
                             discriminator_value="token_updated",
                             discriminator="event",
                         )),
                LeafType(TokenWebhookEvent,
                         Context.create(
                             discriminator_value="token_three_d_s_updated",
                             discriminator="event",
                         )),
                LeafType(TokenWebhookEvent,
                         Context.create(
                             discriminator_value="token_cvv_auth_updated",
                             discriminator="event",
                         )),
                LeafType(TokenWebhookEvent,
                         Context.create(
                             discriminator_value="token_cvv_auth_check_updated",
                             discriminator="event",
                         )),
                LeafType(TokenWebhookEvent,
                         Context.create(
                             discriminator_value="token_replaced",
                             discriminator="event",
                         )),
                LeafType(TokenWebhookEvent,
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
        "subscription": lambda: OneOf(
            [
                LeafType(SubscriptionWebhookEvent,
                         Context.create(
                             discriminator_value="subscription_created",
                             discriminator="event",
                         )),
                LeafType(SubscriptionWebhookEvent,
                         Context.create(
                             discriminator_value="subscription_payment",
                             discriminator="event",
                         )),
                LeafType(SubscriptionWebhookEvent,
                         Context.create(
                             discriminator_value="subscription_completed",
                             discriminator="event",
                         )),
                LeafType(SubscriptionWebhookEvent,
                         Context.create(
                             discriminator_value="subscription_failure",
                             discriminator="event",
                         )),
                LeafType(SubscriptionWebhookEvent,
                         Context.create(
                             discriminator_value="subscription_canceled",
                             discriminator="event",
                         )),
                LeafType(SubscriptionWebhookEvent,
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
