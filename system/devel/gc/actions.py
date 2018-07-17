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
    autotools.autoreconf("-fi")
    
    pisitools.flags.add("-std=gnu++98")
    #shelltools.system ("rm -rf libtool libtool.m4")
    
    autotools.configure("--disable-static \
                         --enable-cplusplus")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "doc/README.linux", "doc/*.html")
    
    #pisitools.removeDir("/usr/share/gc")
