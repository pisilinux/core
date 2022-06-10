#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2019 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s MANDIR=/usr/share/man FIRMWARE_PATH=/lib/firmware CRDA_KEY_PATH=/etc/wireless-regdb/pubkeys" % get.installDIR())
    #pisitools.insinto("/usr/lib/crda/", "regulatory.bin")
    #pisitools.insinto("/lib/firmware", "regulatory.db*")
    #pisitools.insinto("/etc/wireless-regdb/pubkeys", "sforshee.key.pub.pem")
    
    #pisitools.doman("regulatory.db.5")

    pisitools.dodoc("LICENSE", "README", "CONTRIBUTING")
