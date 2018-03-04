# core
core repository
------------------------------------------------------------------------------
* Buradan derlenen pisi dosyalarını **Pisi-1.* serisi üzerine kurmayınız.**
* Pisi-1. sürüm pisi dosyalarını **pisi-2.0 kurulu sistemlere kurmayınız.** 

------------------------------------------------------------------------------

Paketleme Kuralları;

1. Core kaynak deposunda minimum X bağımlılığı hedeflenmiştir.

1. configure seçeneklerinde belge oluşturmaya yönelik seçenekler açılmamalı, bağımlılıklar yazılmalıdır.

1. configure seçeneklerinde pakete yeni bağımlılık getirecek değişiklikler için mutlaka issue açılmalı, tartışılmadan pull request istenmemelidir.

1. systemd olmadığı için paketleri yapılandırırken *"--with-systemdsystemunitdir=/lib/systemd/system"* yerine *"--with-systemdsystemunitdir=no"* kullanıyoruz.

1. Bir paketi yapılandırırken *"--libexecdir="* kullanılacaksa *"--libexecdir=/usr/lib"* böyle olacak.

-----------------------------------------------------------------

Yardım için;
kendi github hesabınıza fork edebilir, yaptığınız değişiklikleri pull request ile gönderebilirsiniz. 

------------------------------------------------------------------

[![Throughput Graph](https://graphs.waffle.io/pisilinux/core/throughput.svg)](https://waffle.io/pisilinux/core/metrics)
