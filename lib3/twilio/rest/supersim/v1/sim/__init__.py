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
from twilio.rest.supersim.v1.sim.billing_period import BillingPeriodList
from twilio.rest.supersim.v1.sim.sim_ip_address import SimIpAddressList


class SimInstance(InstanceResource):
    class Status(object):
        NEW = "new"
        READY = "ready"
        ACTIVE = "active"
        INACTIVE = "inactive"
        SCHEDULED = "scheduled"

    class StatusUpdate(object):
        READY = "ready"
        ACTIVE = "active"
        INACTIVE = "inactive"

    """
    :ivar sid: The unique string that identifies the Sim resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Super SIM belongs to.
    :ivar iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with the SIM.
    :ivar status: 
    :ivar fleet_sid: The unique ID of the Fleet configured for this SIM.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Sim Resource.
    :ivar links: 
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.iccid: Optional[str] = payload.get("iccid")
        self.status: Optional["SimInstance.Status"] = payload.get("status")
        self.fleet_sid: Optional[str] = payload.get("fleet_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[SimContext] = None

    @property
    def _proxy(self) -> "SimContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SimContext for this SimInstance
        """
        if self._context is None:
            self._context = SimContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "SimInstance":
        """
        Fetch the SimInstance


        :returns: The fetched SimInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SimInstance":
        """
        Asynchronous coroutine to fetch the SimInstance


        :returns: The fetched SimInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        unique_name: Union[str, object] = values.unset,
        status: Union["SimInstance.StatusUpdate", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        account_sid: Union[str, object] = values.unset,
    ) -> "SimInstance":
        """
        Update the SimInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param status:
        :param fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned.
        :param callback_url: The URL we should call using the `callback_method` after an asynchronous update has finished.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param account_sid: The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.

        :returns: The updated SimInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            status=status,
            fleet=fleet,
            callback_url=callback_url,
            callback_method=callback_method,
            account_sid=account_sid,
        )

    async def update_async(
        self,
        unique_name: Union[str, object] = values.unset,
        status: Union["SimInstance.StatusUpdate", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        account_sid: Union[str, object] = values.unset,
    ) -> "SimInstance":
        """
        Asynchronous coroutine to update the SimInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param status:
        :param fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned.
        :param callback_url: The URL we should call using the `callback_method` after an asynchronous update has finished.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param account_sid: The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.

        :returns: The updated SimInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
            status=status,
            fleet=fleet,
            callback_url=callback_url,
            callback_method=callback_method,
            account_sid=account_sid,
        )

    @property
    def billing_periods(self) -> BillingPeriodList:
        """
        Access the billing_periods
        """
        return self._proxy.billing_periods

    @property
    def sim_ip_addresses(self) -> SimIpAddressList:
        """
        Access the sim_ip_addresses
        """
        return self._proxy.sim_ip_addresses

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SimInstance {}>".format(context)


class SimContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the SimContext

        :param version: Version that contains the resource
        :param sid: The SID of the Sim resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Sims/{sid}".format(**self._solution)

        self._billing_periods: Optional[BillingPeriodList] = None
        self._sim_ip_addresses: Optional[SimIpAddressList] = None

    def fetch(self) -> SimInstance:
        """
        Fetch the SimInstance


        :returns: The fetched SimInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SimInstance:
        """
        Asynchronous coroutine to fetch the SimInstance


        :returns: The fetched SimInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        unique_name: Union[str, object] = values.unset,
        status: Union["SimInstance.StatusUpdate", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        account_sid: Union[str, object] = values.unset,
    ) -> SimInstance:
        """
        Update the SimInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param status:
        :param fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned.
        :param callback_url: The URL we should call using the `callback_method` after an asynchronous update has finished.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param account_sid: The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.

        :returns: The updated SimInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "Status": status,
                "Fleet": fleet,
                "CallbackUrl": callback_url,
                "CallbackMethod": callback_method,
                "AccountSid": account_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        unique_name: Union[str, object] = values.unset,
        status: Union["SimInstance.StatusUpdate", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        account_sid: Union[str, object] = values.unset,
    ) -> SimInstance:
        """
        Asynchronous coroutine to update the SimInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param status:
        :param fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned.
        :param callback_url: The URL we should call using the `callback_method` after an asynchronous update has finished.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param account_sid: The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.

        :returns: The updated SimInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "Status": status,
                "Fleet": fleet,
                "CallbackUrl": callback_url,
                "CallbackMethod": callback_method,
                "AccountSid": account_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def billing_periods(self) -> BillingPeriodList:
        """
        Access the billing_periods
        """
        if self._billing_periods is None:
            self._billing_periods = BillingPeriodList(
                self._version,
                self._solution["sid"],
            )
        return self._billing_periods

    @property
    def sim_ip_addresses(self) -> SimIpAddressList:
        """
        Access the sim_ip_addresses
        """
        if self._sim_ip_addresses is None:
            self._sim_ip_addresses = SimIpAddressList(
                self._version,
                self._solution["sid"],
            )
        return self._sim_ip_addresses

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SimContext {}>".format(context)


class SimPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> SimInstance:
        """
        Build an instance of SimInstance

        :param payload: Payload response from the API
        """
        return SimInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.SimPage>"


class SimList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SimList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Sims"

    def create(self, iccid: str, registration_code: str) -> SimInstance:
        """
        Create the SimInstance

        :param iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account.
        :param registration_code: The 10-digit code required to claim the Super SIM for your Account.

        :returns: The created SimInstance
        """
        data = values.of(
            {
                "Iccid": iccid,
                "RegistrationCode": registration_code,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload)

    async def create_async(self, iccid: str, registration_code: str) -> SimInstance:
        """
        Asynchronously create the SimInstance

        :param iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account.
        :param registration_code: The 10-digit code required to claim the Super SIM for your Account.

        :returns: The created SimInstance
        """
        data = values.of(
            {
                "Iccid": iccid,
                "RegistrationCode": registration_code,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload)

    def stream(
        self,
        status: Union["SimInstance.Status", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SimInstance]:
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SimInstance.Status&quot; status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
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
            status=status, fleet=fleet, iccid=iccid, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status: Union["SimInstance.Status", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SimInstance]:
        """
        Asynchronously streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SimInstance.Status&quot; status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
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
            status=status, fleet=fleet, iccid=iccid, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status: Union["SimInstance.Status", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SimInstance]:
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SimInstance.Status&quot; status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
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
                status=status,
                fleet=fleet,
                iccid=iccid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status: Union["SimInstance.Status", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SimInstance]:
        """
        Asynchronously lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SimInstance.Status&quot; status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
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
                status=status,
                fleet=fleet,
                iccid=iccid,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        status: Union["SimInstance.Status", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SimPage:
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        """
        data = values.of(
            {
                "Status": status,
                "Fleet": fleet,
                "Iccid": iccid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SimPage(self._version, response)

    async def page_async(
        self,
        status: Union["SimInstance.Status", object] = values.unset,
        fleet: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SimPage:
        """
        Asynchronously retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        """
        data = values.of(
            {
                "Status": status,
                "Fleet": fleet,
                "Iccid": iccid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SimPage(self._version, response)

    def get_page(self, target_url: str) -> SimPage:
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SimPage(self._version, response)

    async def get_page_async(self, target_url: str) -> SimPage:
        """
        Asynchronously retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SimPage(self._version, response)

    def get(self, sid: str) -> SimContext:
        """
        Constructs a SimContext

        :param sid: The SID of the Sim resource to update.
        """
        return SimContext(self._version, sid=sid)

    def __call__(self, sid: str) -> SimContext:
        """
        Constructs a SimContext

        :param sid: The SID of the Sim resource to update.
        """
        return SimContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.SimList>"
