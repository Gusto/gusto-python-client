"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_app_integration.types import BaseModel
from typing import List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class CompanyBenefitWithEmployeeBenefitsValueTiersTypedDict(TypedDict):
    r"""A single tier of a tiered matching scheme."""

    rate: NotRequired[str]
    r"""The percentage of employee deduction within this tier the company contribution will match."""
    threshold: NotRequired[str]
    r"""The percentage threshold at which this tier ends (inclusive).

    For example, a value of \"5\" means the company contribution will match employee deductions from the previous tier's threshold up to and including 5% of payroll.

    If this is the first tier, a value of \"5\" means the company contribution will match employee deductions from 0% up to and including 5% of payroll.
    """
    threshold_delta: NotRequired[str]
    r"""The step up difference between this tier's threshold and the previous tier's threshold. In the first tier, this is equivalent to threshold."""


class CompanyBenefitWithEmployeeBenefitsValueTiers(BaseModel):
    r"""A single tier of a tiered matching scheme."""

    rate: Optional[str] = None
    r"""The percentage of employee deduction within this tier the company contribution will match."""

    threshold: Optional[str] = None
    r"""The percentage threshold at which this tier ends (inclusive).

    For example, a value of \"5\" means the company contribution will match employee deductions from the previous tier's threshold up to and including 5% of payroll.

    If this is the first tier, a value of \"5\" means the company contribution will match employee deductions from 0% up to and including 5% of payroll.
    """

    threshold_delta: Optional[str] = None
    r"""The step up difference between this tier's threshold and the previous tier's threshold. In the first tier, this is equivalent to threshold."""


class CompanyBenefitWithEmployeeBenefitsValue2TypedDict(TypedDict):
    tiers: NotRequired[List[CompanyBenefitWithEmployeeBenefitsValueTiersTypedDict]]


class CompanyBenefitWithEmployeeBenefitsValue2(BaseModel):
    tiers: Optional[List[CompanyBenefitWithEmployeeBenefitsValueTiers]] = None


CompanyBenefitWithEmployeeBenefitsValueTypedDict = TypeAliasType(
    "CompanyBenefitWithEmployeeBenefitsValueTypedDict",
    Union[CompanyBenefitWithEmployeeBenefitsValue2TypedDict, str],
)
r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

For the `tiered` contribution type, an array of tiers.
"""


CompanyBenefitWithEmployeeBenefitsValue = TypeAliasType(
    "CompanyBenefitWithEmployeeBenefitsValue",
    Union[CompanyBenefitWithEmployeeBenefitsValue2, str],
)
r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

For the `tiered` contribution type, an array of tiers.
"""


class CompanyBenefitWithEmployeeBenefitsContributionTypedDict(TypedDict):
    r"""An object representing the type and value of the company contribution."""

    type: NotRequired[str]
    r"""The company contribution scheme.

    \"amount\": The company contributes a fixed amount per payroll. If elective is true, the contribution is matching, dollar-for-dollar.

    \"percentage\": The company contributes a percentage of the payroll amount per payroll period. If elective is true, the contribution is matching, dollar-for-dollar.

    \"tiered\": The company contribution varies according to the size of the employee deduction.
    """
    value: NotRequired[CompanyBenefitWithEmployeeBenefitsValueTypedDict]
    r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

    For the `tiered` contribution type, an array of tiers.
    """


class CompanyBenefitWithEmployeeBenefitsContribution(BaseModel):
    r"""An object representing the type and value of the company contribution."""

    type: Optional[str] = None
    r"""The company contribution scheme.

    \"amount\": The company contributes a fixed amount per payroll. If elective is true, the contribution is matching, dollar-for-dollar.

    \"percentage\": The company contributes a percentage of the payroll amount per payroll period. If elective is true, the contribution is matching, dollar-for-dollar.

    \"tiered\": The company contribution varies according to the size of the employee deduction.
    """

    value: Optional[CompanyBenefitWithEmployeeBenefitsValue] = None
    r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

    For the `tiered` contribution type, an array of tiers.
    """


