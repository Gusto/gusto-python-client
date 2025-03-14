"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fast_payment_limit_required_body import (
    FastPaymentLimitRequiredBody,
    FastPaymentLimitRequiredBodyTypedDict,
)
from .payment_speed_required_body import (
    PaymentSpeedRequiredBody,
    PaymentSpeedRequiredBodyTypedDict,
)
from .versionheader import VersionHeader
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


PutV1CompanyPaymentConfigsRequestBodyTypedDict = TypeAliasType(
    "PutV1CompanyPaymentConfigsRequestBodyTypedDict",
    Union[FastPaymentLimitRequiredBodyTypedDict, PaymentSpeedRequiredBodyTypedDict],
)


PutV1CompanyPaymentConfigsRequestBody = TypeAliasType(
    "PutV1CompanyPaymentConfigsRequestBody",
    Union[FastPaymentLimitRequiredBody, PaymentSpeedRequiredBody],
)


class PutV1CompanyPaymentConfigsRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PutV1CompanyPaymentConfigsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompanyPaymentConfigsRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutV1CompanyPaymentConfigsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
