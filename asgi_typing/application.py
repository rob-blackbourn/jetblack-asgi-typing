"""ASGI Application"""

from typing import Awaitable, Callable, Type, Union

from typing import Protocol

from .http import (
    HTTPScope,
    HTTPRequestEvent,
    HTTPDisconnectEvent,
    HTTPResponseStartEvent,
    HTTPResponseBodyEvent,
    HTTPServerPushEvent
)

from .websocket import (
    WebSocketScope,
    WebSocketConnectEvent,
    WebSocketReceiveEvent,
    WebSocketDisconnectEvent,
    WebSocketAcceptEvent,
    WebSocketSendEvent,
    WebSocketResponseStartEvent,
    WebSocketResponseBodyEvent,
    WebSocketCloseEvent
)

from .lifespan import (
    LifespanScope,
    LifespanStartupEvent,
    LifespanShutdownEvent,
    LifespanStartupCompleteEvent,
    LifespanStartupFailedEvent,
    LifespanShutdownCompleteEvent,
    LifespanShutdownFailedEvent
)

WWWScope = Union[HTTPScope, WebSocketScope]
Scope = Union[HTTPScope, WebSocketScope, LifespanScope]

ASGIReceiveEvent = Union[
    HTTPRequestEvent,
    HTTPDisconnectEvent,
    WebSocketConnectEvent,
    WebSocketReceiveEvent,
    WebSocketDisconnectEvent,
    LifespanStartupEvent,
    LifespanShutdownEvent,
]


ASGISendEvent = Union[
    HTTPResponseStartEvent,
    HTTPResponseBodyEvent,
    HTTPServerPushEvent,
    HTTPDisconnectEvent,
    WebSocketAcceptEvent,
    WebSocketSendEvent,
    WebSocketResponseStartEvent,
    WebSocketResponseBodyEvent,
    WebSocketCloseEvent,
    LifespanStartupCompleteEvent,
    LifespanStartupFailedEvent,
    LifespanShutdownCompleteEvent,
    LifespanShutdownFailedEvent,
]

ASGIReceiveCallable = Callable[[], Awaitable[ASGIReceiveEvent]]
ASGISendCallable = Callable[[ASGISendEvent], Awaitable[None]]


class ASGI2Protocol(Protocol):

    def __init__(self, scope: Scope) -> None:
        ...

    async def __call__(
        self, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None:
        ...


ASGI2Application = Type[ASGI2Protocol]
ASGI3Application = Callable[
    [
        Scope,
        ASGIReceiveCallable,
        ASGISendCallable,
    ],
    Awaitable[None],
]
ASGIApplication = Union[ASGI2Application, ASGI3Application]
