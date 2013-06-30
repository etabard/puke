#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest2 as unittest

import os
import sys
from os.path import join
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import puke2

from stat import ST_MODE

# XXX will break windows obviously for now
root = "~/../../../..%s/tmp" % os.path.dirname(os.path.abspath(__file__))


class ExistenceTest(unittest.TestCase):

    def test_exists(self):
        self.assertEqual(puke2.fs.exists(join(root, "dir")), True)
        self.assertEqual(puke2.fs.exists(join(root, "dirlink")), True)
        self.assertEqual(puke2.fs.exists(join(root, "file")), True)
        self.assertEqual(puke2.fs.exists(join(root, "filelink")), True)
        self.assertEqual(puke2.fs.exists(join(root, "unreadabledir")), True)
        self.assertEqual(puke2.fs.exists(join(root, "unreadablefile")), True)

        self.assertEqual(puke2.fs.exists(join(root, "nonexistent")), False)
        self.assertEqual(puke2.fs.exists(join(root, "danglinglink")), False)

    def test_isfile(self):
        self.assertEqual(puke2.fs.isfile(join(root, "dir")), False)
        self.assertEqual(puke2.fs.isfile(join(root, "dirlink")), False)
        self.assertEqual(puke2.fs.isfile(join(root, "file")), True)
        self.assertEqual(puke2.fs.isfile(join(root, "filelink")), False)
        self.assertEqual(puke2.fs.isfile(join(root, "unreadabledir")), False)
        self.assertEqual(puke2.fs.isfile(join(root, "unreadablefile")), True)

        try:
            p = join(root, "nonexistent")
            puke2.fs.isfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.isfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

    def test_isfile2(self):
        self.assertEqual(puke2.fs.isfile(join(root, "dir"), True), False)
        self.assertEqual(puke2.fs.isfile(join(root, "dirlink"), True), False)
        self.assertEqual(puke2.fs.isfile(join(root, "file"), True), True)
        self.assertEqual(puke2.fs.isfile(join(root, "filelink"), True), True)
        self.assertEqual(
            puke2.fs.isfile(join(root, "unreadabledir"), True), False)
        self.assertEqual(
            puke2.fs.isfile(join(root, "unreadablefile"), True), True)

        try:
            p = join(root, "nonexistent")
            puke2.fs.isfile(p, True)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.isfile(p, True)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

    def test_isdir(self):
        self.assertEqual(puke2.fs.isdir(join(root, "dir")), True)
        self.assertEqual(puke2.fs.isdir(join(root, "dirlink")), False)
        self.assertEqual(puke2.fs.isdir(join(root, "file")), False)
        self.assertEqual(puke2.fs.isdir(join(root, "filelink")), False)
        self.assertEqual(puke2.fs.isdir(join(root, "unreadabledir")), True)
        self.assertEqual(puke2.fs.isdir(join(root, "unreadablefile")), False)

        try:
            p = join(root, "nonexistent")
            puke2.fs.isdir(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.isdir(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

    def test_isdir2(self):
        self.assertEqual(puke2.fs.isdir(join(root, "dir"), True), True)
        self.assertEqual(puke2.fs.isdir(join(root, "dirlink"), True), True)
        self.assertEqual(puke2.fs.isdir(join(root, "file"), True), False)
        self.assertEqual(puke2.fs.isdir(join(root, "filelink"), True), False)
        self.assertEqual(
            puke2.fs.isdir(join(root, "unreadabledir"), True), True)
        self.assertEqual(
            puke2.fs.isdir(join(root, "unreadablefile"), True), False)

        try:
            p = join(root, "nonexistent")
            puke2.fs.isdir(p, True)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.isdir(p, True)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

    def test_islink(self):
        self.assertEqual(puke2.fs.islink(join(root, "dir")), False)
        self.assertEqual(puke2.fs.islink(join(root, "dirlink")), True)
        self.assertEqual(puke2.fs.islink(join(root, "file")), False)
        self.assertEqual(puke2.fs.islink(join(root, "filelink")), True)
        self.assertEqual(puke2.fs.islink(join(root, "unreadabledir")), False)
        self.assertEqual(puke2.fs.islink(join(root, "unreadablefile")), False)

        try:
            p = join(root, "nonexistent")
            puke2.fs.islink(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.SymlinkNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.islink(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.SymlinkNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))


class FileManipulationTest(unittest.TestCase):

    def test_read(self):
        try:
            p = join(root, "dir")
            puke2.fs.readfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "dirlink")
            puke2.fs.readfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        self.assertEqual(puke2.fs.readfile(join(root, "file")), "ß")
        self.assertEqual(puke2.fs.readfile(join(root, "filelink")), "ß")

        try:
            p = join(root, "unreadabledir")
            puke2.fs.readfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "unreadablefile")
            puke2.fs.readfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.PermissionDenied)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "nonexistent")
            puke2.fs.readfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.readfile(p)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

    def test_write(self):
        content = "♥"
        try:
            p = join(root, "dir")
            puke2.fs.writefile(p, content)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "dirlink")
            puke2.fs.writefile(p, content)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        puke2.fs.writefile(join(root, "file"), content)
        self.assertEqual(puke2.fs.readfile(join(root, "file")), content)

        puke2.fs.writefile(join(root, "filelink"), "ß")
        self.assertEqual(puke2.fs.readfile(join(root, "filelink")), "ß")

        try:
            p = join(root, "unreadabledir")
            puke2.fs.writefile(p, content)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "unreadablefile")
            puke2.fs.writefile(p, content)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.PermissionDenied)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        p = join(root, "nonexistent")
        puke2.fs.writefile(p, content)
        self.assertEqual(puke2.fs.readfile(join(root, "nonexistent")), content)
        puke2.fs.rm(join(root, "nonexistent"))

        try:
            p = join(root, "danglinglink")
            puke2.fs.writefile(p, content)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.PathNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

    def test_copy(self):
        destination = join(root, "copyresult")
        try:
            p = join(root, "dir")
            puke2.fs.copyfile(p, destination)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "dirlink")
            puke2.fs.copyfile(p, destination)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        puke2.fs.copyfile(join(root, "file"), destination)
        self.assertEqual(puke2.fs.readfile(destination), "ß")

        puke2.fs.rm(destination)

        puke2.fs.copyfile(join(root, "filelink"), destination)
        self.assertEqual(puke2.fs.readfile(destination), "ß")

        puke2.fs.rm(destination)

        try:
            p = join(root, "unreadabledir")
            puke2.fs.copyfile(p, destination)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "unreadablefile")
            puke2.fs.copyfile(p, destination)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.PermissionDenied)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "nonexistent")
            puke2.fs.copyfile(p, destination)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.copyfile(p, destination)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.FileNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

    def test_chmod(self):
        for p in ["dir", "dirlink", "file", "filelink",
                  "unreadabledir", "unreadablefile"]:
            p = join(root, p)
            puke2.fs.chmod(p, 0o777)
            self.assertEqual(
                oct(os.stat(puke2.fs.resolvepath(p))[ST_MODE])[-3:],
                "777")

        puke2.fs.chmod(join(root, "unreadabledir"), 0000)
        puke2.fs.chmod(join(root, "unreadablefile"), 0000)

        try:
            p = join(root, "nonexistent")
            puke2.fs.chmod(p, 0o777)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.PathNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

        try:
            p = join(root, "danglinglink")
            puke2.fs.chmod(p, 0o777)
            self.assertTrue(False)
        except Exception as e:
            self.assertIsInstance(e, puke2.exceptions.PathNotFound)
            self.assertEqual(str(e), puke2.fs.abspath(p))

  # Kind of m00t - none of these tests might work without root
    def test_chown(self):
        pass


if __name__ == '__main__':
    unittest.main()


# XXX still todo
# puke.fs.chown(path, uname, gname=None, recursive=False)
# puke.fs.mkdir(path)
# puke.fs.rm(path)
# puke.fs.symlink(source, linkpath)
# puke.fs.checksum(path, hash="md5")
# puke.fs.MD5 puke.fs.HA1

# puke.fs.abspath(path) transforme en path absolue (~ et ..)
# puke.fs.relpath(path) fournir une path relative par rapport à cwd

# puke.fs.join(...)
# puke.fs.basename(path)
# puke.fs.dirname(path)









# puke.fs.resolvepath(path) résoud les ~/
# puke.fs.normpath(path) collapse les /../
# puke.fs.realpath(path) résoud les symlink

# puke.fs.sep()
