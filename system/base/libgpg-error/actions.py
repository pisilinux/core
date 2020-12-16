# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

LIBDIR = "/usr/lib32" if get.buildTYPE() == "emul32" else "/usr/lib"
bindir = "/usr/bin32" if get.buildTYPE() == "emul32" else "/usr/bin"

def setup():
    autotools.configure("--enable-nls \
                         --libdir=%s \
                         --bindir=%s \
                         --disable-rpath \
                         --disable-languages"% (LIBDIR, bindir))

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return

    pisitools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "NEWS", "README", "THANKS")
