"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ActiveCompaniesTypedDict(TypedDict):
    company_uuid: NotRequired[str]
    r"""unique identifier for the company associated with the invoice data"""
    active_employees: NotRequired[int]
    r"""The number of active employees the company was or will be invoiced for that invoice period. Active employees are calculated as the count of onboarded employees hired before the end of the invoice period and not terminated before the start of the invoice period."""
    active_contractors: NotRequired[int]
    r"""The number of active contractors the company was or will be invoiced for that invoice period. Active contractors are calculated as any contractor with an active contractor payment during the invoice period."""
    initial_invoice_period: NotRequired[str]
    r"""The first invoice period for the company. This will either be the invoice period of the first invoice-able event (first payroll or contractor payment) or the date they migrated to embedded, whichever is later."""


class ActiveCompanies(BaseModel):
    company_uuid: Optional[str] = None
    r"""unique identifier for the company associated with the invoice data"""

    active_employees: Optional[int] = None
    r"""The number of active employees the company was or will be invoiced for that invoice period. Active employees are calculated as the count of onboarded employees hired before the end of the invoice period and not terminated before the start of the invoice period."""

    active_contractors: Optional[int] = None
    r"""The number of active contractors the company was or will be invoiced for that invoice period. Active contractors are calculated as any contractor with an active contractor payment during the invoice period."""

    initial_invoice_period: Optional[str] = None
    r"""The first invoice period for the company. This will either be the invoice period of the first invoice-able event (first payroll or contractor payment) or the date they migrated to embedded, whichever is later."""


class InvoiceDataTypedDict(TypedDict):
    r"""Representation of a partners invoice data"""

    active_companies: NotRequired[List[ActiveCompaniesTypedDict]]
    r"""The list of companies that are active within the invoice period"""


class InvoiceData(BaseModel):
    r"""Representation of a partners invoice data"""

    active_companies: Optional[List[ActiveCompanies]] = None
    r"""The list of companies that are active within the invoice period"""
