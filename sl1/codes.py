# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

"""
SL1 error codes

Warning: The codes has not yet been officially approved.
"""


from shared.codes import Code, Category, unique_codes, Codes, Printer


@unique_codes
class Sl1Codes(Codes):
    """
    Error, exception and warning identification codes
    """

    PRINTER = Printer.SL1

    # Mechanical
    GENERAL_TILT_HOME_FAILURE = Code(PRINTER, Category.MECHANICAL, 1, None)
    GENERAL_TOWER_HOME_FAILURE = Code(PRINTER, Category.MECHANICAL, 2, None)
    EXPOSURE_TOWER_MOVE_FAILURE = Code(PRINTER, Category.MECHANICAL, 3, None)
    EXPOSURE_FAN_FAILURE = Code(PRINTER, Category.MECHANICAL, 6, None)
    EXPOSURE_RESIN_TOO_LOW = Code(PRINTER, Category.MECHANICAL, 8, None)
    EXPOSURE_RESIN_TOO_HIGH = Code(PRINTER, Category.MECHANICAL, 9, None)
    EXPOSURE_TILT_FAILURE = Code(PRINTER, Category.MECHANICAL, 10, None)
    EXPOSURE_TOWER_FAILURE = Code(PRINTER, Category.MECHANICAL, 12, None)
    GENERAL_NOT_MECHANICALLY_CALIBRATED = Code(PRINTER, Category.MECHANICAL, 13, None)

    # Temperature
    EXPOSURE_TEMP_SENSOR_FAILURE = Code(PRINTER, Category.TEMPERATURE, 5, None)

    # Connectivity
    GENERAL_FAILED_TO_MQTT_SEND = Code(PRINTER, Category.CONNECTIVITY, 1, "Cannot send factory config to MQTT!")
    GENERAL_NOT_CONNECTED_TO_NETWORK = Code(PRINTER, Category.CONNECTIVITY, 2, None)
    GENERAL_CONNECTION_FAILED = Code(PRINTER, Category.CONNECTIVITY, 3, None)
    GENERAL_DOWNLOAD_FAILED = Code(PRINTER, Category.CONNECTIVITY, 4, None)

    # Electrical
    GENERAL_MOTION_CONTROLLER_EXCEPTION = Code(PRINTER, Category.ELECTRICAL, 6, None)
    EXPOSURE_RESIN_SENSOR_FAILURE = Code(PRINTER, Category.ELECTRICAL, 7, None)
    GENERAL_NOT_UV_CALIBRATED = Code(PRINTER, Category.ELECTRICAL, 8, None)

    # System
    NONE = Code(PRINTER, Category.SYSTEM, 0, "No problem")
    UNKNOWN = Code(PRINTER, Category.SYSTEM, 1, "An unknown error has occurred")
    EXPOSURE_PROJECT_FAILURE = Code(PRINTER, Category.SYSTEM, 4, None)
    GENERAL_CONFIG_EXCEPTION = Code(PRINTER, Category.SYSTEM, 5, "Failed to read configuration file")
    GENERAL_NOT_AVAILABLE_IN_STATE = Code(PRINTER, Category.SYSTEM, 6, None)
    GENERAL_DBUS_MAPPING_EXCEPTION = Code(PRINTER, Category.SYSTEM, 7, None)
    GENERAL_REPRINT_WITHOUT_HISTORY = Code(PRINTER, Category.SYSTEM, 8, None)
    GENERAL_MISSING_WIZARD_DATA = Code(PRINTER, Category.SYSTEM, 9, "The wizard did not finish successfully!")
    GENERAL_MISSING_CALIBRATION_DATA = Code(
        PRINTER, Category.SYSTEM, 10, "The calibration did not finish successfully!"
    )
    GENERAL_MISSING_UVCALIBRATION_DATA = Code(
        PRINTER, Category.SYSTEM, 11, "The automatic UV LED calibration did not finish successfully!"
    )
    GENERAL_MISSING_UVPWM_SETTINGS = Code(PRINTER, Category.SYSTEM, 12, None)
    GENERAL_FAILED_UPDATE_CHANNEL_SET = Code(PRINTER, Category.SYSTEM, 13, "Cannot set update channel")
    GENERAL_FAILED_UPDATE_CHANNEL_GET = Code(PRINTER, Category.SYSTEM, 14, None)
    EXPOSURE_WARNING_ESCALATION = Code(PRINTER, Category.SYSTEM, 15, None)
    GENERAL_NOT_ENOUGH_INTERNAL_SPACE = Code(PRINTER, Category.SYSTEM, 16, None)
    GENERAL_ADMIN_NOT_AVAILABLE = Code(PRINTER, Category.SYSTEM, 17, None)
    GENERAL_FILE_NOT_FOUND = Code(PRINTER, Category.SYSTEM, 18, "Cannot find a file!")
    GENERAL_INVALID_EXTENSION = Code(PRINTER, Category.SYSTEM, 19, "File has an invalid extension!")
    GENERAL_FILE_ALREADY_EXISTS = Code(PRINTER, Category.SYSTEM, 20, "File already exists!")
    GENERAL_INVALID_PROJECT = Code(PRINTER, Category.SYSTEM, 21, "The project file is invalid!")

    # Warnings
    NONE_WARNING = Code(PRINTER, Category.WARNINGS, 0, "No warning")
    UNKNOWN_WARNING = Code(PRINTER, Category.WARNINGS, 1, "Unknown warning")
    EXPOSURE_AMBIENT_TOO_HOT_WARNING = Code(PRINTER, Category.WARNINGS, 2, None)
    EXPOSURE_AMBIENT_TOO_COLD_WARNING = Code(PRINTER, Category.WARNINGS, 3, None)
    EXPOSURE_PRINTING_DIRECTLY_WARNING = Code(PRINTER, Category.WARNINGS, 4, None)
    EXPOSURE_PRINTER_MODEL_MISMATCH_WARNING = Code(PRINTER, Category.WARNINGS, 5, None)
    EXPOSURE_RESIN_NOT_ENOUGH_WARNING = Code(PRINTER, Category.WARNINGS, 6, None)
    EXPOSURE_PROJECT_SETTINGS_MODIFIED_WARNING = Code(PRINTER, Category.WARNINGS, 7, None)

    @classmethod
    def get(cls, code: str):
        """
        Get Code by its number

        UNKNOWN Code is received on unknown code number

        :param code: Code number
        :return: Code instance
        """
        try:
            return super().get(code)
        except KeyError:
            return cls.UNKNOWN
