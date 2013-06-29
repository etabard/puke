#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import puke2

from stat import ST_MODE



# XXX will break windows obviously for now
root="~/../../../..%s/tmp" % os.path.dirname(os.path.abspath(__file__))


class ExistenceTest(unittest.TestCase):
  def test_exists(self):
    self.assertEqual(puke2.fs.exists(os.path.join(root, "dir")), True)
    self.assertEqual(puke2.fs.exists(os.path.join(root, "dirlink")), True)
    self.assertEqual(puke2.fs.exists(os.path.join(root, "file")), True)
    self.assertEqual(puke2.fs.exists(os.path.join(root, "filelink")), True)
    self.assertEqual(puke2.fs.exists(os.path.join(root, "unreadabledir")), True)
    self.assertEqual(puke2.fs.exists(os.path.join(root, "unreadablefile")), True)

    self.assertEqual(puke2.fs.exists(os.path.join(root, "nonexistent")), False)
    self.assertEqual(puke2.fs.exists(os.path.join(root, "danglinglink")), False)

  def test_isfile(self):
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "dir")), False)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "dirlink")), False)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "file")), True)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "filelink")), False)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "unreadabledir")), False)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "unreadablefile")), True)

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.isfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.isfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

  def test_isfile2(self):
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "dir"), True), False)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "dirlink"), True), False)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "file"), True), True)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "filelink"), True), True)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "unreadabledir"), True), False)
    self.assertEqual(puke2.fs.isfile(os.path.join(root, "unreadablefile"), True), True)

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.isfile(p, True)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.isfile(p, True)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))


  def test_isdir(self):
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "dir")), True)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "dirlink")), False)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "file")), False)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "filelink")), False)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "unreadabledir")), True)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "unreadablefile")), False)

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.isdir(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.isdir(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

  def test_isdir2(self):
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "dir"), True), True)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "dirlink"), True), True)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "file"), True), False)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "filelink"), True), False)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "unreadabledir"), True), True)
    self.assertEqual(puke2.fs.isdir(os.path.join(root, "unreadablefile"), True), False)

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.isdir(p, True)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.isdir(p, True)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.DirectoryNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))


  def test_islink(self):
    self.assertEqual(puke2.fs.islink(os.path.join(root, "dir")), False)
    self.assertEqual(puke2.fs.islink(os.path.join(root, "dirlink")), True)
    self.assertEqual(puke2.fs.islink(os.path.join(root, "file")), False)
    self.assertEqual(puke2.fs.islink(os.path.join(root, "filelink")), True)
    self.assertEqual(puke2.fs.islink(os.path.join(root, "unreadabledir")), False)
    self.assertEqual(puke2.fs.islink(os.path.join(root, "unreadablefile")), False)

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.islink(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.SymlinkNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.islink(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.SymlinkNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))




class FileManipulationTest(unittest.TestCase):
  def test_read(self):
    try:
      p=os.path.join(root, "dir")
      puke2.fs.readfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "dirlink")
      puke2.fs.readfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    self.assertEqual(puke2.fs.readfile(os.path.join(root, "file")), "ß")
    self.assertEqual(puke2.fs.readfile(os.path.join(root, "filelink")), "ß")

    try:
      p=os.path.join(root, "unreadabledir")
      puke2.fs.readfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "unreadablefile")
      puke2.fs.readfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.PermissionDenied)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.readfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.readfile(p)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

  def test_write(self):
    content="♥"
    try:
      p=os.path.join(root, "dir")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "dirlink")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    puke2.fs.writefile(os.path.join(root, "file"), content)
    self.assertEqual(puke2.fs.readfile(os.path.join(root, "file")), content)

    puke2.fs.writefile(os.path.join(root, "filelink"), "ß")
    self.assertEqual(puke2.fs.readfile(os.path.join(root, "filelink")), "ß")

    try:
      p=os.path.join(root, "unreadabledir")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "unreadablefile")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.PermissionDenied)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    p=os.path.join(root, "nonexistent")
    puke2.fs.writefile(p, content)
    self.assertEqual(puke2.fs.readfile(os.path.join(root, "nonexistent")), content)
    puke2.fs.rm(os.path.join(root, "nonexistent"))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.PathNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

  def test_copy(self):
    destination=os.path.join(root, "copyresult")
    try:
      p=os.path.join(root, "dir")
      puke2.fs.copyfile(p, destination)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "dirlink")
      puke2.fs.copyfile(p, destination)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    puke2.fs.copyfile(os.path.join(root, "file"), destination)
    self.assertEqual(puke2.fs.readfile(destination), "ß")

    puke2.fs.rm(destination)

    puke2.fs.copyfile(os.path.join(root, "filelink"), destination)
    self.assertEqual(puke2.fs.readfile(destination), "ß")

    puke2.fs.rm(destination)

    try:
      p=os.path.join(root, "unreadabledir")
      puke2.fs.copyfile(p, destination)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.UnexpectedDirectory)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "unreadablefile")
      puke2.fs.copyfile(p, destination)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.PermissionDenied)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.copyfile(p, destination)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.copyfile(p, destination)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

  def test_chmod(self):
    for p in ["dir", "dirlink", "file", "filelink", "unreadabledir", "unreadablefile"]:
      p=os.path.join(root, p)
      puke2.fs.chmod(p, 0777)
      self.assertEqual(oct(os.stat(puke2.fs.resolvepath(p))[ST_MODE])[-3:], "777")

    puke2.fs.chmod(os.path.join(root, "unreadabledir"), 0000)
    puke2.fs.chmod(os.path.join(root, "unreadablefile"), 0000)

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.chmod(p, 0777)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.PathNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.chmod(p, 0777)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.PathNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

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


