#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/sbin/depmod -ae")
