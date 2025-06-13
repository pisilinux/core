from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."

def setup():
    shelltools.system("./configure --prefix=/usr --disable-static")

def build():
    shelltools.system("make")

def check():
    shelltools.system("make test")
    shelltools.system("make test-fsck")
    shelltools.system("make test-convert")

def install():
    pisitools.dodoc("README.md", "LICENSE")
    shelltools.system("make DESTDIR=%s install" % get.installDIR())
