"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto_embedded.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ContractorBankAccountAccountType(str, Enum):
    r"""Bank account type"""

    CHECKING = "Checking"
    SAVINGS = "Savings"


class ContractorBankAccountTypedDict(TypedDict):
    r"""Example response"""

    uuid: str
    r"""UUID of the bank account"""
    contractor_uuid: NotRequired[str]
    r"""UUID of the employee"""
    account_type: NotRequired[ContractorBankAccountAccountType]
    r"""Bank account type"""
    name: NotRequired[str]
    r"""Name for the bank account"""
    routing_number: NotRequired[str]
    r"""The bank account's routing number"""
    hidden_account_number: NotRequired[str]
    r"""Masked bank account number"""


class ContractorBankAccount(BaseModel):
    r"""Example response"""

    uuid: str
    r"""UUID of the bank account"""

    contractor_uuid: Optional[str] = None
    r"""UUID of the employee"""

    account_type: Optional[ContractorBankAccountAccountType] = None
    r"""Bank account type"""

    name: Optional[str] = None
    r"""Name for the bank account"""

    routing_number: Optional[str] = None
    r"""The bank account's routing number"""

    hidden_account_number: Optional[str] = None
    r"""Masked bank account number"""
