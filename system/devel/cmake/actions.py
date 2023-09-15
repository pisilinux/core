# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #This command disables applications using cmake from attempting to install files in /usr/lib64/
    pisitools.dosed('Modules/GNUInstallDirs.cmake', '"lib64"', '"lib"')
    autotools.rawConfigure("--parallel=%s \
                            --system-libs \
                            --no-qt-gui \
                            --prefix=/usr \
                            --no-system-jsoncpp  \
                            --no-system-librhash \
                            --no-system-cppdap   \
                            --datadir=/share/cmake \
                            --docdir=/share/doc/cmake \
                            --mandir=/share/man" % get.makeJOBS().replace("-j", ""))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
