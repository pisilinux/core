#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    #shelltools.system("sed -i '211,217 d; 219,229 d; 232 d' lib/glob.c")
    autotools.configure("--enable-nls \
                         --program-prefix=g")

def build():
    autotools.make()

#def check():
    #shelltools.export("LANG", "C")
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("gmake", "/usr/bin/make")
    pisitools.dosym("gmake.1","/usr/share/man/man1/make.1")

    pisitools.dodoc("AUTHORS", "NEWS", "README*")
