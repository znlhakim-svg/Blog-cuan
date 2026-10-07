#!/usr/bin/env python3
"""
Tayangkan artikel blog ke web sendiri (blog.radar9.my.id).

Dijalankan cron setelah artikel baru ditulis:
1. Build Hugo (public/)
2. Restart server blog (port 8094) -> artikel langsung live
3. Push ke GitHub sebagai arsip
4. Verifikasi artikel benar-benar tayang dari LUAR (mesin Kamar Barat)

Jangan uji dari server ini sendiri: DNS server mengarah balik ke jaringan
lokal sehingga hasilnya menyesatkan (pernah membuat laporan 200 padahal 404).
"""
import os
import re
import subprocess
import sys
import time

BLOG = "/home/server/blog-cuan"
SLUG_CARI = sys.argv[1] if len(sys.argv) > 1 else None
MESIN_LUAR = "azhari@100.64.240.59"  # Kamar Barat, jaringan berbeda


def sh(cmd, timeout=300, cwd=None, env=None):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                       timeout=timeout, cwd=cwd, env=env)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    print("=== 1. Build Hugo ===")
    env = dict(os.environ, HOME="/home/server")
    rc, out = sh("/snap/bin/hugo --gc --minify 2>&1 | tail -8", cwd=BLOG, env=env)
    print(out.strip() or f"(rc={rc})")

    jumlah = len([f for f in os.listdir(f"{BLOG}/content/posts") if f.endswith(".md")])
    print(f"total artikel: {jumlah}")

    print("\n=== 2. Restart server blog (artikel langsung live) ===")
    rc, out = sh("sudo -n systemctl restart web-blog && sleep 6 && "
                 "sudo -n systemctl is-active web-blog")
    print(out.strip())
    if "active" not in out:
        print("!! server blog TIDAK aktif — laporkan ke Bos")

    print("\n=== 3. Push ke GitHub (arsip) ===")
    rc, out = sh('git add -A && git commit -m "artikel: tayang otomatis" '
                 '&& git push origin main 2>&1 | tail -3', cwd=BLOG)
    print(out.strip()[:400] or "(tidak ada perubahan)")

    print("\n=== 4. VERIFIKASI DARI LUAR (mesin Kamar Barat) ===")
    time.sleep(5)
    slug = SLUG_CARI
    perintah = (
        f'curl -s -o /dev/null -w "beranda=%{{http_code}} " --max-time 25 '
        f'https://radar9.my.id/'
    )
    if slug:
        perintah += (
            f'; curl -s -o /dev/null -w "artikel=%{{http_code}}\\n" --max-time 25 '
            f'https://radar9.my.id/posts/{slug}/'
        )
    else:
        perintah += '; echo ""'
    rc, out = sh(f'ssh -o StrictHostKeyChecking=no -o ConnectTimeout=12 '
                 f'{MESIN_LUAR} {json_quote(perintah)}', timeout=120)
    hasil = out.strip()
    print(hasil)
    if "200" not in hasil:
        print("!! VERIFIKASI GAGAL dari luar — jangan klaim sudah tayang")


def json_quote(s):
    import json
    return json.dumps(s)


if __name__ == "__main__":
    main()
