#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export('CFLAGS', get.CFLAGS().replace('-pipe', '').replace(' -g ', ' -g3 ') + ' -Wall')
shelltools.export('CXXFLAGS', get.CXXFLAGS().replace('-pipe', '').replace(' -g ', ' -g3 ') + ' -Wall')


def setup():
    pisitools.dosed("gcc/Makefile.in", "\.\/fixinc\.sh", "-c true")
    pisitools.dosed("gcc/config/i386/t-linux64", "m64=../lib64", "m64=../lib")
    pisitools.dosed("gcc/configure", "^(ac_cpp='\$CPP\s\$CPPFLAGS)", r"\1 -O2")
    pisitools.dosed("libiberty/configure", "^(ac_cpp='\$CPP\s\$CPPFLAGS)", r"\1 -O2")

    shelltools.move("isl-0.21", "isl")
    shelltools.move("mpfr-4.0.2", "mpfr")
    shelltools.move("mpc-1.1.0", "mpc")
    shelltools.move("gmp-6.1.2", "gmp")

    shelltools.makedirs("../build")
    shelltools.cd("../build")

    shelltools.system('../gcc-%s/configure \
                       --prefix=/usr \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib \
                       --libexecdir=/usr/lib \
                       --includedir=/usr/include \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-bugurl=https://pisilinux.org/bugs \
                       --enable-languages=c,c++,fortran,lto,objc,obj-c++ \
                       --enable-shared \
                       --enable-threads=posix \
                       --with-system-zlib \
                       --enable-__cxa_atexit \
                       --disable-libunwind-exceptions \
                       --enable-clocale=gnu \
                       --disable-libstdcxx-pch \
                       --disable-libssp \
                       --enable-gnu-unique-object \
                       --enable-linker-build-id \
                       --enable-lto \
                       --enable-plugin \
                       --with-linker-hash-style=gnu \
                       --with-pkgversion="Pisi Linux" \
                       --disable-werror \
                       --enable-checking=release \
                       --enable-install-libiberty \
                       --enable-gnu-indirect-function \
                       --enable-multilib \
                       --enable-default-pie \
                       --enable-default-ssp \
                       --enable-cet' % get.srcVERSION())


def build():
    shelltools.cd("../build")
    autotools.make()


def check():
    shelltools.cd("../build")
    autotools.make("-k check || true")
    shelltools.system("%s/gcc/contrib/test_summary" % get.srcDIR())


def install():
    shelltools.cd("../build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Not needed
    pisitools.removeDir("/usr/lib/gcc/*/*/include-fixed")

    # cc symlink
    pisitools.dosym("/usr/bin/gcc", "/usr/bin/cc")

    # /lib/cpp symlink for legacy X11 stuff
    pisitools.dosym("/usr/bin/cpp", "/lib/cpp")

    # TODO: Add liblto_plugin.so link to necessary place.

    gdbpy_files = shelltools.ls("%s/usr/lib/*gdb.py" % get.installDIR())
    for i in gdbpy_files:
        pisitools.domove("/usr/lib/%s" % shelltools.baseName(i), "/usr/share/gdb/auto-load/usr/lib")
