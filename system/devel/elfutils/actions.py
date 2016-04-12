#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():

    # Remove -Wall from default flags. The makefiles enable enough warnings
    # themselves, and they use -Werror.
   
    
    options ='-disable-nls --program-prefix=\"eu-\" --with-zlib'
    
    if get.buildTYPE() == "emul32":
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
    
    elif get.ARCH() == "x86_64":
        pisitools.flags.add("-fexceptions")
        autotools.autoreconf("-vfi")

        pisitools.cflags.remove("-Wall")
        
        options +=" \
                    --enable-dwz \
                    --enable-thread-safety \
                    --with-bzlib \
                    --with-lzma"
    
    autotools.configure(options)

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.remove("/usr/lib32/libelf.a")
        pisitools.remove("/usr/lib32/libasm.a")
        pisitools.remove("/usr/lib32/libdw.a")
        
        
    elif get.ARCH() == "x86_64":
    # Don't remove all the static libs as libebl.a is needed by other packages
        pisitools.remove("/usr/lib/libelf.a")
        pisitools.remove("/usr/lib/libasm.a")
        pisitools.remove("/usr/lib/libdw.a")

        pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "NOTES", "README", "THANKS", "TODO")
