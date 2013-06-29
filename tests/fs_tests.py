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
    content="b"
    try:
      p=os.path.join(root, "dir")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "dirlink")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    puke2.fs.writefile(os.path.join(root, "file"), content)
    self.assertEqual(puke2.fs.readfile(os.path.join(root, "file")), "b")
    puke2.fs.writefile(os.path.join(root, "filelink"), "ß")
    self.assertEqual(puke2.fs.readfile(os.path.join(root, "filelink")), "ß")

    puke2.fs.writefile(os.path.join(root, "newfile"), content)
    self.assertEqual(puke2.fs.readfile(os.path.join(root, "newfile")), "b")

    puke2.fs.rm(os.path.join(root, "newfile"))

    try:
      p=os.path.join(root, "unreadabledir")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "unreadablefile")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.PermissionDenied)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "nonexistent")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
      self.assertEqual(e.message, puke2.fs.abspath(p))

    try:
      p=os.path.join(root, "danglinglink")
      puke2.fs.writefile(p, content)
      self.assertTrue(False)
    except Exception as e:
      self.assertIsInstance(e, puke2.exceptions.FileNotFound)
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


if __name__ == '__main__':
  unittest.main()


# puke.fs.exists(path)
# puke.fs.isfile(path, followSymlink=False)
# puke.fs.isdir(path, followSymlink=False)
# puke.fs.islink(path)

# puke.fs.copyfile(sourcepath, destpath, force = False)
# puke.fs.readfile(path)
# puke.fs.writefile(path, content)

# puke.fs.chown(path, uname, gname=None, recursive=False)
# puke.fs.chmod(path, mode, recursive=False)


# puke.fs.mkdir(path)
# puke.fs.rm(path)
# puke.fs.symlink(source, linkpath)
# puke.fs.checksum(path, hash="md5")

# puke.fs.join(...)
# puke.fs.basename(path)
# puke.fs.dirname(path)

# puke.fs.sep()
# puke.fs.resolvepath(path) résoud les ~/
# puke.fs.abspath(path) transforme en path absolue
# puke.fs.normpath(path) collapse les /../
# puke.fs.realpath(path) résoud les symlink

# FileSystemError
# PathNotFound
# FileNotFound
# DirectoryNotFound
# SymlinkNotFound
# FileExists
# PermissionDenied


# Method  Checks that New in
# assertEqual(a, b) a == b   
# assertNotEqual(a, b)  a != b   
# assertTrue(x) bool(x) is True  
# assertFalse(x)  bool(x) is False   
# assertIs(a, b)  a is b  2.7
# assertIsNot(a, b) a is not b  2.7
# assertIsNone(x) x is None 2.7
# assertIsNotNone(x)  x is not None 2.7
# assertIn(a, b)  a in b  2.7
# assertNotIn(a, b) a not in b  2.7
# assertIsInstance(a, b)  isinstance(a, b)  2.7
# assertNotIsInstance(a, b) not isinstance(a, b)  2.7
