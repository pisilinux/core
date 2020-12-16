#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("makefile", " -O ", " $(CFLAGS) ")
    #shelltools.system("find . -type f -name \*.c -print0 | xargs -0 sed -i 's/YYSTACKSIZE 500/YYSTACKSIZE 10000/g'")
    autotools.configure("--disable-dependency-tracking")

def build():
    autotools.make()
    #autotools.make('-j1 CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))
    
#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dobin("yacc")
    
    pisitools.dosym("/usr/bin/yacc", "/usr/bin/byacc")
    pisitools.dosym("/usr/share/man/man1/yacc.1", "/usr/share/man/man1/byacc.1")

    #pisitools.doman("yacc.1")
    pisitools.dodoc("ACKNOWLEDGEMENTS", "NEW_FEATURES", "NOTES", "README*")
