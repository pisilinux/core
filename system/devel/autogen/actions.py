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
    pisitools.cflags.add("  -Wno-implicit-fallthrough -Wno-format-overflow -Wno-format-truncation")
    shelltools.system("sed -i 's/ -Werror / /' configure")
    # autotools.autoreconf("-vfi")
    autotools.configure("--prefix=/usr \
                         --disable-static --disable-dependency-tracking")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS", "TODO", "VERSION")
