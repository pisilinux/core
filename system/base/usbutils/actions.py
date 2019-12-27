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
    shelltools.system("./autogen.sh \
					--datadir=/usr/share/misc \
				    --disable-zlib")
    #autotools.configure("--datadir=/usr/share/misc \
                         #--disable-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.removeDir("/usr/sbin")

    pisitools.dodoc("NEWS", "README.md")
