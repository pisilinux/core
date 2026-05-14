#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools


def setup():
    mesontools.configure("-Dsystemd=disabled")

def build():
    mesontools.build()


def install():
    mesontools.install()

    pisitools.removeDir("/usr/lib/kernel")
    pisitools.removeDir("/usr/share/libalpm")

    pisitools.dodoc("LICENSE", "README.*")
