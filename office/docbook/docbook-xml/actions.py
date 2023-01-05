#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."


def install():
    for version in ["4.1.2"]:
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.1.2/*.dtd")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.1.2/*.mod")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.1.2/docbook.cat")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.1.2/ent/*.ent")
        
    for version in ["4.2"]:
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.2/*.dtd")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.2/*.mod")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.2/docbook.cat")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.2/ent/*.ent")
        
    for version in ["4.3"]:
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.3/*.dtd")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.3/*.mod")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.3/docbook.cat")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.3/ent/*.ent")
        
    for version in ["4.4"]:
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.4/*.dtd")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.4/*.mod")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.4/docbook.cat")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.4/ent/*.ent")
        
    for version in ["4.5"]:
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.5/*.dtd")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.5/*.mod")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "4.5/docbook.cat")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "4.5/ent/*.ent")
        
    for version in ["5.0"]:
        pisitools.insinto("/usr/share/xml/docbook/schema/dtd/%s/" % version, "docbook-5.0/dtd/*.dtd")
        pisitools.insinto("/usr/share/xml/docbook/schema/rng/%s/" % version, "docbook-5.0/rng/*.rng")
        pisitools.insinto("/usr/share/xml/docbook/schema/rng/%s/" % version, "docbook-5.0/rng/*.rnc")
        pisitools.insinto("/usr/share/xml/docbook/schema/xsd/%s/" % version, "docbook-5.0/xsd/*.xsd")
        pisitools.insinto("/usr/share/xml/docbook/schema/sch/%s/" % version, "docbook-5.0/sch/*.sch")

    for version in ["5.1"]:
        pisitools.insinto("/usr/share/xml/docbook/schema/sch/%s/" % version, "5.1/schemas/*.xml")
        pisitools.insinto("/usr/share/xml/docbook/schema/rng/%s/" % version, "5.1/schemas/rng/*.rng")
        pisitools.insinto("/usr/share/xml/docbook/schema/rng/%s/" % version, "5.1/schemas/rng/*.rnc")
        pisitools.insinto("/usr/share/xml/docbook/schema/sch/%s/" % version, "5.1/schemas/sch/*.sch")
        pisitools.insinto("/usr/share/xml/docbook/stylesheet/docbook5", "5.1/tools/db4-upgrade.xsl")
        pisitools.dobin("5.1/tools/db4-entities.pl")

    shelltools.cd("docbook-5.0")
    pisitools.dodoc("ChangeLog", "README")
