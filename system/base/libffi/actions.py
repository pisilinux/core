#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "--disable-static"
    
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        
    autotools.configure(options)

def build():
    autotools.make()

def check():
    # Needs dejagnu package
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.dosym("/usr/lib/libffi.so.8", "/usr/lib/libffi.so.7")
        pisitools.dosym("/usr/lib32/libffi.so.8", "/usr/lib32/libffi.so.7")
        return

    #if get.buildTYPE() == "emul32":
        ## Remove duplicated header files
        #pisitools.removeDir("/usr/lib32/%s" % get.srcDIR())
        ## Fix emul32 includedir
        #pisitools.dosym("/usr/lib/%s/include" % get.srcDIR(),
        #"/usr/lib32/%s/include" % get.srcDIR())

    pisitools.dodoc("ChangeLog*", "LICENSE", "README*")
