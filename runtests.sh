#!/bin/bash

chmod -R a+rwx tests/tmp
rm -Rf tests/tmp
mkdir -p tests/tmp/dir
echo -n "ß" > tests/tmp/file
ln -s dir tests/tmp/dirlink
ln -s file tests/tmp/filelink
ln -s dangling/dangling/dangling tests/tmp/danglinglink

mkdir -p tests/tmp/unreadabledir
echo -n "ß" > tests/tmp/unreadablefile
chmod a-rwx tests/tmp/unreadable*

nosetests tests/fs_tests.py
