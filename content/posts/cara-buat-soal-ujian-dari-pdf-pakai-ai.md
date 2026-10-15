---
title: "Membuat Soal dari Bahan Ajar Pakai AI: Alur Kerja, Rambu-rambu, dan Kesalahan yang Sering Terjadi"
date: 2026-10-14T10:03:00+07:00
draft: false
description: "Alur kerja menyusun soal dengan bantuan AI: menyiapkan bahan ajar, menyusun perintah per bagian, memeriksa kualitas soal, sampai menyimpan bank soal yang bisa dipakai ulang."
tags: ["ai untuk guru", "bank soal", "asesmen", "soal ujian"]
categories: ["teknologi pendidikan"]
---

Bantuan AI untuk menyusun soal sudah banyak dipakai guru, tetapi hasilnya sering mengecewakan: soal terlalu mudah, kunci jawabannya ada yang salah, dan pertanyaannya menanyakan hal yang tidak penting. Hampir selalu penyebabnya bukan AI-nya, melainkan cara bahan ajar dimasukkan ke dalam perintah dan seberapa teliti hasilnya diperiksa.

Tulisan ini membahas alur kerjanya dari awal sampai soal siap diujikan — termasuk bagian yang paling sering dilewati, yaitu pemeriksaan.

## Yang perlu disiapkan sebelum mulai

Tiga hal, dan ini menentukan seluruh hasilnya:

**1. Bahan ajarnya harus berupa teks yang bisa dibaca mesin.** Berkas hasil pindai (gambar dari pemindai atau foto) tidak bisa dibaca langsung. Perlu diubah dulu menjadi teks. Banyak guru membuang waktu di sini karena tidak sadar bahan ajarnya masih berupa gambar.

**2. Satu bagian kecil untuk satu kali kerja.** Jangan menyerahkan satu buku penuh. Ambil satu pertemuan, satu subbab, atau paling banyak satu bab. Bahan yang terlalu luas membuat soal menyebar ke hal-hal yang tidak dibahas di kelas.

**3. Tentukan dulu apa yang ingin diukur.** Kalau guru belum memutuskan apakah ingin menguji ingatan, pemahaman, atau penerapan, AI akan memilih "yang paling ringan" — yaitu sekadar mengulang kalimat dari buku.

## Alur kerja tujuh langkah

### Langkah 1 — Ubah bahan hasil pindai menjadi teks

Kalau bahan ajar berupa gambar hasil pemindaian, ubah dulu menjadi teks. Caranya bisa dengan perangkat gratis yang tersedia dalam jaringan (banyak layanan pemindai daring menyediakan ini) atau dengan perangkat yang dipasang di komputer.

Praktik yang menghemat waktu: **jangan mengubah seluruh buku sekaligus.** Ubah hanya bagian yang akan diujikan. Hasil pengubahan teks selalu perlu dibetulkan di sana-sini — terutama angka, nama, dan istilah asing — maka makin sedikit yang diubah, makin sedikit yang harus dibetulkan.

### Langkah 2 — Rapikan teks sebelum dipakai

Setelah menjadi teks, buang bagian yang tidak diperlukan: nomor halaman, kepala halaman yang berulang, daftar pustaka, dan gambar keterangan. Teks yang bersih mengurangi soal yang aneh.

Periksa juga hal-hal yang sering rusak saat pengubahan: **satuan, angka, dan tanda baca**. Soal hitungan yang angkanya berubah akibat salah baca akan menghasilkan kunci jawaban yang salah, dan itu sulit dilacak setelah soal tercetak.

### Langkah 3 — Susun perintah yang lengkap

Perintah yang hanya berbunyi "buatkan soal dari teks ini" menghasilkan soal yang datar. Perintah yang baik memuat lima hal:

- **Jenis soal** dan jumlahnya
- **Tingkat berpikir** yang diinginkan (mengingat, memahami, menerapkan, menganalisis)
- **Bahan acuan** yang boleh dipakai
- **Bentuk jawaban** yang diminta (kunci, pembahasan, atau keduanya)
- **Batasan** yang jelas, misalnya "jangan menanyakan tahun terbit" atau "gunakan istilah yang ada di teks saja"

