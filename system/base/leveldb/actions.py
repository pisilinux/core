#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
		                  -DCMAKE_INSTALL_LIBDIR=lib")

def build():
    #shelltools.chmod("build_detect_platform", 0755)
    cmaketools.make()

def check():
    cmaketools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dolib_so("libleveldb.so.1.18")
    #pisitools.dosym("libleveldb.so.1.18", "/usr/lib/libleveldb.so.1")
    #pisitools.dosym("libleveldb.so.1.18", "/usr/lib/libleveldb.so")

    #pisitools.insinto("/usr/include", "include/*")
    #pisitools.insinto("/usr/include", "helpers/memenv/memenv.h")

    pisitools.dodoc("README.md", "LICENSE", "NEWS", "AUTHORS")