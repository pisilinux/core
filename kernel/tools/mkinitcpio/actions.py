#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/lib/kernel")
    pisitools.removeDir("/usr/lib/tmpfiles.d")
    pisitools.remove("/usr/lib/initcpio/install/sd-*")
    pisitools.removeDir("/usr/share/libalpm")

    pisitools.dodoc("LICENSE", "README")
