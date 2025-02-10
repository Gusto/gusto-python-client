"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1CompaniesCompanyUUIDContractorsType(str, Enum):
    r"""The contractor type."""

    INDIVIDUAL = "Individual"
    BUSINESS = "Business"


class PostV1CompaniesCompanyUUIDContractorsWageType(str, Enum):
    r"""The contractor’s wage type."""

    FIXED = "Fixed"
    HOURLY = "Hourly"


class PostV1CompaniesCompanyUUIDContractorsRequestBodyTypedDict(TypedDict):
    r"""Create an individual or business contractor."""

    wage_type: PostV1CompaniesCompanyUUIDContractorsWageType
    r"""The contractor’s wage type.

    """
    start_date: str
    r"""The day when the contractor will start working for the company.

    """
    type: NotRequired[PostV1CompaniesCompanyUUIDContractorsType]
    r"""The contractor type."""
    hourly_rate: NotRequired[str]
    r"""The contractor’s hourly rate. This attribute is required if the wage_type is `Hourly`."""
    self_onboarding: NotRequired[bool]
    r"""Whether the contractor or the payroll admin will complete onboarding in Gusto.
    Self-onboarding is recommended so that contractors receive Gusto accounts.
    If self_onboarding is true, then email is required.
    """
    email: NotRequired[str]
    r"""The contractor’s email address."""
    first_name: NotRequired[str]
    r"""The contractor’s first name.
    This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.
    """
    last_name: NotRequired[str]
    r"""The contractor’s last name.
    This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.
    """
    middle_initial: NotRequired[str]
    r"""The contractor’s middle initial.
    This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    """
    file_new_hire_report: NotRequired[bool]
    r"""The boolean flag indicating whether Gusto will file a new hire report for the contractor.
    This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    """
    work_state: NotRequired[Nullable[str]]
    r"""State where the contractor will be conducting the majority of their work for the company.
    This value is used when generating the new hire report.
    This attribute is required for `Individual` contractors if `file_new_hire_report` is true and will be ignored for `Business` contractors.
    """
    ssn: NotRequired[str]
    r"""This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    Social security number is needed to file the annual 1099 tax form.
    """
    business_name: NotRequired[str]
    r"""The name of the contractor business. This attribute is required for `Business` contractors and will be ignored for `Individual` contractors."""
    ein: NotRequired[str]
    r"""The employer identification number of the contractor business.
    This attribute is optional for `Business` contractors and will be ignored for `Individual` contractors.
    """
    is_active: NotRequired[bool]
    r"""The status of the contractor. If the contractor's start date is in the future, updating this field to true means we are setting the start date to today."""


class PostV1CompaniesCompanyUUIDContractorsRequestBody(BaseModel):
    r"""Create an individual or business contractor."""

    wage_type: PostV1CompaniesCompanyUUIDContractorsWageType
    r"""The contractor’s wage type.

    """

    start_date: str
    r"""The day when the contractor will start working for the company.

    """

    type: Optional[PostV1CompaniesCompanyUUIDContractorsType] = (
        PostV1CompaniesCompanyUUIDContractorsType.INDIVIDUAL
    )
    r"""The contractor type."""

    hourly_rate: Optional[str] = None
    r"""The contractor’s hourly rate. This attribute is required if the wage_type is `Hourly`."""

    self_onboarding: Optional[bool] = False
    r"""Whether the contractor or the payroll admin will complete onboarding in Gusto.
    Self-onboarding is recommended so that contractors receive Gusto accounts.
    If self_onboarding is true, then email is required.
    """

    email: Optional[str] = None
    r"""The contractor’s email address."""

    first_name: Optional[str] = None
    r"""The contractor’s first name.
    This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.
    """

    last_name: Optional[str] = None
    r"""The contractor’s last name.
    This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.
    """

    middle_initial: Optional[str] = None
    r"""The contractor’s middle initial.
    This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    """

    file_new_hire_report: Optional[bool] = False
    r"""The boolean flag indicating whether Gusto will file a new hire report for the contractor.
    This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    """

    work_state: OptionalNullable[str] = UNSET
    r"""State where the contractor will be conducting the majority of their work for the company.
    This value is used when generating the new hire report.
    This attribute is required for `Individual` contractors if `file_new_hire_report` is true and will be ignored for `Business` contractors.
    """

    ssn: Optional[str] = None
    r"""This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    Social security number is needed to file the annual 1099 tax form.
    """

    business_name: Optional[str] = None
    r"""The name of the contractor business. This attribute is required for `Business` contractors and will be ignored for `Individual` contractors."""

    ein: Optional[str] = None
    r"""The employer identification number of the contractor business.
    This attribute is optional for `Business` contractors and will be ignored for `Individual` contractors.
    """

    is_active: Optional[bool] = None
    r"""The status of the contractor. If the contractor's start date is in the future, updating this field to true means we are setting the start date to today."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "type",
            "hourly_rate",
            "self_onboarding",
            "email",
            "first_name",
            "last_name",
            "middle_initial",
            "file_new_hire_report",
            "work_state",
            "ssn",
            "business_name",
            "ein",
            "is_active",
        ]
        nullable_fields = ["work_state"]
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


class PostV1CompaniesCompanyUUIDContractorsRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PostV1CompaniesCompanyUUIDContractorsRequestBodyTypedDict
    r"""Create an individual or business contractor."""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1CompaniesCompanyUUIDContractorsRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostV1CompaniesCompanyUUIDContractorsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Create an individual or business contractor."""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
