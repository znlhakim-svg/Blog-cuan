---
title: "Menyiapkan Komputer Sekolah dari Nol: Urutan Pemasangan, Lisensi, dan Jebakan yang Mahal"
date: 2026-10-14T10:01:00+07:00
draft: false
description: "Urutan memasang ulang komputer sekolah: partisi, driver, aplikasi, akun, dan pengamanan. Termasuk hal yang wajib dicatat dan kesalahan yang membuat komputer lab cepat rusak."
tags: ["laboratorium komputer", "aplikasi", "open source", "pengadaan"]
categories: ["teknologi pendidikan"]
---

Komputer sekolah paling sering rusak bukan karena perangkatnya jelek, tetapi karena tidak pernah ada yang tahu bagaimana isinya diatur. Tidak ada catatan partisi, tidak ada daftar aplikasi, tidak ada keterangan akun. Begitu guru yang mengurusnya pindah, komputer itu berubah menjadi kotak hitam — dan setiap masalah kecil harus diselesaikan dengan memasang ulang dari nol.

Tulisan ini bukan daftar aplikasi. Ini urutan kerja menyiapkan komputer sekolah supaya isinya bisa dipertanggungjawabkan, dan supaya komputer berikutnya lebih cepat disiapkan.

## Urutan yang benar: satu unit dirapikan sampai selesai, baru digandakan

Kesalahan paling umum adalah memasang satu-satu aplikasi di 20 unit secara bergiliran. Hasilnya: unit pertama sudah rapi, unit ke-20 masih setengah jalan, dan tidak ada satu pun yang benar-benar siap dipakai hari pertama sekolah.

Urutan yang jauh lebih hemat waktu:

**Langkah 1 — Tetapkan satu komputer "induk".** Pilih satu unit, rapikan sampai benar-benar selesai: partisi, sistem operasi, driver, aplikasi, akun, dan pengaturan. Unit ini menjadi patokan.

**Langkah 2 — Catat semua yang dipasang.** Tuliskan di buku atau berkas teks: nama aplikasi, versi, dari mana diunduh, dan lisensinya. Catatan ini yang nanti dipakai saat ada komputer rusak dan harus dipasang ulang.

**Langkah 3 — Buat salinan induk.** Cara paling aman dan tidak perlu membongkar komputer adalah membuat berkas salinan (image) dari unit induk memakai perangkat lunak gratis seperti Clonezilla. Hasilnya satu berkas yang bisa dikembalikan ke unit mana pun. Alternatif yang lebih sederhana: simpan semua pemasang aplikasi di satu folder USB, ditata rapi menurut urutan pemasangan.

**Langkah 4 — Gandakan ke unit lain, satu per satu sambil diuji.** Periksa yang paling sering bermasalah: suara, jaringan, tampilan layar, dan pencetakan.

**Langkah 5 — Tempel label nomor unit di badan komputer**, dan sesuaikan dengan catatan. Ini sepele tetapi menyelamatkan banyak waktu di kemudian hari.

## Windows atau Linux? Jawabannya soal siapa penggunanya

Ini keputusan yang menentukan biaya dan kerumitan selama bertahun-tahun.

**Windows** dipilih kalau sekolah memakai aplikasi yang tidak ada padanannya — khususnya aplikasi administrasi dari dinas, aplikasi ujian berbasis komputer tertentu, dan Dapodik. Aplikasi-aplikasi ini umumnya hanya berjalan di Windows.

**Linux** (misalnya edisi yang dirancang khusus untuk sekolah) dipilih kalau pemakaian utama hanya untuk mengetik, mengolah angka, membuka internet, dan mengajar. Keuntungannya nyata: tidak ada biaya lisensi, lebih tahan terhadap virus, dan bisa dijalankan pada komputer lama dengan memori kecil.

Pilihan yang paling banyak dipakai madrasah dan sekolah saat ini adalah **campuran**:

- **Ruang laboratorium siswa**: Linux, karena pemakaian terbatas dan tidak perlu lisensi.
- **Komputer tata usaha dan operator**: Windows, karena aplikasi dinas berjalan di sana.
- **Komputer guru**: menyesuaikan kebutuhan masing-masing; kalau tidak ada aplikasi khusus, Linux sudah cukup.

Yang harus dihindari adalah memasang Windows hasil salinan tidak resmi di sekolah. Selain tidak sah, Windows salinan seperti itu sering gagal diperbarui, dan pada suatu waktu tertentu seluruh laboratorium harus dipasang ulang serentak — pekerjaan besar yang bisa dihindari sejak awal.

## Aplikasi: pilih sedikit, tapi dipakai

Daftar aplikasi biasanya berisi hal-hal yang jarang dipakai. Lebih bermanfaat menetapkan dulu **pekerjaan yang akan dikerjakan** di komputer itu, baru mencari aplikasinya.

Pekerjaan rutin di komputer sekolah, dan padanan gratis yang paling sering dipakai:

| Pekerjaan | Pilihan gratis | Catatan |
|---|---|---|
| Mengetik, menghitung, presentasi | LibreOffice / WPS Office | Bisa membuka dan menyimpan berkas Word dan Excel |
| Membaca dan menyunting PDF | PDF24, PDF-XChange | Gabung, pisah, kompres, tanpa tanda air |
| Membuka berkas terkompresi | 7-Zip | Tanpa iklan dan tanpa batas waktu percobaan |
| Membaca PDF di komputer lama | Penampil PDF ringan bawaan sistem | Jangan pasang pembaca PDF berat di komputer memori kecil |
| Memotong dan menyunting gambar | GIMP, Paint.NET | Untuk poster dan spanduk kecil |
| Merekam layar untuk video ajar | OBS Studio | Bisa juga untuk siaran langsung kegiatan sekolah |
| Menyunting suara | Audacity | Untuk bahan ajar audio |
| Memindai dokumen | Aplikasi bawaan pemindai | Cek dulu, biasanya sudah ada |

