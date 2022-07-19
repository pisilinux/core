#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("configure.ac", "pardus-release", "pisilinux-release")
    #pisitools.dosed("configure", "pardus-release", "pisilinux-release")
    autotools.autoreconf("-f")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --with-pam-module-dir=/lib/security/ \
                         --with-duktape \
                         --with-dbus \
                         --enable-examples \
                         --enable-introspection \
                         --with-systemdsystemunitdir=no \
                         --enable-libsystemd-login=no \
                         --enable-libelogind=yes \
                         --disable-man-pages \
                         --enable-gtk-doc=no \
                         --enable-gtk-doc-html=no \
                         --enable-gtk-doc-pdf=no \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.export('HOME', get.workDIR())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.dodir("/var/lib/polkit-1")
    shelltools.chmod("%s/var/lib/polkit-1" % get.installDIR(), mode=00700)
    shelltools.chmod("%s/etc/polkit-1/rules.d" % get.installDIR(), mode=00700)
    shelltools.chown("%s/etc/polkit-1/rules.d" % get.installDIR(),"polkitd","root") #yada? "polkitd","root"
    shelltools.chown("%s/var/lib/polkit-1" % get.installDIR(),"polkitd","polkitd")
    shelltools.chown("%s/usr/share/polkit-1" % get.installDIR(),"polkitd","root") #yada? "polkitd","root"
    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING", "COPYING")
