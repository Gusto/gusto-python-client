"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto import models, utils
from gusto._hooks import HookContext
from gusto.types import OptionalNullable, UNSET
from gusto.utils import get_security_from_env
from typing import Any, List, Mapping, Optional, Union


class EmployeePaymentMethodSDK(BaseSDK):
    def update(
        self,
        *,
        employee_id: str,
        version: str,
        type_: models.PutV1EmployeesEmployeeIDPaymentMethodType,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        split_by: Optional[models.PutV1EmployeesEmployeeIDPaymentMethodSplitBy] = None,
        splits: Optional[
            Union[List[models.Splits], List[models.SplitsTypedDict]]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EmployeePaymentMethod:
        r"""Update an employee's payment method

        Updates an employee's payment method. Note that creating an employee
        bank account will also update the employee's payment method.

        scope: `employee_payment_methods:write`

        :param employee_id: The UUID of the employee
        :param version: The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.
        :param type: The payment method type. If type is Check, then split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param split_by: Describes how the payment will be split. If split_by is Percentage, then the split amounts must add up to exactly 100. If split_by is Amount, then the last split amount must be nil to capture the remainder.
        :param splits:
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

        request = models.PutV1EmployeesEmployeeIDPaymentMethodRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1EmployeesEmployeeIDPaymentMethodRequestBody(
                version=version,
                type=type_,
                split_by=split_by,
                splits=utils.get_pydantic_model(splits, Optional[List[models.Splits]]),
            ),
        )

        req = self._build_request(
            method="PUT",
            path="/v1/employees/{employee_id}/payment_method",
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
                models.PutV1EmployeesEmployeeIDPaymentMethodRequestBody,
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
                operation_id="put-v1-employees-employee_id-payment_method",
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
            return utils.unmarshal_json(http_res.text, models.EmployeePaymentMethod)
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

    async def update_async(
        self,
        *,
        employee_id: str,
        version: str,
        type_: models.PutV1EmployeesEmployeeIDPaymentMethodType,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        split_by: Optional[models.PutV1EmployeesEmployeeIDPaymentMethodSplitBy] = None,
        splits: Optional[
            Union[List[models.Splits], List[models.SplitsTypedDict]]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EmployeePaymentMethod:
        r"""Update an employee's payment method

        Updates an employee's payment method. Note that creating an employee
        bank account will also update the employee's payment method.

        scope: `employee_payment_methods:write`

        :param employee_id: The UUID of the employee
        :param version: The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.
        :param type: The payment method type. If type is Check, then split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param split_by: Describes how the payment will be split. If split_by is Percentage, then the split amounts must add up to exactly 100. If split_by is Amount, then the last split amount must be nil to capture the remainder.
        :param splits:
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

        request = models.PutV1EmployeesEmployeeIDPaymentMethodRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1EmployeesEmployeeIDPaymentMethodRequestBody(
                version=version,
                type=type_,
                split_by=split_by,
                splits=utils.get_pydantic_model(splits, Optional[List[models.Splits]]),
            ),
        )

        req = self._build_request_async(
            method="PUT",
            path="/v1/employees/{employee_id}/payment_method",
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
                models.PutV1EmployeesEmployeeIDPaymentMethodRequestBody,
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
                operation_id="put-v1-employees-employee_id-payment_method",
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
            return utils.unmarshal_json(http_res.text, models.EmployeePaymentMethod)
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
