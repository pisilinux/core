#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("watch.c", "ncursesw/ncurses.h", "ncurses.h")
    
    autotools.configure("--prefix=/usr \
                         --exec-prefix=/ \
                         --disable-static \
                         --sysconfdir=/etc \
                         --libdir=/usr/lib \
                         --bindir=/usr/bin \
                         --sbindir=/usr/bin \
                         --enable-watch8bit \
                         --without-systemd")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('ln_f="ln -sf" ldconfig="true" lib64=lib DESTDIR=%s' % get.installDIR())
    
    #remove conflicts
    pisitools.remove("/usr/bin/kill")
    pisitools.remove("/usr/bin/pidof")
    pisitools.remove("/usr/share/man/man1/kill.1")
    pisitools.remove("/usr/share/man/man1/pidof.1")
    
    # for mudur and comar
    pisitools.dosym("/usr/bin/sysctl", "/sbin/sysctl")
    pisitools.dosym("/usr/bin/ps", "/bin/ps")

    #pisitools.dosym("libproc-%s.so" % get.srcVERSION(), "/lib/libproc.so")

    pisitools.dodoc("NEWS", "ps/HACKING")
