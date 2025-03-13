"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_app_integration.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1JobsJobIDRequestBodyTypedDict(TypedDict):
    r"""Create a job."""

    title: str
    r"""The job title"""
    hire_date: str
    r"""The date when the employee was hired or rehired for the job."""
    two_percent_shareholder: NotRequired[bool]
    r"""Whether the employee owns at least 2% of the company."""
    state_wc_covered: NotRequired[Nullable[bool]]
    r"""Whether this job is eligible for workers' compensation coverage in the state of Washington (WA)."""
    state_wc_class_code: NotRequired[Nullable[str]]
    r"""The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more."""


class PostV1JobsJobIDRequestBody(BaseModel):
    r"""Create a job."""

    title: str
    r"""The job title"""

    hire_date: str
    r"""The date when the employee was hired or rehired for the job."""

    two_percent_shareholder: Optional[bool] = None
    r"""Whether the employee owns at least 2% of the company."""

    state_wc_covered: OptionalNullable[bool] = UNSET
    r"""Whether this job is eligible for workers' compensation coverage in the state of Washington (WA)."""

    state_wc_class_code: OptionalNullable[str] = UNSET
    r"""The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "two_percent_shareholder",
            "state_wc_covered",
            "state_wc_class_code",
        ]
        nullable_fields = ["state_wc_covered", "state_wc_class_code"]
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


class PostV1JobsJobIDRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    request_body: PostV1JobsJobIDRequestBodyTypedDict
    r"""Create a job."""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1JobsJobIDRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    request_body: Annotated[
        PostV1JobsJobIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Create a job."""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
