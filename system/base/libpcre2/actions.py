#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

LIBDIR = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"
bindir = "/usr/bin32" if get.buildTYPE() == "emul32" else "/usr/bin"

def setup():
    autotools.autoreconf("-vif")
    options = "--enable-jit \
                         --libdir=%s \
                         --bindir=%s \
                         --enable-pcre2test-libreadline \
                         --enable-pcre2-32 \
                         --enable-pcre2-16 \
                         --enable-unicode \
                         --docdir=/%s/%s \
                         --disable-static" % (LIBDIR, bindir, get.docDIR(), get.srcNAME())

    if get.buildTYPE() != "emul32":
        options += " --enable-pcre2grep-libz \
                     --enable-pcre2grep-libbz2 \
                   "
    autotools.configure(options)
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    if get.buildTYPE() == "emul32":
        pass
    else:
        autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return
