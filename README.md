[![Telegram](https://img.shields.io/badge/Telegram-Pisi%20GNU%2FLinux-blue)](https://t.me/joinchat/DnOmFNS_KOjzEpnn)
[![Forum](https://img.shields.io/badge/Forum-Pisi%20GNU%2FLinux-orange)](https://pisilinux.org/forum)
[![Website](https://img.shields.io/badge/Website-Pisi%20GNU%2FLinux-green)](https://pisilinux.org/)
# DİKKAT: Geliştiriciler içindir, sisteminize zarar verebilir.
![](https://github.com/PisiLinuxNew/package-manager/blob/master/data/tray-zero.png)

# Pisi GNU/Linux
Pisi GNU/Linux; Pisi tabanlı son Pardus sürümünü temel alan, özgür yazılım topluluğu tarafından geliştirilen, bilgisayar kullanıcılarına kurulum, yapılandırma ve kullanım konusunda kolaylık sağlamaya çalışan, onların temel masaüstü gereksinimlerini karşılamayı amaçlayan, son kullanıcı odaklı bir GNU/Linux dağıtımıdır. **_Bu depo Pisi GNU/Linux projesinin X bağımlılığı olmadan çalışabilen asgari bişenlerini içerir._**


Paketleme Kuralları;

1. Ana sürümler dışında **_toolchain_** güncellemesinden kaçınılmalıdır.
1. ```configure``` seçeneklerinde belge oluşturmaya yönelik seçenekler açılmamalı, bağımlılıklar yazılmalıdır.
1. ```configure``` seçeneklerinde pakete yeni bağımlılık getirecek değişiklikler için mutlaka issue açılmalı, tartışılmadan Pull Request istenmemelidir.
1. systemd olmadığı için paketleri yapılandırırken ```--with-systemdsystemunitdir=/lib/systemd/system``` yerine ```--with-systemdsystemunitdir=no``` kullanılmalıdır.
1. Bir paketi yapılandırırken ```--libexecdir=``` kullanılacaksa ```--libexecdir=/usr/lib``` şeklinde kullanılmalıdır.
---------------------------------------------------------------------
Pisi GNU/Linux projesinin geliştirilmesine yardım etmek istiyorsanız;
* Öncelikle kendi github hesabınıza projeyi fork'layıp
* Yaptığınız değişiklikleri Pull Request ile gönderebilirsiniz. 
