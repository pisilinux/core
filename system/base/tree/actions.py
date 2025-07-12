#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    # Tree uses a simple Makefile. No configure script.
    # Pass CFLAGS and LDFLAGS from the environment.
    # The default Makefile already includes OBJS, so no need to list sources.
    shelltools.system("make CFLAGS="%s" LDFLAGS="%s"" % (get.CFLAGS(), get.LDFLAGS()))

def build():
    # Compilation is done in the setup() step for tree's Makefile structure
    pass

def install():
    # Install to DESTDIR with prefix /usr
    # The Makefile includes an install target that handles man page and binary.
    shelltools.system("make DESTDIR="%s" prefix="/usr" install" % get.installDIR())
    # pisitools.dodoc("LICENSE", "README", "CHANGES") # Optional: if we want to install docs
