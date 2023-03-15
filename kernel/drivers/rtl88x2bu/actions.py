#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()
KVER ="5.15.102"

def build():
    autotools.make("KVER=%s" % KVER )

def install():
    pisitools.insinto("/lib/modules/%s/kernel/drivers/net/wireless" % KDIR, "*.ko")

    pisitools.insinto("/etc/modprobe.d", "88x2bu.conf")

    shelltools.chmod(get.installDIR() + "/etc/modprobe.d/88x2bu.conf")
    shelltools.chmod(get.installDIR() + "/lib/modules/%s/kernel/drivers/net/wireless/*.ko" % KDIR )

    pisitools.dodoc("README*", "LICENSE")
