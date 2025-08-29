import platform


def is_windows() -> bool:
    """
    Check if the current system is Windows.

    Returns:
        bool: True if the current system is Windows, False otherwise.
    """
    return platform.system().lower() == "windows"
