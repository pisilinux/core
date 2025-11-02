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
    shelltools.system("mkdir build-libxcrypt build-libxcrypt-compat")

    if not get.buildTYPE() == "emul32":
        shelltools.cd("build-libxcrypt")
        # autotools.autoreconf("-fi")
        shelltools.system("../configure --prefix=/usr \
                         --disable-static \
                         --enable-hashes=strong,glibc \
                         --enable-obsolete-api=no \
                         --disable-failure-tokens")

        shelltools.cd("..")

        shelltools.cd("build-libxcrypt-compat")
        # autotools.autoreconf("-fi")
        autotools.system("../configure --prefix=/usr \
                         --disable-static \
                         --enable-hashes=strong,glibc \
                         --enable-obsolete-api=glibc \
                         --disable-failure-tokens")

        shelltools.cd("..")

    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

        shelltools.cd("build-libxcrypt")
        shelltools.system("../configure --prefix=/usr \
                           --libdir=/usr/lib32 \
                           --libexecdir=/usr/lib32 \
                           --disable-static \
                           --enable-hashes=strong,glibc \
                           --enable-obsolete-api=no \
                           --disable-failure-tokens")

        shelltools.cd("..")

        shelltools.cd("build-libxcrypt-compat")
        # autotools.autoreconf("-fi")
        autotools.system("../configure --prefix=/usr \
                          --libdir=/usr/lib32 \
                          --libexecdir=/usr/lib32 \
                          --disable-static \
                          --enable-hashes=strong,glibc \
                          --enable-obsolete-api=glibc \
                          --disable-failure-tokens")

        # shelltools.cd("..")

def build():
    shelltools.cd("build-libxcrypt")
    autotools.make()

    shelltools.cd("..")
    shelltools.cd("build-libxcrypt-compat")
    autotools.make()

def install():
    shelltools.cd("build-libxcrypt")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    shelltools.cd("build-libxcrypt-compat")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        return

    # Fix conflicts with glibc
    # pisitools.rename("/usr/lib/libcrypt.so", "libxcrypt.so")
    # pisitools.rename("/usr/include/crypt.h", "xcrypt.h")

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING.LIB")
