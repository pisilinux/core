#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared \
                         --enable-thread-safe")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()
    pisitools.dosym("/usr/lib/libmpfr.so.6.0.2", "/usr/lib/libmpfr.so.4.1.5")
    pisitools.dosym("/usr/lib/libmpfr.so.6.0.2", "/usr/lib/libmpfr.so.4")

    pisitools.dodoc("NEWS", "README", "TODO")
