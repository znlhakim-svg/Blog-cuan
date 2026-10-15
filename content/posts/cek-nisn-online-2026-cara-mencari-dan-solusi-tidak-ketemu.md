---
title: "Cek NISN Online 2026: Cara Mencari NISN Siswa, Arti 10 Digit, dan Solusi Kalau Tidak Ketemu"
date: "2026-10-14T20:15:00+07:00"
draft: false
tags: ["NISN", "administrasi sekolah", "dapodik", "operator sekolah", "siswa"]
categories: ["Tips Administrasi Sekolah"]
description: "Panduan lengkap cek NISN online: cara mencari berdasarkan nama atau NISN, arti 3 digit pertama, kenapa NISN tidak ditemukan, dan langkah verval di VervalPD."
---

Setiap awal tahun ajaran, pertanyaan yang paling sering masuk ke ruang operator sekolah bukan soal Dapodik yang error, melainkan satu hal sederhana: **nomor NISN siswa ini berapa, dan kenapa saat dicek tidak keluar?** Nomor itu dipakai untuk mendaftar SNBP, mengajukan PIP, mengurus ijazah, sampai mencetak kartu peserta ujian. Kalau nomornya tidak ketemu, seluruh urusan itu ikut tertahan.

Halaman ini menjelaskan cara mengecek NISN dari luar sekolah, arti angka di dalamnya, dan — bagian yang paling jarang dibahas — apa yang harus dilakukan kalau pencariannya kosong.

## NISN itu nomor apa, dan siapa yang menerbitkannya

NISN (Nomor Induk Siswa Nasional) adalah **kode referensi berbentuk nomor unik** yang menjadi identitas peserta didik. Aturannya: **satu peserta didik hanya boleh memiliki satu NISN**. Nomor ini melekat seumur hidup dan tidak berubah meski siswa pindah sekolah, pindah kota, atau pindah provinsi.

Dasar hukum yang dipakai sekarang adalah **Lampiran Kepmendikbudristek Nomor 303/M/2022** tentang Petunjuk Teknis Data Pendidikan, Bagian D. Kode Referensi. Penerbitannya dilakukan oleh **PDSPK** (Pusat Data dan Statistik Pendidikan dan Kebudayaan) sebagai bagian dari program Dapodik.

Dua konsekuensi yang sering mengejutkan guru baru:

1. **NISN tidak diterbitkan sekolah.** Sekolah hanya memasukkan data ke Dapodik, lalu mengajukan verifikasi ke pusat.
2. **NISN bukan NIS.** NIS (Nomor Induk Siswa) adalah nomor lokal buatan sekolah dan bisa berbeda di tiap sekolah. Yang berlaku nasional adalah NISN.

## Arti 10 digit NISN — dan kenapa ada yang "tidak sesuai"

NISN selalu **10 digit angka**, dengan pola:

| Bagian | Jumlah digit | Isi |
|---|---|---|
| 3 digit pertama | 3 | Tiga digit terakhir **tahun kelahiran** |
| 7 digit berikutnya | 7 | Nomor acak |

Misalnya siswa lahir 2011, maka tiga angka pertamanya adalah `201`.

Satu catatan yang jarang diketahui: **kalau 3 digit pertama tidak sesuai tahun kelahiran, NISN-nya tetap dinyatakan valid.** Nomor itu tidak perlu diganti. Yang bisa diubah adalah data siswanya (nama, tempat lahir, tanggal lahir, nama ibu kandung), bukan nomornya.

Ini penting supaya Anda tidak panik saat memeriksa NISN siswa dan mendapati awalan angkanya "salah". Itu bukan tanda nomornya palsu.

## Cara cek NISN online

Portal resmi pencarian NISN bernama **NISN Data Kemdikbud** (alamatnya `nisn.data.kemdikbud.go.id`). Di laman itu ada pilihan menu **Pencarian Nama** di pojok kanan atas. Ada dua jalur pencarian:

### Jalur 1 — Cari berdasarkan NISN

Anda sudah memegang nomornya dan ingin memastikan nomor itu memang milik siswa yang benar. Data yang perlu disiapkan: **NISN** dan **nama lengkap ibu kandung**.

Jalur ini yang paling sering dipakai operator untuk memeriksa data ganda.

### Jalur 2 — Cari berdasarkan nama (kalau NISN-nya belum tahu)

Data yang perlu disiapkan lebih banyak karena sistem harus menyaring dari seluruh siswa se-Indonesia:

- **nama lengkap siswa**
- **tempat lahir**
- **tanggal lahir**
- **nama ibu kandung**

