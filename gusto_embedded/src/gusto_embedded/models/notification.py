"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto_embedded.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class NotificationStatus(str, Enum):
    r"""Represents the notification's status as managed by our system. It is updated based on observable system events and internal business logic, and does not reflect resolution steps taken outside our system. This field is read-only and cannot be modified via the API."""

    OPEN = "open"
    RESOLVED = "resolved"
    EXPIRED = "expired"


class ResourcesTypedDict(TypedDict):
    entity_type: str
    r"""The type of entity being described, could be “Contractor”, “Employee”, “BankAccount”, “Payroll”, “ContractorPayment”, “RecoveryCase”, or “Signatory”"""
    entity_uuid: str
    r"""Unique identifier of the entity"""
    reference_type: NotRequired[str]
    r"""Optional. The type of a resource that is related to the one described by entity_type and entity_uuid. For instance, if the entity_type is “BankAccount”, the reference_type could be the “Employee” or “Contractor” to whom the bank account belongs."""
    reference_uuid: NotRequired[str]
    r"""Optional. Unique identifier of the reference."""


class Resources(BaseModel):
    entity_type: str
    r"""The type of entity being described, could be “Contractor”, “Employee”, “BankAccount”, “Payroll”, “ContractorPayment”, “RecoveryCase”, or “Signatory”"""

    entity_uuid: str
    r"""Unique identifier of the entity"""

    reference_type: Optional[str] = None
    r"""Optional. The type of a resource that is related to the one described by entity_type and entity_uuid. For instance, if the entity_type is “BankAccount”, the reference_type could be the “Employee” or “Contractor” to whom the bank account belongs."""

    reference_uuid: Optional[str] = None
    r"""Optional. Unique identifier of the reference."""


class NotificationTypedDict(TypedDict):
    r"""Representation of a notification"""

    uuid: str
    r"""Unique identifier of a notification."""
    company_uuid: NotRequired[str]
    r"""Unique identifier of the company to which the notification belongs."""
    title: NotRequired[str]
    r"""The title of the notification. This highlights the actionable component of the notification."""
    message: NotRequired[str]
    r"""The message of the notification. This provides additional context for the user and recommends a specific action to resolve the notification."""
    status: NotRequired[NotificationStatus]
    r"""Represents the notification's status as managed by our system. It is updated based on observable system events and internal business logic, and does not reflect resolution steps taken outside our system. This field is read-only and cannot be modified via the API."""
    category: NotRequired[str]
    r"""The notification's category."""
    actionable: NotRequired[bool]
    r"""Indicates whether a notification requires action or not. If false, the notification provides critical information only."""
    can_block_payroll: NotRequired[bool]
    r"""Indicates whether a notification may block ability to run payroll. If true, we suggest that these notifications are prioritized to your end users."""
    published_at: NotRequired[str]
    r"""Timestamp of when the notification was published."""
    due_at: NotRequired[str]
    r"""Timestamp of when the notification is due. If the notification has no due date, this field will be null."""
    template_variables: NotRequired[Dict[str, str]]
    r"""An object containing template variables used to render the notification. The structure of this object depends on the notification category. Each category defines a fixed set of variable names (keys), which are always present. The values of these variables can vary depending on the specific notification instance."""
    resources: NotRequired[List[ResourcesTypedDict]]
    r"""An array of entities relevant to the notification"""


class Notification(BaseModel):
    r"""Representation of a notification"""

    uuid: str
    r"""Unique identifier of a notification."""

    company_uuid: Optional[str] = None
    r"""Unique identifier of the company to which the notification belongs."""

    title: Optional[str] = None
    r"""The title of the notification. This highlights the actionable component of the notification."""

    message: Optional[str] = None
    r"""The message of the notification. This provides additional context for the user and recommends a specific action to resolve the notification."""

    status: Optional[NotificationStatus] = None
    r"""Represents the notification's status as managed by our system. It is updated based on observable system events and internal business logic, and does not reflect resolution steps taken outside our system. This field is read-only and cannot be modified via the API."""

    category: Optional[str] = None
    r"""The notification's category."""

    actionable: Optional[bool] = None
    r"""Indicates whether a notification requires action or not. If false, the notification provides critical information only."""

    can_block_payroll: Optional[bool] = None
    r"""Indicates whether a notification may block ability to run payroll. If true, we suggest that these notifications are prioritized to your end users."""

    published_at: Optional[str] = None
    r"""Timestamp of when the notification was published."""

    due_at: Optional[str] = None
    r"""Timestamp of when the notification is due. If the notification has no due date, this field will be null."""

    template_variables: Optional[Dict[str, str]] = None
    r"""An object containing template variables used to render the notification. The structure of this object depends on the notification category. Each category defines a fixed set of variable names (keys), which are always present. The values of these variables can vary depending on the specific notification instance."""

    resources: Optional[List[Resources]] = None
    r"""An array of entities relevant to the notification"""
