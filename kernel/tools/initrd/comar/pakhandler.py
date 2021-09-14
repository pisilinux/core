#!/usr/bin/python

import piksemel
import os

def updateInitrd(filepath):
    patterns = ("/lib/modules", "/lib/initrd", "/boot/kernel", "/bin/busybox")
    parse = piksemel.parse(filepath)
    for xmlfile in parse.tags("File"):
        path = xmlfile.getTagData("Path")
        if not path.startswith("/"):
            path = "/%s" % path  # Just in case
        if path.startswith(patterns):
            # Handle the proper case of modules
            version = path.split("/")[3]
            os.environ['PATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/bin'
            cmd = "update-initrd KERNELVER=%s MODDIR=/lib/modules/%s OUTPUT=/boot/initramfs-%s" % (version, version, version)
            os.system(cmd)
            if os.path.exists("/proc/cmdline"):
                os.system("/usr/bin/update-grub")
            break

def setupPackage(metapath, filepath):
    updateInitrd(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    # TODO: Remove old initramfs!
    pass
