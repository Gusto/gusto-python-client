"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .contractor_payment_summary import (
    ContractorPaymentSummary,
    ContractorPaymentSummaryTypedDict,
)
from .contractor_payment_summary_by_dates import (
    ContractorPaymentSummaryByDates,
    ContractorPaymentSummaryByDatesTypedDict,
)
from .versionheader import VersionHeader
from gusto_app_integration.types import BaseModel
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetV1CompaniesCompanyIDContractorPaymentsRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    start_date: str
    r"""The time period for which to retrieve contractor payments"""
    end_date: str
    r"""The time period for which to retrieve contractor payments. If left empty, defaults to today's date."""
    contractor_uuid: NotRequired[str]
    r"""The UUID of the contractor. When specified, will load all payments for that contractor."""
    group_by_date: NotRequired[bool]
    r"""Display contractor payments results group by check date if set to true."""
    page: NotRequired[int]
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""
    per: NotRequired[int]
    r"""Number of objects per page. For majority of endpoints will default to 25"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class GetV1CompaniesCompanyIDContractorPaymentsRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    start_date: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The time period for which to retrieve contractor payments"""

    end_date: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The time period for which to retrieve contractor payments. If left empty, defaults to today's date."""

    contractor_uuid: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The UUID of the contractor. When specified, will load all payments for that contractor."""

    group_by_date: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Display contractor payments results group by check date if set to true."""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The page that is requested. When unspecified, will load all objects unless endpoint forces pagination."""

    per: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Number of objects per page. For majority of endpoints will default to 25"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


GetV1CompaniesCompanyIDContractorPaymentsResponseBodyTypedDict = TypeAliasType(
    "GetV1CompaniesCompanyIDContractorPaymentsResponseBodyTypedDict",
    Union[ContractorPaymentSummaryTypedDict, ContractorPaymentSummaryByDatesTypedDict],
)
r"""A JSON object containing contractor payments information"""


GetV1CompaniesCompanyIDContractorPaymentsResponseBody = TypeAliasType(
    "GetV1CompaniesCompanyIDContractorPaymentsResponseBody",
    Union[ContractorPaymentSummary, ContractorPaymentSummaryByDates],
)
r"""A JSON object containing contractor payments information"""
