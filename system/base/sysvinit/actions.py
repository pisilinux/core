#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sysvinit-%s" % get.srcVERSION()

def build():
    autotools.make("-C src CC=\"%s\" CFLAGS=\"%s -D_GNU_SOURCE\" LCRYPT=\"-lcrypt\"" % (get.CC(), get.CFLAGS()))

def install():
    shelltools.cd("src")
    autotools.rawInstall("ROOT='%s' STRIP=/bin/true" % get.installDIR())

    pisitools.remove("/bin/pidof")
    # These files conflict with e2fsprogs
    pisitools.remove("/sbin/logsave")
    pisitools.remove("/usr/share/man/man8/logsave.8")
    
    pisitools.dosym("killall5", "/sbin/pidof")
