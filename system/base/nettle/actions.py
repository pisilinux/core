#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


bindir = "/usr/bin32" if get.buildTYPE() == "emul32" else "/usr/bin"

def setup():
    options = " --enable-shared \
                --bindir=%s \
              " % ( bindir)

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                   "
    
    
    autotools.autoreconf("-fiv")
    autotools.configure(options)

def build():
    autotools.make("-j1")
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return

    #pisitools.remove("/usr/lib/*.a")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README", "nettle.pdf")
