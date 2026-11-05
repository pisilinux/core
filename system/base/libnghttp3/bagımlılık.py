#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import re
import shutil

# Bilinen kütüphaneler için hızlı eşleştirme sözlüğü
LIB_TO_PACKAGE = {
    # Temel sistem kütüphaneleri
    'libc.so.6': 'glibc', 'libm.so.6': 'glibc', 'libpthread.so.0': 'glibc',
    'libdl.so.2': 'glibc', 'librt.so.1': 'glibc', 'ld-linux-x86-64.so.2': 'glibc',
    'libgcc_s.so.1': 'gcc-libs', 'libstdc++.so.6': 'gcc-libs', 'libquadmath.so.0': 'gcc-libs',
    
    # Sıkıştırma ve veri
    'libz.so.1': 'zlib', 'libbz2.so.1.0': 'bzip2', 'liblzma.so.5': 'xz',
    'libzstd.so.1': 'zstd', 'libicuuc.so.78': 'icu', 'libicui18n.so.78': 'icu', 'libicudata.so.78': 'icu',
    
    # Ağ ve XML
    'libxml2.so.2': 'libxml2', 'libxml2.so.16': 'libxml2', 'libcurl.so.4': 'curl',
    'libssl.so': 'openssl', 'libcrypto.so': 'openssl',
    
    # Grafik ve GUI
    'libglib-2.0.so.0': 'glib2', 'libgobject-2.0.so.0': 'glib2', 'libgio-2.0.so.0': 'glib2',
    'libQt6Core.so.6': 'qt6', 'libQt5Core.so.5': 'qt5',
    'libfreetype.so.6': 'freetype2', 'libpng16.so.16': 'libpng',
    'libX11.so.6': 'xorg-libs', 'libfontconfig.so.1': 'fontconfig',
    'libwayland-client.so.0': 'wayland', 'libpipewire-0.3.so.0': 'pipewire',
}

def run_command(cmd):
    """Verilen komutu çalıştırır ve çıktısını döndürür."""
    try:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if isinstance(out, bytes): out = out.decode('utf-8', errors='replace')
        if isinstance(err, bytes): err = err.decode('utf-8', errors='replace')
        return out, err, p.returncode
    except Exception as e:
        return "", str(e), 1

def find_package_by_file(lib_name):
    """Pisi sf komutunu kullanarak bir kütüphanenin hangi pakete ait olduğunu bulur."""
    search_name = os.path.basename(lib_name)
    out, err, ret = run_command("pisi sf %s" % search_name)
    if ret == 0 and out:
        lines = out.splitlines()
        for line in lines:
            match = re.search(r'(\S+)\s+paketi\s+içinde', line)
            if match:
                return match.group(1)
            if "paketi" in line and "dosyası" in line:
                parts = line.split()
                if len(parts) > 0:
                    return parts[0]
    return None

def get_runtime_deps(pisi_file):
    print("[*] '%s' paketinin çalışma bağımlılıkları analiz ediliyor..." % pisi_file)
    
    tmp_dir = "/tmp/pisi-deps-%d" % os.getpid()
    extract_dir = os.path.join(tmp_dir, "extracted")
    
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(extract_dir)
    
    print("  -> Pisi paketi (ZIP) açılıyor: %s" % extract_dir)
    out, err, ret = run_command("unzip -o %s -d %s" % (pisi_file, extract_dir))
    if ret != 0:
        print("Hata: Pisi paketi açılamadı. %s" % err)
        shutil.rmtree(tmp_dir)
        return

    tar_file = os.path.join(extract_dir, "install.tar.xz")
    if not os.path.exists(tar_file):
        for f in os.listdir(extract_dir):
            if f.startswith("install.tar"):
                tar_file = os.path.join(extract_dir, f)
                break
    
    if not os.path.exists(tar_file):
        print("Hata: install.tar.* dosyası bulunamadı.")
        shutil.rmtree(tmp_dir)
        return

    print("  -> %s açılıyor..." % os.path.basename(tar_file))
    out, err, ret = run_command("tar -xf %s -C %s" % (tar_file, extract_dir))
    if ret != 0:
        print("Hata: %s açılamadı. %s" % (os.path.basename(tar_file), err))
        shutil.rmtree(tmp_dir)
        return

    found_deps = set()
    file_count = 0
    
    for root, dirs, files in os.walk(extract_dir):
        for f in files:
            file_count += 1
            filepath = os.path.join(root, f)
            if f in ("metadata.xml", "files.xml") or f.startswith("install.tar"):
                continue
            if f.endswith('.so') or (os.access(filepath, os.X_OK) and not f.endswith('.')):
                out, err, ret = run_command("ldd %s" % filepath)
                if ret == 0:
                    for line in out.splitlines():
                        if "=>" in line:
                            lib = line.split()[0]
                            found_deps.add(lib)
    
    print("  -> Toplam %d dosya tarandı." % file_count)

    print("\n[*] Tespit Edilen Çalışma Bağımlılıkları:")
    if not found_deps:
        print("  (Hiçbir dinamik bağımlılık bulunamadı.)")
    
    pkg_deps = set()
    for lib in sorted(found_deps):
        pkg = LIB_TO_PACKAGE.get(lib)
        if not pkg:
            print("  -> %s için pisi sf ile paket aranıyor..." % lib)
            pkg = find_package_by_file(lib)
        
        if pkg:
            pkg_deps.add(pkg)
        else:
            print("  - %s (Paket eşleşmesi bulunamadı)" % lib)
            
    if pkg_deps:
        print("\n[*] Eşleşen Pisi Paketleri:")
        for pkg in sorted(pkg_deps):
            print("  + %s" % pkg)

    print("\n  -> Geçici dizin temizleniyor...")
    shutil.rmtree(tmp_dir)

