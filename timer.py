# Credit: https://stackoverflow.com/questions/45419723/python-timer-with-asyncio-coroutine

import asyncio

class Timer:
    def __init__(self, timeout, callback):
        print(f"Timer started for {timeout}.")
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.create_task(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    def cancel(self):
        self._task.cancel()