---
title: "Penyusutan & Penghapusan Aset TIK Sekolah 2026: Cara Hitung Umur Ekonomis dan Menyusun Berita Acara"
date: 2026-10-14T20:40:00+07:00
draft: false
description: "Cara menghitung penyusutan komputer, laptop, dan proyektor sekolah dengan metode garis lurus, menentukan umur ekonomis menurut aturan perpajakan, dan menyusun berita acara penghapusan aset yang tidak bermasalah saat pemeriksaan."
tags: ["inventaris", "dana bos", "pembukuan", "pengadaan", "aset"]
categories: ["administrasi sekolah"]
---

Komputer sekolah yang sudah dipakai lima tahun biasanya masih hidup, tetapi nilainya di buku sudah tidak sama dengan saat dibeli. Masalahnya muncul ketika barang itu rusak, hilang, atau diganti: tidak ada catatan berapa nilai sisanya, tidak ada berita acara penghapusan, dan ketika pemeriksa meminta penjelasan, semua orang hanya bisa menjawab "sudah lama rusak". Bagian yang paling sering hilang bukan barangnya, melainkan jejaknya di atas kertas.

Tulisan ini menjelaskan dua hal yang berurutan: cara menghitung nilai aset TIK dari tahun ke tahun, dan cara melepas aset yang sudah tidak dipakai dengan dokumen yang benar. Keduanya cukup dikerjakan dengan spreadsheet, tanpa aplikasi berlangganan.

## Kenapa aset TIK perlu disusutkan, bukan sekadar dicatat

Daftar inventaris hanya menjawab "berapa jumlah barang". Penyusutan menjawab pertanyaan yang berbeda: **berapa nilai barang itu hari ini**. Bagi sekolah dan madrasah, angka itu dipakai untuk tiga hal nyata:

1. **Menyusun anggaran penggantian.** Komputer yang umurnya sudah mendekati akhir nilai buku adalah kandidat pertama yang akan minta dana penggantian tahun depan.
2. **Menentukan harga jual barang bekas.** Kalau unit lama dilepas ke pihak lain, harga jual harus punya dasar, bukan angka tebakan.
3. **Menghitung kerugian saat barang hilang atau rusak berat.** Laporan kehilangan yang menyebut nilai barang jauh lebih kuat daripada laporan yang hanya menyebut tahun pembelian.

Sekolah negeri yang mengelola dana BOS dan barang milik negara tidak selalu wajib menyusutkan secara akuntansi penuh, tetapi **mencatat nilai sisa tetap berguna**, karena itu dasar dari keputusan penggantian dan bahan pendukung saat pemeriksaan aset. Untuk entitas yang memang menyusun laporan keuangan, penyusutan wajib.

## Umur ekonomis: angka acuan yang dipakai untuk aset TIK

Perhitungannya memakai **metode garis lurus** (straight line): harga perolehan dibagi rata selama umur ekonomis. Untuk aset TIK, kelompok masa manfaatnya mengikuti tabel penyusutan fiskal yang lazim dipakai di Indonesia — bukan angka karangan.

| Jenis aset | Kelompok | Masa manfaat | Tarif per tahun |
|---|---|---|---|
| Komputer, laptop, printer, proyektor, perangkat jaringan | Kelompok 1 (bukan bangunan) | 4 tahun | 25% |
| Perabot dan perlengkapan kantor (meja, kursi, lemari) | Kelompok 2 | 8 tahun | 12,5% |
| AC, sound system, instalasi listrik pendukung | Kelompok 2 | 8 tahun | 12,5% |
| Bangunan permanen | Bangunan | 20 tahun | 5% |

Satu hal yang harus disepakati lebih dulu dan **dicatat sebagai kebijakan** sekolah: apakah penyusutan mulai dihitung di bulan pembelian atau tetap dihitung satu tahun penuh pada tahun pertama. Dua-duanya sah, yang tidak boleh adalah berganti-ganti tanpa catatan — itulah yang membuat angka tahun ini dan tahun lalu tidak bisa dibandingkan.

## Rumus garis lurus, dan contoh nyata 1 unit komputer

Rumusnya hanya dua baris:

```
Penyusutan per tahun   = (Harga perolehan − Nilai residu) ÷ Umur ekonomis
Penyusutan per bulan   = Penyusutan per tahun ÷ 12
```

**Contoh:** sekolah membeli 10 unit komputer desktop @ Rp5.500.000 pada Maret 2026, ditambah satu paket pemasangan dan kabel Rp2.000.000. Total perolehan Rp57.000.000. Umur ekonomis 4 tahun, nilai residu diasumsikan Rp500.000 per unit (Rp5.000.000 untuk 10 unit).

