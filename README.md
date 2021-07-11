# jetblack-asgi-typing

Just the types for ASGI.

Taken from [asgiref](https://github.com/django/asgiref)
and [hypercorn](https://gitlab.com/pgjones/hypercorn).

## Installation

From `pypi.org`:

```bash
pip install jetblack-asgi-typing
```

## Usage

```python

from asgi_typing import (
    Scope,
    ASGIReceiveCallable,
    ASGISendCallable
)

async def app(
        scope: Scope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable
) -> None:
    # Implement your ASGI application here.
    pass
```
