"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
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
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class PutV1EmployeeBenefitsEmployeeBenefitIDType(str, Enum):
    r"""The company contribution scheme.

    `amount`: The company contributes a fixed amount per payroll. If elective is true, the contribution is matching, dollar-for-dollar.

    `percentage`: The company contributes a percentage of the payroll amount per payroll period. If elective is true, the contribution is matching, dollar-for-dollar.

    `tiered`: The size of the company contribution corresponds to the size of the employee deduction relative to a tiered matching scheme.
    """

    AMOUNT = "amount"
    PERCENTAGE = "percentage"
    TIERED = "tiered"


class PutV1EmployeeBenefitsEmployeeBenefitIDValue2TypedDict(TypedDict):
    r"""A single tier of a tiered matching scheme."""

    rate: NotRequired[str]
    r"""The percentage of employee deduction within this tier the company contribution will match."""
    threshold: NotRequired[str]
    r"""The percentage threshold at which this tier ends (inclusive).

    For example, a value of \"5\" means the company contribution will match employee deductions from the previous tier's threshold up to and including 5% of payroll.

    If this is the first tier, a value of \"5\" means the company contribution will match employee deductions from 0% up to and including 5% of payroll.
    """


class PutV1EmployeeBenefitsEmployeeBenefitIDValue2(BaseModel):
    r"""A single tier of a tiered matching scheme."""

    rate: Optional[str] = None
    r"""The percentage of employee deduction within this tier the company contribution will match."""

    threshold: Optional[str] = None
    r"""The percentage threshold at which this tier ends (inclusive).

    For example, a value of \"5\" means the company contribution will match employee deductions from the previous tier's threshold up to and including 5% of payroll.

    If this is the first tier, a value of \"5\" means the company contribution will match employee deductions from 0% up to and including 5% of payroll.
    """


PutV1EmployeeBenefitsEmployeeBenefitIDValueTypedDict = TypeAliasType(
    "PutV1EmployeeBenefitsEmployeeBenefitIDValueTypedDict",
    Union[str, List[PutV1EmployeeBenefitsEmployeeBenefitIDValue2TypedDict]],
)
r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

For the `tiered` contribution type, an array of tiers.
"""


PutV1EmployeeBenefitsEmployeeBenefitIDValue = TypeAliasType(
    "PutV1EmployeeBenefitsEmployeeBenefitIDValue",
    Union[str, List[PutV1EmployeeBenefitsEmployeeBenefitIDValue2]],
)
r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

For the `tiered` contribution type, an array of tiers.
"""


class PutV1EmployeeBenefitsEmployeeBenefitIDContributionTypedDict(TypedDict):
    r"""An object representing the type and value of the company contribution."""

    type: NotRequired[PutV1EmployeeBenefitsEmployeeBenefitIDType]
    r"""The company contribution scheme.

    `amount`: The company contributes a fixed amount per payroll. If elective is true, the contribution is matching, dollar-for-dollar.

    `percentage`: The company contributes a percentage of the payroll amount per payroll period. If elective is true, the contribution is matching, dollar-for-dollar.

    `tiered`: The size of the company contribution corresponds to the size of the employee deduction relative to a tiered matching scheme.
    """
    value: NotRequired[PutV1EmployeeBenefitsEmployeeBenefitIDValueTypedDict]
    r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

    For the `tiered` contribution type, an array of tiers.
    """


class PutV1EmployeeBenefitsEmployeeBenefitIDContribution(BaseModel):
    r"""An object representing the type and value of the company contribution."""

    type: Optional[PutV1EmployeeBenefitsEmployeeBenefitIDType] = None
    r"""The company contribution scheme.

    `amount`: The company contributes a fixed amount per payroll. If elective is true, the contribution is matching, dollar-for-dollar.

    `percentage`: The company contributes a percentage of the payroll amount per payroll period. If elective is true, the contribution is matching, dollar-for-dollar.

    `tiered`: The size of the company contribution corresponds to the size of the employee deduction relative to a tiered matching scheme.
    """

    value: Optional[PutV1EmployeeBenefitsEmployeeBenefitIDValue] = None
    r"""For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.

    For the `tiered` contribution type, an array of tiers.
    """


class PutV1EmployeeBenefitsEmployeeBenefitIDLimitOption(str, Enum):
    r"""Some benefits require additional information to determine
    their limit.

    `Family` or `Individual`: Applicable to HSA benefit.

    `Joint Filing or Single` or `Married and Filing Separately`: Applicable to Dependent Care FSA benefit.
    """

    FAMILY = "Family"
    INDIVIDUAL = "Individual"
    JOINT_FILING_OR_SINGLE = "Joint Filing or Single"
    MARRIED_AND_FILING_SEPARATELY = "Married and Filing Separately"


class PutV1EmployeeBenefitsEmployeeBenefitIDDeductionReducesTaxableIncome(str, Enum):
    r"""Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \"unset\", coverage amount and coverage salary multiplier are ignored."""

    UNSET = "unset"
    REDUCES_TAXABLE_INCOME = "reduces_taxable_income"
    DOES_NOT_REDUCE_TAXABLE_INCOME = "does_not_reduce_taxable_income"


