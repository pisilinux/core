#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "linux-firmware"
NoStrip = ["/lib"]

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("linux-firmware/*", "linux-firmware-%s" % get.srcVERSION())
    shelltools.cd("linux-firmware-%s" % get.srcVERSION())
    
    # Remove source files
    shelltools.unlink("usbdux/*dux")
    shelltools.unlink("*/*.asm")

    # These + a lot of other firmware are shipped within alsa-firmware
    for fw in ("ess", "korg", "sb16", "yamaha"):
        shelltools.unlinkDir(fw)

def build():
    #shelltools.cd("linux-firmware")
    
    # Processing amd-ucode...
    shelltools.system("mkdir -p kernel/x86/microcode")
    shelltools.system("cat " + get.curDIR() + "/amd-ucode/microcode_amd*.bin > kernel/x86/microcode/AuthenticAMD.bin")
    shelltools.system("touch kernel/x86/microcode/AuthenticAMD.bin")
    shelltools.system("echo kernel/x86/microcode/AuthenticAMD.bin | cpio -o -H newc -R 0:0 > amd-ucode.img")
    shelltools.chmod(get.curDIR() + "/amd-ucode.img", 0644)
    shelltools.chmod(get.curDIR() + "/LICENSE.amd-ucode", 0644)

    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/lib/firmware", "mix/*")
    
    # Install amd-ucode
    pisitools.insinto("/boot", "amd-ucode.img")
    shelltools.system("mv LICENSE.amd-ucode LICENSE")
    pisitools.insinto("/usr/share/licenses/amd-ucode/", "LICENSE")

    # Remove installed and LIC* files from /lib/firmware
    #pisitools.remove("/lib/firmware/GPL-3")
    pisitools.remove("/lib/firmware/LICENCE*")
    pisitools.remove("/lib/firmware/LICENSE*")
    #pisitools.remove("/lib/firmware/configure")
    #pisitools.remove("/lib/firmware/Makefile")
    #pisitools.removeDir("/lib/firmware/mix")
    #conflict on alsa-firmware
    #pisitools.remove("/lib/firmware/ctefx.bin")
    pisitools.remove("/lib/firmware/ctspeq.bin")

    # Install LICENSE files
    pisitools.dodoc("WHENCE", "LICENCE.*", "LICENSE.*")
