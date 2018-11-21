#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('OPT="%s" \
                    SHARED="yes" \
                    PREFIX=/usr \
                    IDSDIR="/usr/share/misc" \
                    all' % get.CFLAGS())

def install():
    autotools.rawInstall('DESTDIR="%s" \
                          PREFIX=/usr \
                          SHARED="yes" \
                          IDSDIR="/usr/share/misc" \
                          install-lib' % get.installDIR())
   
    # remove update-pciids
    pisitools.remove("/usr/sbin/update-pciids")
    pisitools.remove("/usr/share/man/man8/update-pciids.8")

