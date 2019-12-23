#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    options = "--enable-nls \
               --disable-java \
               --disable-csharp \
               --disable-rpath \
               --disable-gtk-doc \
               --disable-static \
               --without-libunistring-prefix"

    if get.buildTYPE() == "emul32":
        options += " --bindir=/emul32/bin"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def check():
    if get.buildTYPE() != "emul32":
       autotools.make("-C tests check")
    else:
       shelltools.system("echo 'No test in emul32'")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "COPYING*", "README*")
