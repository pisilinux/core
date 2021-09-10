#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/groups$(EXEEXT) //' src/Makefile.in && \
                       find man -name Makefile.in -exec sed -i 's/groups\.1 / /'   {} \; && \
                       find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \; && \
                       find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \; && \
                       sed -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' \
                       -e 's@/var/spool/mail@/var/mail@'                 \
                       -e '/PATH=/{s@/sbin:@@;s@/bin:@@}'                \
                       -i etc/login.defs                                 && \
                       sed -i 's/1000/100/' etc/useradd")

    shelltools.system("./pisi-shadowbase.sh")

    autotools.configure("--sysconfdir=/etc \
                         --with-group-name-max-length=32 \
                         --with-audit \
                         --with-libcrack \
                         --with-acl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.system("sed -i 's/yes/no/' " + get.installDIR() + "/etc/default/useradd")
    shelltools.system("install -v -m644 " + get.installDIR() + "/etc/login.defs{,.orig}")

    for f in ["login", "passwd", "su", "chage", "system-login"]:
        shelltools.system("chmod 755 " + f)
        pisitools.insinto("/etc/pam.d/", "%s" % f)

    for f in ["FAIL_DELAY", "FAILLOG_ENAB", "LASTLOG_ENAB", "MAIL_CHECK_ENAB", "OBSCURE_CHECKS_ENAB",
              "PORTTIME_CHECKS_ENAB", "QUOTAS_ENAB", "CONSOLE MOTD_FILE", "FTMP_FILE NOLOGINS_FILE",
              "ENV_HZ PASS_MIN_LEN", "SU_WHEEL_ONLY", "CRACKLIB_DICTPATH", "PASS_CHANGE_TRIES",
              "PASS_ALWAYS_WARN", "CHFN_AUTH ENCRYPT_METHOD", "ENVIRON_FILE"]:
        shelltools.system('sed -i "s/^' + f + '/# &/" ' + get.installDIR() + "/etc/login.defs")

    ### Pisi Linux specific preferences
    shelltools.system("sed -i 's;PATH=/usr/sbin:/usr/bin;PATH=/sbin:/bin:/usr/sbin:/usr/bin;g' " + get.installDIR() + "/etc/login.defs")
    shelltools.system("sed -i 's;PATH=/usr/bin;PATH=/sbin:/bin:/usr/sbin:/usr/bin;g' " + get.installDIR() + "/etc/login.defs")
    shelltools.system("sed -i 's;/var/mail;/var/spool/mail;g' " + get.installDIR() + "/etc/login.defs")
    shelltools.system("sed -i 's;#CREATE_HOME;CREATE_HOME;g' " + get.installDIR() + "/etc/login.defs")
    ###

    for f in ["chfn", "chgpasswd", "chpasswd", "chsh" "groupadd", "groupdel",
              "groupmems", "groupmod", "newusers", "useradd", "userdel", "usermod"]:
        shelltools.system("install -v -m644 " + get.installDIR() + "/etc/pam.d/chage " + get.installDIR() + "/etc/pam.d/" + f)
        shelltools.system('sed -i "s/chage/' + f + '/" ' + get.installDIR() + "/etc/pam.d/" + f)

    pisitools.insinto("/etc/", "etc/login.access")
    shelltools.chmod("%s/etc/login.access" % get.installDIR(), 0600)

    pisitools.insinto("/etc/", "etc/limits")
    shelltools.chmod("%s/etc/limits" % get.installDIR(), 0644)

    shelltools.system("[ -f " + get.installDIR() + "/etc/login.access ]" + " && mv -v " + get.installDIR() + "/etc/login.access{,.NOUSE}")
    shelltools.system("[ -f " + get.installDIR() + "/etc/limits ]" + " && mv -v " + get.installDIR() + "/etc/limits{,.NOUSE}")

    pisitools.dodoc("ChangeLog","README","NEWS")
