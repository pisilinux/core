#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--libexecdir=/usr/lib/dhcpcd \
                         --dbdir=/var/lib/dhcpcd \
                         --localstatedir=/var \
                         --sbindir=/usr/bin \
                         --rundir=/run")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # Set Options in /etc/dhcpcd.conf Disable ip4vall
    shelltools.echo("%s/etc/dhcpcd.conf" % get.installDIR(), "noipv4ll")
    # Remove hooks install the compat one
    pisitools.remove("/usr/lib/dhcpcd/dhcpcd-hooks/*")
    pisitools.insinto("/usr/lib/dhcpcd/dhcpcd-hooks", "dhcpcd-hooks/50-dhcpcd-compat")

    pisitools.dodoc("README")
#DBDIR=/var/lib/dhcpcd LIBEXECDIR=/usr/lib/dhcpcd
