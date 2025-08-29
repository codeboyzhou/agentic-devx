import subprocess

from loguru import logger
from pydantic import BaseModel

from adx.common.consts import String


class CommandExecutionResult(BaseModel):
    code: int
    success: bool
    stdout: str
    stderr: str


def execute_command(commands: list[str]) -> CommandExecutionResult:
    """
    Execute a shell command and return the output.

    Args:
        commands (list[str]): The command to execute.

    Returns:
        CommandExecutionResult: The result of the command execution.
    """
    try:
        command = String.SPACE.join(commands)
        logger.debug(f"Executing shell command: {command}")

        result = subprocess.run(command, shell=True, text=True, check=True, capture_output=True)
        logger.debug(f"Command executed successfully: code={result.returncode}, stdout={String.NEWLINE}{result.stdout}")

        return CommandExecutionResult(
            code=result.returncode,
            success=result.returncode == 0,
            stdout=result.stdout.strip(),
            stderr=result.stderr.strip(),
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Command execution failed: code={e.returncode}, stderr={e.stderr}")
        return CommandExecutionResult(
            code=e.returncode,
            success=False,
            stdout=String.EMPTY,
            stderr=e.stderr.strip(),
        )
