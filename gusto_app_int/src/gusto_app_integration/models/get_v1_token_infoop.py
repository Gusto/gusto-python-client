"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto_app_integration.types import BaseModel, Nullable, UNSET_SENTINEL
from gusto_app_integration.utils import FieldMetadata, HeaderMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetV1TokenInfoRequestTypedDict(TypedDict):
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1TokenInfoRequest(BaseModel):
    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class ResourceTypedDict(TypedDict):
    r"""Information about the token resource."""

    type: str
    r"""Type of object"""
    uuid: str
    r"""UUID of object"""


class Resource(BaseModel):
    r"""Information about the token resource."""

    type: str
    r"""Type of object"""

    uuid: str
    r"""UUID of object"""


class GetV1TokenInfoType(str, Enum):
    COMPANY_ADMIN = "CompanyAdmin"
    EMPLOYEE = "Employee"
    CONTRACTOR = "Contractor"


class ResourceOwnerTypedDict(TypedDict):
    r"""Information about the token owner"""

    type: GetV1TokenInfoType
    uuid: str
    r"""UUID of resource owner"""


class ResourceOwner(BaseModel):
    r"""Information about the token owner"""

    type: GetV1TokenInfoType

    uuid: str
    r"""UUID of resource owner"""


class GetV1TokenInfoResponseBodyTypedDict(TypedDict):
    r"""Example response"""

    scope: str
    r"""Space delimited string of accessible scopes."""
    resource: Nullable[ResourceTypedDict]
    r"""Information about the token resource."""
    resource_owner: Nullable[ResourceOwnerTypedDict]
    r"""Information about the token owner"""


class GetV1TokenInfoResponseBody(BaseModel):
    r"""Example response"""

    scope: str
    r"""Space delimited string of accessible scopes."""

    resource: Nullable[Resource]
    r"""Information about the token resource."""

    resource_owner: Nullable[ResourceOwner]
    r"""Information about the token owner"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["resource", "resource_owner"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
