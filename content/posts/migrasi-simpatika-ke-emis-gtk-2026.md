---
title: "Migrasi Simpatika ke EMIS GTK 2026: Urutan Kerja Operator Madrasah, Syarat Aktivasi, dan Berkas yang Wajib Disiapkan"
date: "2026-10-14T20:30:00+07:00"
draft: false
description: "Panduan operator madrasah memindahkan pendataan dari Simpatika (EMIS GTK lama) ke EMIS GTK baru 2026: alur login SSO EMIS 4.0, lima syarat keaktifan kolektif, rasio rombel, dan berkas pendukung TPG serta PPG."
tags: ["EMIS GTK", "Simpatika", "operator madrasah", "EMIS 4.0", "pendataan guru"]
categories: ["tips administrasi sekolah"]
---

Tahun ajaran 2026/2027 adalah tahun pertama madrasah mengerjakan pendataan guru dan tenaga kependidikan sepenuhnya di **EMIS GTK baru** — sistem yang menggantikan Simpatika. Yang membuat pekerjaan ini terasa berat bukan jumlah menunya, tetapi urutannya: di sistem lama, guru mengurus keaktifan diri lebih dulu lalu madrasah menyusul. Di sistem baru, **urutannya dibalik**.

Akibat urutan yang terbalik itu nyata dan bisa dilihat di layar. Selama madrasah belum melakukan keaktifan kolektif, semua akun guru akan berstatus merah dengan pesan: *"Tidak Dapat Mengaktifkan PTK, Aktivasi akun tidak dapat dilakukan karena madrasah satminkal belum aktif: NAMA MADRASAH. Hubungi Admin Sekolah untuk melakukan aktivasi instansi terlebih dahulu."*

Banyak operator berhenti di situ, mengira akun gurunya yang bermasalah. Yang bermasalah justru satu langkah sebelumnya — dan langkah itu ada di tangan operator, bukan guru.

## Kenapa pindah, dan sejak kapan

Perpindahan ini berlangsung bertahap sepanjang 2026, dengan target rampung pada Juli 2026. Sejak 5 Juli 2026 aplikasi resmi memakai domain utama `emisgtk.kemenag.go.id`, sementara alamat lama masih dipertahankan di `old-emisgtk.kemenag.go.id` selama masa transisi. Jadi kalau ada guru yang masih membuka tautan Simpatika lama, datanya mungkin masih terbaca — tetapi itu bukan tempat mengerjakan pendataan baru.

Skala pekerjaannya besar. Data yang beredar menyebut sekitar **87.614 madrasah** dan **843.717 pendidik aktif** yang berada di dalam sistem ini. Artinya, kelambatan satu madrasah tidak hanya mengganggu guru di madrasah itu: data EMIS menjadi acuan untuk BOS, PIP, sarana prasarana, NRG, SKAKPT, TPG, hingga PPG. Kalau data tidak mutakhir, yang tertunda bukan cuma urusan administratif, tetapi juga kesiapan ikut PPG dan pemasukan tunjangan.

## Perbedaan yang paling sering menjebak

Ini yang membuat operator yang sudah bertahun-tahun memegang Simpatika tetap tersandung:

| Hal | Simpatika (EMIS GTK lama) | EMIS GTK baru |
|---|---|---|
| Login | Akun Simpatika sendiri | **SSO EMIS 4.0** ("Masuk dengan EMIS") |
| Urutan keaktifan | Guru aktif dulu, madrasah menyusul | **Madrasah (keaktifan kolektif) dulu**, baru guru |
| Rombel | Dibuat langsung di Simpatika | **Harus ditarik dari EMIS 4.0**, tidak bisa dibuat manual |
| Data induk | Terpisah-pisah | Satu basis data terintegrasi |

Baris ketiga itu yang paling menyita waktu. EMIS GTK **tidak menyediakan pembuatan rombongan belajar secara manual**. Rombel wajib hasil sinkronisasi atau "tarik data dari EMIS 4.0". Kalau rombel belum ada di EMIS 4.0, tiga dari lima syarat keaktifan kolektif otomatis tidak bisa dipenuhi.

