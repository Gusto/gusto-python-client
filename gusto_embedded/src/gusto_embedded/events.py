"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto_embedded import models, utils
from gusto_embedded._hooks import HookContext
from gusto_embedded.types import OptionalNullable, UNSET
from gusto_embedded.utils import get_security_from_env
from typing import List, Mapping, Optional, Union


class Events(BaseSDK):
    def get(
        self,
        *,
        security: Union[models.GetEventsSecurity, models.GetEventsSecurityTypedDict],
        starting_after_uuid: Optional[str] = None,
        resource_uuid: Optional[str] = None,
        limit: Optional[str] = None,
        event_type: Optional[str] = None,
        sort_order: Optional[models.SortOrder] = None,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.Event]:
        r"""Get all events

        Fetch all events, going back up to 30 days, that your partner application has the required scopes for. Note that a partner does NOT have to have verified webhook subscriptions in order to utilize this endpoint.

        > 📘 System Access Authentication
        >
        > This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access).

        scope: `events:read`

        :param security:
        :param starting_after_uuid: A cursor for pagination. Returns all events occuring after the specified UUID (exclusive). Events are sorted according to the provided sort_order param.
        :param resource_uuid: The UUID of the company. If not specified, will return all events for all companies.
        :param limit: Limits the number of objects returned in a single response, between 1 and 100. The default is 25
        :param event_type: A string containing the exact event name (e.g. `employee.created`), or use a wildcard match to filter for a group of events (e.g. `employee.*`, `*.created`, `notification.*.created` etc.)
        :param sort_order: A string indicating whether to sort resulting events in ascending (asc) or descending (desc) chronological order. Events are sorted by their `timestamp`. Defaults to asc if left empty.
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

        request = models.GetEventsRequest(
            starting_after_uuid=starting_after_uuid,
            resource_uuid=resource_uuid,
            limit=limit,
            event_type=event_type,
            sort_order=sort_order,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(security, models.GetEventsSecurity),
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
                operation_id="get-events",
                oauth2_scopes=[],
                security_source=get_security_from_env(security, models.Security),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, List[models.Event])
        if utils.match_response(http_res, "4XX", "*"):
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
        security: Union[models.GetEventsSecurity, models.GetEventsSecurityTypedDict],
        starting_after_uuid: Optional[str] = None,
        resource_uuid: Optional[str] = None,
        limit: Optional[str] = None,
        event_type: Optional[str] = None,
        sort_order: Optional[models.SortOrder] = None,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.Event]:
        r"""Get all events

        Fetch all events, going back up to 30 days, that your partner application has the required scopes for. Note that a partner does NOT have to have verified webhook subscriptions in order to utilize this endpoint.

        > 📘 System Access Authentication
        >
        > This endpoint uses the [Bearer Auth scheme with the system-level access token in the HTTP Authorization header](https://docs.gusto.com/embedded-payroll/docs/system-access).

        scope: `events:read`

        :param security:
        :param starting_after_uuid: A cursor for pagination. Returns all events occuring after the specified UUID (exclusive). Events are sorted according to the provided sort_order param.
        :param resource_uuid: The UUID of the company. If not specified, will return all events for all companies.
        :param limit: Limits the number of objects returned in a single response, between 1 and 100. The default is 25
        :param event_type: A string containing the exact event name (e.g. `employee.created`), or use a wildcard match to filter for a group of events (e.g. `employee.*`, `*.created`, `notification.*.created` etc.)
        :param sort_order: A string indicating whether to sort resulting events in ascending (asc) or descending (desc) chronological order. Events are sorted by their `timestamp`. Defaults to asc if left empty.
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

        request = models.GetEventsRequest(
            starting_after_uuid=starting_after_uuid,
            resource_uuid=resource_uuid,
            limit=limit,
            event_type=event_type,
            sort_order=sort_order,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/events",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=utils.get_pydantic_model(security, models.GetEventsSecurity),
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
                operation_id="get-events",
                oauth2_scopes=[],
                security_source=get_security_from_env(security, models.Security),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, List[models.Event])
        if utils.match_response(http_res, "4XX", "*"):
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
