#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    pisitools.flags.add("-U_FORTIFY_SOURCE")
    autotools.autoreconf("-vfi")
    
    options = "--enable-shared \
               --disable-static \
              "
              
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        
        options += "--build=i686-pc-linux-gnu \
                    --host=i686-pc-linux-gnu \
                    --prefix=/emul32 \
                    --libdir=/usr/lib32 \
                    --disable-documentation \
                   " 
    
    autotools.configure(options)
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

# https://savannah.nongnu.org/bugs/?22368
# https://bugs.gentoo.org/273372
#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/include", "include/libunwind-x86.h")
        return

    # FIXME: Fedora removes it, Suse keeps it, breaks samba build, investigate further
    pisitools.remove("/usr/lib/libunwind*.a")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "TODO")
