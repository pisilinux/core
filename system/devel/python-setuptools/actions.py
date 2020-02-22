# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="setuptools-%s" % get.srcVERSION()

def build():
    pythonmodules.run("bootstrap.py")
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.rename("/usr/bin/easy_install", "py2easy-install")
    pisitools.remove("/usr/lib/%s/site-packages/setuptools/*.exe" % get.curPYTHON())