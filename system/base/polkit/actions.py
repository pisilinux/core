#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("meson.build", "pardus", "pisilinux")
    pisitools.dosed("meson_options.txt", "pardus", "pisilinux")
    #pisitools.dosed("configure", "pardus-release", "pisilinux-release")
    #autotools.autoreconf("-fiv")
    mesontools.configure("-Dos_type='pisilinux' \
                          -Dsystemdsystemunitdir=/tmp \
                          -Dpam_module_dir=/lib/security \
                          -Dexamples=true \
                          -Dauthfw='pam' \
                          -Djs_engine='duktape' \
                          -Dsession_tracking=libelogind")

def build():
    shelltools.export('HOME', get.workDIR())
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodir("/var/lib/polkit-1")
    shelltools.chmod("%s/var/lib/polkit-1" % get.installDIR(), mode=00700)
    shelltools.chmod("%s/etc/polkit-1/rules.d" % get.installDIR(), mode=00700)
    shelltools.chown("%s/etc/polkit-1/rules.d" % get.installDIR(),"polkitd","root") #yada? "polkitd","root"
    shelltools.chown("%s/var/lib/polkit-1" % get.installDIR(),"polkitd","polkitd")
    shelltools.chown("%s/usr/share/polkit-1" % get.installDIR(),"polkitd","root") #yada? "polkitd","root"

    pisitools.removeDir("/tmp")

    pisitools.dodoc("AUTHORS", "NEWS*", "README*", "HACKING*", "COPYING*")
