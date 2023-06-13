r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SyncListPermissionInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sync List Permission resource.
    :ivar service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with.
    :ivar list_sid: The SID of the Sync List to which the Permission applies.
    :ivar identity: The application-defined string that uniquely identifies the resource's User within the Service to an FPA token.
    :ivar read: Whether the identity can read the Sync List and its Items.
    :ivar write: Whether the identity can create, update, and delete Items in the Sync List.
    :ivar manage: Whether the identity can delete the Sync List.
    :ivar url: The absolute URL of the Sync List Permission resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        list_sid: str,
        identity: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.list_sid: Optional[str] = payload.get("list_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.read: Optional[bool] = payload.get("read")
        self.write: Optional[bool] = payload.get("write")
        self.manage: Optional[bool] = payload.get("manage")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "list_sid": list_sid,
            "identity": identity or self.identity,
        }
        self._context: Optional[SyncListPermissionContext] = None

    @property
    def _proxy(self) -> "SyncListPermissionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncListPermissionContext for this SyncListPermissionInstance
        """
        if self._context is None:
            self._context = SyncListPermissionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                list_sid=self._solution["list_sid"],
                identity=self._solution["identity"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the SyncListPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncListPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SyncListPermissionInstance":
        """
        Fetch the SyncListPermissionInstance


        :returns: The fetched SyncListPermissionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SyncListPermissionInstance":
        """
        Asynchronous coroutine to fetch the SyncListPermissionInstance


        :returns: The fetched SyncListPermissionInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, read: bool, write: bool, manage: bool
    ) -> "SyncListPermissionInstance":
        """
        Update the SyncListPermissionInstance

        :param read: Whether the identity can read the Sync List and its Items. Default value is `false`.
        :param write: Whether the identity can create, update, and delete Items in the Sync List. Default value is `false`.
        :param manage: Whether the identity can delete the Sync List. Default value is `false`.

        :returns: The updated SyncListPermissionInstance
        """
        return self._proxy.update(
            read=read,
            write=write,
            manage=manage,
        )

    async def update_async(
        self, read: bool, write: bool, manage: bool
    ) -> "SyncListPermissionInstance":
        """
        Asynchronous coroutine to update the SyncListPermissionInstance

        :param read: Whether the identity can read the Sync List and its Items. Default value is `false`.
        :param write: Whether the identity can create, update, and delete Items in the Sync List. Default value is `false`.
        :param manage: Whether the identity can delete the Sync List. Default value is `false`.

        :returns: The updated SyncListPermissionInstance
        """
        return await self._proxy.update_async(
            read=read,
            write=write,
            manage=manage,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.SyncListPermissionInstance {}>".format(context)


class SyncListPermissionContext(InstanceContext):
    def __init__(
        self, version: Version, service_sid: str, list_sid: str, identity: str
    ):
        """
        Initialize the SyncListPermissionContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to update.
        :param list_sid: The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List resource's `sid` or its `unique_name`.
        :param identity: The application-defined string that uniquely identifies the User's Sync List Permission resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "list_sid": list_sid,
            "identity": identity,
        }
        self._uri = (
            "/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the SyncListPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncListPermissionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SyncListPermissionInstance:
        """
        Fetch the SyncListPermissionInstance


        :returns: The fetched SyncListPermissionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            identity=self._solution["identity"],
        )

    async def fetch_async(self) -> SyncListPermissionInstance:
        """
        Asynchronous coroutine to fetch the SyncListPermissionInstance


        :returns: The fetched SyncListPermissionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            identity=self._solution["identity"],
        )

    def update(
        self, read: bool, write: bool, manage: bool
    ) -> SyncListPermissionInstance:
        """
        Update the SyncListPermissionInstance

        :param read: Whether the identity can read the Sync List and its Items. Default value is `false`.
        :param write: Whether the identity can create, update, and delete Items in the Sync List. Default value is `false`.
        :param manage: Whether the identity can delete the Sync List. Default value is `false`.

        :returns: The updated SyncListPermissionInstance
        """
        data = values.of(
            {
                "Read": read,
                "Write": write,
                "Manage": manage,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            identity=self._solution["identity"],
        )

    async def update_async(
        self, read: bool, write: bool, manage: bool
    ) -> SyncListPermissionInstance:
        """
        Asynchronous coroutine to update the SyncListPermissionInstance

        :param read: Whether the identity can read the Sync List and its Items. Default value is `false`.
        :param write: Whether the identity can create, update, and delete Items in the Sync List. Default value is `false`.
        :param manage: Whether the identity can delete the Sync List. Default value is `false`.

        :returns: The updated SyncListPermissionInstance
        """
        data = values.of(
            {
                "Read": read,
                "Write": write,
                "Manage": manage,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            identity=self._solution["identity"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.SyncListPermissionContext {}>".format(context)


class SyncListPermissionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> SyncListPermissionInstance:
        """
        Build an instance of SyncListPermissionInstance

        :param payload: Payload response from the API
        """
        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.SyncListPermissionPage>"


class SyncListPermissionList(ListResource):
    def __init__(self, version: Version, service_sid: str, list_sid: str):
        """
        Initialize the SyncListPermissionList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resources to read.
        :param list_sid: The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List resource's `sid` or its `unique_name`.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "list_sid": list_sid,
        }
        self._uri = "/Services/{service_sid}/Lists/{list_sid}/Permissions".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SyncListPermissionInstance]:
        """
        Streams SyncListPermissionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SyncListPermissionInstance]:
        """
        Asynchronously streams SyncListPermissionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SyncListPermissionInstance]:
        """
        Lists SyncListPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SyncListPermissionInstance]:
        """
        Asynchronously lists SyncListPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SyncListPermissionPage:
        """
        Retrieve a single page of SyncListPermissionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListPermissionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SyncListPermissionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SyncListPermissionPage:
        """
        Asynchronously retrieve a single page of SyncListPermissionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListPermissionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SyncListPermissionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SyncListPermissionPage:
        """
        Retrieve a specific page of SyncListPermissionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SyncListPermissionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncListPermissionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SyncListPermissionPage:
        """
        Asynchronously retrieve a specific page of SyncListPermissionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SyncListPermissionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncListPermissionPage(self._version, response, self._solution)

    def get(self, identity: str) -> SyncListPermissionContext:
        """
        Constructs a SyncListPermissionContext

        :param identity: The application-defined string that uniquely identifies the User's Sync List Permission resource to update.
        """
        return SyncListPermissionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            identity=identity,
        )

    def __call__(self, identity: str) -> SyncListPermissionContext:
        """
        Constructs a SyncListPermissionContext

        :param identity: The application-defined string that uniquely identifies the User's Sync List Permission resource to update.
        """
        return SyncListPermissionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            identity=identity,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.SyncListPermissionList>"