class EmployeeBenefitsModelTypedDict(TypedDict):
    employee_uuid: NotRequired[str]
    r"""The UUID of the employee to which the benefit belongs."""
    company_benefit_uuid: NotRequired[str]
    r"""The UUID of the company benefit."""
    active: NotRequired[bool]
    r"""Whether the employee benefit is active."""
    deduct_as_percentage: NotRequired[bool]
    r"""Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll."""
    employee_deduction: NotRequired[str]
    r"""The amount to be deducted, per pay period, from the employee's pay."""
    company_contribution: NotRequired[str]
    r"""The value of the company contribution"""
    uuid: NotRequired[str]
    contribution: NotRequired[CompanyBenefitWithEmployeeBenefitsContributionTypedDict]
    r"""An object representing the type and value of the company contribution."""


class EmployeeBenefitsModel(BaseModel):
    employee_uuid: Optional[str] = None
    r"""The UUID of the employee to which the benefit belongs."""

    company_benefit_uuid: Optional[str] = None
    r"""The UUID of the company benefit."""

    active: Optional[bool] = True
    r"""Whether the employee benefit is active."""

    deduct_as_percentage: Optional[bool] = False
    r"""Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll."""

    employee_deduction: Optional[str] = "0.00"
    r"""The amount to be deducted, per pay period, from the employee's pay."""

    company_contribution: Optional[str] = None
    r"""The value of the company contribution"""

    uuid: Optional[str] = None

    contribution: Optional[CompanyBenefitWithEmployeeBenefitsContribution] = None
    r"""An object representing the type and value of the company contribution."""


class CompanyBenefitWithEmployeeBenefitsTypedDict(TypedDict):
    r"""The representation of a company benefit."""

    uuid: str
    r"""The UUID of the company benefit."""
    version: NotRequired[str]
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    benefit_type: NotRequired[float]
    r"""The type of the benefit to which the company benefit belongs (same as benefit_id)."""
    active: NotRequired[bool]
    r"""Whether this benefit is active for employee participation. Company benefits may only be deactivated if no employees are actively participating."""
    description: NotRequired[str]
    r"""The description of the company benefit. For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”."""
    deletable: NotRequired[bool]
    r"""Whether this company benefit can be deleted. Deletable will be set to true if the benefit has not been used in payroll, has no employee benefits associated, and the benefit is not owned by Gusto or a Partner"""
    supports_percentage_amounts: NotRequired[bool]
    r"""Whether employee deductions and company contributions can be set as percentages of payroll for an individual employee. This is determined by the type of benefit and is not configurable by the company."""
    responsible_for_employer_taxes: NotRequired[bool]
    r"""Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to third party sick pay benefits."""
    responsible_for_employee_w2: NotRequired[bool]
    r"""Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to third party sick pay benefits."""
    employee_benefits: NotRequired[List[EmployeeBenefitsModelTypedDict]]


class CompanyBenefitWithEmployeeBenefits(BaseModel):
    r"""The representation of a company benefit."""

    uuid: str
    r"""The UUID of the company benefit."""

    version: Optional[str] = None
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    benefit_type: Optional[float] = None
    r"""The type of the benefit to which the company benefit belongs (same as benefit_id)."""

    active: Optional[bool] = True
    r"""Whether this benefit is active for employee participation. Company benefits may only be deactivated if no employees are actively participating."""

    description: Optional[str] = None
    r"""The description of the company benefit. For example, a company may offer multiple benefits with an ID of 1 (for Medical Insurance). The description would show something more specific like “Kaiser Permanente” or “Blue Cross/ Blue Shield”."""

    deletable: Optional[bool] = None
    r"""Whether this company benefit can be deleted. Deletable will be set to true if the benefit has not been used in payroll, has no employee benefits associated, and the benefit is not owned by Gusto or a Partner"""

    supports_percentage_amounts: Optional[bool] = None
    r"""Whether employee deductions and company contributions can be set as percentages of payroll for an individual employee. This is determined by the type of benefit and is not configurable by the company."""

    responsible_for_employer_taxes: Optional[bool] = None
    r"""Whether the employer is subject to pay employer taxes when an employee is on leave. Only applicable to third party sick pay benefits."""

    responsible_for_employee_w2: Optional[bool] = None
    r"""Whether the employer is subject to file W-2 forms for an employee on leave. Only applicable to third party sick pay benefits."""

    employee_benefits: Optional[List[EmployeeBenefitsModel]] = None
