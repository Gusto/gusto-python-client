"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto_embedded import models, utils
from gusto_embedded._hooks import HookContext
from gusto_embedded.types import OptionalNullable, UNSET
from gusto_embedded.utils import get_security_from_env
from typing import Mapping, Optional, Union


class HistoricalEmployees(BaseSDK):
    def update(
        self,
        *,
        company_uuid: str,
        historical_employee_uuid: str,
        version: str,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        ssn: str,
        work_address: Union[
            models.PutV1HistoricalEmployeesWorkAddress,
            models.PutV1HistoricalEmployeesWorkAddressTypedDict,
        ],
        home_address: Union[
            models.PutV1HistoricalEmployeesHomeAddress,
            models.PutV1HistoricalEmployeesHomeAddressTypedDict,
        ],
        termination: Union[
            models.PutV1HistoricalEmployeesTermination,
            models.PutV1HistoricalEmployeesTerminationTypedDict,
        ],
        job: Union[
            models.PutV1HistoricalEmployeesJob,
            models.PutV1HistoricalEmployeesJobTypedDict,
        ],
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        middle_initial: Optional[str] = None,
        preferred_first_name: Optional[str] = None,
        email: Optional[str] = None,
        employee_state_taxes: Optional[
            Union[
                models.PutV1HistoricalEmployeesEmployeeStateTaxes,
                models.PutV1HistoricalEmployeesEmployeeStateTaxesTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Employee:
        r"""Update a historical employee

        Update a historical employee, an employee that was previously dismissed from the company in the current year.

        scope: `employees:manage`

        :param company_uuid: The UUID of the company
        :param historical_employee_uuid: The UUID of the historical employee
        :param version: The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
        :param first_name:
        :param last_name:
        :param date_of_birth:
        :param ssn:
        :param work_address:
        :param home_address:
        :param termination:
        :param job:
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param middle_initial:
        :param preferred_first_name:
        :param email: Optional. If provided, the email address will be saved to the employee.
        :param employee_state_taxes:
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

        request = models.PutV1HistoricalEmployeesRequest(
            company_uuid=company_uuid,
            historical_employee_uuid=historical_employee_uuid,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1HistoricalEmployeesRequestBody(
                version=version,
                first_name=first_name,
                middle_initial=middle_initial,
                last_name=last_name,
                preferred_first_name=preferred_first_name,
                date_of_birth=date_of_birth,
                ssn=ssn,
                work_address=utils.get_pydantic_model(
                    work_address, models.PutV1HistoricalEmployeesWorkAddress
                ),
                home_address=utils.get_pydantic_model(
                    home_address, models.PutV1HistoricalEmployeesHomeAddress
                ),
                termination=utils.get_pydantic_model(
                    termination, models.PutV1HistoricalEmployeesTermination
                ),
                email=email,
                job=utils.get_pydantic_model(job, models.PutV1HistoricalEmployeesJob),
                employee_state_taxes=utils.get_pydantic_model(
                    employee_state_taxes,
                    Optional[models.PutV1HistoricalEmployeesEmployeeStateTaxes],
                ),
            ),
        )

        req = self._build_request(
            method="PUT",
            path="/v1/companies/{company_uuid}/historical_employees/{historical_employee_uuid}",
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
                models.PutV1HistoricalEmployeesRequestBody,
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
                operation_id="put-v1-historical_employees",
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
            return utils.unmarshal_json(http_res.text, models.Employee)
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

    async def update_async(
        self,
        *,
        company_uuid: str,
        historical_employee_uuid: str,
        version: str,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        ssn: str,
        work_address: Union[
            models.PutV1HistoricalEmployeesWorkAddress,
            models.PutV1HistoricalEmployeesWorkAddressTypedDict,
        ],
        home_address: Union[
            models.PutV1HistoricalEmployeesHomeAddress,
            models.PutV1HistoricalEmployeesHomeAddressTypedDict,
        ],
        termination: Union[
            models.PutV1HistoricalEmployeesTermination,
            models.PutV1HistoricalEmployeesTerminationTypedDict,
        ],
        job: Union[
            models.PutV1HistoricalEmployeesJob,
            models.PutV1HistoricalEmployeesJobTypedDict,
        ],
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        middle_initial: Optional[str] = None,
        preferred_first_name: Optional[str] = None,
        email: Optional[str] = None,
        employee_state_taxes: Optional[
            Union[
                models.PutV1HistoricalEmployeesEmployeeStateTaxes,
                models.PutV1HistoricalEmployeesEmployeeStateTaxesTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.Employee:
        r"""Update a historical employee

        Update a historical employee, an employee that was previously dismissed from the company in the current year.

        scope: `employees:manage`

        :param company_uuid: The UUID of the company
        :param historical_employee_uuid: The UUID of the historical employee
        :param version: The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
        :param first_name:
        :param last_name:
        :param date_of_birth:
        :param ssn:
        :param work_address:
        :param home_address:
        :param termination:
        :param job:
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param middle_initial:
        :param preferred_first_name:
        :param email: Optional. If provided, the email address will be saved to the employee.
        :param employee_state_taxes:
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

        request = models.PutV1HistoricalEmployeesRequest(
            company_uuid=company_uuid,
            historical_employee_uuid=historical_employee_uuid,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1HistoricalEmployeesRequestBody(
                version=version,
                first_name=first_name,
                middle_initial=middle_initial,
                last_name=last_name,
                preferred_first_name=preferred_first_name,
                date_of_birth=date_of_birth,
                ssn=ssn,
                work_address=utils.get_pydantic_model(
                    work_address, models.PutV1HistoricalEmployeesWorkAddress
                ),
                home_address=utils.get_pydantic_model(
                    home_address, models.PutV1HistoricalEmployeesHomeAddress
                ),
                termination=utils.get_pydantic_model(
                    termination, models.PutV1HistoricalEmployeesTermination
                ),
                email=email,
                job=utils.get_pydantic_model(job, models.PutV1HistoricalEmployeesJob),
                employee_state_taxes=utils.get_pydantic_model(
                    employee_state_taxes,
                    Optional[models.PutV1HistoricalEmployeesEmployeeStateTaxes],
                ),
            ),
        )

        req = self._build_request_async(
            method="PUT",
            path="/v1/companies/{company_uuid}/historical_employees/{historical_employee_uuid}",
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
                models.PutV1HistoricalEmployeesRequestBody,
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
                operation_id="put-v1-historical_employees",
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
            return utils.unmarshal_json(http_res.text, models.Employee)
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
