#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
		                 --with-lzo2 \
		                 ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosed("%s/usr/lib/pkgconfig/libarchive.pc" % get.installDIR(), "iconv", "")

    pisitools.dodoc("COPYING","NEWS")
