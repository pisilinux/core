#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools


def setup():
    pisitools.dosed("udev/69-dm-lvm.rules", "/usr/bin/lvm", "/usr/sbin/lvm")
    mesontools.configure("-Dsystemd=disabled")

def build():
    mesontools.build()


def install():
    mesontools.install()

    pisitools.removeDir("/usr/lib/kernel")
    pisitools.removeDir("/usr/share/libalpm")

    pisitools.dosed("%s/usr/bin/mkinitcpio"% get.installDIR(), "/usr/bin:/bin", "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")
    pisitools.dosed("%s/usr/lib/initcpio/install/udev"% get.installDIR(), "/usr/", "/")
    pisitools.dosed("%s/usr/lib/initcpio/install/fsck"% get.installDIR(), "/usr/bin", "/sbin")

    pisitools.dosed("%s/usr/bin/mkinitcpio"% get.installDIR(), "/usr/lib/modules", "/lib/modules")

    pisitools.dodoc("LICENSE", "README.*")
