#####################################################################
# testExample.py
#
# (c) Copyright 2013-2015, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################

import unittest

import secsgem

class TestExampleSecsGem(unittest.TestCase):
    def setUp(self):
        self.connection = secsgem.GemHandler("10.211.55.33", 5000, False, 0, "test")

        self.connection.enable()
        self.connection.waitfor_communicating()

    def tearDown(self):
        self.connection.disable()

    def testLinktest(self):
        result_packet = self.connection.send_linktest_req()

        self.assertEqual(result_packet.header.sType, 6)
        self.assertEqual(result_packet.header.sessionID, 65535)


