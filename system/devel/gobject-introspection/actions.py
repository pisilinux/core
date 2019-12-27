#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    #autotools.autoreconf("-fiv")
    #autotools.configure("--disable-static \
                         #--disable-doctool")
                         
    options = "  --libdir=/usr/lib \
				 --bindir=/usr/bin \
                 --sbindir=/usr/sbin \
                 --datadir=/usr/share \
                 --prefix=/usr"
                 
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. %s" % options)
    
    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    #autotools.make()
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    