Nama ibu kandung bukan hiasan — ia dipakai sebagai pembeda karena nama siswa bisa sama persis. Karena itu, saat mengisi, tulis nama sesuai dokumen kependudukan, bukan nama panggilan.

> Nama yang ditulis "Eka" padahal di Kartu Keluarga tertulis "Eka Nurhaliza" adalah sebab paling umum pencarian gagal. Sistem mencocokkan huruf, bukan maksud.

## Kenapa NISN tidak ditemukan saat dicek

Kalau pencarian kosong, penyebabnya hampir selalu salah satu dari lima ini. Urutkan pemeriksaannya dari yang paling murah:

**1. Data identitas tidak sama dengan dokumen kependudukan.** Salah satu huruf di nama, tanggal lahir yang tertukar, atau nama ibu kandung yang belum diperbarui setelah perceraian/perubahan dokumen.

**2. Siswa belum pernah diinput ke Dapodik.** Ini terjadi pada siswa yang baru masuk, siswa pindahan dari sekolah non-Kemendikdasmen, atau siswa dari sekolah yang belum memiliki NPSN.

**3. NISN-nya ada, tapi berstatus tidak valid.** Dalam istilah resmi, ini disebut **residu NISN** — data peserta didik yang tidak valid karena **belum memiliki NISN (NISN kosong)** atau **berstatus NISN ganda**, yaitu satu NISN dipakai lebih dari satu peserta didik.

**4. Siswa terdaftar ganda di dua sekolah.** Ini khas siswa pindahan: sekolah asal belum mengeluarkan datanya, sementara sekolah tujuan sudah mendaftarkannya. Akibatnya siswa terbaca aktif di dua sekolah sekaligus.

**5. Siswa sudah lulus dan datanya tidak ikut terverifikasi.** Lulusan yang butuh NISN untuk SNBP/SNBT atau kuliah sering menemukan jalurnya berbeda dari siswa aktif — lihat bagian verval lulusan di bawah.

## Kalau NISN tidak ketemu: langkah yang harus dilakukan operator

Semua perbaikan NISN berjalan lewat dua aplikasi: **Dapodik** (input data) dan **VervalPD** (verifikasi & validasi). Pembagian kewenangannya jelas dan sebaiknya tidak dilewati:

| Peran | Tugas |
|---|---|
| Operator Sekolah | Memastikan semua peserta didik punya NISN; menangani data di menu residu; menangani siswa belum ber-NISN (termasuk mencari sekolah asal untuk siswa mutasi); memperbaiki data Dapodik |
| Operator Dinas | Mengelola data peserta didik; menyetujui (approval) pengajuan **perubahan identitas** dan pengajuan **mutasi** dari sekolah |
| Operator PDSPK | Menyetujui pengajuan perubahan NISN; menyetujui mutasi yang diajukan Dinas; verifikasi NISN lulusan menengah atas |

Langkah praktisnya:

1. **Perbaiki identitas di Dapodik** agar sesuai Kartu Keluarga/Akta Kelahiran, lalu sinkron.
2. **Ajukan perubahan identitas lewat VervalPD** pada menu Edit Identitas. Pengajuan ini menunggu persetujuan Dinas.
3. **Untuk data invalid/residu**, selesaikan lewat menu residu di VervalPD sesuai keterangan status yang muncul.
4. **Untuk siswa mutasi**, ajukan lewat fitur **Pengeluaran Siswa (Tercatat Ganda)** dengan memilih jenis keluar **MUTASI**, lalu unggah Surat Keterangan Pindah.

### Dokumen yang disiapkan untuk mutasi

Dokumen mutasi harus **ditandatangani kepala satuan pendidikan dan dibubuhi stempel asli**, lalu dipindai:

- format **PDF**
- ukuran **maksimal 1 MB**

Kalau gagal unggah, hampir selalu karena ukuran atau karena berkas hasil foto HP yang sebenarnya bukan PDF melainkan JPG yang hanya diganti nama.

### Data yang perlu disiapkan saat mengajukan siswa ganda

Siapkan: **NPSN satuan pendidikan asal**, **NISN**, **nama**, dan **tanggal lahir** peserta didik. Empat data ini yang diisi pada form pengajuan pengeluaran siswa.

## Khusus lulusan: jalur verval lulusan berbeda

Lulusan SMA/SMK/MA yang butuh NISN untuk mendaftar kuliah **tidak memakai jalur siswa aktif**. Ada layanan khusus **Verval Lulusan** di subdomain PD (`pd.data.kemdikbud.go.id`, di bawah `/verval-lulusan/`).

