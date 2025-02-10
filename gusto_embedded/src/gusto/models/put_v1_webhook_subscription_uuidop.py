"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto.types import BaseModel
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1WebhookSubscriptionUUIDSecurityTypedDict(TypedDict):
    system_access_auth: str


class PutV1WebhookSubscriptionUUIDSecurity(BaseModel):
    system_access_auth: Annotated[
        str,
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ]


class PutV1WebhookSubscriptionUUIDSubscriptionTypes(str, Enum):
    BANK_ACCOUNT = "BankAccount"
    COMPANY = "Company"
    COMPANY_BENEFIT = "CompanyBenefit"
    CONTRACTOR = "Contractor"
    CONTRACTOR_PAYMENT = "ContractorPayment"
    EMPLOYEE = "Employee"
    EMPLOYEE_BENEFIT = "EmployeeBenefit"
    EMPLOYEE_JOB_COMPENSATION = "EmployeeJobCompensation"
    EXTERNAL_PAYROLL = "ExternalPayroll"
    FORM = "Form"
    LOCATION = "Location"
    NOTIFICATION = "Notification"
    PAYROLL = "Payroll"
    PAY_SCHEDULE = "PaySchedule"
    SIGNATORY = "Signatory"


class PutV1WebhookSubscriptionUUIDRequestBodyTypedDict(TypedDict):
    subscription_types: List[PutV1WebhookSubscriptionUUIDSubscriptionTypes]


class PutV1WebhookSubscriptionUUIDRequestBody(BaseModel):
    subscription_types: List[PutV1WebhookSubscriptionUUIDSubscriptionTypes]


class PutV1WebhookSubscriptionUUIDRequestTypedDict(TypedDict):
    webhook_subscription_uuid: str
    r"""The webhook subscription UUID."""
    request_body: PutV1WebhookSubscriptionUUIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1WebhookSubscriptionUUIDRequest(BaseModel):
    webhook_subscription_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The webhook subscription UUID."""

    request_body: Annotated[
        PutV1WebhookSubscriptionUUIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
