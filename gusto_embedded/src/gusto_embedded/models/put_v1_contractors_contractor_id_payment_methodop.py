"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1ContractorsContractorIDPaymentMethodType(str, Enum):
    r"""The payment method type. If type is Direct Deposit, the contractor is required to have a bank account.
    see [Bank account endpoint](./post-v1-contractors-contractor_uuid-bank_accounts)
    """

    DIRECT_DEPOSIT = "Direct Deposit"
    CHECK = "Check"


class PutV1ContractorsContractorIDPaymentMethodRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    type: PutV1ContractorsContractorIDPaymentMethodType
    r"""The payment method type. If type is Direct Deposit, the contractor is required to have a bank account.
    see [Bank account endpoint](./post-v1-contractors-contractor_uuid-bank_accounts)
    """


class PutV1ContractorsContractorIDPaymentMethodRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    type: PutV1ContractorsContractorIDPaymentMethodType
    r"""The payment method type. If type is Direct Deposit, the contractor is required to have a bank account.
    see [Bank account endpoint](./post-v1-contractors-contractor_uuid-bank_accounts)
    """


class PutV1ContractorsContractorIDPaymentMethodRequestTypedDict(TypedDict):
    contractor_uuid: str
    r"""The UUID of the contractor"""
    request_body: PutV1ContractorsContractorIDPaymentMethodRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1ContractorsContractorIDPaymentMethodRequest(BaseModel):
    contractor_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the contractor"""

    request_body: Annotated[
        PutV1ContractorsContractorIDPaymentMethodRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
