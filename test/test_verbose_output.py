#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

import unittest

import sys
import os
import subprocess

from test.helper import FakeYDL, assertEqual
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestVerboseOutput(unittest.TestCase):
    def test_private_info_arg(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'youtube_dl/__main__.py', '-v',
                '--username', 'johnsmith@gmail.com',
                '--password', 'secret',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'--username' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'--password' in serr)
        self.assertTrue(b'secret' not in serr)

    def test_private_info_shortarg(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'youtube_dl/__main__.py', '-v',
                '-u', 'johnsmith@gmail.com',
                '-p', 'secret',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'-u' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'-p' in serr)
        self.assertTrue(b'secret' not in serr)

    def test_private_info_eq(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'youtube_dl/__main__.py', '-v',
                '--username=johnsmith@gmail.com',
                '--password=secret',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'--username' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'--password' in serr)
        self.assertTrue(b'secret' not in serr)

    def test_private_info_shortarg_eq(self):
        outp = subprocess.Popen(
            [
                sys.executable, 'youtube_dl/__main__.py', '-v',
                '-u=johnsmith@gmail.com',
                '-p=secret',
            ], cwd=rootDir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sout, serr = outp.communicate()
        self.assertTrue(b'-u' in serr)
        self.assertTrue(b'johnsmith' not in serr)
        self.assertTrue(b'-p' in serr)
        self.assertTrue(b'secret' not in serr)

    def test_concat_avg_speed(self):
        ydl = FakeYDL()
        ydl.s['total_bytes'] = 1000;
        ydl.s['elapsed'] = 1000;
        msg = ydl.test_concat_avg_speed("",self.s);
        correct_msg =  ' at ' + str(round(ydl.s['total_bytes'] / (ydl.s['elapsed'] * 1000000), 2)) + ' mBps';
        assertEqual(msg,correct_msg)


if __name__ == '__main__':
    unittest.main()
