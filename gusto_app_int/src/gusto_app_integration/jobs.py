"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto_app_integration import models, utils
from gusto_app_integration._hooks import HookContext
from gusto_app_integration.types import OptionalNullable, UNSET
from typing import Any, List, Mapping, Optional, Union


class Jobs(BaseSDK):
    def create(
        self,
        *,
        employee_id: str,
        title: str,
        hire_date: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        two_percent_shareholder: Optional[bool] = None,
        state_wc_covered: OptionalNullable[bool] = UNSET,
        state_wc_class_code: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Job:
        r"""Create a job

        Create a job.

        scope: `jobs:write`

        :param employee_id: The UUID of the employee
        :param title: The job title
        :param hire_date: The date when the employee was hired or rehired for the job.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param two_percent_shareholder: Whether the employee owns at least 2% of the company.
        :param state_wc_covered: Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).
        :param state_wc_class_code: The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.
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

        request = models.PostV1JobsJobIDRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostV1JobsJobIDRequestBody(
                title=title,
                hire_date=hire_date,
                two_percent_shareholder=two_percent_shareholder,
                state_wc_covered=state_wc_covered,
                state_wc_class_code=state_wc_class_code,
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/employees/{employee_id}/jobs",
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
                models.PostV1JobsJobIDRequestBody,
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
                operation_id="post-v1-jobs-job_id",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Job)
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

    async def create_async(
        self,
        *,
        employee_id: str,
        title: str,
        hire_date: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        two_percent_shareholder: Optional[bool] = None,
        state_wc_covered: OptionalNullable[bool] = UNSET,
        state_wc_class_code: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Job:
        r"""Create a job

        Create a job.

        scope: `jobs:write`

        :param employee_id: The UUID of the employee
        :param title: The job title
        :param hire_date: The date when the employee was hired or rehired for the job.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param two_percent_shareholder: Whether the employee owns at least 2% of the company.
        :param state_wc_covered: Whether this job is eligible for workers' compensation coverage in the state of Washington (WA).
        :param state_wc_class_code: The risk class code for workers' compensation in Washington state. Please visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more.
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

        request = models.PostV1JobsJobIDRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostV1JobsJobIDRequestBody(
                title=title,
                hire_date=hire_date,
                two_percent_shareholder=two_percent_shareholder,
                state_wc_covered=state_wc_covered,
                state_wc_class_code=state_wc_class_code,
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/employees/{employee_id}/jobs",
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
                models.PostV1JobsJobIDRequestBody,
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
                operation_id="post-v1-jobs-job_id",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Job)
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

    def create_compensation(
        self,
        *,
        job_id: str,
        payment_unit: models.PostV1CompensationsCompensationIDPaymentUnit,
        flsa_status: models.FlsaStatusType,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        rate: Optional[str] = None,
        effective_date: Optional[str] = None,
        adjust_for_minimum_wage: Optional[bool] = None,
        minimum_wages: Optional[
            Union[
                List[models.PostV1CompensationsCompensationIDMinimumWages],
                List[models.PostV1CompensationsCompensationIDMinimumWagesTypedDict],
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Compensation:
        r"""Create a compensation

        Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

        scope: `jobs:write`

        :param job_id: The UUID of the job
        :param payment_unit: The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.
        :param flsa_status: The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param rate: The dollar amount paid per payment unit.
        :param effective_date: The date when the compensation takes effect.
        :param adjust_for_minimum_wage: Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees.
        :param minimum_wages:
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

        request = models.PostV1CompensationsCompensationIDRequest(
            job_id=job_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostV1CompensationsCompensationIDRequestBody(
                rate=rate,
                payment_unit=payment_unit,
                effective_date=effective_date,
                flsa_status=flsa_status,
                adjust_for_minimum_wage=adjust_for_minimum_wage,
                minimum_wages=utils.get_pydantic_model(
                    minimum_wages,
                    Optional[
                        List[models.PostV1CompensationsCompensationIDMinimumWages]
                    ],
                ),
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/jobs/{job_id}/compensations",
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
                models.PostV1CompensationsCompensationIDRequestBody,
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
                operation_id="post-v1-compensations-compensation_id",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Compensation)
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

    async def create_compensation_async(
        self,
        *,
        job_id: str,
        payment_unit: models.PostV1CompensationsCompensationIDPaymentUnit,
        flsa_status: models.FlsaStatusType,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        rate: Optional[str] = None,
        effective_date: Optional[str] = None,
        adjust_for_minimum_wage: Optional[bool] = None,
        minimum_wages: Optional[
            Union[
                List[models.PostV1CompensationsCompensationIDMinimumWages],
                List[models.PostV1CompensationsCompensationIDMinimumWagesTypedDict],
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Compensation:
        r"""Create a compensation

        Compensations contain information on how much is paid out for a job. Jobs may have many compensations, but only one that is active. The current compensation is the one with the most recent `effective_date`.

        scope: `jobs:write`

        :param job_id: The UUID of the job
        :param payment_unit: The unit accompanying the compensation rate. If the employee is an owner, rate should be 'Paycheck'.
        :param flsa_status: The FLSA status for this compensation. Salaried ('Exempt') employees are paid a fixed salary every pay period. Salaried with overtime ('Salaried Nonexempt') employees are paid a fixed salary every pay period, and receive overtime pay when applicable. Hourly ('Nonexempt') employees are paid for the hours they work, and receive overtime pay when applicable. Commissioned employees ('Commission Only Exempt') earn wages based only on commission. Commissioned with overtime ('Commission Only Nonexempt') earn wages based on commission, and receive overtime pay when applicable. Owners ('Owner') are employees that own at least twenty percent of the company.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param rate: The dollar amount paid per payment unit.
        :param effective_date: The date when the compensation takes effect.
        :param adjust_for_minimum_wage: Determines whether the compensation should be adjusted for minimum wage. Only applies to Nonexempt employees.
        :param minimum_wages:
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

        request = models.PostV1CompensationsCompensationIDRequest(
            job_id=job_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostV1CompensationsCompensationIDRequestBody(
                rate=rate,
                payment_unit=payment_unit,
                effective_date=effective_date,
                flsa_status=flsa_status,
                adjust_for_minimum_wage=adjust_for_minimum_wage,
                minimum_wages=utils.get_pydantic_model(
                    minimum_wages,
                    Optional[
                        List[models.PostV1CompensationsCompensationIDMinimumWages]
                    ],
                ),
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/jobs/{job_id}/compensations",
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
                models.PostV1CompensationsCompensationIDRequestBody,
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
                operation_id="post-v1-compensations-compensation_id",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.Compensation)
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
