# ruff: noqa: D100

from django.urls import path

from tests.framework_integrations.webhooks.apps.django_charge_app import (
    webhooks,
)

urlpatterns = [
    path("webhooks", webhooks),
]
