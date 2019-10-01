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
    shelltools.system("sed -i '/MV.*old/d' Makefile.in")
    shelltools.system("sed -i '/{OLDSUFF}/c:' support/shlib-install")
    pisitools.cflags.add("-fPIC")

    #Force link to ncurses instead of tinfo, which we don't have, will be needed when we use as-needed ;)
    pisitools.dosed("support/shobj-conf", "^(SHLIB_LIBS=)", "\\1-lncurses")

    pisitools.dosed("support/shobj-conf", "\-Wl,\-rpath,\$\(libdir\)\s")
    autotools.configure("--with-curses \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    pisitools.removeDir("/usr/bin")
    
    pisitools.dosym("/usr/lib/libreadline.so.8", "/usr/lib/libreadline.so.7")
    pisitools.dosym("/usr/lib32/libreadline.so.8", "/usr/lib32/libreadline.so.7")
    
    pisitools.dosym("/usr/lib/libhistory.so.8", "/usr/lib/libhistory.so.7")
    pisitools.dosym("/usr/lib32/libhistory.so.8", "/usr/lib32/libhistory.so.7")

    pisitools.dohtml("doc/")
    pisitools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS")
