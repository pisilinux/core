#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/c_rehash /etc/ssl/certs")
