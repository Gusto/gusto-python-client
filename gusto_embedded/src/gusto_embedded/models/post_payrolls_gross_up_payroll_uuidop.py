"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .payroll_blockers_error import PayrollBlockersErrorData
from .unprocessable_entity_error_object_error import (
    UnprocessableEntityErrorObjectErrorData,
)
from .versionheader import VersionHeader
from gusto_embedded import utils
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


class PostPayrollsGrossUpPayrollUUIDRequestBodyTypedDict(TypedDict):
    employee_uuid: str
    r"""Employee UUID"""
    net_pay: str
    r"""Employee net earnings"""


class PostPayrollsGrossUpPayrollUUIDRequestBody(BaseModel):
    employee_uuid: str
    r"""Employee UUID"""

    net_pay: str
    r"""Employee net earnings"""


class PostPayrollsGrossUpPayrollUUIDRequestTypedDict(TypedDict):
    payroll_uuid: str
    r"""The UUID of the payroll"""
    request_body: PostPayrollsGrossUpPayrollUUIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostPayrollsGrossUpPayrollUUIDRequest(BaseModel):
    payroll_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the payroll"""

    request_body: Annotated[
        PostPayrollsGrossUpPayrollUUIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


PostPayrollsGrossUpPayrollUUIDResponseBodyUnion = TypeAliasType(
    "PostPayrollsGrossUpPayrollUUIDResponseBodyUnion",
    Union[UnprocessableEntityErrorObjectErrorData, PayrollBlockersErrorData],
)
r"""Unprocessable Entity"""


class PostPayrollsGrossUpPayrollUUIDResponseBody(Exception):
    r"""Unprocessable Entity"""

    data: PostPayrollsGrossUpPayrollUUIDResponseBodyUnion

    def __init__(self, data: PostPayrollsGrossUpPayrollUUIDResponseBodyUnion):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, PostPayrollsGrossUpPayrollUUIDResponseBodyUnion
        )
