#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("CONFIG_SHELL", "/bin/bash")
    autotools.configure("--with-usrlibdir=/usr/lib \
                         --with-usrsbindir=%s \
                         --with-confdir=/etc \
                         --with-udevdir=/lib/udev/rules.d \
                         --with-default-pid-dir=/run \
                         --with-default-run-dir=/run/lvm \
                         --with-default-locking-dir=/run/lock/lvm \
                         --with-device-uid=0 \
                         --with-device-gid=6 \
                         --with-device-mode=0660 \
                         --with-cache=internal \
                         --with-snapshots=internal \
                         --with-mirrors=internal \
                         --with-thin=internal \
                         --with-interface=ioctl \
                         --enable-udev_rules \
                         --enable-udev_sync \
                         --disable-selinux \
                         --enable-readline \
                         --enable-fsadm \
                         --enable-applib \
                         --enable-cmdlib \
                         --enable-pkgconfig \
                         --enable-dmeventd \
                         --enable-lvmetad \
                         --enable-lvmpolld" % get.sbinDIR())

#    pisitools.dosed("make.tmpl","-lm","")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    for dir in ["archive", "backup", "cache"]:
        pisitools.dodir("/etc/lvm/%s" % dir)
        shelltools.chmod(get.installDIR() + "/etc/lvm/%s" % dir, 0755)
        shelltools.chown(get.installDIR() + "/etc/lvm/%s" % dir, uid = 'root', gid = 'root')

    shelltools.system("sed -i 's,use_lvmetad = 1,use_lvmetad = 1,' %s/etc/lvm/lvm.conf" % get.installDIR())

    #pisitools.move("/sbin/lvmconf","scripts/lvmconf.sh")

    pisitools.dodoc("COPYING", "COPYING.LIB", "README", "VERSION", "WHATS_NEW") # "VERSION_DM", "WHATS_NEW_DM"
