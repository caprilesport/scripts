#!/usr/bin/env python3

import os
import sys
from pathlib import Path


def main() -> None:
    """Main Entry point of our script."""
    config_path = Path("~/.config/niri/config.kdl").expanduser()
    config, toggle_off_line_num = open_config(config_path)
    if toggle_off_line_num:
        toggle_on_off(toggle_off_line_num, config)
        write_config(config_path, config)
    else:
        sys.exit(1)


def open_config(path: Path) -> tuple[list[str], int | None]:
    """Opens and reads the niri config file config.kdl This function returns our
    configuration file as a tuple containing a list containing each line in the
    configuration and an int our line number that our inline comment toggleOffTouchpad
    is located at.

    :param path: The path to niri configuration file.
    :type path: Path
    :return: A tuple(list[str], int)
    :rtype: tuple[list[str], int | None]
    :raises FileNotFoundError: If the path does not exist.
    :raises ValueError: If config.kdl is not found.
    :raises PermissionError: If user lacks r/w/x permissions.
    """
    if not path.exists():
        raise FileNotFoundError(f"Config file not found at location: {path}")
    if not path.is_file():
        raise ValueError(f"File does not exist: {path}")
    if not os.access(path, os.R_OK):
        raise PermissionError(f"No read persmission: {path}")

    contents = []
    toggle_off_line_num = None
    with open(path, "r") as f:
        for line_num, line in enumerate(f):
            if "toggleOffTouchpad" in line:
                toggle_off_line_num = line_num
                contents.append(line)
            else:
                contents.append(line)
    return contents, toggle_off_line_num


def write_config(path: Path, config: list) -> None:
    """Write Config function rewrites our configuration file setting either toucpad off
    or // off.

    :param path: The path to niri configuration file.
    :type path: Path
    :param config: Our newly written configuration file.
    """
    with open(path, "w") as f:
        for line in config:
            f.write(line)


def toggle_on_off(line_num: int, contents: list) -> list:
    """Toggle function sets the touchpad setting in the niri configuration file to off
    or // off while keeping users indentation.

    :param line_num: line number of the setting identified by the inline comment.
    :type line_num: int
    :param contents: our configuration file as type list.
    :type contents: list
    :return: A list the modified configuration file.
    :rtype: list
    """
    toggle = contents[line_num]
    leading_spaces = len(toggle) - len(toggle.lstrip())
    indent = " " * leading_spaces
    if "// off // toggleOffTouchpad" in toggle:
        toggle = f"{indent}off // toggleOffTouchpad\n"
    else:
        toggle = f"{indent}// off // toggleOffTouchpad\n"

    contents[line_num] = toggle
    return contents


if __name__ == "__main__":
    main()
