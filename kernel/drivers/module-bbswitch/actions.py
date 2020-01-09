#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("KDIR=/lib/modules/%s/build" % KDIR)

def install():
    pisitools.insinto("/lib/modules/%s/misc" % KDIR, "bbswitch.ko")
    pisitools.dosed("dkms/dkms.conf",  "#MODULE_VERSION#", get.srcVERSION())
    for f in "Makefile bbswitch.c dkms/dkms.conf".split():
        pisitools.insinto("/usr/src/bbswitch-%s" % get.srcVERSION(), f)

    pisitools.dodoc("NEWS", "README*")
