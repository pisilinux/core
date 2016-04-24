# -*- coding: utf-8 -*-

import os
import piksemel
import subprocess


def generateinitrd(filepath):
    doc = piksemel.parse(filepath)
    for item in doc.tags("File"):
        path = item.getTagData("Path")
        if path.startswith("lib/modules/"):
            kver = path.split("/")[2]
            subprocess.call(["/usr/bin/mkinitcpio","-k","%s"% kver ,"-c","/etc/mkinitcpio.conf","-g","/boot/initramfs-%s"% kver,"-S","autodetect"])
            return

def setupPackage(metapath, filepath):
    generateinitrd(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    pass    
    
    
    
    

    
