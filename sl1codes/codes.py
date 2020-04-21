# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

import functools
import json
from enum import unique, IntEnum
from typing import Optional, TextIO


@unique
class Class(IntEnum):
    # This mapping is taken from general Prusa guidelines on errors, do not modify.
    MECHANICAL = 1  # Mechanical failures, engines XYZ, tower
    TEMPERATURE = 2  # Temperature measurement, thermistors, heating
    ELECTRICAL = 3  # Electrical, MINDA, FINDA, Motion Controller, …
    CONNECTIVITY = 4  # Connectivity - Wi - Fi, LAN, Prusa Connect Cloud
    SYSTEM = 5  # System - BSOD, ...


@functools.total_ordering
class Code:
    def __init__(self, cls: Class, code: int, message: Optional[str]):
        if cls.value < 0 or cls.value > 9:
            raise ValueError(f"Error class {cls.value} out of range")

        if code < 0 or code > 99:
            raise ValueError(f"Error code {code} out of range")

        self._category = cls
        self._code = code
        self._message = message

    @property
    def code(self) -> int:
        return self._category.value * 100 + self._code

    @property
    def category(self) -> Class:
        return self._category

    @property
    def message(self) -> str:
        return self._message

    def __lt__(self, other):
        if not isinstance(other, Code):
            return NotImplemented
        return self.code < other.code

    def __eq__(self, other):
        if not isinstance(other, Code):
            return NotImplemented
        return self.code == other.code


class Codes:
    @classmethod
    def get_codes(cls):
        return {item: var for item, var in vars(cls).items() if isinstance(var, Code)}

    @classmethod
    def dump_json(cls, fp: TextIO) -> str:
        obj = {name.lower(): {"code": code.code, "message": code.message} for name, code in cls.get_codes().items()}
        return json.dump(obj, fp, indent=True)

    @classmethod
    def dump_cpp_enum(cls, fd: TextIO):
        fd.write("// Generated error code enum\n")
        fd.write("enum class Errors {\n")

        for name, code in cls.get_codes().items():
            fd.write(f"\t{name} = {code.code};\n")

        fd.write("};\n")

    @classmethod
    def dump_cpp_messages(cls, fd: TextIO):
        fd.write("// Generated error code to message mapping\n")
        fd.write("static QMap<int, QString> error_messages{\n")

        for _, code in cls.get_codes().items():
            if code.message:
                fd.write("\t{" + str(code.code) + ', "' + code.message + '"}\n')

        fd.write("};\n")

    @classmethod
    def dump_cpp_ts(cls, fd: TextIO):
        fd.write("// Generated translation string definitions for all defined error messages\n")
        for _, code in cls.get_codes().items():
            if code.message:
                fd.write(f'tr("{code.message}");\n')


def unique_codes(cls):
    used = set()
    for name, code in cls.get_codes().items():
        if code.code in used:
            raise ValueError(f"Code {name} with value {code.code} is deficit!")
        used.add(code.code)

    return cls
