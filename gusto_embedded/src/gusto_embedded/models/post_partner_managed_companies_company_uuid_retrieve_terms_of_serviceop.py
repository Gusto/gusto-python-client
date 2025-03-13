"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
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


class PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceRequestBodyTypedDict(
    TypedDict
):
    email: str
    r"""The user's email address on Gusto. You can retrieve the user's email via company's `/admins`, `/employees`, `/signatories`, and `/contractors` endpoints."""


class PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceRequestBody(
    BaseModel
):
    email: str
    r"""The user's email address on Gusto. You can retrieve the user's email via company's `/admins`, `/employees`, `/signatories`, and `/contractors` endpoints."""


class PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceRequestTypedDict(
    TypedDict
):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: (
        PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceRequestBodyTypedDict
    )
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceResponseBodyTypedDict(
    TypedDict
):
    r"""Example response"""

    latest_terms_accepted: NotRequired[bool]
    r"""Whether the latest terms have been accepted by the user."""


class PostPartnerManagedCompaniesCompanyUUIDRetrieveTermsOfServiceResponseBody(
    BaseModel
):
    r"""Example response"""

    latest_terms_accepted: Optional[bool] = None
    r"""Whether the latest terms have been accepted by the user."""
