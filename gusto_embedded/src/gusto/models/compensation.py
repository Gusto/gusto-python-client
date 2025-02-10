"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .flsa_status_type import FlsaStatusType
from enum import Enum
from gusto.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PaymentUnit(str, Enum):
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""

    HOUR = "Hour"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    PAYCHECK = "Paycheck"


class MinimumWagesTypedDict(TypedDict):
    uuid: NotRequired[str]
    r"""The UUID of the minimum wage."""
    wage: NotRequired[str]
    r"""The wage amount."""
    effective_date: NotRequired[str]
    r"""The effective date of the minimum wage."""


class MinimumWages(BaseModel):
    uuid: Optional[str] = None
    r"""The UUID of the minimum wage."""

    wage: Optional[str] = None
    r"""The wage amount."""

    effective_date: Optional[str] = None
    r"""The effective date of the minimum wage."""


class CompensationTypedDict(TypedDict):
    r"""The representation of compensation in Gusto."""

    uuid: str
    r"""The UUID of the compensation in Gusto."""
    version: NotRequired[str]
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    job_uuid: NotRequired[str]
    r"""The UUID of the job to which the compensation belongs."""
    employee_uuid: NotRequired[str]
    r"""The UUID of the employee to which the compensation belongs."""
    rate: NotRequired[str]
    r"""The dollar amount paid per payment unit."""
    payment_unit: NotRequired[PaymentUnit]
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""
    flsa_status: NotRequired[FlsaStatusType]
    r"""The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company."""
    effective_date: NotRequired[str]
    r"""The effective date for this compensation. For the first compensation, this defaults to the job's hire date."""
    adjust_for_minimum_wage: NotRequired[bool]
    r"""Indicates if the compensation could be adjusted to minimum wage during payroll calculation."""
    minimum_wages: NotRequired[List[MinimumWagesTypedDict]]
    r"""The minimum wages associated with the compensation."""


class Compensation(BaseModel):
    r"""The representation of compensation in Gusto."""

    uuid: str
    r"""The UUID of the compensation in Gusto."""

    version: Optional[str] = None
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    job_uuid: Optional[str] = None
    r"""The UUID of the job to which the compensation belongs."""

    employee_uuid: Optional[str] = None
    r"""The UUID of the employee to which the compensation belongs."""

    rate: Optional[str] = None
    r"""The dollar amount paid per payment unit."""

    payment_unit: Optional[PaymentUnit] = None
    r"""The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'."""

    flsa_status: Optional[FlsaStatusType] = None
    r"""The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company."""

    effective_date: Optional[str] = None
    r"""The effective date for this compensation. For the first compensation, this defaults to the job's hire date."""

    adjust_for_minimum_wage: Optional[bool] = None
    r"""Indicates if the compensation could be adjusted to minimum wage during payroll calculation."""

    minimum_wages: Optional[List[MinimumWages]] = None
    r"""The minimum wages associated with the compensation."""