Contoh perintah yang bisa langsung dipakai:

```
Berdasarkan bahan ajar di bawah ini, buatkan 15 soal pilihan ganda
dengan 4 opsi jawaban.

Ketentuan:
- 5 soal menguji pemahaman, 7 soal menguji penerapan, 3 soal menguji analisis.
- Semua istilah harus yang ada di dalam teks.
- Sertakan kunci jawaban dan alasan singkat mengapa opsi lain salah.
- Sebutkan bagian teks mana yang menjadi dasar setiap soal.

Bahan ajar:
[tempelkan teks di sini]
```

Permintaan "sebutkan bagian teks mana yang menjadi dasar setiap soal" sangat berguna. Dengannya guru bisa memeriksa dalam sekali baca apakah soalnya benar-benar berasal dari bahan yang diujikan, atau melenceng ke hal lain.

### Langkah 4 — Minta perbaikan bertahap, jangan sekali jadi

Hasil pertama hampir selalu perlu diperbaiki. Perbaikan yang efektif dilakukan bertahap dengan menunjuk bagian yang kurang:

- "Soal nomor 3 terlalu mudah; ubah menjadi soal penerapan."
- "Opsi B dan D pada nomor 7 terlalu mirip; perjelas pembedanya."
- "Nomor 11 menanyakan hal yang tidak ada di teks; ganti dengan pengertian yang dibahas di paragraf ketiga."

Cara ini jauh lebih hemat waktu daripada meminta AI "membuat ulang semuanya".

### Langkah 5 — Periksa satu per satu (langkah yang tidak boleh dilewati)

Inilah bagian yang paling sering membuat masalah. Soal bantuan AI wajib diperiksa guru, dan yang diperiksa bukan hanya jawabannya:

**Periksa kuncinya sendiri.** Hitung ulang soal hitungan. Cocokkan jawaban soal hafalan dengan teks. Kesalahan kunci jawaban adalah kesalahan yang paling merugikan karena baru ketahuan setelah ujian berjalan.

**Periksa apakah soalnya bisa dijawab tanpa membaca teks.** Soal yang bisa dijawab dari pengalaman umum tidak mengukur apa pun. Kalau opsi jawabannya bisa ditebak hanya dari panjang kalimatnya, soal itu perlu diubah.

**Periksa sebaran jawaban.** Kadang jawaban benar menumpuk pada satu huruf dalam jumlah yang tidak wajar.

**Periksa tata bahasa dan istilah.** Perhatikan kata serapan atau istilah yang tidak dipakai di sekolah, dan istilah asing yang seharusnya ditulis miring.

**Periksa kepatutan.** Buang soal yang menyentuh hal pribadi, perbandingan antarsiswa, atau hal yang bisa menyinggung golongan tertentu.

Satu kebiasaan yang layak dipertahankan: **kerjakan sendiri soal itu seperti siswa mengerjakannya**, tanpa melihat kunci. Sering di situ ketahuan soal yang ambigu atau punya lebih dari satu jawaban benar.

### Langkah 6 — Rapikan format dan susun kisi-kisi

Setelah soal bersih, susun dalam bentuk yang siap dicetak: kepala sekolah, mata pelajaran, kelas, waktu, petunjuk pengerjaan, dan lembar jawaban kalau perlu.

Kalau ada waktu, buat **tabel kisi-kisi sederhana** yang memetakan setiap soal ke tujuan pembelajarannya. Tabel ini dua kegunaan sekaligus: memastikan semua bagian bahan ajar terwakili, dan menjadi bukti bahwa penilaian disusun dengan sengaja ketika ada pemeriksaan.

### Langkah 7 — Simpan sebagai bank soal

Soal yang tersimpan rapi akan menghemat waktu paling besar di tahun berikutnya. Simpan dengan penataan yang sederhana:

- Satu berkas per mata pelajaran per tingkat
- Kolom: nomor soal, isi soal, kunci, tingkat berpikir, dan bagian bahan ajar asalnya
- Tandai soal yang pernah dipakai dan tahun pemakaiannya

