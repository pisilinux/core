#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/lib", "/boot"]

shelltools.export("KBUILD_BUILD_USER", "pisilinux")
shelltools.export("KBUILD_BUILD_HOST", "buildfarm")
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

#cpupower_arch = get.ARCH().replace("i686", "i386")

def setup():
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)

    
def install():
    kerneltools.install()

    # Install kernel headers needed for out-of-tree module compilation
    kerneltools.installHeaders()

    kerneltools.installLibcHeaders()

    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s" % (get.installDIR(), kerneltools.__getSuffix()))
    
    objtool()
    
    #mkinitcpio default config
    pisitools.dodir("/etc/mkinitcpio.d")
    shelltools.touch("linux.preset")
        
    shelltools.echo("linux.preset", "# mkinitcpio preset file for the 'linux' package\n" +
                    
                    'ALL_config="/etc/mkinitcpio.conf"\n'+
                    
                    'ALL_kver="/boot/kernel-%s"\n\n'% get.srcVERSION() +
                    "PRESETS=('default' 'fallback') \n\n" +
                    '#default_config="/etc/mkinitcpio.conf"\n' +
                    'default_image="/boot/initramfs-%s.img"\n'% get.srcVERSION() +
                    
                    '#default_options=""\n\n' +
                    '#fallback_config="/etc/mkinitcpio.conf"\n'+
                    'fallback_image="/boot/initramfs-%s-fallback.img"\n'% get.srcVERSION() +
                    'fallback_options="-S autodetect"\n')
    
    pisitools.insinto("/etc/mkinitcpio.d", "linux.preset")

def objtool():
    # add objtool for external module building and enabled VALIDATION_STACK option
    shelltools.cd("tools/objtool")
    autotools.make("objtool")
    
    pisitools.insinto("/usr/src/linux-headers-4.14.48/tools/objtool","%s/objtool" % get.curDIR())
