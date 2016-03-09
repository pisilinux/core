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
   
    #for polkit
    pisitools.rename("/usr/lib/pkgconfig/mozjs-..pc", "mozjs-17.0.pc")
    pisitools.remove("usr/lib/libmozjs-..a")
    
    pisitools.dodoc("README*")
    
    # add link for polkit
    pisitools.dosym("libmozjs-..so", "/usr/lib/libmozjs-17.0.so")