- Penyusutan setahun = (57.000.000 − 5.000.000) ÷ 4 = **Rp13.000.000**
- Penyusutan sebulan = 13.000.000 ÷ 12 = **Rp1.083.333**
- Nilai buku akhir 2026 (mulai dihitung April, 9 bulan) = 57.000.000 − (9 × 1.083.333) = **Rp47.250.000**
- Nilai buku akhir tahun ke-4 = **Rp5.000.000** (nilai residu)

Kalau tahun depan sekolah ingin mengganti 5 unit, angka yang dipakai sebagai dasar pengajuan bukan harga beli 2026, melainkan **harga barang sejenis tahun itu** — dan nilai buku 5 unit lama dipakai sebagai bahan pertimbangan apakah unitnya masih layak dipindahkan ke ruang lain daripada dibuang.

**Rincian biaya pemasangan harus ikut masuk harga perolehan.** Kesalahan yang umum: kabel, bracket, dan jasa pemasangan dicatat sebagai belanja terpisah dan hilang jejaknya, sehingga nilai aset lebih rendah dari uang yang benar-benar keluar. Semua biaya sampai barang siap dipakai adalah bagian dari harga perolehan.

## Kesalahan pencatatan yang paling sering terjadi pada aset TIK

Empat hal berikut muncul berulang di hampir setiap daftar inventaris sekolah, dan masing-masing menimbulkan masalah di kemudian hari:

1. **Harga perolehan diisi harga "kata orang", bukan harga di kuitansi.** Akibatnya nilai buku tidak bisa dipertanggungjawabkan. Solusinya sederhana: salin angka persis dari kuitansi/nota, termasuk PPN dan biaya kirim.
2. **Satu entri untuk pembelian borongan.** "20 komputer, Rp110.000.000" tidak bisa disusutkan per unit dan tidak bisa ditelusuri saat satu unit rusak. Pecah per unit sejak awal, walau barangnya dibeli sekaligus.
3. **Nomor seri dan lokasi ruang tidak dicatat.** Tanpa nomor seri, barang yang ditukar oleh pihak lain tidak bisa dibuktikan. Tanpa lokasi ruang, stok opname selalu berakhir dengan "tidak tahu ada di mana".
4. **Aset dipindah ruang tanpa catatan.** Perpindahan dari lab ke ruang guru wajib ada baris mutasi (tanggal, dari ruang, ke ruang, siapa yang memindahkan). Ini yang membuat barang sering "hilang" saat pemeriksaan padahal masih ada.

## Kode inventaris: cara membuatnya sekali dan dipakai bertahun-tahun

Kode yang baik harus bisa dibaca tanpa kamus. Pola yang bekerja dan tidak perlu diubah saat sekolah berganti bendahara:

```
JENIS-TAHUN-URUT-RUANG
KOM-2026-014-RLAB
```

- **JENIS** — tiga huruf: KOM (komputer), LAP (laptop), PRN (printer), PRJ (proyektor), NET (perangkat jaringan), ACU (AC).
- **TAHUN** — tahun perolehan, bukan tahun pencatatan.
- **URUT** — nomor urut tiga digit dalam tahun itu.
- **RUANG** — kode ruang yang dipakai sekolah (RLAB = ruang lab, RGUR = ruang guru, TU = tata usaha, PKEP = ruang kepala).

Kode ini ditempel di badan barang dan disalin ke kolom pertama spreadsheet. Kuncinya: kode **tidak berubah** walau barang berpindah ruang — perpindahan dicatat di kolom mutasi, bukan dengan mengganti kode. Kalau kode diganti, riwayat barangnya putus.

## Struktur kolom daftar aset yang bisa dipakai untuk menyusutkan

Satu spreadsheet dengan satu baris per unit. Kolom minimum:

| Kolom | Isi |
|---|---|
| Kode aset | KOM-2026-014-RLAB |
| Nama barang & tipe | Komputer desktop, Core i3, RAM 8GB |
| Nomor seri | dari label pabrik |
| Tanggal perolehan | 2026-03-18 |
| Sumber dana | BOS / komite / bantuan |
| Harga perolehan | angka dari kuitansi |
| Umur ekonomis (tahun) | 4 |
| Nilai residu | mis. 10% harga perolehan |
| Penyusutan per bulan | rumus otomatis |
| Nilai buku saat ini | rumus otomatis |
| Lokasi ruang | RLAB |
| Kondisi | Baik / Rusak Ringan / Rusak Berat |
| Riwayat mutasi | tanggal, ruang asal → tujuan |

Dua kolom terakhir — kondisi dan riwayat mutasi — yang paling sering dilupakan, padahal keduanya yang dipakai saat menyusun usulan penghapusan. Kondisi "rusak berat yang tidak ekonomis diperbaiki" adalah syarat utama sebuah aset boleh dihapus.

## Penghapusan aset: urutan kerja yang tidak bermasalah saat pemeriksaan

Menghapus barang bukan berarti membuangnya diam-diam. Urutannya seperti ini:

