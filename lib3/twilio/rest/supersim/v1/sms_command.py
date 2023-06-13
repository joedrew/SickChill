r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SmsCommandInstance(InstanceResource):
    class Direction(object):
        TO_SIM = "to_sim"
        FROM_SIM = "from_sim"

    class Status(object):
        QUEUED = "queued"
        SENT = "sent"
        DELIVERED = "delivered"
        RECEIVED = "received"
        FAILED = "failed"

    """
    :ivar sid: The unique string that we created to identify the SMS Command resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SMS Command resource.
    :ivar sim_sid: The SID of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) that this SMS Command was sent to or from.
    :ivar payload: The message body of the SMS Command sent to or from the SIM. For text mode messages, this can be up to 160 characters.
    :ivar status: 
    :ivar direction: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the SMS Command resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sim_sid: Optional[str] = payload.get("sim_sid")
        self.payload: Optional[str] = payload.get("payload")
        self.status: Optional["SmsCommandInstance.Status"] = payload.get("status")
        self.direction: Optional["SmsCommandInstance.Direction"] = payload.get(
            "direction"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[SmsCommandContext] = None

    @property
    def _proxy(self) -> "SmsCommandContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SmsCommandContext for this SmsCommandInstance
        """
        if self._context is None:
            self._context = SmsCommandContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "SmsCommandInstance":
        """
        Fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SmsCommandInstance":
        """
        Asynchronous coroutine to fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SmsCommandInstance {}>".format(context)


class SmsCommandContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the SmsCommandContext

        :param version: Version that contains the resource
        :param sid: The SID of the SMS Command resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/SmsCommands/{sid}".format(**self._solution)

    def fetch(self) -> SmsCommandInstance:
        """
        Fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SmsCommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SmsCommandInstance:
        """
        Asynchronous coroutine to fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SmsCommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SmsCommandContext {}>".format(context)


class SmsCommandPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> SmsCommandInstance:
        """
        Build an instance of SmsCommandInstance

        :param payload: Payload response from the API
        """
        return SmsCommandInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.SmsCommandPage>"


class SmsCommandList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SmsCommandList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/SmsCommands"

    def create(
        self,
        sim: str,
        payload: str,
        callback_method: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
    ) -> SmsCommandInstance:
        """
        Create the SmsCommandInstance

        :param sim: The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the SMS Command to.
        :param payload: The message body of the SMS Command.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param callback_url: The URL we should call using the `callback_method` after we have sent the command.

        :returns: The created SmsCommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Payload": payload,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SmsCommandInstance(self._version, payload)

    async def create_async(
        self,
        sim: str,
        payload: str,
        callback_method: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
    ) -> SmsCommandInstance:
        """
        Asynchronously create the SmsCommandInstance

        :param sim: The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the SMS Command to.
        :param payload: The message body of the SMS Command.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param callback_url: The URL we should call using the `callback_method` after we have sent the command.

        :returns: The created SmsCommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Payload": payload,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SmsCommandInstance(self._version, payload)

    def stream(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["SmsCommandInstance.Status", object] = values.unset,
        direction: Union["SmsCommandInstance.Direction", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SmsCommandInstance]:
        """
        Streams SmsCommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param &quot;SmsCommandInstance.Status&quot; status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param &quot;SmsCommandInstance.Direction&quot; direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim, status=status, direction=direction, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["SmsCommandInstance.Status", object] = values.unset,
        direction: Union["SmsCommandInstance.Direction", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SmsCommandInstance]:
        """
        Asynchronously streams SmsCommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param &quot;SmsCommandInstance.Status&quot; status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param &quot;SmsCommandInstance.Direction&quot; direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            sim=sim, status=status, direction=direction, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["SmsCommandInstance.Status", object] = values.unset,
        direction: Union["SmsCommandInstance.Direction", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SmsCommandInstance]:
        """
        Lists SmsCommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param &quot;SmsCommandInstance.Status&quot; status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param &quot;SmsCommandInstance.Direction&quot; direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                sim=sim,
                status=status,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["SmsCommandInstance.Status", object] = values.unset,
        direction: Union["SmsCommandInstance.Direction", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SmsCommandInstance]:
        """
        Asynchronously lists SmsCommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param &quot;SmsCommandInstance.Status&quot; status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param &quot;SmsCommandInstance.Direction&quot; direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                sim=sim,
                status=status,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["SmsCommandInstance.Status", object] = values.unset,
        direction: Union["SmsCommandInstance.Direction", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SmsCommandPage:
        """
        Retrieve a single page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SmsCommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SmsCommandPage(self._version, response)

    async def page_async(
        self,
        sim: Union[str, object] = values.unset,
        status: Union["SmsCommandInstance.Status", object] = values.unset,
        direction: Union["SmsCommandInstance.Direction", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SmsCommandPage:
        """
        Asynchronously retrieve a single page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SmsCommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SmsCommandPage(self._version, response)

    def get_page(self, target_url: str) -> SmsCommandPage:
        """
        Retrieve a specific page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SmsCommandInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SmsCommandPage(self._version, response)

    async def get_page_async(self, target_url: str) -> SmsCommandPage:
        """
        Asynchronously retrieve a specific page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SmsCommandInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SmsCommandPage(self._version, response)

    def get(self, sid: str) -> SmsCommandContext:
        """
        Constructs a SmsCommandContext

        :param sid: The SID of the SMS Command resource to fetch.
        """
        return SmsCommandContext(self._version, sid=sid)

    def __call__(self, sid: str) -> SmsCommandContext:
        """
        Constructs a SmsCommandContext

        :param sid: The SID of the SMS Command resource to fetch.
        """
        return SmsCommandContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.SmsCommandList>"
