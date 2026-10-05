---
title: "Membangun Laboratorium Komputer Sekolah & Madrasah 2026: Spesifikasi Minimal, Rincian Biaya & Tips Hemat"
date: "2026-10-05T09:00:00+07:00"
draft: false
description: "Panduan lengkap membangun lab komputer sekolah dan madrasah 2026: spesifikasi resmi TKA/ANBK, rincian biaya, dan tips hemat untuk dana BOS."
tags: ["peralatan sekolah", "laboratorium komputer", "dana bos", "anbk", "teknologi pendidikan"]
categories: ["peralatan sekolah"]
---

Ruangan ber-AC, meja panjang berjajar, dan deretan komputer yang menyala serentak — begitulah gambaran ideal laboratorium komputer di sekolah. Masalahnya, bagi banyak madrasah dan sekolah di daerah, lab komputer kerap jadi ruangan paling sepi peralatan: komputer warisan dari zaman Windows XP, keyboard ada yang hilang beberapa tombol, dan satu-dua unit mati begitu dinyalakan.

Beban bertambah ketika sekolah harus menyelenggarakan asesmen berbasis komputer seperti ANBK dan sekarang TKA (Tes Kemampuan Akademik). Mau tidak mau, lab harus benar-benar siap perangkat dan jaringannya. Artikel ini membahas cara membangun atau meremajakan lab komputer langkah demi langkah, mulai dari jumlah unit yang dibutuhkan, spesifikasi yang benar-benar diminta regulasi, sampai hitungan biaya dan cara menekan pengeluaran tanpa mengorbankan fungsi.

## Berapa Komputer yang Sebenarnya Dibutuhkan?

Pertanyaan pertama yang biasanya muncul di rapat komite: mau beli berapa unit? Jawabannya bukan berdasarkan jumlah murid satu sekolah, tetapi berdasarkan jumlah peserta tes dalam satu sesi sekaligus.

Aturan praktisnya begini. Jika satu kelas berisi 30–32 murid, sekolah umumnya menggelar tes dalam beberapa sesi. Untuk menampung satu sesi penuh plus satu unit cadangan (yang wajib ada, karena kalau komputer peserta mati di tengah tes, tidak ada yang bisa menggantikan), ukuran lab minimal adalah:

- Sekolah kecil (peserta tes per jenjang di bawah 60 murid): 20–24 unit klien + 1 komputer proktor.
- Sekolah sedang (60–150 murid): 32–36 unit klien + 1 komputer proktor + 1 unit cadangan.
- Sekolah besar/madrasah dengan banyak rombel: 40 unit klien, dipecah menjadi dua ruang atau dua sesi.

Yang sering terlupakan adalah komputer proktor. Ini perangkat terpisah dari komputer peserta, dan spesifikasinya justru lebih tinggi karena menjalankan aplikasi pengelola tes, sinkronisasi data, sampai token. Banyak sekolah salah kaprah memakai satu komputer proktor merangkap klien — padahal kalau proktor berhenti bekerja, seluruh sesi di ruangan itu ikut tersendat.

## Spesifikasi Resmi: Jangan Beli Komputer Kalah dari Ketentuan

Bagian ini yang paling sering membuat sekolah membeli perangkat "seadanya", lalu terpaksa kucing-kucingan saat pendataan infrastruktur. Juknis penyelenggaraan asesmen nasional dan TKA mengatur spesifikasi minimal yang harus dipenuhi sekolah, dan itu berbeda antara moda daring (online penuh) dan moda semi daring.

### Komputer Klien (komputer peserta)

Untuk komputer yang dipakai peserta, ketentuannya relatif ringan:

- Berbentuk PC, All-in-One, atau laptop.
- Prosesor dual core.
- RAM minimal 2 GB.
- Monitor minimal 11,6 inci, resolusi minimal 1024 x 720 piksel.
- NIC/WiFi tersedia, webcam opsional.
- Ruang penyimpanan kosong minimal 10 GB.
- Sistem operasi minimal Windows 7, Mac OS, atau Chrome OS yang terdaftar pada akun belajar.id.
- Aplikasi wajib: Exambrowser Client. Untuk peserta disabilitas tuna netra perlu screen reader (NVDA atau JAWS).

Perhatikan satu hal penting di sini: Chrome OS diperbolehkan untuk komputer klien, asalkan perangkatnya terdaftar pada akun belajar.id. Inilah dasar hukum mengapa Chromebook boleh dipakai untuk asesmen — kabar baik bagi sekolah yang ingin perangkat murah, ringan, dan hemat daya.

### Komputer Proktor

Spesifikasi proktor jauh lebih berat, dan khusus untuk moda semi daring aturannya sangat ketat:

- Wajib berbentuk PC atau All-in-One, **bukan laptop**.
- Prosesor 4 core dengan clock rate minimal 1,6 GHz (64 bit).
- RAM 8 GB.
- Dua port LAN (NIC) 100/1000 Mbps.
- Ruang penyimpanan kosong minimal 100 GB.
- Sistem operasi Windows 7 64-bit minimal.
- Aplikasi: VirtualBox, VHD, dan Exambrowser Admin.

