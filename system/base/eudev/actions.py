#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--exec-prefix=\"\" \
               --sbindir=/sbin \
               --libdir=/usr/lib \
               --libexecdir=/lib/udev \
               --enable-logging"

    if get.buildTYPE() == "emul32":
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --libexecdir=/emul32/lib/udev \
                     --datadir=/emul32/share \
                     --bindir=/emul32/bin \
                     --sbindir=/emul32/sbin \
                     --disable-extras"

    autotools.autoreconf("-fi")
    autotools.configure(options)

def build():
    autotools.make("all")


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/lib32/","/usr/lib32/libudev.s*")
    if get.buildTYPE() == "emul32":
        
        return

    # create needed directories
    for d in ("", "net", "pts", "shm", "hugepages"):
        pisitools.dodir("/lib/udev/devices/%s" % d)
        pisitools.insinto("/lib/udev/","/usr/lib/udev/*")
        
   

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")
    pisitools.dodir("/run/udev")

    pisitools.doman("man/*.5", "man/*.7", "man/*.8")
    
    pisitools.dodoc("README*", "NOTES")
    
