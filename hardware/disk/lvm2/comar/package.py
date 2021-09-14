#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if os.path.exists("/etc/lvm/lvm.conf"):
        with open("/etc/lvm/lvm.conf", 'r') as file:
            fileContent = file.readlines()
        for lineIndex in range(len(fileContent)):
            if ('use_lvmetad =' in fileContent[lineIndex]):
                fileContent[lineIndex] = '        use_lvmetad = 1\n'
                with open("/etc/lvm/lvm.conf", 'w') as tableFile:
                    tableFile.writelines(fileContent)
                break

    os.system("/sbin/mudur_tmpfiles.py /usr/lib/tmpfiles.d/lvm2.conf")
