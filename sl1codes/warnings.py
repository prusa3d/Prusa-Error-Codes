# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

"""
SL1 Warning codes


Warning identification codes

TODO: @!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!
TODO: Big fat WARNING, these codes are not finalized. Do not copy numbers, use these values.
TODO: There are no guidelines for warnings, yet.
TODO: @!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!
"""

from enum import unique, Enum


def ranged_enum(minimum: int, maximum: int):
    """
    Class decorator to force enum values in defined range

    :param minimum: Minimal allowed value
    :param maximum: Maximal allowed value
    :return: Ranged enum decorator
    """

    def decor(enumeration):
        for name, member in enumeration.__members__.items():
            if member.value < minimum or member.value > maximum:
                raise ValueError(f"{enumeration} value {name} is out of permitted range ({minimum} to {maximum}).")
        return enumeration

    return decor


@unique
@ranged_enum(5000, 9999)
class WarningCode(Enum):
    """
    Warning identification codes

    TODO: @!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!
    TODO: Big fat WARNING, these codes are not finalized. Do not copy numbers, use these values.
    TODO: There are no guidelines for warnings, yet.
    TODO: @!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!
    """

    # Basic warning codes
    NONE = 5000
    UNKNOWN = 5001

    # Exposure warning codes
    EXPOSURE_AMBIENT_TOO_HOT = 6001
    EXPOSURE_AMBIENT_TOO_COLD = 6002
    EXPOSURE_PRINTING_DIRECTLY = 6003
    EXPOSURE_PRINTER_MODEL_MISMATCH = 6004
    EXPOSURE_RESIN_NOT_ENOUGH = 6005
    EXPOSURE_PROJECT_SETTINGS_MODIFIED = 6006
