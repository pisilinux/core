#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("echo -e '\033[0;36mBuilding Bzip2\033[0m' ")
    shelltools.makedirs("%s/temp/lib" %get.workDIR())
    shelltools.cd("bzip2-1.0.8")
    autotools.make('CC=%s AR=%s RANLIB=%s CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC" libbz2.a' % (get.CC(), get.AR(), get.RANLIB(), get.CFLAGS()))
    shelltools.system("cp libbz2.a %s/temp/lib/libbz2.a" % get.workDIR())
    shelltools.cd("..")
	
    pisitools.flags.add("-fwrapv")

    pisitools.dosed("Lib/cgi.py","^#.* /usr/local/bin/python","#!/usr/bin/python")

    shelltools.unlinkDir("Modules/expat")
    #shelltools.unlinkDir("Modules/zlib")
    shelltools.unlinkDir("Modules/_ctypes/darwin")
    #shelltools.unlinkDir("Modules/_ctypes/libffi")
    #shelltools.unlinkDir("Modules/_ctypes/libffi_msvc")
    shelltools.unlinkDir("Modules/_ctypes/libffi_osx")
    #shelltools.unlinkDir("Modules/_decimal/libmpdec")
    
    shelltools.export("CFLAGS", "-I%s/temp/include -O3" %get.workDIR())
    shelltools.export("LDFLAGS", "-L%s/temp/lib -lbz2 -lpthread -ldl" %get.workDIR())
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    autotools.rawConfigure("\
                            --prefix=/usr \
                            --enable-shared \
                            --with-threads \
                            --with-computed-gotos \
                            --enable-ipv6 \
                            --with-system-expat \
                            --with-dbmliborder=gdbm:ndbm \
                            --with-system-ffi \
                            --with-system-libmpdec \
                            --enable-loadable-sqlite-extensions \
                            --without-ensurepip")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/bin/2to3")
    pisitools.dodoc("LICENSE", "README.*")
    
    pisitools.removeDir("/usr/lib/python3.8/idlelib")
    pisitools.removeDir("/usr/lib/python3.8/tkinter")
    pisitools.removeDir("/usr/lib/python3.8/turtledemo")
    pisitools.remove("/usr/bin/idle3*")
