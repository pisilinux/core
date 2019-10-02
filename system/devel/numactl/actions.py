#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")    
    autotools.configure("--prefix=/usr")
      
    
def build():
    autotools.make("CFLAGS='%s -I.'" % get.CFLAGS())

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")
    pisitools.removeDir("/usr/share/man/man2")

    pisitools.dodoc("LICENSE.GPL2", "README.md")
