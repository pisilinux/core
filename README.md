# Pisi GNU/Linux

[![Telegram](https://img.shields.io/badge/Telegram-Pisi%20GNU%2FLinux-blue)](https://t.me/joinchat/DnOmFNS_KOjzEpnn)
[![Forum](https://img.shields.io/badge/Forum-Pisi%20GNU%2FLinux-orange)](https://pisilinux.org/forum)
[![Website](https://img.shields.io/badge/Website-Pisi%20GNU%2FLinux-green)](https://pisilinux.org/)


Pisi GNU/Linux; Pisi tabanlı son Pardus sürümünü temel alan, özgür yazılım topluluğu tarafından geliştirilen, bilgisayar kullanıcılarına kurulum, yapılandırma ve kullanım konusunda kolaylık sağlamaya çalışan, onların temel masaüstü gereksinimlerini karşılamayı amaçlayan, son kullanıcı odaklı bir GNU/Linux dağıtımıdır.

![](https://github.com/PisiLinuxNew/package-manager/blob/master/data/tray-zero.png)

# core repository

***********************************************************************************************
Bu depo Pisi GNU/Linux projesinin X bağımlılığı olmadan çalışabilen minimum bişenlerini içerir.
***********************************************************************************************

Paketleme Kuralları;

1. Ana sürümler dışında *toolchain* güncellemesinden kaçınılmalıdır.

1. *configure* seçeneklerinde belge oluşturmaya yönelik seçenekler açılmamalı, bağımlılıklar yazılmalıdır.

1. *configure* seçeneklerinde pakete yeni bağımlılık getirecek değişiklikler için mutlaka issue açılmalı, tartışılmadan pull request istenmemelidir.

1. systemd olmadığı için paketleri yapılandırırken *"--with-systemdsystemunitdir=/lib/systemd/system"* yerine *"--with-systemdsystemunitdir=no"* kullanılmalıdır.

1. Bir paketi yapılandırırken *"--libexecdir="* kullanılacaksa *"--libexecdir=/usr/lib"* şeklinde kullanılmalıdır.

-----------------------------------------------------------------

Yardım için;
kendi github hesabınıza fork edebilir, yaptığınız değişiklikleri pull request ile gönderebilirsiniz. 

------------------------------------------------------------------------------
# Dikkat

* Bu depodan derlenen pisi dosyalarını **Pisi-1.x serisi üzerine kurmayınız.**
* Pisi-1.x sürüm pisi dosyalarını **pisi-2.0 kurulu sistemlere kurmayınız.** 

------------------------------------------------------------------------------
