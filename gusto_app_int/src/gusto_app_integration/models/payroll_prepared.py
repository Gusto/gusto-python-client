"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .off_cycle_reason_type import OffCycleReasonType
from .payroll_employee_compensations_type import (
    PayrollEmployeeCompensationsType,
    PayrollEmployeeCompensationsTypeTypedDict,
)
from .payroll_fixed_compensation_types_type import (
    PayrollFixedCompensationTypesType,
    PayrollFixedCompensationTypesTypeTypedDict,
)
from .payroll_pay_period_type import PayrollPayPeriodType, PayrollPayPeriodTypeTypedDict
from .payroll_payment_speed_changed_type import (
    PayrollPaymentSpeedChangedType,
    PayrollPaymentSpeedChangedTypeTypedDict,
)
from .payroll_payroll_status_meta_type import (
    PayrollPayrollStatusMetaType,
    PayrollPayrollStatusMetaTypeTypedDict,
)
from .payroll_processing_request import (
    PayrollProcessingRequest,
    PayrollProcessingRequestTypedDict,
)
from .payroll_withholding_pay_period_type import PayrollWithholdingPayPeriodType
from datetime import datetime
from gusto_app_integration.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PayrollPreparedTypedDict(TypedDict):
    r"""A prepared payroll"""

    payroll_deadline: NotRequired[datetime]
    r"""A timestamp that is the deadline for the payroll to be run in order for employees to be paid on time.  If payroll has not been run by the deadline, a prepare request will update both the check date and deadline to reflect the soonest employees can be paid and the deadline by which the payroll must be run in order for said check date to be met."""
    check_date: NotRequired[str]
    r"""The date on which employees will be paid for the payroll."""
    processed: NotRequired[bool]
    r"""Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. Additionally, a payroll is not guaranteed to be processed just because the payroll deadline has passed. Late payrolls are not uncommon. Conversely, users may choose to run payroll before the payroll deadline."""
    processed_date: NotRequired[str]
    r"""The date at which the payroll was processed. Null if the payroll isn't processed yet."""
    calculated_at: NotRequired[str]
    r"""A timestamp of the last valid payroll calculation. Null if there isn't a valid calculation."""
    uuid: NotRequired[str]
    r"""The UUID of the payroll."""
    payroll_uuid: NotRequired[str]
    r"""The UUID of the payroll."""
    company_uuid: NotRequired[str]
    r"""The UUID of the company for the payroll."""
    off_cycle: NotRequired[bool]
    r"""Indicates whether the payroll is an off-cycle payroll"""
    off_cycle_reason: NotRequired[Nullable[OffCycleReasonType]]
    r"""The off-cycle reason. Only included for off-cycle payrolls."""
    auto_pilot: NotRequired[bool]
    r"""Indicates whether the payroll is an auto pilot payroll"""
    external: NotRequired[bool]
    r"""Indicates whether the payroll is an external payroll"""
    final_termination_payroll: NotRequired[bool]
    r"""Indicates whether the payroll is the final payroll for a terminated employee. Only included for off-cycle payrolls."""
    withholding_pay_period: NotRequired[PayrollWithholdingPayPeriodType]
    r"""The payment schedule tax rate the payroll is based on. Only included for off-cycle payrolls."""
    skip_regular_deductions: NotRequired[bool]
    r"""Block regular deductions and contributions for this payroll.  Only included for off-cycle payrolls."""
    fixed_withholding_rate: NotRequired[bool]
    r"""Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages. Only included for off-cycle payrolls."""
    pay_period: NotRequired[PayrollPayPeriodTypeTypedDict]
    payroll_status_meta: NotRequired[PayrollPayrollStatusMetaTypeTypedDict]
    r"""Information about the payroll's status and expected dates"""
    employee_compensations: NotRequired[List[PayrollEmployeeCompensationsTypeTypedDict]]
    payment_speed_changed: NotRequired[PayrollPaymentSpeedChangedTypeTypedDict]
    r"""Only applicable when a payroll is moved to four day processing instead of fast ach."""
    created_at: NotRequired[datetime]
    r"""Datetime for when the resource was created."""
    fixed_compensation_types: NotRequired[
        List[PayrollFixedCompensationTypesTypeTypedDict]
    ]
    processing_request: NotRequired[Nullable[PayrollProcessingRequestTypedDict]]


