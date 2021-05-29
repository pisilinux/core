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
    if get.buildTYPE() != "emul32":
        autotools.autoreconf("-fi")
    
    options = "--disable-static \
               --enable-noexecstack"

    if get.buildTYPE() == "emul32":
        shelltools.system("sed 's:i586\*-\*-\*:x86_64-*-*:' -i mpi/config.links")
        shelltools.system("sed 's:x86_64-\*-\*:ignore:;s:i?86-\*-\*:x86_64-*-*:' -i configure.ac")
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        
        autotools.autoreconf("-fi")
        options += " --libdir=/usr/lib32 --bindir=/usr/bin32"

        # Use 32-bit assembler, another option is to use --disable-asm option
        #pisitools.dosed("mpi/config.links", "path=\"amd64\"", "path=\"i586 i386\"")
        

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/bin32")
        return

    pisitools.dodir("/etc/gcrypt")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "THANKS", "TODO")
