# -*- coding: utf-8 -*-

import os

def preRemove():

    if os.path.exists("/var/db/comar3/apps/mkinitramfs"):
        os.unlink("/var/db/comar3/scripts/System.PackageHandler/mkinitramfs.py")
        os.system("/bin/rm -Rf /var/db/comar3/apps/mkinitramfs")

