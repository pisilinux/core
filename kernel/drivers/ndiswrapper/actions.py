#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("-C driver KVERS_UNAME=%s" % KDIR)

    autotools.make("-C utils")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "*/*.ko")
    pisitools.dosbin("utils/ndiswrapper*", "/usr/sbin")
    pisitools.dosbin("utils/loadndisdriver", "/sbin")
    
    # add man
    pisitools.doman("*.8")
    
    pisitools.dodir("/etc/ndiswrapper")

    pisitools.dodoc("README", "AUTHORS", "ChangeLog")
