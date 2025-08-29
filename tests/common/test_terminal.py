from adx.common import terminal
from adx.common.consts import String


def test_execute_command_success():
    result = terminal.execute_command(["echo", "hello"])
    assert result.success
    assert result.code == 0
    assert result.stdout == "hello"
    assert result.stderr == String.EMPTY

def test_execute_command_failure():
    result = terminal.execute_command(["A non-existent command"])
    assert not result.success
    assert result.code != 0
    assert result.stdout == String.EMPTY
    assert result.stderr != String.EMPTY
