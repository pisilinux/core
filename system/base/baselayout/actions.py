# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def build():
    # NOTE: This is only for the start-stop-daemon
    autotools.make('-C src CC="%s" LD="%s %s" CFLAGS="%s"' % (get.CC(), get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    def chmod(path, mode):
        shelltools.chmod("%s%s" % (get.installDIR(), path), mode)

    # Install everything
    pisitools.insinto("/", "root/*")

    # Install baselayout utilities
    shelltools.cd("src/")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    shelltools.system("ls")

    # Dirty fix for now... (especially for flatpak)
    shelltools.system("mv %s/run/* %s/dev" % (get.installDIR(), get.installDIR()))
    pisitools.remove("/var/lock")
    # shelltools.cd("%s/var" % get.installDIR())
    shelltools.system("ln -rs %s/dev/lock %s/var/lock" % (get.installDIR(), get.installDIR()))
    # shelltools.cd("%s/baselayout/src" % get.workDIR())

    # Adjust permissions
    chmod("/tmp", 01777)
    chmod("/var/tmp", 01777)
    chmod("/dev/shm", 01777)
    chmod("/var/lock", 0775)
    chmod("/usr/share/baselayout/shadow", 0600)

    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        pisitools.dodir("/lib32")
        pisitools.dodir("/usr/lib32")

        # Hack for binary blobs built on multi-lib systems
        pisitools.dosym("lib", "/lib64")

    pisitools.dosym("pisilinux-release", "/etc/system-release")

    #File conflicts:
    pisitools.removeDir("/usr/share/man/man4")
