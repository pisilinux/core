# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#WorkDir = "mozjs%s/js/src" % get.srcVERSION()

def setup():
   shelltools.cd("js/src")
   shelltools.system("sed -i 's/(defined\((@TEMPLATE_FILE)\))/\1/' config/milestone.pl ")
   
   autotools.configure("--prefix=/usr       \
                        --enable-readline   \
                        --enable-threadsafe \
                        --with-system-ffi   \
                        --with-system-nspr")

def build():
    shelltools.cd("js/src")
    autotools.make()

def install():
    shelltools.cd("js/src")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
   
    pisitools.dodir("/usr/include/js-17.0")
    pisitools.domove("/usr/include/js-./*", "/usr/include/js-17.0")
    pisitools.rename("/usr/lib/pkgconfig/mozjs-..pc", "mozjs-17.0.pc")
    pisitools.removeDir("/usr/include/js-.")
    pisitools.rename("/usr/lib/libmozjs-..so", "libmozjs-17.0.so")
    pisitools.rename("/usr/bin/js", "js17")
    pisitools.rename("/usr/bin/js-config", "js17-config")
    pisitools.dodoc("README*")
