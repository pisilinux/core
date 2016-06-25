#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="grub-%s" % (get.srcVERSION().replace("_", "~"))


def setup():
    
    shelltools.copy("../unifont*.bdf", "./unifont.bdf")
    shelltools.export("GRUB_CONTRIB", "%s/grub-%s/grub-extras" % (get.workDIR(), get.srcVERSION()))

    pisitools.cflags.remove("-fstack-protector", "-fasynchronous-unwind-tables", "-fexceptions", "-fPIC")
    pisitools.cflags.sub("\s?(-O[\ds]|-D_FORTIFY_SOURCE=\d)\s?", " ")

    #shelltools.system("./linguas.sh")
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-werror \
                         --with-grubdir=grub2 \
                         --program-transform-name='s,grub,grub2,'\
                         --program-prefix= \
                         --with-platform=pc \
                         --target='i386' \
                         --htmldir='/usr/share/doc/grub2/html' ")
    
    
    shelltools.copytree("../grub-%s" % (get.srcVERSION().replace("_", "~")), "../grub-%s-efi" % get.srcVERSION())
    shelltools.cd("../grub-%s-efi" % get.srcVERSION())
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-werror \
                         --with-grubdir=grub2 \
                         --program-transform-name='s,grub,grub2,'\
                         --program-prefix= \
                         --with-platform=efi \
                         --target=x86_64  \
                         --htmldir='/usr/share/doc/grub2/html' ")
    
    
    shelltools.cd("..")
    
    
def build():
    #make-dist for creating all updated translation files
    autotools.make("dist")
    autotools.make()
    shelltools.cd("../grub-%s-efi" % get.srcVERSION())
    autotools.make()
    shelltools.cd("..")

def install():
    # Install unicode.pf2 using downloaded font source. 
    shelltools.system("./grub-mkfont -o unicode.pf2 unifont.bdf")

    # Create directory for grub.cfg file
    pisitools.dodir("/boot/grub2")
    
    pisitools.insinto("/boot/grub2", "unicode.pf2")

    # Insall our theme
    pisitools.insinto("/usr/share/grub/themes/","themes/pisilinux")

    #remove -r 0x0-0x7F entries to fix ugly fonts or find a suitable range parameter -r ***
    shelltools.system("./grub-mkfont -o DejaVuSans-10.pf2 -r 0x0-0x7F -s 10 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-12.pf2 -r 0x0-0x7F -s 12 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-14.pf2 -r 0x0-0x7F -s 14 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-16.pf2 -r 0x0-0x7F -s 16 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-Bold-14.pf2 -r 0x0-0x7F -s 14 /usr/share/fonts/dejavu/DejaVuSans-Bold.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-Mono-14.pf2 -r 0x0-0x7F -s 14 /usr/share/fonts/dejavu/DejaVuSansMono.ttf")
    shelltools.copy("ascii.pf2","%s/usr/share/grub/themes/pisilinux" % get.installDIR())

    # Do not install auto generated dejavu* fonts
    fonts=["DejaVuSans-10.pf2" , "DejaVuSans-12.pf2" , "DejaVuSans-14.pf2" , "DejaVuSans-16.pf2" , "DejaVuSans-Mono-14.pf2", "DejaVuSans-Bold-14.pf2"]
    for font in fonts:
        shelltools.copy(font,"%s/usr/share/grub/themes/pisilinux" % get.installDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "BUGS", "ChangeLog", "COPYING", "TODO", "README")
    
    shelltools.cd("../grub-%s-efi" % get.srcVERSION())
    
    autotools.rawInstall("DESTDIR=%s/efi" % get.installDIR())
    
    
    shelltools.copytree("/%s/efi/usr/lib/grub/x86_64-efi" % get.installDIR(), "%s/usr/lib/grub/x86_64-efi" % get.installDIR())
    pisitools.removeDir("/efi")



