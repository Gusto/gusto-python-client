"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from datetime import date
from gusto_embedded import models, utils
from gusto_embedded._hooks import HookContext
from gusto_embedded.types import OptionalNullable, UNSET
from gusto_embedded.utils import get_security_from_env
from typing import Any, List, Mapping, Optional


class Reports(BaseSDK):
    def create_custom(
        self,
        *,
        company_uuid: str,
        columns: List[models.Columns],
        groupings: List[models.Groupings],
        file_type: models.FileType,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        custom_name: Optional[str] = None,
        with_totals: Optional[bool] = False,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        dismissed_start_date: Optional[date] = None,
        dismissed_end_date: Optional[date] = None,
        payment_method: Optional[
            models.PostCompaniesCompanyUUIDReportsPaymentMethod
        ] = None,
        employment_type: Optional[models.EmploymentType] = None,
        employment_status: Optional[
            models.PostCompaniesCompanyUUIDReportsEmploymentStatus
        ] = None,
        employee_uuids: Optional[List[str]] = None,
        department_uuids: Optional[List[str]] = None,
        work_address_uuids: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CreateReport:
        r"""Create a custom report

        Create a custom report for a company. This endpoint initiates creating a custom report with custom columns, groupings, and filters. The `request_uuid` in the response can then be used to poll for the status and report URL upon completion using the report GET endpoint.

        scope: `company_reports:write`

        :param company_uuid: The UUID of the company
        :param columns: Columns to include in the report
        :param groupings: How to group the report
        :param file_type: The type of file to generate
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param custom_name: The title of the report
        :param with_totals: Whether to include subtotals and grand totals in the report
        :param start_date: Start date of data to filter by
        :param end_date: End date of data to filter by
        :param dismissed_start_date: Dismissed start date of employees to filter by
        :param dismissed_end_date: Dismissed end date of employees to filter by
        :param payment_method: Payment method to filter by
        :param employment_type: Employee employment type to filter by
        :param employment_status: Employee employment status to filter by
        :param employee_uuids: Employees to filter by
        :param department_uuids: Departments to filter by
        :param work_address_uuids: Work addresses to filter by
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.PostCompaniesCompanyUUIDReportsRequest(
            company_uuid=company_uuid,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostCompaniesCompanyUUIDReportsRequestBody(
                columns=columns,
                groupings=groupings,
                custom_name=custom_name,
                file_type=file_type,
                with_totals=with_totals,
                start_date=start_date,
                end_date=end_date,
                dismissed_start_date=dismissed_start_date,
                dismissed_end_date=dismissed_end_date,
                payment_method=payment_method,
                employment_type=employment_type,
                employment_status=employment_status,
                employee_uuids=employee_uuids,
                department_uuids=department_uuids,
                work_address_uuids=work_address_uuids,
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/companies/{company_uuid}/reports",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.PostCompaniesCompanyUUIDReportsRequestBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="post-companies-company_uuid-reports",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.CreateReport)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectData
            )
            raise models.UnprocessableEntityErrorObject(data=response_data)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_custom_async(
        self,
        *,
        company_uuid: str,
        columns: List[models.Columns],
        groupings: List[models.Groupings],
        file_type: models.FileType,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        custom_name: Optional[str] = None,
        with_totals: Optional[bool] = False,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        dismissed_start_date: Optional[date] = None,
        dismissed_end_date: Optional[date] = None,
        payment_method: Optional[
            models.PostCompaniesCompanyUUIDReportsPaymentMethod
        ] = None,
        employment_type: Optional[models.EmploymentType] = None,
        employment_status: Optional[
            models.PostCompaniesCompanyUUIDReportsEmploymentStatus
        ] = None,
        employee_uuids: Optional[List[str]] = None,
        department_uuids: Optional[List[str]] = None,
        work_address_uuids: Optional[List[str]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.CreateReport:
        r"""Create a custom report

        Create a custom report for a company. This endpoint initiates creating a custom report with custom columns, groupings, and filters. The `request_uuid` in the response can then be used to poll for the status and report URL upon completion using the report GET endpoint.

        scope: `company_reports:write`

        :param company_uuid: The UUID of the company
        :param columns: Columns to include in the report
        :param groupings: How to group the report
        :param file_type: The type of file to generate
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param custom_name: The title of the report
        :param with_totals: Whether to include subtotals and grand totals in the report
        :param start_date: Start date of data to filter by
        :param end_date: End date of data to filter by
        :param dismissed_start_date: Dismissed start date of employees to filter by
        :param dismissed_end_date: Dismissed end date of employees to filter by
        :param payment_method: Payment method to filter by
        :param employment_type: Employee employment type to filter by
        :param employment_status: Employee employment status to filter by
        :param employee_uuids: Employees to filter by
        :param department_uuids: Departments to filter by
        :param work_address_uuids: Work addresses to filter by
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.PostCompaniesCompanyUUIDReportsRequest(
            company_uuid=company_uuid,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostCompaniesCompanyUUIDReportsRequestBody(
                columns=columns,
                groupings=groupings,
                custom_name=custom_name,
                file_type=file_type,
                with_totals=with_totals,
                start_date=start_date,
                end_date=end_date,
                dismissed_start_date=dismissed_start_date,
                dismissed_end_date=dismissed_end_date,
                payment_method=payment_method,
                employment_type=employment_type,
                employment_status=employment_status,
                employee_uuids=employee_uuids,
                department_uuids=department_uuids,
                work_address_uuids=work_address_uuids,
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/companies/{company_uuid}/reports",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.PostCompaniesCompanyUUIDReportsRequestBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="post-companies-company_uuid-reports",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.CreateReport)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectData
            )
            raise models.UnprocessableEntityErrorObject(data=response_data)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get(
        self,
        *,
        report_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Report:
        r"""Get a report

        Get a company's report given the `request_uuid`. The response will include the report request's status and, if complete, the report URL.

        scope: `company_reports:read`

        :param report_uuid: The UUID of the report request
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetReportsReportUUIDRequest(
            report_uuid=report_uuid,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/reports/{report_uuid}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-reports-report_uuid",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Report)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_async(
        self,
        *,
        report_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Report:
        r"""Get a report

        Get a company's report given the `request_uuid`. The response will include the report request's status and, if complete, the report URL.

        scope: `company_reports:read`

        :param report_uuid: The UUID of the report request
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetReportsReportUUIDRequest(
            report_uuid=report_uuid,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/reports/{report_uuid}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-reports-report_uuid",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Report)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get_template(
        self,
        *,
        company_uuid: str,
        report_type: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ReportTemplate:
        r"""Get a report template

        Get a company's report template. The only supported report type is `payroll_journal`. The resulting columns and groupings from this endpoint can be used as a guidance to create the report using the POST create report endpoint.

        scope: `company_reports:write`

        :param company_uuid: The UUID of the company
        :param report_type: The report type
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetCompaniesCompanyUUIDReportTemplatesReportTypeRequest(
            company_uuid=company_uuid,
            report_type=report_type,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/companies/{company_uuid}/report_templates/{report_type}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-companies-company_uuid-report-templates-report_type",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.ReportTemplate)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_template_async(
        self,
        *,
        company_uuid: str,
        report_type: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ReportTemplate:
        r"""Get a report template

        Get a company's report template. The only supported report type is `payroll_journal`. The resulting columns and groupings from this endpoint can be used as a guidance to create the report using the POST create report endpoint.

        scope: `company_reports:write`

        :param company_uuid: The UUID of the company
        :param report_type: The report type
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetCompaniesCompanyUUIDReportTemplatesReportTypeRequest(
            company_uuid=company_uuid,
            report_type=report_type,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/companies/{company_uuid}/report_templates/{report_type}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-companies-company_uuid-report-templates-report_type",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.ReportTemplate)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