Empat hal yang wajib dihindari di komputer sekolah:

1. Perangkat lunak yang meminta **kunci aktivasi dari internet** setiap kali dipakai — sekolah dengan jaringan tidak stabil akan sering tersendat.
2. Aplikasi pembersih "pengoptimal" gratis yang justru menambah iklan.
3. Peramban dengan banyak tambahan yang tidak jelas; satu peramban yang terawat lebih baik daripada tiga yang penuh tambahan.
4. Game di komputer laboratorium. Ini bukan soal moral, tetapi soal ruang penyimpanan dan waktu pemasangan ulang.

## Pengaturan yang menentukan umur pakai komputer

Tiga pengaturan ini jarang disentuh, padahal paling berpengaruh:

**1. Akun terpisah antara pengguna biasa dan pengelola.** Siswa memakai akun pengguna biasa, bukan akun pengelola. Tanpa pemisahan ini, satu siswa yang menekan hal yang salah bisa merusak pengaturan untuk semua orang.

**2. Pemulihan data otomatis (System Restore) dihidupkan.** Ketika aplikasi bermasalah, komputer bisa dikembalikan ke kondisi beberapa hari sebelumnya tanpa memasang ulang.

**3. Pemutakhiran diperiksa sekali sebulan, bukan selalu menyala otomatis.** Pembaruan yang berjalan sendiri saat jam pelajaran bisa membuat komputer tiba-tiba lambat atau minta dinyalakan ulang.

Satu hal kecil yang sangat berguna: **simpan berkas kerja di penyimpanan daring** (Drive sekolah), bukan di komputer. Kalau unitnya rusak, pekerjaan tidak ikut hilang. Ini juga yang membedakan sekolah yang pernah kehilangan data dengan yang belum pernah.

## Yang wajib dicatat sejak hari pertama

Siapkan satu lembar catatan aset untuk setiap unit. Isi minimal:

- Nomor unit dan nomor seri perangkat
- Tahun pembelian dan nilai pembelian
- Tanggal pemasangan sistem terakhir
- Daftar aplikasi beserta versinya
- Nama dan nomor kontak teknisi yang biasa dipanggil
- Riwayat kerusakan dan perbaikan

Lembaran ini menjawab dua kebutuhan sekaligus: mempercepat perbaikan, dan menjadi bukti saat ada pemeriksaan aset. Sekolah yang tidak punya catatan ini akan kesulitan menjelaskan keberadaan barang inventarisnya.

## Kesalahan yang paling sering terjadi

**Memasang semua aplikasi yang ditemukan.** Makin banyak aplikasi, makin sering bentrok dan makin lama memasang ulang. Pilih yang benar-benar dipakai.

**Memberi semua orang hak pengelola.** Satu perubahan yang salah akan diulang di semua unit.

**Tidak menyimpan pemasang aplikasi.** Ketika jaringan bermasalah atau situsnya berubah, pemasang ulang menjadi pekerjaan yang merepotkan.

**Memasang ulang setiap kali muncul masalah kecil.** Banyak masalah hanya perlu membetulkan pengaturan atau driver. Pemasangan ulang sebaiknya menjadi pilihan terakhir, bukan pertama.

**Menyerahkan komputer tanpa dipakai bersama-sama sekali.** Sediakan satu sesi pendampingan untuk guru. Satu jam pendampingan menghemat puluhan pertanyaan pada bulan pertama.

## Pertanyaan yang sering muncul

**Berapa spesifikasi minimal komputer untuk laboratorium sekolah 2026?**
Untuk pekerjaan mengetik, menghitung, dan membuka internet, komputer dengan memori 4 GB dan penyimpanan 128 GB sudah cukup, terutama jika memakai Linux. Kalau akan dipakai untuk ujian berbasis komputer dengan peramban modern, siapkan memori 8 GB supaya tidak tersendat.

**Komputer lama masih layak dipakai?**
Selama bisa menampung memori 4 GB dan masih bisa dihubungkan ke layar, komputer lama masih sangat berguna — terutama untuk mengetik dan pelatihan dasar. Yang perlu diperhatikan justru penyimpanan: cakram mekanik yang sudah tua paling sering menjadi penyebab komputer terasa lambat, dan menggantinya dengan penyimpanan padat (SSD) biasanya memberi perubahan paling terasa dengan biaya paling kecil.

**Apakah boleh memakai aplikasi gratis untuk administrasi sekolah?**
Boleh, selama lisensinya memang mengizinkan pemakaian di lembaga pendidikan. Simpan keterangan lisensi tiap aplikasi — ini cukup untuk menjawab pertanyaan pemeriksaan.

**Bagaimana cara menghindari pemasangan ulang berulang?**
Buat salinan induk (image) begitu satu unit sudah sempurna, lalu simpan berkasnya di dua tempat terpisah. Satu salinan di ruang komputer, satu lagi di penyimpanan daring atau cakram lain.

---

*Angka spesifikasi dan pilihan aplikasi bersifat anjuran umum; sesuaikan dengan aplikasi dinas yang wajib dipakai di sekolah masing-masing.*
