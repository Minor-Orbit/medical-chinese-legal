---
layout: workplace-korean
title: Kebijakan privasi
lang: id
---
# Kebijakan privasi

Berlaku: 24 Oktober 2026. Hanya untuk **Workplace Korean: Learn Korean (한국일터 / Practical Workplace Korean)**, paket Android `com.minororbit.workplacekorean`. Pengembang/dukungan: [davidleepub@gmail.com](mailto:davidleepub@gmail.com).

## 1. Belajar tanpa akun
Aplikasi menyediakan pelajaran Korea bawaan, dasar Hangul opsional, kuis, ulasan ungkapan tersimpan dan lencana. Tidak perlu akun; pengembang tidak menjalankan server data belajar atau menerima riwayat lokal melalui layanan analitik/pelaporan kerusakan. Iklan, layanan suara Android, pencadangan dan situs eksternal dapat memproses informasi secara terpisah.

## 2. Catatan di perangkat
Menyimpan ID pelajaran/ungkapan, posisi belajar, jumlah/tanggal selesai, jawaban/kemajuan latihan, catatan ulasan, hari belajar/ulasan, bahasa, suara, kecepatan, putar otomatis dan pengaturan bantuan. Juga menyimpan pembukaan akses hadiah iklan, waktu jeda iklan, serta catatan sapaan/pergiliran bantuan. Instalasi lama mungkin menyimpan target harian yang kini tidak lagi ditawarkan. Lencana pengenalan mencatat pembukaan lembar berbagi Android, bukan pengiriman atau penerima. Data berada di basis data/pengaturan pribadi aplikasi untuk belajar, melanjutkan, preferensi dan hadiah; tidak diunggah ke server belajar pengembang.

## 3. Latihan mikrofon opsional
Izin mikrofon diminta saat Anda memilih merekam; boleh menolak dan tetap memakai fitur lain. Rekaman disimpan di folder pribadi untuk didengar ulang. Merekam ulang butir yang sama mengganti audio sebelumnya. Tidak diunggah kepada pengembang, SDK iklan atau layanan AI; tidak ada pengenalan suara atau penilaian pengucapan otomatis. Jangan merekam orang lain tanpa izin. Versi ini tidak punya tombol hapus rekaman khusus; hapus penyimpanan aplikasi atau copot pemasangan untuk menghapus rekaman instalasi tersebut.

## 4. MP3 dan TTS Android
MP3 memutar rekaman Korea bawaan tanpa mengirim teks ke server suara pengembang. TTS perangkat dapat dipilih; MP3 yang tidak tersedia dan panduan Hangul opsional memakai TTS perangkat. Teks pelajaran diserahkan ke mesin TTS Android terpasang. Suara/kebutuhan jaringan bergantung pada mesin dan suara; sebagian luring, sedangkan unduhan suara, suara daring dan diagnostik bisa melibatkan layanan/kebijakan penyedia. Rekaman latihan tidak diberikan ke TTS. Aplikasi terpasang tidak memakai kunci API Google Cloud TTS, fal.ai atau ElevenLabs milik pengembang untuk menghasilkan suara. Nama suara/sampel pengembangan tidak berarti API awan tersebut berjalan dalam aplikasi.

