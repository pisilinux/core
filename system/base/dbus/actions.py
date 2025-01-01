#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools


def setup():
    # pisitools.dosed("configure.ac", '(AS_AC_EXPAND\(EXPANDED_LOCALSTATEDIR, )"\$localstatedir"\)', r'\1 "")')
    # for f in ["bus/Makefile.am", "bus/Makefile.in"]:
        # pisitools.dosed(f, "\$\(localstatedir\)(\/run\/dbus)", "\\1")
    options = "\
               -Dselinux=disabled \
               -Druntime_dir=/run \
               -Dasserts=false \
               -Dchecks=false \
               -Dmodular_tests=disabled \
               -Ddoxygen_docs=disabled \
               -Dlibaudit=disabled \
               -Dinotify=enabled \
               -Duser_session=true \
               -Dsystemd=disabled \
               -Dsystemd_system_unitdir=disabled \
               -Dsystemd_user_unitdir=disabled \
               -Dsystem_pid_file=/run/dbus/pid \
               -Dsystem_socket=/run/dbus/system_bus_socket \
               -Dsession_socket_dir=/tmp \
               -Ddbus_user=dbus \
               -Dxml_docs=disabled"

                # --with-console-auth-dir=/run/console/ \
                # --enable-abstract-sockets=auto \

    if get.buildTYPE() == "_emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")
        shelltools.export("LDFLAGS", "%s -L/usr/lib32"  % get.LDFLAGS())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " \
                     --libdir=/usr/lib32 \
                     -Dx11_autolaunch=disabled \
                     -Ddoxygen_docs=disabled \
                   "

    mesontools.configure(options)

def build():
    mesontools.build()

def check():
    mesontools.build("test")

def install():
    mesontools.install()
    if get.buildTYPE() == "_emul32":
        # pisitools.removeDir("/usr/bin32")
        pisitools.dosed("%s/usr/lib32/pkgconfig/*.pc" % get.installDIR(), "bin32", "bin")
        return

    # needs to exist for the system socket
    pisitools.dodir("/run/dbus")
    pisitools.dodir("/var/lib/dbus")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "doc/TODO", "doc/*.txt")
    pisitools.dohtml("doc/")