## Lima syarat keaktifan kolektif — lengkap

Keaktifan kolektif atau aktivasi madrasah dikerjakan lewat akun **Admin Madrasah**. Lima syaratnya:

1. Minimal **1 guru aktif** terdaftar.
2. Minimal **50% guru** sudah mengisi jadwal.
3. **Jadwal kelas mingguan** sudah ada.
4. Setiap **rombel sudah punya wali kelas**.
5. **Kepala madrasah sudah di-assign**.

Kelengkapan kelimanya bisa dicek lewat menu **Madrasah → Keaktifan Kolektif → Cek Kelengkapan & Ajuan**.

Urutan pengerjaan sebelum kelima syarat itu bisa dicentang:

1. **Generate kurikulum** dan perbarui mata pelajaran (menu **Madrasah → Mata Pelajaran**), bila diperlukan.
2. **Kelola kurikulum** (menu **Madrasah → Pengaturan Jadwal → Kelola Kurikulum**).
3. **Buat model jadwal** (menu **Madrasah → Pengaturan Jadwal → Tambah Model**) bila madrasah belum punya.
4. **Edit slot template jadwal** untuk mengatur waktu upacara dan jam istirahat.
5. **Validasi rombel** (menu **Madrasah → Rombel → Validasi EMIS**) untuk memeriksa kesesuaian rombel dan jumlahnya terhadap rasio peserta didik.
6. **Tarik data rombel** dari EMIS 4.0 (menu **Madrasah → Rombel → Tarik dari EMIS**).
7. **Penugasan guru BK/TIK** (menu **Madrasah → Plotting Guru BK → Tambah Plotting**), bila diperlukan.
8. **Tambah jam mengajar** per kelas atau lewat ikon tanda plus di belakang nama guru.
9. **Input wali kelas** (menu **Guru & Tenaga Kependidikan → Tugas Tambahan → ikon mata di belakang nama guru → Tugas Tambahan Lainnya → Tambah**).

## Rasio rombel: angka yang menentukan validasi

Pada langkah validasi rombel, penambahan rombel lebih dari satu harus memenuhi rasio minimal:

- **1:15** untuk RA, MI, MTs, dan MA.
- **1:12** untuk MAK.

Contoh penerapan yang sering ditanyakan: madrasah dengan 40 siswa MI dan sudah punya dua rombel. Rasio 1:15 berarti dua rombel menampung sampai 30 siswa; 40 siswa masih wajar untuk dua rombel (20 per rombel), jadi ajuan dua rombel lolos. Yang sering ditolak adalah menambah rombel ketika setiap rombel lama belum terisi mendekati batas — di situ sistem menandai rombel baru sebagai tidak sesuai rasio.

## Tiga kolom pengaturan yang harus hijau semua

Saat pertama kali membuka **Tambah Jam Mengajar → Jadwal Per Kelas**, akan tampil daftar rombel dengan kolom **Pengaturan** berisi tiga hal. Ketiganya harus beres sebelum jadwal bisa diisi:

- **Kompetensi** — kalau masih merah, perbaiki di menu **Madrasah → Rombel → Kompetensi**. Bila daftar kompetensi belum ada, klik **Tambah Kompetensi**; bila sudah ada, pakai ikon **Set ke rombel kosong** pada kolom Aksi, atau pilih kompetensi per rombel pada kolom Pilih Kompetensi.
- **Kurikulum** — kalau merah, perbaiki di **Madrasah → Pengaturan Jadwal → Kelola Kurikulum**.
- **Model** — kalau merah, buat model di **Madrasah → Pengaturan Jadwal**, lalu klik ikon **Assign Rombel** pada kolom Aksi.