Kalau sekolah memilih moda daring penuh untuk proktor, ketentuannya lebih ringan — cukup dual core, RAM 2 GB, dan menjalankan Proktor Browser. Namun perlu diingat, moda daring penuh menuntut koneksi internet stabil selama tes berlangsung. Moda semi daring hanya butuh internet saat sinkronisasi, aktivasi komputer proktor, rilis token, dan unggah jawaban, sementara komputer klien cukup memakai jaringan lokal.

### Jaringan: Titik yang Paling Sering Gagal

Banyak lab komputer "cukup bagus" komputernya tetapi kacau saat tes karena jaringan. Ketentuan untuk moda daring:

- Bandwidth minimal 16 Mbps untuk 40 klien.
- Rumus perhitungannya: 0,4 Mbps per komputer klien. Jadi kalau ada 100 peserta, kebutuhan minimalnya 40 Mbps.
- Perangkat jaringan memakai switch/hub dan kabel minimal CAT5E 100/1000, atau Access Point yang stabil diakses 20 klien bersamaan, dengan keamanan login dan WPA/PSK.

Sedangkan untuk moda semi daring, aturannya:

- Kabel minimal CAT5E 100/1000, setiap komputer proktor minimal punya satu switch.
- Bandwidth minimal 1 Mbps stabil (jauh lebih ringan, karena klien bekerja offline).
- IP address dibuat statis dengan segmen 192.168.0.n (n = 1 sampai 254, kecuali 200).
- Komputer klien **tidak diperbolehkan memakai WiFi** — harus kabel LAN.

Aturan terakhir ini sering dilanggar. Menggunakan WiFi untuk klien semi daring membuat sinkronisasi data rawan putus, terutama kalau ada puluhan perangkat berebut sinyal di ruangan yang sama.

## Rincian Biaya: Berapa yang Harus Disiapkan?

Harga perangkat bergerak setiap tahun, jadi angka di bawah ini adalah gambaran kisaran pasar 2026 untuk kelas perangkat yang biasa dipakai sekolah. Gunakan sebagai patokan menyusun RAB, lalu verifikasi dengan penawaran vendor lokal atau e-katalog.

**PC desktop rakitan (klien), spesifikasi di atas ketentuan minimal:**

- CPU kelas entry (misalnya seri Celeron atau Ryzen 3 terbaru), motherboard, RAM 8 GB, SSD 256 GB, casing + power supply, monitor 19–21 inci, keyboard + mouse: sekitar Rp4,5 juta sampai Rp6,5 juta per unit.

**PC All-in-One (klien atau proktor):**

- Ukuran 21–24 inci, RAM 8 GB, SSD 256–512 GB: sekitar Rp6,5 juta sampai Rp9,5 juta per unit. Cocok untuk lab yang ruangnya sempit karena tidak perlu CPU terpisah di bawah meja. Untuk proktor, pastikan model yang punya dua port LAN.

**Laptop klien:**

- RAM 8 GB, SSD 256 GB, layar 14 inci: sekitar Rp6 juta sampai Rp8 juta per unit.

**Chromebook:**

- Perangkat Chrome OS resmi, RAM 4–8 GB, penyimpanan 32–64 GB: sekitar Rp3,5 juta sampai Rp6 juta per unit. Ini opsi paling hemat daya dan paling gampang dirawat, asalkan perangkat dikelola lewat akun belajar.id. Perlu dicatat, Chromebook bukan pilihan untuk komputer proktor.

**Perangkat jaringan:**

- Switch 24 port gigabit: sekitar Rp700 ribu sampai Rp1,5 juta.
- Kabel UTP CAT5E per meter plus konektor dan jasa crimping: sekitar Rp8 ribu sampai Rp15 ribu per titik.
- Access Point kelas kantor: sekitar Rp500 ribu sampai Rp1,5 juta per unit.

**Perabot dan pendukung:**

- Meja komputer panjang (per unit): Rp400 ribu sampai Rp900 ribu.
- Kursi: Rp250 ribu sampai Rp500 ribu per unit.
- Stabilizer atau UPS untuk komputer proktor: Rp500 ribu sampai Rp1,5 juta.
- AC ruangan: sesuaikan dengan luas ruang, kisaran Rp3,5 juta sampai Rp7 juta untuk unit 1 PK hingga 2 PK.

Sebagai gambaran, lab 20 unit klien rakitan plus satu proktor, meja, kursi, jaringan, dan satu unit AC bisa menelan biaya sekitar Rp130 juta sampai Rp170 juta. Lab 36 unit dengan All-in-One bisa dua kali lipatnya. Angka ini yang perlu dicocokkan dengan pagu dana BOS dan kemampuan komite sebelum diputuskan.

