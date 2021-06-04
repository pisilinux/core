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
    
    # fix sandbox violations when attempt to read "/missing.xml"
    pisitools.dosed("testapi.c", "\/missing.xml", "missing.xml")
    
    autotools.autoreconf("-fiv")
    
    shelltools.system("mkdir build-py{2,3}")
    shelltools.cd("build-py2")
    shelltools.sym("../configure", "configure")
    options = "--with-zlib \
               --with-readline \
               --enable-ipv6 \
               --includedir=/usr/include \
               --disable-static \
               --with-threads \
               --with-history \
              "

    if get.buildTYPE() == "emul32":
        options += " --bindir=/emul32/bin \
                     --libdir=/usr/lib32 \
                     --without-python"
    else: options += " --with-python=/usr/bin/python \
                       --libdir=/usr/lib"
    
    autotools.configure(options)
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
    shelltools.cd("../build-py3")
    shelltools.sym("../configure", "configure")
    options = "--with-zlib \
               --with-readline \
               --enable-ipv6 \
               --includedir=/usr/include \
               --disable-static \
               --with-threads \
               --with-history \
              "

    if get.buildTYPE() == "emul32":
        options += " --bindir=/emul32/bin \
                     --libdir=/usr/lib32 \
                     --without-python"
    else: options += " --with-python=/usr/bin/python3 \
                       --libdir=/usr/lib"

    autotools.configure(options)
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.cd("build-py2")
    autotools.make()
    shelltools.cd("../build-py3")
    autotools.make()

def check():
    shelltools.cd("build-py2")
    autotools.make("check")
    shelltools.cd("../build-py3")
    autotools.make("check")

def install():
    shelltools.cd("build-py2")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("../build-py3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32" or "i686":
        pisitools.removeDir("/usr/share/gtk-doc")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
