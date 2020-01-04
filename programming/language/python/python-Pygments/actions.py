#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

#WorkDir="%s-%s" % (get.srcNAME().split("-")[1], get.srcVERSION())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.rename("/usr/bin/pygmentize","pygmentize-py2")

    #pisitools.dohtml("docs/build/*")
    #pisitools.insinto("/usr/share/doc/%s/src/" % get.srcNAME(),"docs/src/*")
    pisitools.insinto("/usr/share/man/man1", "doc/pygmentize.1", "pygmentize.1")

