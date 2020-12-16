#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's:doc/testasciidoc.1::' Makefile.in")
    shelltools.system("rm -rf doc/testasciidoc.1.txt")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install-sh" % get.installDIR())

    # Move data files and create symlinks for asciidoc to work
    for d in ("dblatex", "docbook-xsl", "images", "javascripts", "stylesheets"):
        pisitools.domove("/etc/asciidoc/%s" % d, "/usr/share/asciidoc")
        pisitools.dosym("/usr/share/asciidoc/%s" % d, "/etc/asciidoc/%s" % d)

    # Python module
    pisitools.insinto("/usr/lib/%s/site-packages" % get.curPYTHON(), "asciidocapi.py")

    # Vim syntax and filetype plugins
    #pisitools.insinto("/usr/share/vim/vimfiles/syntax/" , "vim/syntax/asciidoc.vim")

    pisitools.dodoc("BUGS*", "CHANGELOG*", "README*")
    pisitools.dodoc("docbook-xsl/asciidoc-docbook-xsl.txt", "filters/code/code-filter-readme.txt")
