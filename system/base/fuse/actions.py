# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("MOUNT_FUSE_PATH", "/usr/bin")
    shelltools.system("sh makeconf.sh")

    # Disable device node creation during build/install
    # pisitools.dosed("util/Makefile.in", "mknod", "echo Disabled: mknod ")

    autotools.configure("--prefix=/usr \
                         --libdir=/usr/lib \
                         --enable-lib \
                         --enable-util \
                         --disable-example \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/lib")
    pisitools.domove("/usr/lib/libfuse.so.*", "/lib")
    shelltools.system("ln -sfv %s/lib/libfuse.so.%s %s/usr/lib/libfuse.so" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("ln -sfv %s/lib/libfuse.so.%s %s/lib/libfuse.so" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    
    pisitools.domove("/usr/lib/libulockmgr.so.*", "/lib")
    shelltools.system("ln -sfv %s/lib/libulockmgr.so.%s %s/usr/lib/libulockmgr.so" % (get.installDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("ln -sfv %s/lib/libulockmgr.so.%s %s/lib/libulockmgr.so" % (get.installDIR(), get.srcVERSION(), get.installDIR()))

    shelltools.system("install -v -m755 -d %s/usr/share/doc/fuse-%s" % (get.installDIR(), get.srcVERSION()))
    shelltools.system("install -v -m644 doc/kernel.txt %s/usr/share/doc/fuse" % get.installDIR())
    # shelltools.system("cp -Rv doc/html %s/usr/share/doc/fuse-%s" % (get.installDIR(), get.srcVERSION()))

    pisitools.remove("/usr/lib/libfuse.la")
    pisitools.remove("/usr/lib/libulockmgr.la")

    pisitools.removeDir("/dev")
    # pisitools.removeDir("/etc")

    # Make compat symlinks into /usr/bin
    # pisitools.dosym("/bin/fusermount", "/usr/bin/fusermount")
    # pisitools.dosym("/bin/ulockmgr_server", "/usr/bin/ulockmgr_server")

    # Move pkgconfig file to /usr/lib
    # pisitools.domove("/lib/pkgconfig", "/usr/lib/")
    
    pisitools.dosed("%s/usr/lib/pkgconfig" % get.installDIR(), "/usr/lib", "/lib")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README.NFS")
