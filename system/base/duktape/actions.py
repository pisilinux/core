#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#def setup():
    #shelltools.copy("Makefile.sharedlibrary", "Makefile")
    #pisitools.dosed("Makefile", "INSTALL_PREFIX = /usr/local", "INSTALL_PREFIX = /usr")
    #pisitools.dosed("Makefile.sharedlibrary", "INSTALL_PREFIX = /usr/local", "INSTALL_PREFIX = /usr")
    
def build():
    shelltools.sym("Makefile.sharedlibrary", "Makefile")
    autotools.make("INSTALL_PREFIX=/usr")

def install():
    autotools.rawInstall("DESTDIR=%s INSTALL_PREFIX=/usr" % get.installDIR())

    pisitools.dodoc("AUTHORS*", "LICENSE*", "README*")
