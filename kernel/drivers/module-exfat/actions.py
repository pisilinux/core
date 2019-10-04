#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

#def setup():
#	

KDIR = kerneltools.getKernelVersion()

def build():
	autotools.make("KDIR=/lib/modules/%s/build" % KDIR)

def install():
	pisitools.insinto("/lib/modules/%s/kernel/fs/exfat" % KDIR, "exfat.ko", "exfat.ko")

	pisitools.dodoc("LICENSE", "README.md")
