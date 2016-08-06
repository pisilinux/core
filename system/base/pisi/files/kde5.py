# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.

# ActionsAPI Modules
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

basename = "kde5"

prefix = "/%s" % get.defaultprefixDIR()
libdir = "%s/lib" % prefix
bindir = "%s/bin" % prefix
libexecdir = "%s/lib" % prefix
iconsdir = "%s/share/icons" % prefix
applicationsdir = "%s/share/applications/%s" % (prefix, basename)
mandir = "/%s" % get.manDIR()
sharedir = "%s/share" % prefix
localedir = "%s/share/locale" % prefix
qmldir = "%s/lib/qt5/qml" % prefix
plugindir = "%s/lib/qt5/plugins" % prefix
moduledir = "%s/lib/qt5/mkspecs/modules" % prefix
pythondir = "%s/bin/python" % prefix
appsdir = "%s" % sharedir
sysconfdir= "/etc"
configdir = "%s/xdg" % sysconfdir
servicesdir = "%s/services" % sharedir
servicetypesdir = "%s/servicetypes" % sharedir
includedir = "%s/include" % prefix
docdir = "/%s/%s" % (get.docDIR(), basename)
htmldir = "%s/html" % docdir
wallpapersdir = "%s/share/wallpapers" % prefix

def configure(parameters = '', installPrefix = prefix, sourceDir = '..'):
    ''' parameters -DLIB_INSTALL_DIR="hede" -DSOMETHING_USEFUL=1'''

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DKDE_INSTALL_LIBEXECDIR=%s \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                          -DKDE_INSTALL_QMLDIR=%s \
                          -DKDE_INSTALL_SYSCONFDIR=%s \
                          -DKDE_INSTALL_PLUGINDIR=%s \
                          -DECM_MKSPECS_INSTALL_DIR=%s \
                          -DBUILD_TESTING=OFF \
                          -DKDE_INSTALL_LIBDIR=lib \
                          -Wno-dev \
                          -DCMAKE_INSTALL_PREFIX=%s %s" % (libexecdir, qmldir, sysconfdir, plugindir, moduledir, prefix, parameters), installPrefix, sourceDir)

    shelltools.cd("..")

def make(parameters = ''):
    cmaketools.make('-C build %s' % parameters)

def install(parameters = '', argument = 'install'):
    cmaketools.install('-C build %s' % parameters, argument)