class PayrollPrepared(BaseModel):
    r"""A prepared payroll"""

    payroll_deadline: Optional[datetime] = None
    r"""A timestamp that is the deadline for the payroll to be run in order for employees to be paid on time.  If payroll has not been run by the deadline, a prepare request will update both the check date and deadline to reflect the soonest employees can be paid and the deadline by which the payroll must be run in order for said check date to be met."""

    check_date: Optional[str] = None
    r"""The date on which employees will be paid for the payroll."""

    processed: Optional[bool] = None
    r"""Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. Additionally, a payroll is not guaranteed to be processed just because the payroll deadline has passed. Late payrolls are not uncommon. Conversely, users may choose to run payroll before the payroll deadline."""

    processed_date: Optional[str] = None
    r"""The date at which the payroll was processed. Null if the payroll isn't processed yet."""

    calculated_at: Optional[str] = None
    r"""A timestamp of the last valid payroll calculation. Null if there isn't a valid calculation."""

    uuid: Optional[str] = None
    r"""The UUID of the payroll."""

    payroll_uuid: Optional[str] = None
    r"""The UUID of the payroll."""

    company_uuid: Optional[str] = None
    r"""The UUID of the company for the payroll."""

    off_cycle: Optional[bool] = None
    r"""Indicates whether the payroll is an off-cycle payroll"""

    off_cycle_reason: OptionalNullable[OffCycleReasonType] = UNSET
    r"""The off-cycle reason. Only included for off-cycle payrolls."""

    auto_pilot: Optional[bool] = None
    r"""Indicates whether the payroll is an auto pilot payroll"""

    external: Optional[bool] = None
    r"""Indicates whether the payroll is an external payroll"""

    final_termination_payroll: Optional[bool] = None
    r"""Indicates whether the payroll is the final payroll for a terminated employee. Only included for off-cycle payrolls."""

    withholding_pay_period: Optional[PayrollWithholdingPayPeriodType] = None
    r"""The payment schedule tax rate the payroll is based on. Only included for off-cycle payrolls."""

    skip_regular_deductions: Optional[bool] = None
    r"""Block regular deductions and contributions for this payroll.  Only included for off-cycle payrolls."""

    fixed_withholding_rate: Optional[bool] = None
    r"""Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages. Only included for off-cycle payrolls."""

    pay_period: Optional[PayrollPayPeriodType] = None

    payroll_status_meta: Optional[PayrollPayrollStatusMetaType] = None
    r"""Information about the payroll's status and expected dates"""

    employee_compensations: Optional[List[PayrollEmployeeCompensationsType]] = None

    payment_speed_changed: Optional[PayrollPaymentSpeedChangedType] = None
    r"""Only applicable when a payroll is moved to four day processing instead of fast ach."""

    created_at: Optional[datetime] = None
    r"""Datetime for when the resource was created."""

    fixed_compensation_types: Optional[List[PayrollFixedCompensationTypesType]] = None

    processing_request: OptionalNullable[PayrollProcessingRequest] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "payroll_deadline",
            "check_date",
            "processed",
            "processed_date",
            "calculated_at",
            "uuid",
            "payroll_uuid",
            "company_uuid",
            "off_cycle",
            "off_cycle_reason",
            "auto_pilot",
            "external",
            "final_termination_payroll",
            "withholding_pay_period",
            "skip_regular_deductions",
            "fixed_withholding_rate",
            "pay_period",
            "payroll_status_meta",
            "employee_compensations",
            "payment_speed_changed",
            "created_at",
            "fixed_compensation_types",
            "processing_request",
        ]
        nullable_fields = ["off_cycle_reason", "processing_request"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
