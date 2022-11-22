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
               --prefix=/usr \
               --without-xmlto"

    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32"

    autotools.autoreconf("-fi")
    autotools.configure(options)


    # autotools.configure("--disable-static \
                         # --without-xmlto")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "_emul32":
        return


    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*")