## Memakai Dana BOS: yang Perlu Diperhatikan

Pengadaan peralatan lab komputer umumnya dibiayai dari dana BOS, dan sejak 2026 aturannya diperbarui melalui Permendikdasmen Nomor 8 Tahun 2026 tentang Petunjuk Teknis Pengelolaan Dana Bantuan Operasional Satuan Pendidikan (BOSP), yang berlaku mulai 6 Februari 2026 dan menggantikan aturan tahun sebelumnya. Dana BOSP 2026 dialokasikan sekitar Rp59 triliun melalui tiga skema: BOSP Reguler, BOSP Kinerja, dan BOSP Afirmasi.

Beberapa batas yang wajib diingat saat menyusun RKAS:

- Komponen sarana dan prasarana maksimal 20% dari total pagu alokasi.
- Komponen buku minimal 10% untuk jenjang pendidikan dasar dan menengah, dan 5% untuk PAUD.
- Honor maksimal 20% dari total pagu untuk sekolah negeri dan 40% untuk sekolah swasta.

Karena komponen sarana dibatasi 20%, pengadaan lab komputer biasanya tidak bisa dilakukan sekaligus dalam satu tahun untuk sekolah dengan pagu kecil. Strategi yang lebih realistis adalah bertahap: tahun pertama membeli 10–12 unit dan perangkat jaringan, tahun kedua menambah sisanya. Kalau kebutuhan mendesak, sekolah juga bisa mengusulkan lewat BOSP Kinerja yang fokusnya mencakup digitalisasi pembelajaran.

Satu hal lagi yang praktis: masukkan kebutuhan asesmen seperti TKA ke dalam ARKAS tahun berjalan. Juknis TKA secara tegas menyebut bahwa satuan pendidikan boleh mengalokasikan anggaran TKA dari dana BOS Reguler, termasuk untuk honor proktor dan teknisi, dengan mengacu Standar Satuan Harga daerah. Jadi jangan ragu menganggarkan honor petugas — itu sah dan memang dimaksudkan begitu.

## Tips Hemat yang Benar-Benar Berhasil

**Pertama, manfaatkan BOSP Kinerja untuk perangkat digital.** Sekolah yang memenuhi kriteria penerima BOSP Kinerja bisa menggunakan dana ini untuk digitalisasi pembelajaran, termasuk perangkat pendukung. Cek kriteria di dinas pendidikan setempat, jangan berasumsi.

**Kedua, beli bertahap dan prioritaskan komputer proktor.** Kalau anggaran mepet, jangan paksakan beli 30 unit sekaligus dengan kualitas pas-pasan. Beli lebih dulu 15 unit klien berkualitas plus satu proktor yang benar-benar memenuhi syarat, lalu tambah unit tiap semester.

**Ketiga, pertimbangkan Chromebook untuk klien.** Harganya jauh lebih murah, hemat listrik, dan resmi diizinkan untuk asesmen dengan syarat akun belajar.id. Namun sediakan minimal satu laptop atau PC Windows di ruang proktor sebagai cadangan kompatibilitas.

**Keempat, gunakan kabel, bukan WiFi, untuk klien.** Ini sekaligus menaati ketentuan moda semi daring dan menghemat biaya dibanding membeli access point mahal yang tetap saja tidak stabil saat 30 klien menyala bersama.

**Kelima, rawat perangkat dengan jadwal rutin.** Debu adalah musuh utama komputer lab di Indonesia. Bersihkan bagian dalam casing setiap tiga bulan, pasang stabilizer untuk melindungi dari lonjakan tegangan, dan buat daftar inventaris berisi nomor seri tiap unit agar tidak ada yang "hilang" saat pergantian pengurus lab.

**Keenam, latih teknisi dan proktor jauh sebelum hari H.** Aplikasi Exambrowser, VirtualBox, dan sinkronisasi data VHD bukan hal yang bisa dipelajari semalam. Jadwalkan gladi bersih minimal dua kali dengan perangkat dan jaringan yang persis sama seperti saat pelaksanaan.

## Penutup

Membangun laboratorium komputer yang benar bukan soal membeli perangkat paling mahal, melainkan soal memenuhi syarat teknis yang sudah diatur sambil menjaga kewarasan anggaran. Tiga hal paling menentukan: jumlah unit yang sesuai kapasitas sesi tes, komputer proktor yang tidak dikorbankan spesifikasinya, dan jaringan kabel yang stabil. Sisanya — merek, warna, dan model — bisa disesuaikan dengan dana yang ada.

Mulailah dengan menghitung kebutuhan sesi peserta tahun ini, cocokkan dengan spesifikasi minimal dalam juknis, susun RAB berbasis batas persentase dana BOS, lalu beli bertahap. Lab yang dibangun dengan rencana biasanya bertahan bertahun-tahun; lab yang dibeli karena terdesak jadwal biasanya menyisakan masalah yang lebih mahal di kemudian hari.