Setelah semua dikerjakan, buka lagi **Keaktifan Kolektif**, jalankan **Cek Kelengkapan Data**, dan pastikan daftar syarat aktivasi **bercentang hijau semua**. Periksa juga bagian **Validasi Wali Kelas**, **Tugas Tambahan Utama yang Diverifikasi Kab/Kota**, dan **Detail Jadwal Kelas Mingguan**. Bila sudah bersih, klik **Ajukan Keaktifan Kolektif** di bagian paling bawah, lalu tunggu persetujuan Admin Kab/Kota.

## Membuat akun untuk guru baru

Guru tidak bisa mendaftar sendiri. Operator harus **meng-generate** akunnya:

1. Login ke akun lembaga EMIS GTK, buka menu **Manajemen Akun**.
2. Saat pertama kali dibuka, daftar nama PTK masih kosong — klik **Generate Akun PTK** di pojok kanan atas.
3. Muncul jendela berisi daftar PTK madrasah; klik **Generate Akun** di pojok kanan bawah.
4. Setelah berhasil, daftar PTK tampil beserta username dan password masing-masing. Klik **Download Excel** dan simpan daftarnya.
5. Bagikan username dan password ke masing-masing PTK. Bila ada yang lupa, operator bisa mereset dengan ikon kunci pada kolom tombol aksi.

PTK yang sudah tidak aktif sebaiknya dinonaktifkan lewat tombol aksi pada kolom Status, dengan memilih alasan, lalu klik **Nonaktifkan**. Membiarkan nama orang yang sudah tidak bertugas di daftar membuat rekap jumlah guru di madrasah membengkak, dan itu ikut terbaca pada perhitungan yang memakai data EMIS.

Guru lalu login memakai username dan password yang diterima, dan **melakukan Aktivasi PTK**. Perlu diingat: pada login pertama, menu di sisi kiri masih terbatas. Menu lengkap baru muncul **setelah** aktivasi PTK selesai. Banyak guru mengira akunnya rusak karena menunya sedikit, lalu melapor ke operator — padahal tinggal menyelesaikan aktivasi.

## Berkas yang sebaiknya disiapkan sebelum periode pendataan

Karena periode pendataan semester ganjil sudah dibuka, ini daftar yang layak disiapkan lebih dulu supaya pengerjaan tidak terputus di tengah:

- **Daftar guru dan tenaga kependidikan** dengan NUPTK, NIK, dan status kepegawaian terbaru.
- **Surat tugas mengajar** semester berjalan untuk setiap guru, karena jadwal mengajar harus diisi dan ditopang bukti penugasan.
- **Susunan rombel dan wali kelas** versi terbaru, agar penarikan data dari EMIS 4.0 tidak ditarik dari berkas lama.
- **Daftar mata pelajaran dan kurikulum** yang berlaku tahun ini.
- **Catatan tugas tambahan** (kepala madrasah, wakil, wali kelas, guru BK, TIK) yang sudah ditetapkan lewat SK.

Kalau lima berkas ini disusun di atas kertas maupun spreadsheet sebelum membuka sistem, urutan pengisian menjadi satu arah: lengkapi kurikulum → buat model jadwal → validasi dan tarik rombel → input jam mengajar → input wali kelas → cek kelengkapan → ajukan keaktifan kolektif → generate akun PTK → guru aktivasi. Mengikuti urutan itu jauh lebih cepat daripada melompat-lompat lalu mengulang dari awal.

Untuk menyusun daftar guru, jadwal, dan tugas tambahan secara rapi, versi ringkas templat administrasi madrasah bisa diunduh gratis lebih dahulu di [Templat Administrasi Madrasah 2026 — Versi Ringkas (Gratis)](/template-administrasi-madrasah-gratis/) sebelum memutuskan memakai versi lengkapnya. Untuk madrasah atau pesantren yang perlu mengolah naskah lama, ijazah, atau arsip guru menjadi berkas digital rapi, rincian paket ada di [Jasa Olah Naskah Kitab jadi Aplikasi Android](/jasa-olah-naskah/).

