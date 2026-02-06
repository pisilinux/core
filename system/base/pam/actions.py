#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-fPIC -D_GNU_SOURCE")
    # shelltools.system("sed -e /service_DATA/d \
                       # -i modules/pam_namespace/Makefile.am && NOCONFIGURE=1 ./autogen.sh")

    shelltools.system("./pisi-pambase.sh")

    mesontools.configure("--buildtype=release \
                          --sbindir=/sbin \
                          -Ddocs=disabled \
                          -Dselinux=disabled \
                          -Dlogind=disabled \
                          -Dpam_userdb=disabled \
                          -Dpwaccess=disabled \
                          -Dsecuredir=/lib/security \
                          -Dvendordir='' \
                          -Ddocdir=/usr/share/doc/Linux-PAM-" + get.srcVERSION())

def build():
    mesontools.build()

def check():
    mesontools.build("test")

def install():
    mesontools.install()

    pisitools.removeDir("/usr/lib/systemd")

    for f in ["system-password", "system-session", "system-account", "system-auth", "other"]:
        shelltools.system("chmod 755 " + f)
        pisitools.insinto("/etc/pam.d/", "%s" % f)

    shelltools.system("chmod -v 4755 " + get.installDIR() + "/sbin/unix_chkpwd")

    #pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("COPYING", "Copyright", "README")
