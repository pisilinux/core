#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

arch = "x86-64" if get.ARCH() == "x86_64" and not get.buildTYPE() == "emul32" else "i686"
defaultflags = "-O3 -g -fasynchronous-unwind-tables -mtune=generic -march=%s" % arch
if get.buildTYPE() == "emul32": defaultflags += " -m32"

def setup():
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    shelltools.export("CC", "gcc %s " % defaultflags)
    shelltools.export("CXX", "g++ %s " % defaultflags)

    shelltools.export("CFLAGS", defaultflags)
    shelltools.export("CXXFLAGS", defaultflags)

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
        # shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

        shelltools.cd("build-libxcrypt")
        shelltools.system("../configure --prefix=/usr \
                           --libdir=/usr/lib32 \
                           --libexecdir=/usr/lib32 \
                           --disable-static \
                           --enable-hashes=strong,glibc \
                           --enable-obsolete-api=no \
                           --disable-failure-tokens \
                           --enable-multi-arch i686-pc-linux-gnu")

        shelltools.cd("..")

        shelltools.cd("build-libxcrypt-compat")
        # autotools.autoreconf("-fi")
        autotools.system("../configure --prefix=/usr \
                          --libdir=/usr/lib32 \
                          --libexecdir=/usr/lib32 \
                          --disable-static \
                          --enable-hashes=strong,glibc \
                          --enable-obsolete-api=glibc \
                          --disable-failure-tokens \
                          --enable-multi-arch i686-pc-linux-gnu")

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
        pisitools.dosym("/usr/lib/libcrypt.so.1.1.0", "/lib/libcrypt.so.1")
        pisitools.dosym("/usr/lib32/libcrypt.so.1.1.0", "/lib32/libcrypt.so.1")
        return

    # Fix conflicts with glibc
    # pisitools.rename("/usr/lib/libcrypt.so", "libxcrypt.so")
    # pisitools.rename("/usr/include/crypt.h", "xcrypt.h")

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING.LIB")
