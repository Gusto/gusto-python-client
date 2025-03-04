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
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesEmployeesTypedDict(
    TypedDict
):
    uuid: NotRequired[str]
    balance: NotRequired[str]


class PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesEmployees(BaseModel):
    uuid: Optional[str] = None

    balance: Optional[str] = None


class PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesRequestBodyTypedDict(
    TypedDict
):
    r"""A list of employee objects containing the employee uuid"""

    employees: NotRequired[
        List[PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesEmployeesTypedDict]
    ]


class PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesRequestBody(BaseModel):
    r"""A list of employee objects containing the employee uuid"""

    employees: Optional[
        List[PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesEmployees]
    ] = None


class PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesRequestTypedDict(TypedDict):
    time_off_policy_uuid: str
    r"""The UUID of the company time off policy"""
    request_body: (
        PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesRequestBodyTypedDict
    )
    r"""A list of employee objects containing the employee uuid"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesRequest(BaseModel):
    time_off_policy_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company time off policy"""

    request_body: Annotated[
        PutVersionTimeOffPoliciesTimeOffPolicyUUIDAddEmployeesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""A list of employee objects containing the employee uuid"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
