# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDefault = "conditional"
serviceDesc = _({"en": "Dhcp client",
                            "tr": "Dhcp istemcisi"})

MSG_BACKEND_WARNING = _({
                        "en" : "dhcp is not enabled by default. You can change this from /etc/dhcpcd.conf.",
                        "tr" : "dhcp öntanımlı olarak etkin değil. /etc/dhcpcd.conf dosyasından bu ayarı değiştirebilirsiniz."
                        })

pidfile="/var/run/dhcpcd.pid"
USETHIS=eval(config.get("DEFAULT", "True"))

@synchronized
def start():
    if not USETHIS:
        fail(MSG_BACKEND_WARNING)

    startService(command="/usr/bin/dhcpcd",
                 args="daemon -q -b %s" % pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/dhcpcd -x",
                donotify=True)

    try:
        os.unlink(pidfile)
    except:
        pass

def ready():
    if not USETHIS:
        fail(MSG_BACKEND_WARNING)
    else:
        start()

def status():
    return isServiceRunning(pidfile=pidfile)
