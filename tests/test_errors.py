# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

from unittest import TestCase
from io import StringIO

from sl1codes.errors import Errors
import json


class TestErrors(TestCase):
    def test_json_export(self):
        sio = StringIO()
        Errors.dump_json(sio)

        print("JSON:")
        print(sio.getvalue())

        sio.seek(0)
        obj = json.load(sio)
        self.assertIn("none", obj)

    def test_cpp_enum_export(self):
        sio = StringIO()
        Errors.dump_cpp_enum(sio)

        print("C++ enum:")
        print(sio.getvalue())

        self.assertRegex(sio.getvalue(), r"NONE = 500;")

    def test_cpp_messages_export(self):
        sio = StringIO()
        Errors.dump_cpp_messages(sio)

        print("C++ messages:")
        print(sio.getvalue())

        self.assertRegex(sio.getvalue(), r'{500, "No problem"}')

    def test_cpp_ts_export(self):
        sio = StringIO()
        Errors.dump_cpp_ts(sio)

        print("C++ ts:")
        print(sio.getvalue())

        self.assertRegex(sio.getvalue(), r'tr\("No problem"\);')

    def test_int_conversion(self):
        self.assertEqual(500, int(Errors.NONE))

    def test_code_lookup(self):
        self.assertEqual(Errors.NONE, Errors.get(500))

    def test_unknown_code_lookup(self):
        self.assertEqual(Errors.UNKNOWN, Errors.get(-123))
