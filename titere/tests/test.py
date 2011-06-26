from unittest import TestCase
from titere import Titere
from StringIO import StringIO
import os
import tempfile


class UserTestCase(TestCase):

    def create_user_test_case(self):

        cfg = StringIO(
"""
[user:test_user]
username=test_user
""")

        Titere(cfg).apply()


class FileTestCase(TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def test_create_file_with_content(self):

        path = os.path.join(self.dir, 'test')
        content = 'test content'

        cfg = StringIO(
"""
[file:test]
path = %s
content = %s
""" % (path, content))

        Titere(cfg).apply()
        self.assertTrue(os.path.exists(path))

        fd = open(path, 'r')
        self.assertTrue(fd.read(), content)


class PackageTestCase(TestCase):

    def test_install_package(self):

        cfg = StringIO(
"""
[package:nginx]
name = nginx
""")

        Titere(cfg).apply()
        
