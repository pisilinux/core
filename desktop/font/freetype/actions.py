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
    options = "--disable-static \
               --with-harfbuzz=no \
               --enable-freetype-config \
              "

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                   "

    else:
        options += " --with-brotli=yes \
                   "

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("ChangeLog", "README")
