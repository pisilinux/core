# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    ##shelltools.export("CFLAGS","%s -fPIC -DPIC" % get.CFLAGS())
    #shelltools.export("LDFLAGS","%s -fPIC" % get.LDFLAGS())
    shelltools.system("./configure --prefix=/usr \
                                   --sysconfdir=/etc \
                                   --enable-lib-shared \
                                   --enable-gettext \
                                   --disable-openssl-runtime \
                                   --enable-openssl")
	
def check():
	autotools.make("test test-lib")
    
def install():
    autotools.make()
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s install-lib-headers install-lib-shared install" % get.installDIR())
    
    pisitools.dosym("usr/lib/librhash.so.0", "/usr/lib/librhash.so")
    
    pisitools.dodoc("ChangeLog", "INSTALL*", "README.md")

