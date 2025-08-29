from loguru import logger

from adx.common import terminal


def pip_list_outdated_packages() -> str:
    """
    List outdated packages using pip.

    Returns:
        str: The output of the pip list --outdated command.
    """
    result = terminal.execute_command(["pip", "list", "--outdated"])
    return result.stdout if result.success else result.stderr


def pip_upgrade_outdated_packages() -> str:
    """
    Upgrade outdated packages using pip.

    Returns:
        str: The output of the pip install --upgrade command.
    """
    list_outdated_packages = terminal.execute_command(["pip", "list", "--outdated"])

    if not list_outdated_packages.success:
        return list_outdated_packages.stderr

    if not list_outdated_packages.stdout:
        return "No outdated packages found."

    packages = list_outdated_packages.stdout.splitlines()[2:]
    success_packages = []
    failed_packages = []
    for package in packages:
        package_info = package.split()
        package_name = package_info[0]
        package_version = package_info[1]
        package_latest_version = package_info[2]

        upgrade_outdated_packages = terminal.execute_command(["pip", "install", "--upgrade", package_name])

        if upgrade_outdated_packages.success:
            success_packages.append(package_name)
            logger.info(f"Package {package_name} upgraded from {package_version} to {package_latest_version}")
        else:
            failed_packages.append(package_name)
            logger.error(f"Failed to upgrade package {package_name}: {upgrade_outdated_packages.stderr}")

    return f"Successfully upgraded {len(success_packages)} packages, failed to upgrade {len(failed_packages)} packages."