## Yang paling sering membuat pendataan terhambat

Beberapa hal yang berulang muncul dan bisa dicegah lebih dulu:

- **Menarik rombel sebelum rombel di EMIS 4.0 rampung.** Rombel di EMIS GTK hasil tarikan, jadi kalau sumbernya belum final, yang tertarik pun belum final. Rapikan di EMIS 4.0 dulu.
- **Mengerjakan jadwal mengajar padahal kolom pengaturan masih merah.** Isian jadwal tidak akan diterima dengan benar; perbaiki kompetensi, kurikulum, dan model lebih dulu.
- **Menganggap keaktifan kolektif bisa dikerjakan setelah guru aktif.** Urutannya justru madrasah lebih dulu. Kalau ini tertukar, semua akun guru akan tetap merah dan waktunya habis untuk mengejar hal yang salah.
- **Menunda sampai mendekati batas waktu.** Beban sistem yang padat menjelang tenggat membuat pengisian terasa macet, padahal persyaratannya sudah lengkap.
- **Membiarkan data guru tidak mutakhir.** Data EMIS menjadi acuan BOS, PIP, NRG, SKAKPT, TPG, dan PPG. Satu nama yang salah atau tidak masuk berarti satu orang yang tertinggal pada seluruh layanan yang bermuara pada data itu.

## Ringkasan yang bisa langsung dikerjakan

Kalau hanya bisa mengerjakan tiga hal minggu ini, kerjakan ini berurutan:

1. **Rapikan rombel di EMIS 4.0 lebih dulu**, lalu validasi dan tarik ke EMIS GTK. Tanpa ini, syarat nomor dua sampai empat tidak akan pernah bisa dicentang.
2. **Selesaikan kurikulum, model jadwal, jam mengajar, dan wali kelas**, lalu jalankan Cek Kelengkapan Data sampai semuanya bercentang hijau.
3. **Ajukan keaktifan kolektif, baru generate akun PTK** dan bagikan ke guru untuk melakukan aktivasi. Ingat urutannya tidak bisa dibalik.

Satu catatan yang sering terlewat: simpan hasil **Download Excel** daftar akun PTK di tempat yang tersimpan baik dan jangan disebar lewat grup terbuka. Data itu memuat username dan password seluruh guru, dan kebocorannya bisa langsung dipakai orang lain untuk mengubah data pribadi mereka di sistem.

## Baca juga

- [Dapodik 2027 untuk Operator Sekolah & Madrasah: Panduan Pemutakhiran Data Semester Ganjil 2026/2027](/posts/dapodik-2027-panduan-operator-sekolah-madrasah-2026/)
- [Panduan Pengelolaan Kinerja Guru 2026 di Ruang GTK: Langkah Praktis Isi SKP hingga Observasi Kelas](/posts/panduan-pengelolaan-kinerja-guru-2026-ruang-gtk/)
- [Panduan Presentasi PowerPoint untuk Guru 2026: Tips dari Slide Pertama sampai Penutup](/posts/panduan-presentasi-powerpoint-guru-2026/)
- [Persiapan ANBK & Ujian Berbasis Komputer 2026: Checklist Teknis, Peran Proktor-Teknisi, dan Tips Anti-Gagal](/posts/persiapan-anbk-ujian-berbasis-komputer-sekolah-madrasah-2026/)

---

**Madrasah Anda punya tumpukan arsip guru dan naskah lama yang perlu dirapikan jadi berkas digital?** Kirim keterangan singkat: jumlah berkas atau judul, perkiraan halaman, jenis pekerjaan yang dibutuhkan (pindai saja, pindai + OCR, atau ada bagian yang harus diketik ulang), dan tenggat yang diinginkan. Beberapa halaman contoh bisa dikerjakan lebih dahulu sebelum pekerjaan penuh disetujui.

{{< bayar judul="Mulai Digitalisasi Arsip Madrasah" nominal="Rp750.000" >}}