def get_build_deps(src_dir):
    print("[*] '%s' dizinindeki derleme bağımlılıkları analiz ediliyor..." % src_dir)
    
    if not os.path.exists(src_dir):
        print("Hata: Dizin bulunamadı.")
        return

    found_pkgs = set()
    cmake_pkgs = set()
    
    # 1. pkg-config çağrıları
    print("  -> pkg-config çağrıları aranıyor...")
    cmd = "grep -r -E 'pkg-config|pkg_check_modules|dependency\\(' %s --include='*.ac' --include='*.am' --include='CMakeLists.txt' --include='meson.build' 2>/dev/null" % src_dir
    out, err, ret = run_command(cmd)
    if out:
        for line in out.splitlines():
            matches = re.findall(r'pkg-config\s+--[a-z]+\s+([a-zA-Z0-9_\-\.]+)', line)
            matches += re.findall(r'pkg_check_modules\([A-Z0-9_]+\s+([a-zA-Z0-9_\-\.]+)', line)
            matches += re.findall(r'dependency\(\s*\'([a-zA-Z0-9_\-\.]+)\'', line)
            for m in matches:
                found_pkgs.add(m)

    # 2. CMake find_package çağrıları
    print("  -> CMake find_package çağrıları aranıyor...")
    cmd = "grep -r -E 'find_package\\(' %s --include='CMakeLists.txt' --include='*.cmake' 2>/dev/null" % src_dir
    out, err, ret = run_command(cmd)
    if out:
        for line in out.splitlines():
            m = re.search(r'find_package\(\s*([a-zA-Z0-9_\-]+)', line)
            if m:
                cmake_pkgs.add(m.group(1))
            if "COMPONENTS" in line:
                parts = line.split("COMPONENTS")
                if len(parts) > 1:
                    comps = re.findall(r'([A-Z][a-zA-Z0-9]+)', parts[1])
                    for c in comps:
                        cmake_pkgs.add(c)

    # 3. Başlık dosyası bağımlılıkları
    print("  -> Başlık dosyası bağımlılıkları aranıyor...")
    cmd = "grep -r -E '#include <[a-zA-Z0-9_\\-]+/' %s --include='*.c' --include='*.cpp' --include='*.h' --include='*.hpp' 2>/dev/null | head -n 100" % src_dir
    out, err, ret = run_command(cmd)
    header_dirs = set()
    if out:
        for line in out.splitlines():
            m = re.search(r'#include <([a-zA-Z0-9_\-]+)/', line)
            if m:
                header_dirs.add(m.group(1))
    
    print("\n[*] Tespit Edilen Derleme Bağımlılıkları (pkg-config):")
    if not found_pkgs:
        print("  (pkg-config çağrısı bulunamadı.)")
    for pkg in sorted(found_pkgs):
        print("  + %s" % pkg)
        
    print("\n[*] Tespit Edilen Derleme Bağımlılıkları (CMake find_package):")
    if not cmake_pkgs:
        print("  (find_package çağrısı bulunamadı.)")
    for pkg in sorted(cmake_pkgs):
        print("  + %s" % pkg)

    # Başlık dizinlerini Pisi paket adlarına çevirmeye çalış
    print("\n[*] Tespit Edilen Başlık Dizinleri (Pisi paket karşılığı tahmini):")
    if not header_dirs:
        print("  (Başlık dizini bulunamadı.)")
    for h in sorted(header_dirs):
        pkg_map = {
            'KDESu': 'kdesu-devel', 'KParts': 'kparts-devel', 'QtCore': 'qt6-devel',
            'QtGui': 'qt6-devel', 'QtWidgets': 'qt6-devel', 'KDE': 'kf6-devel',
            'sys': 'glibc-devel', 'malloc': 'glibc-devel',
            'glib': 'glib2-devel', 'gtk': 'gtk3-devel',
        }
        pkg = pkg_map.get(h, "%s-devel" % h.lower())
        print("  + %s/ -> muhtemelen '%s' paketi" % (h, pkg))

def usage():
    print("Kullanım: python bagimlilik-analiz.py <mod> <yol>")
    print("  -r <pisi_dosyasi>   : Derlenmiş .pisi paketinin çalışma bağımlılıklarını bulur.")
    print("  -s <kaynak_dizini>  : Kaynak kod dizininin derleme bağımlılıklarını bulur.")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
    
    mode = sys.argv[1]
    target = sys.argv[2]
    
    if mode == "-r":
        get_runtime_deps(target)
    elif mode == "-s":
        get_build_deps(target)
    else:
        usage()