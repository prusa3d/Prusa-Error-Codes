# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

"""
SL1 error codes

Warning: The codes has not yet been officially approved.
"""

from prusaerrors.shared.codes import Code, Category, unique_codes, Codes, Printer

try:
    _
except NameError:
    _ = lambda x: x


@unique_codes
class Sl1Codes(Codes):
    """
    Error, exception and warning identification codes
    """

    PRINTER = Printer.SL1

    # Mechanical
    TILT_HOME_FAILURE = Code(PRINTER, Category.MECHANICAL, 1, None, False)
    TOWER_HOME_FAILURE = Code(PRINTER, Category.MECHANICAL, 2, None, False)
    TOWER_MOVE_FAILURE = Code(PRINTER, Category.MECHANICAL, 3, None, False)
    FAN_FAILURE = Code(PRINTER, Category.MECHANICAL, 6, None, False)
    RESIN_TOO_LOW = Code(PRINTER, Category.MECHANICAL, 8, None, False)
    RESIN_TOO_HIGH = Code(PRINTER, Category.MECHANICAL, 9, None, False)
    NOT_MECHANICALLY_CALIBRATED = Code(PRINTER, Category.MECHANICAL, 13, None, False)
    TOWER_ENDSTOP_NOT_REACHED = Code(PRINTER, Category.MECHANICAL, 14, _("Failed to reach tower endstop"), False)
    TILT_ENDSTOP_NOT_REACHED = Code(PRINTER, Category.MECHANICAL, 15, _("Failed to reach tilt endstop"), False)
    TOWER_AXIS_CHECK_FAILED = Code(
        PRINTER,
        Category.MECHANICAL,
        18,
        _(
            "Tower axis check failed!\n\n"
            "Current position: %d nm\n\n"
            "Please check if the ballscrew can move smoothly in its entire range."
        ),
        False,
    )
    TILT_AXIS_CHECK_FAILED = Code(
        PRINTER,
        Category.MECHANICAL,
        19,
        _(
            "Tilt axis check failed!\n\n"
            "Current position: %d steps\n\n"
            "Please check if the tilt can move smoothly in its entire range."
        ),
        False
    )
    DISPLAY_TEST_FAILED = Code(PRINTER, Category.MECHANICAL, 20, _("Display test failed."), False)
    INVALID_TILT_ALIGN_POSITION = Code(PRINTER, Category.MECHANICAL, 21, _("Invalid tilt align position"), False)
    FAN_RPM_OUT_OF_TEST_RANGE = Code(PRINTER, Category.MECHANICAL, 22, _(
        "RPM of %(fan)s not in range!\n\n"
        "Please check if the fan is connected correctly.\n\n"
        "RPM data: %(rpm)s\n"
        "Average: %(avg)s\n"
        "Fan error: %(fanError)s"
    ), False)
    TOWER_BELOW_SURFACE = Code(PRINTER, Category.MECHANICAL, 23, _(
        "Tower not at the expected position.\n\n"
        "Is the platform and tank secured in correct position?\n\n"), False)

    # Temperature
    TEMP_SENSOR_FAILURE = Code(PRINTER, Category.TEMPERATURE, 5, None, False)
    UVLED_HEAT_SINK_FAILURE = Code(
        PRINTER, Category.TEMPERATURE, 6, _("UV LED overheating! Check proper heatsink installation."), False
    )

    # Connectivity
    FAILED_TO_MQTT_SEND = Code(PRINTER, Category.CONNECTIVITY, 1, _("Cannot send factory config to MQTT!"), False)
    NOT_CONNECTED_TO_NETWORK = Code(PRINTER, Category.CONNECTIVITY, 2, None, False)
    CONNECTION_FAILED = Code(PRINTER, Category.CONNECTIVITY, 3, None, False)
    DOWNLOAD_FAILED = Code(PRINTER, Category.CONNECTIVITY, 4, None, False)

    # Electrical
    MOTION_CONTROLLER_WRONG_REVISION = Code(
        PRINTER,
        Category.ELECTRICAL,
        1,
        _("Wrong revision of the motion controller. Please replace it or contact our support."),
        False,
    )
    MOTION_CONTROLLER_EXCEPTION = Code(PRINTER, Category.ELECTRICAL, 6, None, False)
    RESIN_SENSOR_FAILURE = Code(PRINTER, Category.ELECTRICAL, 7, None, False)
    NOT_UV_CALIBRATED = Code(PRINTER, Category.ELECTRICAL, 8, None, False)
    UVLED_VOLTAGE_DIFFER_TOO_MUCH = Code(PRINTER, Category.ELECTRICAL, 9,
                                         _("UV LED voltages differ too much. Possibly LED module is broken."), False)
    SOUND_TEST_FAILED = Code(PRINTER, Category.ELECTRICAL, 10, _("Speaker is broken"), False)

    # System
    NONE = Code(PRINTER, Category.SYSTEM, 0, _("No problem"), False)
    UNKNOWN = Code(
        PRINTER,
        Category.SYSTEM,
        1,
        _(
            "An unexpected error has occurred :-(.\n\n"
            "If the SL1 is printing, current job will be finished.\n\n"
            "You can turn the printer off by pressing the front power button.\n\n"
            "Please follow the instructions in Chapter 3.1 in the handbook to learn how to save a log file. "
            "Please send the log to us and help us improve the printer.\n\n"
            "Thank you!"
        ),
        False,
    )
    PROJECT_FAILURE = Code(PRINTER, Category.SYSTEM, 4, None, False)
    CONFIG_EXCEPTION = Code(PRINTER, Category.SYSTEM, 5, _("Failed to read configuration file"), False)
    NOT_AVAILABLE_IN_STATE = Code(PRINTER, Category.SYSTEM, 6, None, False)
    DBUS_MAPPING_EXCEPTION = Code(PRINTER, Category.SYSTEM, 7, None, False)
    REPRINT_WITHOUT_HISTORY = Code(PRINTER, Category.SYSTEM, 8, None, False)
    MISSING_WIZARD_DATA = Code(PRINTER, Category.SYSTEM, 9, _("The wizard did not finish successfully!"), False)
    MISSING_CALIBRATION_DATA = Code(
        PRINTER, Category.SYSTEM, 10, _("The calibration did not finish successfully!"), False
    )
    MISSING_UVCALIBRATION_DATA = Code(
        PRINTER, Category.SYSTEM, 11, _("The automatic UV LED calibration did not finish successfully!"), False
    )
    MISSING_UVPWM_SETTINGS = Code(PRINTER, Category.SYSTEM, 12, None, False)
    FAILED_UPDATE_CHANNEL_SET = Code(PRINTER, Category.SYSTEM, 13, _("Cannot set update channel"), False)
    FAILED_UPDATE_CHANNEL_GET = Code(PRINTER, Category.SYSTEM, 14, None, False)
    WARNING_ESCALATION = Code(PRINTER, Category.SYSTEM, 15, None, False)
    NOT_ENOUGH_INTERNAL_SPACE = Code(PRINTER, Category.SYSTEM, 16, None, False)
    ADMIN_NOT_AVAILABLE = Code(PRINTER, Category.SYSTEM, 17, None, False)
    FILE_NOT_FOUND = Code(PRINTER, Category.SYSTEM, 18, _("Cannot find a file!"), False)
    INVALID_EXTENSION = Code(PRINTER, Category.SYSTEM, 19, _("File has an invalid extension!"), False)
    FILE_ALREADY_EXISTS = Code(PRINTER, Category.SYSTEM, 20, _("File already exists!"), False)
    INVALID_PROJECT = Code(PRINTER, Category.SYSTEM, 21, _("The project file is invalid!"), False)
    WIZARD_NOT_CANCELABLE = Code(PRINTER, Category.SYSTEM, 22, _("This wizard cannot be canceled"), False)

    # Warnings
    NONE_WARNING = Code(PRINTER, Category.WARNINGS, 0, _("No warning"), False)
    UNKNOWN_WARNING = Code(PRINTER, Category.WARNINGS, 1, _("Unknown warning"), False)
    AMBIENT_TOO_HOT_WARNING = Code(PRINTER, Category.WARNINGS, 2, None, False)
    AMBIENT_TOO_COLD_WARNING = Code(PRINTER, Category.WARNINGS, 3, None, False)
    PRINTING_DIRECTLY_WARNING = Code(PRINTER, Category.WARNINGS, 4, None, False)
    PRINTER_MODEL_MISMATCH_WARNING = Code(PRINTER, Category.WARNINGS, 5, None, False)
    RESIN_NOT_ENOUGH_WARNING = Code(PRINTER, Category.WARNINGS, 6, None, False)
    PROJECT_SETTINGS_MODIFIED_WARNING = Code(PRINTER, Category.WARNINGS, 7, None, False)

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
