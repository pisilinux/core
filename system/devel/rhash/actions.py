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
    
def install():
    autotools.make("PREFIX=/usr DESTDIR=%s build-shared install-gmo install-lib-shared" % get.installDIR())
    autotools.make("PREFIX=/usr DESTDIR=%s -C librhash install-so-link install-headers" % get.installDIR())
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("ChangeLog", "INSTALL*", "README", "COPYING")

