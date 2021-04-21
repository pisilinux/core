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
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS*", "LICENSE*", "README*")
