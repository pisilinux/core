#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' SHARED="yes"',
    ' PREFIX=/usr',
    ' IDSDIR="/usr/share/hwdata" '
    ])

def build():
    autotools.make('OPT="%s" %s all' % (get.CFLAGS(), j))

def install():
    autotools.rawInstall('DESTDIR="%s" %s install-lib' % (get.installDIR(), j))
   
    # remove update-pciids
    pisitools.remove("/usr/sbin/update-pciids")
    pisitools.remove("/usr/share/man/man8/update-pciids.8")

