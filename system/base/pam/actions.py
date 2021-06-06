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
    pisitools.flags.add("-fPIC -D_GNU_SOURCE")
    shelltools.system("sed -e /service_DATA/d \
                       -i modules/pam_namespace/Makefile.am && NOCONFIGURE=1 ./autogen.sh")

    shelltools.system("./pisi-pambase.sh")

    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --libdir=/usr/lib \
                         --disable-regenerate-docu \
                         --disable-doc \
                         --enable-securedir=/lib/security \
                         --docdir=/usr/share/doc/Linux-PAM-" + get.srcVERSION())

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.removeDir("/usr/share/doc/Linux-PAM/")
    for f in ["system-password", "system-session", "system-account", "system-auth", "other"]:
        shelltools.system("chmod 755 " + f)
        pisitools.insinto("/etc/pam.d/", "%s" % f)

    shelltools.system("chmod -v 4755 " + get.installDIR() + "/sbin/unix_chkpwd")

    #pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")
