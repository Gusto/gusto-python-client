"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PostEmployeeYtdBenefitAmountsFromDifferentCompanyTypedDict(TypedDict):
    tax_year: float
    r"""The tax year for which this amount applies."""
    benefit_type: NotRequired[int]
    r"""The benefit type supported by Gusto."""
    ytd_employee_deduction_amount: NotRequired[str]
    r"""The year-to-date employee deduction made outside the current company."""
    ytd_company_contribution_amount: NotRequired[str]
    r"""The year-to-date company contribution made outside the current company."""


class PostEmployeeYtdBenefitAmountsFromDifferentCompany(BaseModel):
    tax_year: float
    r"""The tax year for which this amount applies."""

    benefit_type: Optional[int] = None
    r"""The benefit type supported by Gusto."""

    ytd_employee_deduction_amount: Optional[str] = "0.00"
    r"""The year-to-date employee deduction made outside the current company."""

    ytd_company_contribution_amount: Optional[str] = "0.00"
    r"""The year-to-date company contribution made outside the current company."""
