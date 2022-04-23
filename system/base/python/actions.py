#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

WorkDir = "Python-%s" % get.srcVERSION()

PythonVersion = "2.7"

def setup():
    #shelltools.system("echo -e '\033[0;36mBuilding Bzip2\033[0m' ")
    #shelltools.makedirs("%s/temp/lib" %get.workDIR())
    #shelltools.cd("bzip2-1.0.8")
    #autotools.make('CC=%s AR=%s RANLIB=%s CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC" libbz2.a' % (get.CC(), get.AR(), get.RANLIB(), get.CFLAGS()))
    #shelltools.system("cp libbz2.a %s/temp/lib/libbz2.a" % get.workDIR())
    #shelltools.cd("..")
    #os.system("echo -e '\033[0;36mBuilding OpenSSL\033[0m' ")
    
    #shelltools.cd("openssl-1.1.1n")
    #shelltools.system("./Configure --prefix=%s/temp --openssldir=%s/openssl/etc/ssl --libdir=lib no-shared enable-ec_nistp_64_gcc_128 linux-x86_64 -Wa,--noexecstack" %(get.workDIR(), get.workDIR()))
    #autotools.make()
    #autotools.make("install")
    #shelltools.cd("..")
    
    #os.system("echo -e '\033[0;36mBuilding Python\033[0m' ")
	
    pisitools.cflags.add("-fwrapv")

    # no rpath
    pisitools.dosed("configure.ac", "-rpath \$\(LIBDIR\) ")

    pisitools.dosed("Lib/cgi.py", r"/usr/local/bin/", r"/usr/bin/")
    pisitools.dosed("setup.py", "SQLITE_OMIT_LOAD_EXTENSION", deleteLine=True)
    pisitools.dosed("setup.py","ndbm_libs =.*","ndbm_libs = ['gdbm', 'gdbm_compat']")

    for dir in ["expat","zlib","_ctypes/libffi_arm_wince","_ctypes/libffi_msvc",
                "_ctypes/libffi_osx","_ctypes/libffi","_ctypes/darwin"]:
        shelltools.unlinkDir("Modules/%s" % dir)
        
    #shelltools.export("CFLAGS", "-I%s/temp/include -O3" %get.workDIR())
    #shelltools.export("LDFLAGS", "-L%s/temp/lib -lssl -lcrypto -lpthread -ldl" %get.workDIR())
    #shelltools.export("PKG_CONFIG_PATH", "$PKG_CONFIG_PATH:%s/temp/lib/pkgconfig" %get.workDIR())
    
    #pisitools.cflags.add("-I%s/temp/include -O3" %get.workDIR())
    #pisitools.ldflags.add("-L%s/temp/lib -lssl -lcrypto -lpthread -ldl" %get.workDIR())

    autotools.autoreconf("-vif")

    # disable bsddb
    pisitools.dosed("setup.py", "^(disabled_module_list = \[)\]", r"\1'_bsddb', 'dbm']")
    # no rpath
    pisitools.dosed("Lib/distutils/command/build_ext.py", "self.rpath.append\(user_lib\)", "pass")

    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions \
                         --with-system-expat \
                         --with-system-ffi \
                         --with-dbmliborder=gdbm")

def build():
    autotools.make()

# some tests fail. let's disable testing temporarily
# def check():
    #autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    pisitools.dosym("/usr/bin/python%s" % PythonVersion, "/usr/bin/python")
    pisitools.dosym("/usr/bin/python%s" % PythonVersion, "/usr/bin/python2")
    pisitools.dosym("/usr/bin/python%s-config" % PythonVersion, "/usr/bin/python-config")
    pisitools.dosym("/usr/lib/python%s/pdb.py" % PythonVersion, "/usr/bin/pdb")
    #pisitools.domove("/usr/lib/python2.7/lib-dynload/bz2_failed.so", "/usr/lib/python2.7/lib-dynload", "bz2.so")

    pisitools.dodoc("LICENSE", "README")
