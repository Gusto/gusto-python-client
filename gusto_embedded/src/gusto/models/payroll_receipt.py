"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TotalsTypedDict(TypedDict):
    r"""The subtotals for the payroll."""

    company_debit: NotRequired[str]
    r"""The total company debit for the payroll."""
    net_pay_debit: NotRequired[str]
    r"""The total company net pay for the payroll."""
    child_support_debit: NotRequired[str]
    r"""The total child support debit for the payroll."""
    reimbursement_debit: NotRequired[str]
    r"""The total reimbursements for the payroll."""
    tax_debit: NotRequired[str]
    r"""The total tax debit for the payroll."""


class Totals(BaseModel):
    r"""The subtotals for the payroll."""

    company_debit: Optional[str] = None
    r"""The total company debit for the payroll."""

    net_pay_debit: Optional[str] = None
    r"""The total company net pay for the payroll."""

    child_support_debit: Optional[str] = None
    r"""The total child support debit for the payroll."""

    reimbursement_debit: Optional[str] = None
    r"""The total reimbursements for the payroll."""

    tax_debit: Optional[str] = None
    r"""The total tax debit for the payroll."""


class PayrollReceiptTaxesTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The amount paid for this tax."""
    amount: NotRequired[str]
    r"""The total amount paid by both employer and employee for this tax."""


class PayrollReceiptTaxes(BaseModel):
    name: Optional[str] = None
    r"""The amount paid for this tax."""

    amount: Optional[str] = None
    r"""The total amount paid by both employer and employee for this tax."""


class EmployeeCompensationsTypedDict(TypedDict):
    employee_uuid: NotRequired[str]
    r"""The UUID of the employee."""
    employee_first_name: NotRequired[str]
    r"""The first name of the employee."""
    employee_last_name: NotRequired[str]
    r"""The last name of the employee."""
    payment_method: NotRequired[str]
    r"""The employee's compensation payment method.\n\n`Check` `Direct Deposit`"""
    net_pay: NotRequired[str]
    r"""The employee's net pay. Net pay paid by check is available for reference but is not included in the `[\"totals\"][\"net_pay_debit\"]` amount."""
    total_tax: NotRequired[str]
    r"""The total of employer and employee taxes for the pay period."""
    total_garnishments: NotRequired[str]
    r"""The total garnishments for the pay period."""
    child_support_garnishment: NotRequired[str]
    r"""The total child support garnishment for the pay period."""
    total_reimbursement: NotRequired[str]
    r"""The total reimbursement for the pay period."""


class EmployeeCompensations(BaseModel):
    employee_uuid: Optional[str] = None
    r"""The UUID of the employee."""

    employee_first_name: Optional[str] = None
    r"""The first name of the employee."""

    employee_last_name: Optional[str] = None
    r"""The last name of the employee."""

    payment_method: Optional[str] = None
    r"""The employee's compensation payment method.\n\n`Check` `Direct Deposit`"""

    net_pay: Optional[str] = None
    r"""The employee's net pay. Net pay paid by check is available for reference but is not included in the `[\"totals\"][\"net_pay_debit\"]` amount."""

    total_tax: Optional[str] = None
    r"""The total of employer and employee taxes for the pay period."""

    total_garnishments: Optional[str] = None
    r"""The total garnishments for the pay period."""

    child_support_garnishment: Optional[str] = None
    r"""The total child support garnishment for the pay period."""

    total_reimbursement: Optional[str] = None
    r"""The total reimbursement for the pay period."""


class LicenseeTypedDict(TypedDict):
    r"""The licensed payroll processor"""

    name: NotRequired[str]
    r"""Always the fixed string \"Gusto, Zenpayroll Inc.\" """
    address: NotRequired[str]
    r"""Always the fixed string \"525 20th St\" """
    city: NotRequired[str]
    r"""Always the fixed string \"San Francisco\" """
    state: NotRequired[str]
    r"""Always the fixed string \"CA\" """
    postal_code: NotRequired[str]
    r"""Always the fixed string \"94107\" """
    phone_number: NotRequired[str]
    r"""Always the fixed string \"4157778888\" """


