# This file is part of the SL1 firmware
# Copyright (C) 2020 Prusa Research a.s. - www.prusa3d.com
# SPDX-License-Identifier: GPL-3.0-or-later

# pylint: disable = missing-function-docstring
# pylint: disable = missing-class-docstring
# pylint: disable = missing-module-docstring

import unittest
from asyncio import run
from typing import Dict

from aiohttp import ClientSession, ClientResponse

from prusaerrors.shared.codes import Code
from prusaerrors.sl1.codes import Sl1Codes


class TestErrors(unittest.TestCase):
    def test_str_conversion(self):
        self.assertEqual("#10500", str(Sl1Codes.NONE))

    def test_code_lookup(self):
        self.assertEqual(Sl1Codes.NONE, Sl1Codes.get("#10500"))

    def test_unknown_code_lookup(self):
        self.assertEqual(Sl1Codes.UNKNOWN, Sl1Codes.get("random string"))

    @staticmethod
    async def _test_codes(codes: Dict[str, Code], fail_list: Dict[str, ClientResponse]):
        async with ClientSession() as session:
            for title, code in codes.items():
                url = f'https://prusa.io/{code.raw_code}'
                async with session.get(url) as response:
                    if response.status != 200:
                        fail_list[title] = response
                        print(code.code, title, "error", response.status, response.url)

    def test_approved_codes(self):
        sl1 = Sl1Codes()
        codes = sl1.get_codes_with_approve_status(True)
        failed_codes: Dict[str, ClientResponse] = {}
        run(self._test_codes(codes, failed_codes))
        self.assertEqual(len(failed_codes), 0, failed_codes)

    def test_unapproved_codes(self):
        sl1 = Sl1Codes()
        codes = sl1.get_codes_with_approve_status(False)
        self.assertEqual(len(codes), 0, codes)

if __name__ == "__main__":
    unittest.main()
