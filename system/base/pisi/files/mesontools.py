# -*- coding: utf-8 -*-
import gettext

import pisi.actionsapi
import pisi.context as ctx
from pisi.actionsapi import get
from pisi.actionsapi.shelltools import system

__trans = gettext.translation('pisi', fallback=True)
_ = __trans.ugettext


class ConfigureError(pisi.actionsapi.Error):
    def __init__(self, value=''):
        pisi.actionsapi.Error.__init__(self, value)
        self.value = value
        ctx.ui.error(value)


class CompileError(pisi.actionsapi.Error):
    def __init__(self, value=''):
        pisi.actionsapi.Error.__init__(self, value)
        self.value = value
        ctx.ui.error(value)


class InstallError(pisi.actionsapi.Error):
    def __init__(self, value=''):
        pisi.actionsapi.Error.__init__(self, value)
        self.value = value
        ctx.ui.error(value)


def configure(parameters='', build_dir='build'):
    """
    Configures the project into the build directory with the parameters using meson.

    Args:
        parameters (str): Extra parameters for the command. Default is empty string.
        build_dir (str): Build directory. Default is 'build'.

    Examples:
        >>> mesontools.configure()
        >>> mesontools.configure('extra parameters')
        >>> mesontools.configure('extra parameters', 'custom_build_dir')
    """
    default_parameters = ' '.join([
        '--prefix=/%s' % get.defaultprefixDIR(),
        '--bindir=/usr/bin',
        '--datadir=/%s' % get.dataDIR(),
        '--includedir=/usr/include',
        '--infodir=/%s' % get.infoDIR(),
        '--libdir=/%s' % ('usr/lib32' if get.buildTYPE() == 'emul32' else 'usr/lib'),
        '--libexecdir=/%s' % get.libexecDIR(),
        '--localedir=/usr/share/locale',
        '--localstatedir=/%s' % get.localstateDIR(),
        '--mandir=/%s' % get.manDIR(),
        '--sbindir=/%s' % get.sbinDIR(),
        '--sharedstatedir=com',
        '--sysconfdir=/etc',
        '--default-library=shared',
    ])
    if system('meson setup %s %s %s' % (default_parameters, parameters, build_dir)):
        raise ConfigureError(_('Configuration failed.'))


def build(parameters='', build_dir='build'):
    """
    Builds the project into the build directory with the parameters using ninja. Instead of letting ninja
    to detect number of cores, this function gets the number from PISI configurations.

    Args:
        parameters (str): Extra parameters for the command. Default is empty string.
        build_dir (str): Build directory. Default is 'build'.

    Examples:
        >>> mesontools.build()
        >>> mesontools.build('extra parameters')
        >>> mesontools.build('extra parameters', 'custom_build_dir')
    """
    if system('ninja -C %s %s %s' % (build_dir, parameters, get.makeJOBS())):
        raise CompileError(_('Make failed.'))


def install(parameters='', build_dir='build'):
    """
    Installs the project to the destination directory.

    Args:
        parameters (str): Extra parameters for the command. Default is empty string.
        build_dir (str): Build directory. Default is 'build'.

    Examples:
        >>> mesontools.install()
        >>> mesontools.install('extra parameters')
        >>> mesontools.install('extra parameters', 'custom_build_dir')
    """
    if system('DESTDIR=%s ninja -C %s %s install' % (get.installDIR(), build_dir, parameters, )):
        raise InstallError(_('Install failed.'))
