# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="setuptools-%s" % get.srcVERSION()

#def setup():
    #shelltools.makedirs("%s/setuptools-54.2.0/build/scripts-3.8" % get.workDIR())
    
def build():
    pythonmodules.compile(pyVer="3")
    
    
    
def install():
    pythonmodules.install(pyVer="3")
