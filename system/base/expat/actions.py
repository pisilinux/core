#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    cflags = "%s -fPIC" % get.CFLAGS()
    shelltools.export("CFLAGS", cflags)
    options = "--disable-static"
    
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        options += " --libdir=/usr/lib32 \
                     --bindir=/usr/bin32"

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR=%s man1dir=/usr/share/man/man1' % get.installDIR())
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("usr/bin32")
        return

    pisitools.dohtml("doc/*")
    pisitools.dodoc("Changes", "README.md")
