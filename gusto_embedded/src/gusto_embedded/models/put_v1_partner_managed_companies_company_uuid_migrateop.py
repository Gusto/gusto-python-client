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


class PutV1PartnerManagedCompaniesCompanyUUIDMigrateRequestBodyTypedDict(TypedDict):
    email: str
    r"""Email of the company signatory who is authorized to accept our [Terms of Service](https://flows.gusto.com/terms) and migration decision. You can retrieve the signatory email from the `GET /v/1/companies/{company_id}/signatories` endpoint."""
    ip_address: str
    r"""The IP address of the signatory who viewed and accepted the Terms of Service."""
    external_user_id: str
    r"""The signatory's user ID on your platform."""


class PutV1PartnerManagedCompaniesCompanyUUIDMigrateRequestBody(BaseModel):
    email: str
    r"""Email of the company signatory who is authorized to accept our [Terms of Service](https://flows.gusto.com/terms) and migration decision. You can retrieve the signatory email from the `GET /v/1/companies/{company_id}/signatories` endpoint."""

    ip_address: str
    r"""The IP address of the signatory who viewed and accepted the Terms of Service."""

    external_user_id: str
    r"""The signatory's user ID on your platform."""


class PutV1PartnerManagedCompaniesCompanyUUIDMigrateRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PutV1PartnerManagedCompaniesCompanyUUIDMigrateRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1PartnerManagedCompaniesCompanyUUIDMigrateRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutV1PartnerManagedCompaniesCompanyUUIDMigrateRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class MigrationStatus(str, Enum):
    r"""The migration status. 'success' is the only valid return value."""

    SUCCESS = "success"


class PutV1PartnerManagedCompaniesCompanyUUIDMigrateResponseBodyTypedDict(TypedDict):
    r"""Example response"""

    company_uuid: NotRequired[str]
    r"""The company UUID"""
    migration_status: NotRequired[MigrationStatus]
    r"""The migration status. 'success' is the only valid return value."""


class PutV1PartnerManagedCompaniesCompanyUUIDMigrateResponseBody(BaseModel):
    r"""Example response"""

    company_uuid: Optional[str] = None
    r"""The company UUID"""

    migration_status: Optional[MigrationStatus] = None
    r"""The migration status. 'success' is the only valid return value."""
