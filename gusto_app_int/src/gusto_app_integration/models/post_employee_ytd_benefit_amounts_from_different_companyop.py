"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .post_employee_ytd_benefit_amounts_from_different_company import (
    PostEmployeeYtdBenefitAmountsFromDifferentCompany,
    PostEmployeeYtdBenefitAmountsFromDifferentCompanyTypedDict,
)
from .versionheader import VersionHeader
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostEmployeeYtdBenefitAmountsFromDifferentCompanyRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    post_employee_ytd_benefit_amounts_from_different_company: (
        PostEmployeeYtdBenefitAmountsFromDifferentCompanyTypedDict
    )
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostEmployeeYtdBenefitAmountsFromDifferentCompanyRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    post_employee_ytd_benefit_amounts_from_different_company: Annotated[
        PostEmployeeYtdBenefitAmountsFromDifferentCompany,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
