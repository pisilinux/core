#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules

KeepSpecial=["perl"]

def setup():
    # use system zlib
    shelltools.unlinkDir("cpan/Compress-Raw-Zlib/zlib-src")
    pisitools.dosed("MANIFEST", "zlib-src", deleteLine=True)
    pisitools.dosed("cpan/Compress-Raw-Zlib/config.in", "(BUILD_ZLIB\s+=\s)True", r"\1False")
    pisitools.dosed("cpan/Compress-Raw-Zlib/config.in", "(INCLUDE\s+=\s)\.\/zlib-src", r"\1/usr/include")
    pisitools.dosed("cpan/Compress-Raw-Zlib/config.in", "(LIB\s+=\s)\.\/zlib-src", r"\1/usr/lib")

    shelltools.export("LC_ALL", "C")

    #fix one of tests
    #shelltools.system('sed -i "s#version vutil.c .*#version vutil.c f1c7e4778fcf78c04141f562b80183b91cbbf6c9#" t/porting/customized.dat')

    shelltools.system('sh Configure -des \
                      -Darchname=%s-linux \
                      -Dcccdlflags=-fPIC \
                      -Dccdlflags="-rdynamic -Wl,--enable-new-dtags" \
                      -Dcc=%s \
                      -Dprefix=/usr \
                      -Dvendorprefix=/usr \
                      -Dsiteprefix=/usr \
                      -Ulocincpth=  \
                      -Doptimize="%s" \
                      -Duselargefiles \
                      -Dusethreads \
                      -Duseithreads \
                      -Dd_semctl_semun \
                      -Dscriptdir=/usr/bin \
                      -Dman1dir=/usr/share/man/man1 \
                      -Dman3dir=/usr/share/man/man3 \
                      -Dinstallman1dir=%s/usr/share/man/man1 \
                      -Dinstallman3dir=%s/usr/share/man/man3 \
                      -Dlibperl=libperl.so.%s \
                      -Duseshrplib \
                      -Dman1ext=1 \
                      -Dman3ext=3pm \
                      -Dcf_by="PisiLinux" \
                      -Ud_csh \
                      -Di_ndbm \
                      -Di_gdbm \
                      -Di_db \
                      -Ubincompat5005 \
                      -Uversiononly \
                      -Dprivlib=/usr/share/perl5/core_perl \
                      -Darchlib=/usr/lib/perl5/%s/core_perl \
                      -Dsitelib=/usr/share/perl5/site_perl \
                      -Dsitearch=/usr/lib/perl5/%s/site_perl \
                      -Dvendorlib=/usr/share/perl5/vendor_perl \
                      -Dvendorarch=/usr/lib/perl5/%s/vendor_perl \
                      -Dpager="/usr/bin/less -isr" \
                      -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
                      -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
                      -Ud_endservent_r_proto -Ud_setservent_r_proto \
                      -Dlibpth="/lib /usr/lib" \
                      ' %(get.ARCH(), get.CC(), get.CFLAGS(), get.installDIR(), get.installDIR(), get.srcVERSION(), get.srcVERSION(), get.srcVERSION(), get.srcVERSION()))
    

def build():
    # colorgcc uses Term::ANSIColor
    paths = get.ENV("PATH").split(":")
    if "/usr/share/colorgcc" in paths:
        paths.remove("/usr/share/colorgcc")
    shelltools.export("PATH", ":".join(paths))
    ##
    autotools.make()

#def check():
#    autotools.make("-j1 test_harness")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/perl")
    # Conflicts with perl-Module-Build
    # pisitools.remove("/usr/bin/config_data")

    pisitools.dosym("/usr/bin/perl%s" % get.srcVERSION(), "/usr/bin/perl")

    # Perl5 library
    # NEEDS MODIFICATION FOR NEW VERSION
    pisitools.dosym("/usr/lib/perl5/%s/core_perl/CORE/libperl.so.%s" % (get.srcVERSION(),  get.srcVERSION()), "/usr/lib/libperl.so")
    pisitools.dosym("/usr/lib/perl5/%s/core_perl/CORE/libperl.so.%s" % (get.srcVERSION(),  get.srcVERSION()), "/usr/lib/libperl.so.5")
    pisitools.dosym("/usr/lib/perl5/%s/core_perl/CORE/libperl.so.%s" % (get.srcVERSION(),  get.srcVERSION()), "/usr/lib/libperl.so.5.40")
    pisitools.dosym("/usr/lib/perl5/%s/core_perl/CORE/libperl.so.%s" % (get.srcVERSION(),  get.srcVERSION()), "/usr/lib/libperl.so.5.40.2")
    # pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so")
    # pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5")
    # pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.38")
    # pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.38.2")

    # Docs
    pisitools.dodir("/usr/share/doc/%s/html" % get.srcNAME())
    shelltools.system('LD_LIBRARY_PATH=%s ./perl installhtml \
                       --podroot="." \
                       --podpath="lib:ext:pod:vms" \
                       --recurse \
                       --htmldir="%s/usr/share/doc/%s/html"' % (get.curDIR(), get.installDIR(), get.srcNAME()))

    ### Arch linux Perl Settings ###
    # Change man page extensions for site and vendor module builds.
    # Set no mail address since bug reports should go to the bug tracker
    # and not someone's email.
    shelltools.system("""sed -e '/^man1ext=/ s/1perl/1p/' -e '/^man3ext=/ s/3perl/3pm/' \
                           -e "/^cf_email=/ s/'.*'/''/" \
                           -e "/^perladmin=/ s/'.*'/''/" \
                           -i %s/usr/lib/perl5/%s/core_perl/Config_heavy.pl""" % (get.installDIR(), get.srcVERSION()))

    shelltools.system("""sed -e '/(makepl_arg =>/   s/""/"INSTALLDIRS=site"/' \
                           -e '/(mbuildpl_arg =>/ s/""/"installdirs=site"/' \
                           -i %s/usr/share/perl5/core_perl/CPAN/FirstTime.pm""" % get.installDIR())

    perlmodules.removePodfiles()
    perlmodules.removePacklist()
    pisitools.dodoc("Changes*", "Artistic", "Copying", "README", "AUTHORS")
