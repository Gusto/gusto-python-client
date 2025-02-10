"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .payroll_blockers_error import PayrollBlockersErrorData
from .unprocessable_entity_error_object import UnprocessableEntityErrorObjectData
from .versionheader import VersionHeader
from gusto import utils
from gusto.types import BaseModel
from gusto.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    payroll_id: str
    r"""The UUID of the payroll"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    payroll_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the payroll"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateResponseBodyUnion = TypeAliasType(
    "PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateResponseBodyUnion",
    Union[UnprocessableEntityErrorObjectData, PayrollBlockersErrorData],
)
r"""Unprocessable Entity"""


class PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateResponseBody(Exception):
    r"""Unprocessable Entity"""

    data: PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateResponseBodyUnion

    def __init__(
        self, data: PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateResponseBodyUnion
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            PutV1CompaniesCompanyIDPayrollsPayrollIDCalculateResponseBodyUnion,
        )
