#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_flask_microbrewrey
----------------------------------

Tests for `flask_microbrewrey` module.
"""
import os
import unittest
import tempfile

from flask_microbrewrey.app import app


class TestFlask_microbrewrey(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_000_something(self):
        response = self.app.get('/api/Beer')
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
