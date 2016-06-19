import brood
from unittest import mock


def mock_coro():
    """create a mock coroutine"""
    async def _mock_coro(*args, **kwargs): return
    return mock.Mock(wraps=_mock_coro)


class SimpleAgent(brood.Agent):
    state_vars = ['sup', 'huh']

    def init(self, *args, **kwargs):
        self._counter = 0

    @brood.expose
    def what(self):
        return 'what'

    @brood.expose
    def counter(self):
        return self._counter

    async def decide(self):
        self._counter += 1