class Licensee(BaseModel):
    r"""The licensed payroll processor"""

    name: Optional[str] = None
    r"""Always the fixed string \"Gusto, Zenpayroll Inc.\" """

    address: Optional[str] = None
    r"""Always the fixed string \"525 20th St\" """

    city: Optional[str] = None
    r"""Always the fixed string \"San Francisco\" """

    state: Optional[str] = None
    r"""Always the fixed string \"CA\" """

    postal_code: Optional[str] = None
    r"""Always the fixed string \"94107\" """

    phone_number: Optional[str] = None
    r"""Always the fixed string \"4157778888\" """


class PayrollReceiptTypedDict(TypedDict):
    r"""Example response"""

    payroll_uuid: NotRequired[str]
    r"""A unique identifier of the payroll receipt."""
    company_uuid: NotRequired[str]
    r"""A unique identifier of the company for the payroll."""
    name_of_sender: NotRequired[str]
    r"""The name of the company by whom the payroll was paid"""
    name_of_recipient: NotRequired[str]
    r"""Always the fixed string \"Payroll Recipients\" """
    recipient_notice: NotRequired[str]
    r"""Always the fixed string \"Payroll recipients include the employees listed below plus the tax agencies for the taxes listed below.\" """
    debit_date: NotRequired[str]
    r"""The debit or funding date for the payroll"""
    license: NotRequired[str]
    r"""Always the fixed string \"ZenPayroll, Inc., dba Gusto is a licensed money transmitter. For more about Gusto’s licenses and your state-specific rights to request information, submit complaints, dispute errors, or cancel transactions, visit our license page.\" """
    license_uri: NotRequired[str]
    r"""URL for the license information for the licensed payroll processor. Always the fixed string \"https://gusto.com/about/licenses\" """
    right_to_refund: NotRequired[str]
    liability_of_licensee: NotRequired[str]
    totals: NotRequired[TotalsTypedDict]
    r"""The subtotals for the payroll."""
    taxes: NotRequired[List[PayrollReceiptTaxesTypedDict]]
    r"""An array of totaled employer and employee taxes for the pay period."""
    employee_compensations: NotRequired[List[EmployeeCompensationsTypedDict]]
    r"""An array of employee compensations and withholdings for this payroll"""
    licensee: NotRequired[LicenseeTypedDict]
    r"""The licensed payroll processor"""


class PayrollReceipt(BaseModel):
    r"""Example response"""

    payroll_uuid: Optional[str] = None
    r"""A unique identifier of the payroll receipt."""

    company_uuid: Optional[str] = None
    r"""A unique identifier of the company for the payroll."""

    name_of_sender: Optional[str] = None
    r"""The name of the company by whom the payroll was paid"""

    name_of_recipient: Optional[str] = None
    r"""Always the fixed string \"Payroll Recipients\" """

    recipient_notice: Optional[str] = None
    r"""Always the fixed string \"Payroll recipients include the employees listed below plus the tax agencies for the taxes listed below.\" """

    debit_date: Optional[str] = None
    r"""The debit or funding date for the payroll"""

    license: Optional[str] = None
    r"""Always the fixed string \"ZenPayroll, Inc., dba Gusto is a licensed money transmitter. For more about Gusto’s licenses and your state-specific rights to request information, submit complaints, dispute errors, or cancel transactions, visit our license page.\" """

    license_uri: Optional[str] = None
    r"""URL for the license information for the licensed payroll processor. Always the fixed string \"https://gusto.com/about/licenses\" """

    right_to_refund: Optional[str] = None

    liability_of_licensee: Optional[str] = None

    totals: Optional[Totals] = None
    r"""The subtotals for the payroll."""

    taxes: Optional[List[PayrollReceiptTaxes]] = None
    r"""An array of totaled employer and employee taxes for the pay period."""

    employee_compensations: Optional[List[EmployeeCompensations]] = None
    r"""An array of employee compensations and withholdings for this payroll"""

    licensee: Optional[Licensee] = None
    r"""The licensed payroll processor"""
