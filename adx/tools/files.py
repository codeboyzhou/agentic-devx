from adx.common import systems, terminal


def find(path: str, pattern: str) -> str:
    """
    Find files recursively in a directory that match a pattern.

    Args:
        path (str): The path to the directory to search.
        pattern (str): The pattern to match.

    Returns:
        str: The output of the find command.
    """
    if systems.is_windows():
        result = terminal.execute_command(["cmd.exe", "/c", "dir", path, "/s", "/b", "|", "findstr", "/i", pattern])
        return result.stdout if result.success else result.stderr
    else:
        result = terminal.execute_command(["find", path, "-name", pattern])
        return result.stdout if result.success else result.stderr


def read(path: str) -> str:
    """
    Read the content of a file.

    Args:
        path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(path, encoding="utf-8") as file:
        return file.read()
