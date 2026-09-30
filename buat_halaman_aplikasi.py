#!/usr/bin/env python3
"""
Buat halaman publik "Aplikasi" di blog dari katalog APK Bos.

Sumber: /home/server/toko_apps/katalog.json (25 aplikasi)
Hasil:  /home/server/blog-cuan/content/aplikasi/_index.md  (halaman daftar)
        /home/server/blog-cuan/content/aplikasi/<slug>.md  (halaman per aplikasi)

Dijalankan otomatis lewat cron, jadi halaman selalu ikut katalog terbaru.
"""
import json
import os
import re
import time

KATALOG = "/home/server/toko_apps/katalog.json"
BLOG = "/home/server/blog-cuan"
FOLDER = os.path.join(BLOG, "content", "aplikasi")


def slug_aman(s):
    s = s.lower().strip()
    s = s.replace("'", "").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def bersih(teks):
    """Buang karakter yang merusak YAML/front matter."""
    if not teks:
        return ""
    return str(teks).replace('"', "'").replace("\n", " ").strip()


def tulis_halaman_apk(app):
    nama = bersih(app.get("nama"))
    slug = slug_aman(app.get("slug") or nama)
    ringkas = bersih(app.get("ringkas"))
    lengkap = bersih(app.get("lengkap") or app.get("ringkas"))
    kategori = bersih(app.get("kategori"))
    versi = bersih(app.get("versi"))
    android = bersih(app.get("android"))
    bintang = app.get("bintang", 5)
    ukuran = bersih(app.get("ukuran"))

    # Deskripsi SEO, maks ~155 karakter
    deskripsi = ringkas[:150] if ringkas else f"Aplikasi {nama} untuk Android."

    isi = f"""---
title: "{nama}"
date: "{time.strftime('%Y-%m-%d')}T09:00:00+07:00"
draft: false
description: "{deskripsi}"
categories: ["Aplikasi"]
tags: ["{kategori}", "aplikasi android", "gratis"]
---

**{nama}** — {ringkas}

## Tentang aplikasi ini

{lengkap}

## Rincian

| Keterangan | Nilai |
|---|---|
| Kategori | {kategori} |
| Versi | {versi} |
| Minimal Android | {android or 'Android 7.0'} |
| Penilaian | {'★' * int(bintang or 5)} |
{f"| Ukuran | {ukuran} |" if ukuran else ""}

## Cara memasang

1. Unduh berkas APK-nya
2. Buka berkas yang sudah diunduh
3. Kalau muncul peringatan, pilih **Izinkan dari sumber ini** (aplikasi di luar Play Store memang begitu)
4. Tunggu sampai selesai, lalu buka aplikasinya

## Catatan

Aplikasi ini dibuat dan dirawat sendiri, bukan dari Play Store. Tidak ada iklan, tidak ada pelacak, dan tidak meminta izin yang tidak perlu.

Kumpulan aplikasi lainnya bisa dilihat di [halaman Aplikasi](/aplikasi/).
"""
    jalur = os.path.join(FOLDER, slug + ".md")
    with open(jalur, "w") as f:
        f.write(isi)
    return slug, nama, kategori, ringkas


def main():
    os.makedirs(FOLDER, exist_ok=True)
    with open(KATALOG) as f:
        apps = json.load(f)

    dibuat = []
    for app in apps:
        try:
            dibuat.append(tulis_halaman_apk(app))
        except Exception as e:
            print(f"!! gagal: {app.get('nama')} — {e}")

    # Halaman induk: daftar semua aplikasi, dikelompokkan per kategori
    per_kategori = {}
    for slug, nama, kategori, ringkas in dibuat:
        per_kategori.setdefault(kategori, []).append((slug, nama, ringkas))

    baris = [
        "---",
        'title: "Aplikasi Buatan Sendiri"',
        f'date: "{time.strftime("%Y-%m-%d")}T09:00:00+07:00"',
        "draft: false",
        'description: "Kumpulan aplikasi Android buatan sendiri: kitab terjemahan, fiqih, nahwu shorof, doa, dan alat praktis. Gratis, tanpa iklan."',
        'categories: ["Aplikasi"]',
        'tags: ["aplikasi android", "kitab", "gratis"]',
        "---",
        "",
        "Semua aplikasi di halaman ini dibuat sendiri — bukan hasil salin dari toko aplikasi.",
        "Tidak ada iklan, tidak ada pelacak, dan bisa dipakai tanpa internet untuk sebagian besar fiturnya.",
        "",
        f"Jumlah aplikasi saat ini: **{len(dibuat)}**",
        "",
    ]
    for kat in sorted(per_kategori):
        isi_kat = sorted(per_kategori[kat], key=lambda x: x[1])
        baris.append(f"## {kat}")
        baris.append("")
        for slug, nama, ringkas in isi_kat:
            baris.append(f"- **[{nama}](/aplikasi/{slug}/)** — {ringkas}")
        baris.append("")

    with open(os.path.join(FOLDER, "_index.md"), "w") as f:
        f.write("\n".join(baris))

    print(f"selesai: {len(dibuat)} halaman aplikasi + 1 halaman daftar")
    print(f"kategori: {', '.join(sorted(per_kategori))}")


if __name__ == "__main__":
    main()
