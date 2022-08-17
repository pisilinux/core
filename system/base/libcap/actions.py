#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools



pam = "no" if get.buildTYPE() == "emul32" else "yes"

cc = "'gcc -m32'" if get.buildTYPE() == "emul32" else "'gcc'"

pisitools.cflags.add("-D_LARGEFILE64_SOURCE", "-D_FILE_OFFSET_BITS=64")

def setup():
    # fix linkage
    pisitools.dosed("pam_cap/Makefile", "(.*<\s\$\(LDLIBS\))", r"\1 -lpam")
    # no static libs
    #pisitools.dosed("libcap/Makefile", "install.*STALIBNAME", deleteLine=True)
    shelltools.system("sed -i '/install -m.*STA/d' libcap/Makefile")
    # change shared libs mode
    #pisitools.dosed("libcap/Makefile", "(.*?install -m) 0644 (.*?MINLIBNAME.*)", r"\1 0755 \2")
    # use pisilinux flags
    #pisitools.dosed("Make.Rules", "^(CC|CFLAGS|LD)\s:=.*", deleteLine=True)

    pisitools.dosed("Make.Rules", "^(PAM_CAP\s:=).*", r"\1 %s" % ("no" if get.buildTYPE() == "emul32" else "yes"))



def build():
    autotools.make("prefix=/usr lib=lib%s PAM_CAP=%s CC=%s" % ("32" if get.buildTYPE() == "emul32" else "", pam, cc))

#def check():
    #autotools.make("test -k CC=%s PAM_CAP=%s" % (cc, pam))

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("DESTDIR=%s prefix=/usr lib=lib32 SBINDIR=/_emul32 MANDIR=/_emul32 RAISE_SETFCAP=no PAM_CAP=no" % get.installDIR())
        pisitools.removeDir("/_emul32")
        return

    autotools.rawInstall("prefix=/usr DESTDIR=%s SBINDIR=/sbin RAISE_SETFCAP=no" % (get.installDIR()))

    pisitools.insinto("/etc/security", "pam_cap/capability.conf")

    pisitools.dodoc("CHANGELOG", "License", "README", "doc/capability.notes")
