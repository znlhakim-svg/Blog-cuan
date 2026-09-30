#!/usr/bin/env python3
"""
Terbitkan artikel blog yang MENUNGGU PERSETUJUAN Bos.

Alur:
  cron malam  -> tulis artikel, simpan ke /home/server/blog-cuan/tinjau/
  lalu kirim ke Bos via Telegram, minta balas "ok"
  setelah Bos balas ok (dijalankan manual/agent) -> pindah ke content/posts/
  -> build -> live di https://blog.radar9.my.id

Pakai:
  python3 tinjau_artikel.py daftar          # lihat artikel menunggu
  python3 tinjau_artikel.py setujui <slug>  # setujui + tayangkan
  python3 tinjau_artikel.py tolak <slug>    # buang artikel (tanpa backup)
"""
import os
import shutil
import subprocess
import sys
import time

BLOG = "/home/server/blog-cuan"
FOLDER_TINJAU = os.path.join(BLOG, "tinjau")
FOLDER_POSTS = os.path.join(BLOG, "content", "posts")
MESIN_LUAR = "azhari@100.64.240.59"


def sh(cmd, timeout=300, cwd=None, env=None):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                       timeout=timeout, cwd=cwd, env=env)
    return r.returncode, ((r.stdout or "") + (r.stderr or "")).strip()


def daftar():
    if not os.path.isdir(FOLDER_TINJAU):
        print("(belum ada artikel menunggu)")
        return []
    berkas = sorted(f for f in os.listdir(FOLDER_TINJAU) if f.endswith(".md"))
    if not berkas:
        print("(belum ada artikel menunggu)")
    for f in berkas:
        jalur = os.path.join(FOLDER_TINJAU, f)
        judul = ""
        try:
            with open(jalur) as fh:
                for baris in fh:
                    if baris.startswith("title:"):
                        judul = baris.split(":", 1)[1].strip().strip('"')
                        break
        except Exception:
            pass
        print(f"  {f}  ->  {judul}")
    return berkas


def setujui(slug):
    slug = slug.replace(".md", "")
    asal = os.path.join(FOLDER_TINJAU, slug + ".md")
    if not os.path.exists(asal):
        print(f"!! tidak ada artikel menunggu bernama: {slug}")
        return 1
    tujuan = os.path.join(FOLDER_POSTS, slug + ".md")

    # 1. Pindahkan ke folder terbit
    shutil.move(asal, tujuan)
    print(f"dipindahkan -> {tujuan}")

    # 2. Catat riwayat
    judul, kategori = slug, ""
    with open(tujuan) as fh:
        for baris in fh:
            if baris.startswith("title:"):
                judul = baris.split(":", 1)[1].strip().strip('"')
            if baris.startswith("categories:"):
                kategori = baris.split(":", 1)[1].strip().strip('[]"')
    tanggal = time.strftime("%Y-%m-%d")
    with open(os.path.join(BLOG, "article-history.txt"), "a") as fh:
        fh.write(f"{tanggal} | {judul} | {kategori}\n")
    print(f"riwayat dicatat: {judul}")

    # 3. Build + live + push + verifikasi dari luar
    print("\n=== tayangkan ===")
    rc, out = sh(f"python3 {BLOG}/tayangkan.sh {slug}", timeout=400, cwd=BLOG)
    print(out[-800:])
    return 0 if "200" in out else 1


def tolak(slug):
    slug = slug.replace(".md", "")
    jalur = os.path.join(FOLDER_TINJAU, slug + ".md")
    if os.path.exists(jalur):
        os.remove(jalur)
        print(f"dibuang: {slug}")
    else:
        print(f"!! tidak ada: {slug}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        daftar()
    elif sys.argv[1] == "daftar":
        daftar()
    elif sys.argv[1] == "setujui" and len(sys.argv) > 2:
        sys.exit(setujui(sys.argv[2]))
    elif sys.argv[1] == "tolak" and len(sys.argv) > 2:
        sys.exit(tolak(sys.argv[2]))
    else:
        print(__doc__)
