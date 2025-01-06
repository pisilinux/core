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
    shelltools.system("export SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES=0")
    pythonmodules.compile(pyVer="3")
    
    
    
def install():
    pythonmodules.install(pyVer="3")

    pisitools.removeDir("/usr/lib/python3.11/site-packages/setuptools/_vendor")
    # pisitools.removeDir("/usr/lib/python3.11/site-packages/pkg_resources/_vendor")

    # pisitools.removeDir("/usr/lib/python3.11/site-packages/setuptools/extern")
    # pisitools.removeDir("/usr/lib/python3.11/site-packages/pkg_resources/extern")

    shelltools.system("find %s -name '*.py' -exec sed \
                                          -e 's:from \w*[.]\+extern ::' -e 's:\w*[.]\+extern[.]::' \
                                          -i {} + || die" % get.installDIR())
