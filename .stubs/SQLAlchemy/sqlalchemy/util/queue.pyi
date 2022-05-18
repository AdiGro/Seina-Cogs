"""
MIT License

Copyright (c) 2022-present japandotorg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Any

class Empty(Exception): ...
class Full(Exception): ...

class Queue:
    mutex: Any
    not_empty: Any
    not_full: Any
    use_lifo: Any
    def __init__(self, maxsize: int = ..., use_lifo: bool = ...) -> None: ...
    def qsize(self): ...
    def empty(self): ...
    def full(self): ...
    def put(self, item, block: bool = ..., timeout: Any | None = ...) -> None: ...
    def put_nowait(self, item): ...
    def get(self, block: bool = ..., timeout: Any | None = ...): ...
    def get_nowait(self): ...

class AsyncAdaptedQueue:
    await_: Any
    use_lifo: Any
    maxsize: Any
    def __init__(self, maxsize: int = ..., use_lifo: bool = ...) -> None: ...
    def empty(self): ...
    def full(self): ...
    def qsize(self): ...
    def put_nowait(self, item): ...
    def put(self, item, block: bool = ..., timeout: Any | None = ...): ...
    def get_nowait(self): ...
    def get(self, block: bool = ..., timeout: Any | None = ...): ...

class FallbackAsyncAdaptedQueue(AsyncAdaptedQueue):
    await_: Any
