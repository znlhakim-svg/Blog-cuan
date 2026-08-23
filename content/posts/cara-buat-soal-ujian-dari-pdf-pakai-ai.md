---
title: "Cara Membuat Soal Ujian Otomatis dari PDF Pakai AI (Gratis)"
date: 2026-08-23T21:45:00+07:00
draft: false
description: "Langkah demi langkah mengubah PDF materi ajar menjadi soal ujian pilihan ganda dan esai menggunakan AI gratis — tanpa install, tanpa bayar."
tags: ["ai", "soal", "ujian", "pdf", "guru"]
categories: ["teknologi pendidikan"]
---

Membuat soal ujian dari materi PDF biasanya butuh berjam-jam. Dengan AI, proses ini bisa dipersingkat jadi menitan — dan gratis.

## Apa yang Dibutuhkan

1. File PDF materi ajar (buku, modul, diktat)
2. Akses internet
3. AI gratis: ChatGPT (chat.openai.com), Gemini (gemini.google.com), atau DeepSeek (chat.deepseek.com)

## Langkah 1: Siapkan Materi

Pastikan PDF sudah berupa teks (bukan scan/gambar). Kalau masih scan, gunakan OCR gratis seperti:
- **PDF24 Tools** (pdf24.org) — online, gratis
- **Tesseract** (command line, gratis)

## Langkah 2: Copy Teks dari PDF

Buka PDF, copy teks bab yang ingin dibuatkan soalnya. Ambil per bab agar hasilnya lebih fokus — jangan sekaligus seluruh buku.

## Langkah 3: Prompt ke AI

Copy-paste teks materi ke AI, lalu gunakan prompt berikut:

```
Buatkan 20 soal pilihan ganda (4 opsi) berdasarkan materi berikut.
Tingkat kesulitan: HOTS (analisis, aplikasi, evaluasi — bukan hafalan).
Sertakan kunci jawaban dan penjelasan singkat untuk setiap soal.

Materi:
[paste teks di sini]
```

## Langkah 4: Hasil dan Revisi

AI akan menghasilkan soal dengan kunci jawaban. **Wajib cek manual** karena:
- AI kadang salah menjawab soalnya sendiri
- Beberapa opsi jawaban bisa ambigu
- Konteks materi mungkin perlu disesuaikan dengan kurikulum

## Langkah 5: Format ke Word/Google Docs

Copy hasilnya ke Word atau Google Docs, format rapi, tambahkan header sekolah. Selesai.

## Variasi Prompt yang Berguna

**Soal esai:**
```
Buatkan 5 soal esai uraian berdasarkan materi berikut.
Sertakan rubrik penilaian (skor maksimal 100 per soal).
```

**Soal benar-salah:**
```
Buatkan 15 soal benar-salah berdasarkan materi berikut.
Sertakan kunci jawaban dan penjelasan singkat.
```

**Soal menjodohkan:**
```
Buatkan 10 pasangan soal menjodohkan berdasarkan materi berikut.
Format: kolom A (istilah), kolom B (definisi).
```

## Tips agar Soal Berkualitas

1. **Bagi per bab** — jangan masukkan seluruh buku sekaligus
2. **Pilih tingkat kesulitan** — tambahkan "HOTS" atau "C1-C6" di prompt
3. **Minta variasi** — "soal yang berbeda dari yang sudah ada di pasaran"
4. **Selalu review** — AI bisa salah, guru tetap penjaga kualitas
5. **Simpan di bank soal** — kumpulkan untuk pakai ulang

---

*AI adalah alat bantu, bukan pengganti profesionalisme guru. Selalu cek dan revisi hasil sebelum dipakai.*