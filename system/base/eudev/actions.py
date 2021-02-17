#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

suffix = "32" if get.buildTYPE() == "emul32" else ""

def setup():
    autotools.autoreconf("-fis")

    j = "--prefix=/usr          \
         --bindir=/sbin         \
         --sbindir=/sbin        \
         --libdir=/usr/lib      \
         --sysconfdir=/etc      \
         --libexecdir=/lib      \
         --with-rootprefix=     \
         --with-rootlibdir=/lib \
         --enable-split-usr     \
         --enable-static        \
         --disable-manpages "

    if get.buildTYPE() == "emul32":
        j += "--libdir=/usr/lib32 --libexecdir=/lib32 --with-rootlibdir=/lib32"

    autotools.configure(j)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s%s" % (get.installDIR(), suffix))
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # emul32 stop here
    if get.buildTYPE() == "emul32":
        shelltools.move("%s%s/lib32" % (get.installDIR(), suffix), "%s/lib%s" % (get.installDIR(), suffix))
        shelltools.move("%s%s/usr/lib32" % (get.installDIR(), suffix), "%s/usr/lib%s" % (get.installDIR(), suffix))
        #for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
        #    pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "emul32", "usr")
        #shelltools.unlinkDir("%s%s" % (get.installDIR(), suffix))
        shelltools.unlink("%s/usr/lib%s/libudev.so" % (get.installDIR(), suffix))
        pisitools.dosym("/lib%s/libudev.so.1.6.3" % suffix, "/usr/lib%s/libudev.so" % suffix)
        #shelltools.unlinkDir("%s/usr/lib%s/pkgconfig" % (get.installDIR(), suffix))
        shelltools.unlinkDir("%s/lib%s/udev" % (get.installDIR(), suffix))
        return

    #add link
    pisitools.dosym("/sbin/udevadm", "/bin/udevadm")

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /sbin/systemd-udevd -> /sbin/udevd sysmlink, we need it for MUDUR, do not touch this sysmlink.
    # pisitools.dosym("/lib/systemd/systemd-udevd", "/sbin/systemd-udevd")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")
    pisitools.dodir("/run/udev")

    # Add man files
    pisitools.doman("man/*.5", "man/*.7", "man/*.8")

    pisitools.dodoc("README*", "NOTES")
