"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto_embedded.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class Status(str, Enum):
    r"""The status of the external payroll. The status will be `unprocessed` when the external payroll is created and transition to `processed` once tax liabilities are entered and finalized.  Once in the `processed` status all actions that can edit an external payroll will be disabled."""

    UNPROCESSED = "unprocessed"
    PROCESSED = "processed"


class EarningsTypedDict(TypedDict):
    amount: NotRequired[str]
    hours: NotRequired[str]
    earning_type: NotRequired[str]
    earning_id: NotRequired[int]


class Earnings(BaseModel):
    amount: Optional[str] = None

    hours: Optional[str] = None

    earning_type: Optional[str] = None

    earning_id: Optional[int] = None


class ExternalPayrollBenefitsTypedDict(TypedDict):
    benefit_id: NotRequired[int]
    company_contribution_amount: NotRequired[str]
    employee_deduction_amount: NotRequired[str]


class ExternalPayrollBenefits(BaseModel):
    benefit_id: Optional[int] = None

    company_contribution_amount: Optional[str] = None

    employee_deduction_amount: Optional[str] = None


class ExternalPayrollTaxesTypedDict(TypedDict):
    tax_id: NotRequired[int]
    amount: NotRequired[str]


class ExternalPayrollTaxes(BaseModel):
    tax_id: Optional[int] = None

    amount: Optional[str] = None


class ExternalPayrollItemsTypedDict(TypedDict):
    employee_uuid: NotRequired[str]
    earnings: NotRequired[List[EarningsTypedDict]]
    benefits: NotRequired[List[ExternalPayrollBenefitsTypedDict]]
    taxes: NotRequired[List[ExternalPayrollTaxesTypedDict]]


class ExternalPayrollItems(BaseModel):
    employee_uuid: Optional[str] = None

    earnings: Optional[List[Earnings]] = None

    benefits: Optional[List[ExternalPayrollBenefits]] = None

    taxes: Optional[List[ExternalPayrollTaxes]] = None


class ApplicableEarningsTypedDict(TypedDict):
    earning_type: NotRequired[str]
    earning_id: NotRequired[float]
    name: NotRequired[str]
    input_type: NotRequired[str]
    category: NotRequired[str]


class ApplicableEarnings(BaseModel):
    earning_type: Optional[str] = None

    earning_id: Optional[float] = None

    name: Optional[str] = None

    input_type: Optional[str] = None

    category: Optional[str] = None


class ApplicableBenefitsTypedDict(TypedDict):
    id: NotRequired[int]
    description: NotRequired[str]
    active: NotRequired[bool]


class ApplicableBenefits(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    active: Optional[bool] = None


class ApplicableTaxesTypedDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    employer_tax: NotRequired[bool]
    r"""Some taxes may have an amount withheld from the employee and an amount withheld from the employer, e.g. Social Security. A `true` value indicates this is the employer's amount."""
    resident_tax: NotRequired[bool]
    r"""Some taxes may have different rates or reporting requirements depending on if the employee is a resident or non-resident of the tax jurisdiction."""


class ApplicableTaxes(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    employer_tax: Optional[bool] = None
    r"""Some taxes may have an amount withheld from the employee and an amount withheld from the employer, e.g. Social Security. A `true` value indicates this is the employer's amount."""

    resident_tax: Optional[bool] = None
    r"""Some taxes may have different rates or reporting requirements depending on if the employee is a resident or non-resident of the tax jurisdiction."""


class ExternalPayrollMetadataTypedDict(TypedDict):
    r"""Stores metadata of the external payroll."""

    deletable: NotRequired[bool]
    r"""Determines if the external payroll can be deleted."""


class ExternalPayrollMetadata(BaseModel):
    r"""Stores metadata of the external payroll."""

    deletable: Optional[bool] = None
    r"""Determines if the external payroll can be deleted."""


class ExternalPayrollTypedDict(TypedDict):
    r"""The representation of an external payroll."""

    uuid: str
    r"""The UUID of the external payroll."""
    company_uuid: NotRequired[str]
    r"""The UUID of the company."""
    check_date: NotRequired[str]
    r"""External payroll's check date."""
    payment_period_start_date: NotRequired[str]
    r"""External payroll's pay period start date."""
    payment_period_end_date: NotRequired[str]
    r"""External payroll's pay period end date."""
    status: NotRequired[Status]
    r"""The status of the external payroll. The status will be `unprocessed` when the external payroll is created and transition to `processed` once tax liabilities are entered and finalized.  Once in the `processed` status all actions that can edit an external payroll will be disabled."""
    external_payroll_items: NotRequired[List[ExternalPayrollItemsTypedDict]]
    r"""External payroll items for employees"""
    applicable_earnings: NotRequired[List[ApplicableEarningsTypedDict]]
    r"""Applicable earnings based on company provisioning."""
    applicable_benefits: NotRequired[List[ApplicableBenefitsTypedDict]]
    r"""Applicable benefits based on company provisioning."""
    applicable_taxes: NotRequired[List[ApplicableTaxesTypedDict]]
    r"""Applicable taxes based on company provisioning."""
    metadata: NotRequired[ExternalPayrollMetadataTypedDict]
    r"""Stores metadata of the external payroll."""


class ExternalPayroll(BaseModel):
    r"""The representation of an external payroll."""

    uuid: str
    r"""The UUID of the external payroll."""

    company_uuid: Optional[str] = None
    r"""The UUID of the company."""

    check_date: Optional[str] = None
    r"""External payroll's check date."""

    payment_period_start_date: Optional[str] = None
    r"""External payroll's pay period start date."""

    payment_period_end_date: Optional[str] = None
    r"""External payroll's pay period end date."""

    status: Optional[Status] = None
    r"""The status of the external payroll. The status will be `unprocessed` when the external payroll is created and transition to `processed` once tax liabilities are entered and finalized.  Once in the `processed` status all actions that can edit an external payroll will be disabled."""

    external_payroll_items: Optional[List[ExternalPayrollItems]] = None
    r"""External payroll items for employees"""

    applicable_earnings: Optional[List[ApplicableEarnings]] = None
    r"""Applicable earnings based on company provisioning."""

    applicable_benefits: Optional[List[ApplicableBenefits]] = None
    r"""Applicable benefits based on company provisioning."""

    applicable_taxes: Optional[List[ApplicableTaxes]] = None
    r"""Applicable taxes based on company provisioning."""

    metadata: Optional[ExternalPayrollMetadata] = None
    r"""Stores metadata of the external payroll."""