Ini yang membuat banyak lulusan *gap year* gagal membuat akun SNPMB: NISN mereka tidak bisa divalidasi karena verifikasi lulusan belum disetujui. Urutannya harus benar — verval lulusan selesai dulu, baru registrasi akun.

Kebutuhan ini juga muncul pada siswa yang lulus sebelum perubahan kurikulum dan datanya belum ikut dipindahkan.

## Yang membuat NISN tetap sama saat pindah sekolah

Ini pertanyaan yang paling sering muncul dari orang tua: **apakah NISN berubah kalau anak pindah sekolah?** Jawabannya **tidak**. NISN adalah identitas tunggal se-Indonesia; yang berubah hanya sekolah tempat ia terdata.

Yang justru sering salah justru sebaliknya: operator sekolah tujuan **memasukkan data lama yang sudah tidak sesuai**, sehingga muncul data ganda. Karena itu, setelah siswa pindah, periksa kembali empat hal ini di Dapodik sekolah baru:

1. Nama sesuai dokumen kependudukan
2. Tempat dan tanggal lahir
3. **Nama ibu kandung**
4. NISN tetap nomor yang sama seperti di sekolah asal

Kalau salah satu keliru, ajukan koreksi ke operator Dapodik sekolah baru sebelum masalahnya menumpuk di akhir tahun ajaran.

## Cara menyimpan bukti NISN

Banyak sekolah terlambat menyadari hal ini: **halaman hasil pencarian NISN tidak menyimpan daftar.** Setiap kali ingin memeriksa satu siswa, datanya harus diisi ulang.

Karena itu, hal paling hemat waktu yang bisa dilakukan operator adalah menyimpan hasilnya sendiri. Cara yang paling praktis: catat NISN tiap siswa ke satu berkas **spreadsheet** berdampingan dengan data Dapodik (NISN, nama, tempat/tanggal lahir, nama ibu kandung, NPSN). Sekali disusun, ia menjadi rujukan yang bisa dipakai berulang untuk urusan SNBP, PIP, ijazah, dan pencetakan kartu peserta ujian.

Untuk sekolah yang beralih dari catatan kertas, berkas administrasi madrasah seperti kartu data siswa bisa dibuat dari template spreadsheet yang sama, sehingga NISN siswa tidak perlu dicari ulang setiap tahun. Versi ringkasnya bisa diunduh tanpa biaya di [Template Administrasi Madrasah 2026 — Versi Ringkas (Gratis)](/template-administrasi-madrasah-gratis/).

{{< bayar nominal="Rp25.000" >}}

## Ringkasan urutan kerja

Kalau Anda menemukan satu siswa tidak keluar NISN-nya, kerjakan berurutan — jangan langsung mengajukan ke pusat:

1. **Cocokkan identitas** dengan Kartu Keluarga/Akta Kelahiran (nama, tempat/tanggal lahir, nama ibu kandung).
2. **Cek di Dapodik** apakah siswa sudah terinput dan sinkron.
3. **Periksa status data** di VervalPD: residu, invalid, atau tercatat ganda?
4. **Ajukan sesuai jenis masalahnya** — perubahan identitas, pengeluaran siswa ganda, atau pengajuan NISN baru.
5. **Simpan nomor yang sudah benar** ke berkas administrasi supaya tidak dicari lagi tahun depan.

## Pertanyaan yang sering muncul

**Apakah NISN bisa diurus sendiri tanpa lewat sekolah?**
Untuk pencarian, ya. Untuk perbaikan data, tidak. Semua perubahan data peserta didik harus lewat operator sekolah karena hanya akun sekolah yang bisa menyentuh Dapodik dan VervalPD.

**Berapa lama pengajuan perbaikan disetujui?**
Bergantung pada tahap persetujuannya. Pengajuan identitas menunggu approval Dinas; pengajuan perubahan NISN dan mutasi dari Dinas menunggu approval PDSPK. Karena itu ajukan lebih awal, jangan saat mendekati tenggat pendaftaran.

**Kalau tiga digit awal NISN tidak sesuai tahun lahir, apakah nomornya harus diganti?**
Tidak. NISN itu tetap valid. Yang bisa diperbaiki adalah data siswanya, bukan nomornya.

---

**Butuh bantuan merapikan data siswa jadi berkas administrasi yang siap dipakai?** Saya mengerjakan olahan naskah dan dokumen administrasi sekolah. Kirim keterangan kebutuhan Anda ke **znl.hakim.arisandi@gmail.com** — jelaskan jumlah siswa dan data apa saja yang perlu direkap.
