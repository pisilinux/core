#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi.shelltools import system
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doman("sbin/update-ca-certificates.8")

    system("find ./mozilla -name '*.crt' | sort | cut -b3- > ca-certificates.conf")
    pisitools.insinto("/etc", "ca-certificates.conf")

    pisitools.dodir("/etc/ssl/certs")
    pisitools.dodir("/etc/ca-certificates/update.d")
