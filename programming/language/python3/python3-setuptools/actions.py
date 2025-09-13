# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="setuptools-%s" % get.srcVERSION()

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","78.1.1")

#def setup():
    #shelltools.makedirs("%s/setuptools-54.2.0/build/scripts-3.8" % get.workDIR())
    
def build():
    pythonmodules.compile(pyVer="3 -B")
    
    
    
def install():
    pythonmodules.install(pyVer="3 -B")

    pisitools.removeDir("/usr/lib/python3.11/site-packages/setuptools/_vendor")

    shelltools.system("find %s -name '*.py' -exec sed \
                                          -e 's:from \w*[.]\+extern ::' -e 's:\w*[.]\+extern[.]::' \
                                          -i {} + || die" % get.installDIR())