Soal lama bisa dipakai ulang dengan pengubahan pilihan jawaban, tetapi jangan menyusun seluruh ujian dari soal yang pernah dipakai — siswa saling berbagi pengalaman soal.

## Kapan sebaiknya AI tidak dipakai

Bantuan AI paling tidak cocok untuk **soal yang membutuhkan penilaian pertimbangan**, misalnya soal yang meminta pendapat pribadi, karya tulis, atau jawaban yang sahihnya bergantung pada konteks kelas. Untuk jenis ini, guru lebih baik menyusun sendiri kerangka soal dan rubrik penilaiannya.

Begitu pula untuk **materi yang wajib persis**: ayat, teks undang-undang, rumus, dan definisi baku. Sekali salah kutip, kesalahannya ikut tersebar ke seluruh kelas. Untuk bagian seperti ini, salin langsung dari sumbernya, jangan minta AI menuliskannya.

## Pertanyaan yang sering muncul

**Apakah soal hasil bantuan AI boleh dipakai untuk ujian resmi?**
Boleh, selama guru memeriksa dan bertanggung jawab atas isinya. Tanggung jawab penilaian tetap ada pada guru, bukan pada alat yang dipakai.

**Mengapa soal yang dihasilkan terasa dangkal?**
Hampir selalu karena bahan ajar yang dimasukkan terlalu luas dan perintahnya terlalu singkat. Perkecil bahan, perjelas ketentuan.

**Apakah bahan ajar sekolah aman dimasukkan ke layanan AI?**
Jangan memasukkan data pribadi siswa — nama, nomor induk, nilai, atau data keluarga. Bahan ajar berupa teks pelajaran umumnya aman, tetapi simpan kebiasaan untuk membuang identitas sebelum menyalin isi berkas.

**Perlu berapa lama untuk satu set soal?**
Menyiapkan dan memeriksa 20 soal biasanya lebih cepat daripada menyusunnya sendiri, tetapi bukan berarti tanpa kerja. Sisakan waktu untuk pemeriksaan; menghemat waktu di bagian ini justru yang paling berisiko.

---

*Tulisan ini membahas cara kerja, bukan menyarankan satu layanan tertentu. Periksa kembali seluruh soal sebelum dipakai menilai.*

---

## Butuh naskah atau kitab dijadikan aplikasi?

Kalau lembaga Anda punya naskah, kitab, atau catatan pengajian yang masih berbentuk PDF scan atau tulisan tangan, kami mengerjakan pengubahan naskah itu menjadi aplikasi Android yang bisa dibuka langsung dari HP — lengkap dengan pencarian, harakat, dan terjemahan. Naskah yang dikirimkan hanya dipakai untuk pesanan lembaga Anda.

Rincian paket dan estimasi biaya: [Jasa Olah Naskah Arab](https://radar9.my.id/jasa-olah-naskah/) (mulai Rp750.000).

<!-- Blok Umpan Gratis -->
<div class="blok-umpan">
  <h3 class="blok-umpan__judul">Rekap nilainya tidak perlu dibuat manual</h3>
  <p>Setelah soal jadi, yang berikutnya dibutuhkan adalah lembar rekap nilai dan daftar hadir. Formatnya bisa dipakai langsung.</p>
  <p>Versi ringkasnya bisa <strong>diunduh gratis</strong> — 3 sheet berisi data siswa, absensi,
     dan kas dengan saldo berjalan otomatis. Berkas <code>.xlsx</code> tanpa makro, tanpa perlu
     instal apa pun.</p>
  <p><strong>→ <a href="/template-administrasi-madrasah-gratis/">Unduh gratis: Template Administrasi Madrasah 2026 (versi ringkas, 3 sheet)</a></strong></p>
  <p>Kalau butuh yang lebih lengkap (8 sheet, termasuk daftar hadir guru, inventaris, dan rekap
     nilai), versinya Rp25.000 ada di halaman
     <a href="/produk-template-excel-madrasah-2026/">Template Administrasi Madrasah 2026</a>.</p>
</div>