1. **Rekap barang berkondisi rusak berat.** Jalankan stok opname, catat unit yang benar-benar tidak bisa dipakai.
2. **Hitung nilai buku barang yang akan dihapus.** Ini angka yang muncul di berita acara.
3. **Susun usulan penghapusan** yang memuat: daftar unit (kode, nama, nomor seri, tanggal perolehan, nilai buku), alasan penghapusan, dan tujuan (dimusnahkan, dilelang, atau dihibahkan).
4. **Bentuk panitia penghapusan** dengan surat keputusan kepala sekolah/madrasah. Untuk barang milik negara, ada prosedur tersendiri yang harus diikuti sesuai aturan pengelolaan barang milik negara.
5. **Buat berita acara penghapusan** yang ditandatangani panitia, memuat hasil pemeriksaan fisik dan cara pemusnahan atau pelepasan.
6. **Perbarui daftar aset.** Baris yang dihapus dipindah ke arsip penghapusan, jangan langsung dihapus dari berkas — riwayatnya harus tetap ada.

**Alasan penghapusan harus spesifik.** "Rusak" tidak cukup. Tulisan yang bertahan saat ditanya: "mainboard rusak, biaya penggantian Rp1.200.000 sementara nilai buku unit Rp825.000 — perbaikan tidak ekonomis". Angka itu bisa diperiksa, dan itulah yang membedakan administrasi rapi dari administrasi asal jadi.

## Barang bekas yang masih layak: jangan langsung dimusnahkan

Sebelum menghapus, periksa apakah unitnya masih bisa dipakai untuk keperluan yang lebih ringan. Komputer yang tidak lagi kuat untuk ujian berbasis komputer sering masih memadai sebagai:

- komputer administrasi ruang tata usaha atau ruang guru;
- komputer untuk papan informasi digital (running text) di lobi;
- komputer cadangan untuk pencetakan dan pemindaian dokumen.

Perpindahan seperti ini dicatat sebagai **mutasi**, bukan penghapusan — dan itu justru menaikkan nilai manfaat barang tanpa menambah belanja. Barang yang benar-benar dihapus hanya yang sudah tidak ekonomis diperbaiki.

## Menyiapkan angka penghapusan tanpa mengetik ulang

Sekilas pekerjaan ini terlihat berat karena setiap perhitungan butuh tanggal, harga, dan tarif dari baris yang berbeda. Kuncinya: **hitung sekali dengan rumus, bukan ulang setiap tahun**. Kalau kolom tanggal perolehan, harga, dan umur ekonomis sudah ada, nilai buku dan penyusutan bulan berjalan bisa muncul otomatis, dan saat penghapusan hanya perlu menyalin hasilnya ke berita acara.

Satu hal yang membantu: pisahkan berkas **daftar aset** dari berkas **berita acara**. Daftar aset dipakai setiap hari dan diubah terus; berita acara adalah dokumen yang angkanya sudah dibekukan sejak ditandatangani. Mencampur keduanya di satu berkas membuat angka yang sudah disetujui ikut berubah tanpa sengaja.

## Kalau yang dihapus bukan komputer, tetapi arsip dan naskahnya

Di banyak madrasah dan pesantren, yang menumpuk bukan hanya perangkat, tetapi juga naskah dan berkas lama — kitab berbahasa Arab, buku induk, arsip surat, catatan penilaian bertahun-tahun. Benda-benda ini umurnya jauh lebih panjang daripada komputer, tetapi keadaannya lebih berisiko: kertas lapuk hilang sekali dan tidak bisa dibeli lagi.

Untuk naskah seperti itu, tindakan yang tepat bukan penghapusan, melainkan **pengalihan bentuk**: disalin ke berkas digital dengan nama yang teratur, lalu kertas aslinya tetap disimpan. Kami mengerjakan pekerjaan itu — pemindaian, penamaan, pengelompokan, termasuk naskah Arab berharakat yang perlu penanganan khusus.

**→ [Unduh gratis: Template Administrasi Madrasah 2026 (versi ringkas, 3 sheet)](/template-administrasi-madrasah-gratis/)**

Kalau butuh yang lebih lengkap (8 sheet, termasuk daftar hadir guru, inventaris, dan rekap nilai),
versinya Rp25.000 di halaman [Template Administrasi Madrasah 2026](/produk-template-excel-madrasah-2026/).

## Butuh naskah atau kitab dijadikan aplikasi?

Naskahnya Anda kirimkan, hasilnya menjadi milik lembaga Anda. Kirim satu bab contoh dulu untuk melihat hasilnya.

{{< bayar judul="Mulai dari Paket Konversi Naskah" nominal="Rp750.000" >}}

*Ditulis oleh Edukasi Praktis — mengerjakan pengolahan naskah Arab, harakat, terjemah, dan konversi ke aplikasi untuk pesantren, madrasah, dan perorangan.*
