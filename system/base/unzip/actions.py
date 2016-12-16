#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def build():

    shelltools.system('sed -i "/MANDIR =/s#)/#)/share/#" unix/Makefile')

    opt='-DACORN_FTYPE_NFS \
         -DWILD_STOP_AT_DIR \
         -DLARGE_FILE_SUPPORT \
         -DUNICODE_SUPPORT \
         -DUNICODE_WCHAR \
         -DUTF8_MAYBE_NATIVE \
         -DNO_LCHMOD \
         -DDATE_FORMAT=DF_YMD \
         -DUSE_BZIP2 -DNOMEMCPY \
         -DNO_WORKING_ISPRINT'


    autotools.make('-f unix/Makefile prefix=/usr D_USE_BZ2=-DUSE_BZIP2 L_BZ2=-lbz2 LF2="%s" CF="%s -I. %s" unzips'% (get.LDFLAGS(),get.CFLAGS(),opt))


def install():
    autotools.make("-f unix/Makefile prefix=%s/usr install" % get.installDIR())


    pisitools.doman("man/*.1")
    pisitools.dodoc("BUGS", "History*", "README", "ToDo", "WHERE" , "LICENSE")