class PutV1EmployeeBenefitsEmployeeBenefitIDRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    active: NotRequired[bool]
    r"""Whether the employee benefit is active."""
    employee_deduction: NotRequired[str]
    r"""The amount to be deducted, per pay period, from the employee's pay."""
    deduct_as_percentage: NotRequired[bool]
    r"""Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll."""
    employee_deduction_annual_maximum: NotRequired[Nullable[str]]
    r"""The maximum employee deduction amount per year. A null value signifies no limit."""
    contribution: NotRequired[
        PutV1EmployeeBenefitsEmployeeBenefitIDContributionTypedDict
    ]
    r"""An object representing the type and value of the company contribution."""
    elective: NotRequired[bool]
    r"""Whether the company contribution is elective (aka \"matching\"). For `tiered`, `elective_amount`, and `elective_percentage` contribution types this is ignored and assumed to be `true`."""
    company_contribution_annual_maximum: NotRequired[Nullable[str]]
    r"""The maximum company contribution amount per year. A null value signifies no limit."""
    limit_option: NotRequired[
        Nullable[PutV1EmployeeBenefitsEmployeeBenefitIDLimitOption]
    ]
    r"""Some benefits require additional information to determine
    their limit.

    `Family` or `Individual`: Applicable to HSA benefit.

    `Joint Filing or Single` or `Married and Filing Separately`: Applicable to Dependent Care FSA benefit.
    """
    catch_up: NotRequired[bool]
    r"""Whether the employee should use a benefit’s \"catch up\" rate. Only Roth 401k and 401k benefits use this value for employees over 50."""
    coverage_amount: NotRequired[Nullable[str]]
    r"""The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set."""
    deduction_reduces_taxable_income: NotRequired[
        Nullable[PutV1EmployeeBenefitsEmployeeBenefitIDDeductionReducesTaxableIncome]
    ]
    r"""Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \"unset\", coverage amount and coverage salary multiplier are ignored."""
    coverage_salary_multiplier: NotRequired[str]
    r"""The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set."""
    company_contribution: NotRequired[str]
    r"""The amount to be paid, per pay period, by the company."""
    contribute_as_percentage: NotRequired[bool]
    r"""Whether the company contribution amount should be treated as a percentage to be deducted from each payroll."""


class PutV1EmployeeBenefitsEmployeeBenefitIDRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    active: Optional[bool] = None
    r"""Whether the employee benefit is active."""

    employee_deduction: Optional[str] = "0.00"
    r"""The amount to be deducted, per pay period, from the employee's pay."""

    deduct_as_percentage: Optional[bool] = None
    r"""Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll."""

    employee_deduction_annual_maximum: OptionalNullable[str] = UNSET
    r"""The maximum employee deduction amount per year. A null value signifies no limit."""

    contribution: Optional[PutV1EmployeeBenefitsEmployeeBenefitIDContribution] = None
    r"""An object representing the type and value of the company contribution."""

    elective: Optional[bool] = False
    r"""Whether the company contribution is elective (aka \"matching\"). For `tiered`, `elective_amount`, and `elective_percentage` contribution types this is ignored and assumed to be `true`."""

    company_contribution_annual_maximum: OptionalNullable[str] = UNSET
    r"""The maximum company contribution amount per year. A null value signifies no limit."""

    limit_option: OptionalNullable[
        PutV1EmployeeBenefitsEmployeeBenefitIDLimitOption
    ] = UNSET
    r"""Some benefits require additional information to determine
    their limit.

    `Family` or `Individual`: Applicable to HSA benefit.

    `Joint Filing or Single` or `Married and Filing Separately`: Applicable to Dependent Care FSA benefit.
    """

    catch_up: Optional[bool] = False
    r"""Whether the employee should use a benefit’s \"catch up\" rate. Only Roth 401k and 401k benefits use this value for employees over 50."""

    coverage_amount: OptionalNullable[str] = UNSET
    r"""The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set."""

    deduction_reduces_taxable_income: OptionalNullable[
        PutV1EmployeeBenefitsEmployeeBenefitIDDeductionReducesTaxableIncome
    ] = PutV1EmployeeBenefitsEmployeeBenefitIDDeductionReducesTaxableIncome.UNSET
    r"""Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \"unset\", coverage amount and coverage salary multiplier are ignored."""

    coverage_salary_multiplier: Optional[str] = "0.00"
    r"""The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set."""

    company_contribution: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = "0.00"
    r"""The amount to be paid, per pay period, by the company."""

    contribute_as_percentage: Annotated[
        Optional[bool],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = False
    r"""Whether the company contribution amount should be treated as a percentage to be deducted from each payroll."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "active",
            "employee_deduction",
            "deduct_as_percentage",
            "employee_deduction_annual_maximum",
            "contribution",
            "elective",
            "company_contribution_annual_maximum",
            "limit_option",
            "catch_up",
            "coverage_amount",
            "deduction_reduces_taxable_income",
            "coverage_salary_multiplier",
            "company_contribution",
            "contribute_as_percentage",
        ]
        nullable_fields = [
            "employee_deduction_annual_maximum",
            "company_contribution_annual_maximum",
            "limit_option",
            "coverage_amount",
            "deduction_reduces_taxable_income",
        ]
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


class PutV1EmployeeBenefitsEmployeeBenefitIDRequestTypedDict(TypedDict):
    employee_benefit_id: str
    r"""The UUID of the employee benefit."""
    request_body: PutV1EmployeeBenefitsEmployeeBenefitIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1EmployeeBenefitsEmployeeBenefitIDRequest(BaseModel):
    employee_benefit_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee benefit."""

    request_body: Annotated[
        PutV1EmployeeBenefitsEmployeeBenefitIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
