# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("PYTHON","/usr/bin/python3")

    pisitools.dosed("Makefile.in", "$(datarootdir)/pkgconfig", "$(libdir)/pkgconfig")
    pisitools.dosed("Makefile.am", "$(datarootdir)/pkgconfig", "$(libdir)/pkgconfig")
    
    autotools.autoreconf("-vif")

    #pisitools.dosed("Makefile", "pkgconfigdir = $(datarootdir)/pkgconfig", "pkgconfigdir = $(libdir)/pkgconfig")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/*.txt", "COPYING", "NEWS", "README*", "TODO")