## 5. Iklan dan pilihan privasi
Versi Unity menyertakan Unity Ads SDK 4.16.6, Google Mobile Ads SDK 25.5.0 dan Google UMP. Keduanya menyediakan banner dan iklan berhadiah opsional. Setelah gerbang privasi dan kedua SDK siap, permintaan awal dipilih kira-kira Unity 80%/Google 20%; gagal memuat dapat beralih sekali ke penyedia lain yang siap. Jika hanya satu siap, hanya itu yang dipakai. Ini pembagian permintaan, bukan jaminan penayangan; versi lama mungkin hanya Google.
SDK/mitra dapat memproses alamat IP, perkiraan lokasi umum, ID perangkat/iklan, interaksi dan diagnostik untuk iklan, pengukuran dan pencegahan penyalahgunaan. Tidak meminta GPS, kontak atau galeri foto. UMP meminta informasi persetujuan, dan hasil boleh-meminta-iklan mengendalikan inisialisasi. Penanda persetujuan privasi pengembang Unity bernilai false, bukan klaim persetujuan iklan personal. Pilihan privasi iklan muncul di pengaturan bila diwajibkan UMP; formulir bergantung konfigurasi Google/wilayah. Pengaturan ID iklan Android juga tersedia. Jeda banner tidak menjamin seluruh pemrosesan SDK berhenti.
Hadiah opsional yang berhasil diperoleh menjeda banner selama 2 jam; hadiah terpisah membuka paket pelajaran tambahan. Hadiah lokal bukan pembelian berbayar, uang tunai atau hak akun yang dapat dipindahtangankan; ketersediaannya bergantung layanan iklan dan penyelesaian berhasil.
Google menyatakan transmisi SDK memakai TLS. Google, Unity dan mitranya memproses/menyimpan sesuai kebijakan masing-masing, mungkin di luar negara Anda; lihat tautan resmi di bawah. Aplikasi tidak melampirkan riwayat belajar/rekaman ke permintaan iklan. Pengungkapan Unity mencantumkan ID SDK/pengguna, informasi riwayat pembelian dan interaksi iklan; bukan berarti aplikasi meminta nama, email, informasi bank/kartu atau menawarkan pembelian dalam aplikasi. Tidak mengirim profil akun pengembang/peristiwa pembelian kepada Unity. Iklan/atribusi berbeda dari hadiah belajar lokal. Unity juga menjelaskan waktu penggunaan aplikasi bila fitur opsional Acquire Optimization aktif.

## 6. Cadangan dan transfer perangkat
Cadangan otomatis Android aktif, mencakup basis data, shared preferences dan DataStore pengaturan. Bergantung pengaturan akun/perangkat, OS bisa mencadangkan data belajar/pengaturan lewat penyedianya. Folder rekaman dikecualikan dari cadangan awan yang dikonfigurasi, tetapi disertakan dalam transfer antarperangkat. Perilaku nyata bergantung Android, perangkat dan penyedia. Tidak ada sinkronisasi awan sendiri atau ekspor cadangan belajar manual. Kelola salinan awan melalui akun/perangkat, bukan pengembang. Menghapus data lokal tidak menjamin salinan OS terdahulu terhapus; data bisa kembali setelah instalasi ulang/transfer.

## 7. Retensi, penghapusan dan keamanan
Data bertahan sampai dihapus melalui kontrol tersedia, diganti, penyimpanan dihapus atau aplikasi dicopot. Membatalkan simpan ungkapan hanya menghapus kaitan kartu, bukan riwayat latihan selesai. Hapus melalui Pengaturan Android → Aplikasi → Workplace Korean → Penyimpanan → Hapus penyimpanan, atau copot; akses hadiah/pengaturan ikut hilang, tetapi dapat dipulihkan OS. Kelola cadangan/data suara melalui penyedia masing-masing. Pengembang tidak bisa melihat/menghapus dari jauh data yang hanya di perangkat. Penyimpanan pribadi Android bukan janji enkripsi ujung-ke-ujung tambahan atau keamanan perangkat yang dibobol. Retensi/penghapusan data iklan dikelola layanan iklan.

## 8. Tautan, berbagi, dukungan dan audiens
Sumber Hangul opsional, kebijakan, penyedia suara/unduhan membuka layanan luar yang bisa menerima data permintaan/perangkat sesuai kebijakannya. Dokumen dihosting GitHub Pages; GitHub dapat memproses IP/informasi permintaan menurut pernyataan privasinya, bukan backend belajar. Berbagi pengenalan memberikan teks siap pakai kepada aplikasi pilihan di lembar berbagi tanpa rekaman/riwayat; aplikasi itu dapat mengirim menurut kebijakannya. Email dukungan memberi kami alamat dan informasi yang Anda kirim untuk menjawab. Jangan mengirim sandi/rekaman pribadi yang tidak diperlukan. Aplikasi bagi pelajar dewasa di tempat kerja, bukan layanan khusus anak; tidak mengumpulkan profil usia dalam aplikasi.

## 9. Kontak dan pembaruan
Pertanyaan, permintaan privasi atau kesalahan: hubungi email di atas dan sebut Workplace Korean. Tanggal diperbarui saat praktik berubah; perubahan penting diberitahukan melalui informasi aplikasi/rilis yang sesuai.
