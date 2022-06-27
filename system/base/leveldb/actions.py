#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build") 
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DLEVELDB_BUILD_TESTS:BOOL=OFF \
                          -DLEVELDB_BUILD_BENCHMARKS:BOOL=OFF \
                          -DBUILD_SHARED_LIBS=1", sourceDir="..")

def build():
    #shelltools.chmod("build_detect_platform", 0755)
    shelltools.cd("build")
    cmaketools.make()
    #autotools.make()

#def check():
    #autotools.make("check")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.dolib_so("libleveldb.so.1.18")
    #pisitools.dosym("libleveldb.so.1.18", "/usr/lib/libleveldb.so.1")
    #pisitools.dosym("libleveldb.so.1.18", "/usr/lib/libleveldb.so")

    #pisitools.insinto("/usr/include", "include/*")
    #pisitools.insinto("/usr/include", "helpers/memenv/memenv.h")
    shelltools.cd("..")
    pisitools.dodoc("README*", "LICENSE", "NEWS", "LICENSE")
