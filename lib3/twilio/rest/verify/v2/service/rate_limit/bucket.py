r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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


class BucketInstance(InstanceResource):

    """
    :ivar sid: A 34 character string that uniquely identifies this Bucket.
    :ivar rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Rate Limit resource.
    :ivar max: Maximum number of requests permitted in during the interval.
    :ivar interval: Number of seconds that the rate limit will be enforced over.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        rate_limit_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.rate_limit_sid: Optional[str] = payload.get("rate_limit_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.max: Optional[int] = deserialize.integer(payload.get("max"))
        self.interval: Optional[int] = deserialize.integer(payload.get("interval"))
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "rate_limit_sid": rate_limit_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[BucketContext] = None

    @property
    def _proxy(self) -> "BucketContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BucketContext for this BucketInstance
        """
        if self._context is None:
            self._context = BucketContext(
                self._version,
                service_sid=self._solution["service_sid"],
                rate_limit_sid=self._solution["rate_limit_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the BucketInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BucketInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "BucketInstance":
        """
        Fetch the BucketInstance


        :returns: The fetched BucketInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BucketInstance":
        """
        Asynchronous coroutine to fetch the BucketInstance


        :returns: The fetched BucketInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        max: Union[int, object] = values.unset,
        interval: Union[int, object] = values.unset,
    ) -> "BucketInstance":
        """
        Update the BucketInstance

        :param max: Maximum number of requests permitted in during the interval.
        :param interval: Number of seconds that the rate limit will be enforced over.

        :returns: The updated BucketInstance
        """
        return self._proxy.update(
            max=max,
            interval=interval,
        )

    async def update_async(
        self,
        max: Union[int, object] = values.unset,
        interval: Union[int, object] = values.unset,
    ) -> "BucketInstance":
        """
        Asynchronous coroutine to update the BucketInstance

        :param max: Maximum number of requests permitted in during the interval.
        :param interval: Number of seconds that the rate limit will be enforced over.

        :returns: The updated BucketInstance
        """
        return await self._proxy.update_async(
            max=max,
            interval=interval,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.BucketInstance {}>".format(context)


class BucketContext(InstanceContext):
    def __init__(
        self, version: Version, service_sid: str, rate_limit_sid: str, sid: str
    ):
        """
        Initialize the BucketContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
        :param rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
        :param sid: A 34 character string that uniquely identifies this Bucket.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "rate_limit_sid": rate_limit_sid,
            "sid": sid,
        }
        self._uri = (
            "/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the BucketInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BucketInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> BucketInstance:
        """
        Fetch the BucketInstance


        :returns: The fetched BucketInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> BucketInstance:
        """
        Asynchronous coroutine to fetch the BucketInstance


        :returns: The fetched BucketInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        max: Union[int, object] = values.unset,
        interval: Union[int, object] = values.unset,
    ) -> BucketInstance:
        """
        Update the BucketInstance

        :param max: Maximum number of requests permitted in during the interval.
        :param interval: Number of seconds that the rate limit will be enforced over.

        :returns: The updated BucketInstance
        """
        data = values.of(
            {
                "Max": max,
                "Interval": interval,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        max: Union[int, object] = values.unset,
        interval: Union[int, object] = values.unset,
    ) -> BucketInstance:
        """
        Asynchronous coroutine to update the BucketInstance

        :param max: Maximum number of requests permitted in during the interval.
        :param interval: Number of seconds that the rate limit will be enforced over.

        :returns: The updated BucketInstance
        """
        data = values.of(
            {
                "Max": max,
                "Interval": interval,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.BucketContext {}>".format(context)


class BucketPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> BucketInstance:
        """
        Build an instance of BucketInstance

        :param payload: Payload response from the API
        """
        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.BucketPage>"


class BucketList(ListResource):
    def __init__(self, version: Version, service_sid: str, rate_limit_sid: str):
        """
        Initialize the BucketList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
        :param rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "rate_limit_sid": rate_limit_sid,
        }
        self._uri = (
            "/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets".format(
                **self._solution
            )
        )

    def create(self, max: int, interval: int) -> BucketInstance:
        """
        Create the BucketInstance

        :param max: Maximum number of requests permitted in during the interval.
        :param interval: Number of seconds that the rate limit will be enforced over.

        :returns: The created BucketInstance
        """
        data = values.of(
            {
                "Max": max,
                "Interval": interval,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
        )

    async def create_async(self, max: int, interval: int) -> BucketInstance:
        """
        Asynchronously create the BucketInstance

        :param max: Maximum number of requests permitted in during the interval.
        :param interval: Number of seconds that the rate limit will be enforced over.

        :returns: The created BucketInstance
        """
        data = values.of(
            {
                "Max": max,
                "Interval": interval,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[BucketInstance]:
        """
        Streams BucketInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[BucketInstance]:
        """
        Asynchronously streams BucketInstance records from the API as a generator stream.
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
    ) -> List[BucketInstance]:
        """
        Lists BucketInstance records from the API as a list.
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
    ) -> List[BucketInstance]:
        """
        Asynchronously lists BucketInstance records from the API as a list.
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
    ) -> BucketPage:
        """
        Retrieve a single page of BucketInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BucketInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return BucketPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BucketPage:
        """
        Asynchronously retrieve a single page of BucketInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BucketInstance
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
        return BucketPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> BucketPage:
        """
        Retrieve a specific page of BucketInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BucketInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BucketPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> BucketPage:
        """
        Asynchronously retrieve a specific page of BucketInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BucketInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BucketPage(self._version, response, self._solution)

    def get(self, sid: str) -> BucketContext:
        """
        Constructs a BucketContext

        :param sid: A 34 character string that uniquely identifies this Bucket.
        """
        return BucketContext(
            self._version,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> BucketContext:
        """
        Constructs a BucketContext

        :param sid: A 34 character string that uniquely identifies this Bucket.
        """
        return BucketContext(
            self._version,
            service_sid=self._solution["service_sid"],
            rate_limit_sid=self._solution["rate_limit_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.BucketList>"
