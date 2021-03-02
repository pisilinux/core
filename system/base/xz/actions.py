#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


bindir = "/usr/bin32" if get.buildTYPE() == "emul32" else "/usr/bin"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --bindir=%s \
                         --disable-rpath" % (bindir))
    # Remove RPATH
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")
    

def build():
    #shelltools.export("LDFLAGS", "-lpthread")
    autotools.make()

def check():
    shelltools.export("LD_LIBRARY_PATH", "%s/src/liblzma/.libs" % get.curDIR())
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        pisitools.remove("/usr/share/man/man1/lzmadec.1")
        return
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
