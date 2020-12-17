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
    shelltools.touch("ChangeLog")
    pisitools.flags.add("-fPIC -D_GNU_SOURCE")
    
    shelltools.system("./conf.sh")
        
    autotools.autoreconf("-fi")
    autotools.configure("--libdir=/usr/lib \
                         --enable-nls \
                         --disable-doc \
                         --disable-audit \
                         --enable-usergroups \
                         --enable-securedir=/lib/security \
                         --enable-isadir=/lib/security")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    # Update .po files
    autotools.make("-C po update-gmo")

    autotools.make()

def check():
    autotools.make("check")

    # dlopen check
    shelltools.system("./dlopen-test.sh")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.removeDir("/usr/share/doc/Linux-PAM/")
    for f in ["system-password", "system-session", "system-account"]:
        pisitools.insinto("/etc/pam.d/", "%s" % f)
    
    #pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")
