#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pass

def build():
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.make(parameters="PREFIX=/usr")

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())
    pisitools.dodoc("README", "LICENSE")
