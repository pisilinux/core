#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i '/math.h/a #include <malloc.h>' src/flexdef.h")
    pisitools.flags.add("-fPIC")
    shelltools.export("AUTOPOINT", "true")

    autotools.autoreconf("-vfi")
    # do not enable nls http://bugs.gentoo.org/121408
    autotools.configure("--disable-nls \
                         --disable-dependency-tracking")
    
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("flex", "/usr/bin/lex")

    pisitools.dodoc("NEWS", "README.md")
