#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|datadir|libdir|g' meson.build")
    
    #shelltools.makedirs("build")
    #shelltools.cd("build")
    #shelltools.system("meson .. --prefix=/usr --libdir=lib -Dlegacy=true")
    autotools.configure("--enable-legacy")
    
def build():
    #shelltools.cd("build")
    #shelltools.system("ninja")
    autotools.make()
    
def install():
    #shelltools.cd("build")
    #shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    #shelltools.cd("..")
    autotools.install()
    pisitools.dodoc("README.md", "COPYING*", "AUTHORS")
    shelltools.system("mkdir -p %s/usr/lib/pkgconfig" %get.installDIR())
    shelltools.system("mv %s/usr/share/pkgconfig/* %s/usr/lib/pkgconfig" %(get.installDIR(), get.installDIR()))
    pisitools.removeDir("/usr/share/pkgconfig")
    
    #pisitools.remove("/usr/include/X11/extensions/apple*")
    #pisitools.remove("/usr/include/X11/extensions/windows*")
    #pisitools.remove("/usr/share/doc/xorg-proto/COPYING-windowswmproto")
    #pisitools.remove("/usr/share/doc/xorg-proto/COPYING-applewmproto")
    #pisitools.remove("/usr/lib/pkgconfig/applewmproto.pc")
    #pisitools.remove("/usr/lib/pkgconfig/windowswmproto.pc")
