---
layout: workplace-korean
title: Maxfiylik siyosati
lang: uz
---
# Maxfiylik siyosati

Amal qilish sanasi: 2026-yil 24-oktabr. Faqat **Workplace Korean: Learn Korean (한국일터 / Practical Workplace Korean)** uchun. Android paketi: `com.minororbit.workplacekorean`. Ishlab chiquvchi/yordam: [davidleepub@gmail.com](mailto:davidleepub@gmail.com).

## 1. Hisobsiz o‘rganish
Ilovada koreys tili darslari, ixtiyoriy Hangul asoslari, testlar, saqlangan iboralarni takrorlash va nishonlar bor. Hisob talab qilinmaydi. Ishlab chiquvchi o‘quv ma’lumotlari serverini yuritmaydi va mahalliy tarixni tahlil yoki nosozlik hisobotlari tizimi orqali olmaydi. Reklama, Android ovoz, zaxiralash va tashqi saytlar ma’lumotlarni alohida qayta ishlashi mumkin.

## 2. Qurilmadagi yozuvlar
Dars/ibora identifikatorlari, o‘qish joyi, tugatish soni va sanasi, javoblar/jarayon, takrorlash tarixi, o‘qish/takrorlash kunlari, til, ovoz, tezlik, avtomatik ijro va yordamchi sozlamalari saqlanadi. Reklama mukofoti orqali ochilish, reklama tanaffusi va yordamchi salomlari/navbati ham saqlanadi. Eski o‘rnatishda kunlik maqsad qolishi mumkin, ammo hozirgi sozlamalarda bu imkoniyat yo‘q. Tanishuv nishoni faqat Android ulashish oynasi ochilganini bildiradi, xabar yuborilishi yoki yetib borishini emas. Bular ilovaning xususiy bazasi/sozlamalarida o‘rganish, davom ettirish va mukofot uchun saqlanadi, ishlab chiquvchi serveriga yuklanmaydi.

## 3. Ixtiyoriy mikrofon mashqi
Yozib olishni tanlaganda mikrofon ruxsati so‘raladi; rad etib boshqa imkoniyatlarni ishlatish mumkin. Yozuvlar qayta tinglash uchun xususiy papkada, ayni mashqni qayta yozish avvalgisini almashtiradi. Ishlab chiquvchi, reklama SDK yoki AI xizmatiga yuklanmaydi; nutqni tanish yoki talaffuzni avtomatik baholash yo‘q. Boshqalarni ruxsatsiz yozmang. Maxsus yozuv o‘chirish tugmasi yo‘q; ilova xotirasini tozalash yoki o‘chirish shu o‘rnatishdagi yozuvlarni yo‘qotadi.

## 4. MP3 va Android TTS
MP3 ichki koreys audiofayllarini ijro etadi, matnni ishlab chiquvchi ovoz serveriga yubormaydi. Qurilma TTS tanlanishi mumkin; MP3 yo‘q bo‘lsa va ixtiyoriy Hangul yo‘riqnomasida qurilma TTS ishlatiladi. Matn o‘rnatilgan Android TTS dvigateliga beriladi. Ovoz/tarmoq talabi dvigatel va ovozga bog‘liq; ba’zilari oflayn. Ovoz yuklash, onlayn ovozlar va diagnostika provayder xizmati/siyosatiga tegishli bo‘lishi mumkin. Mashq yozuvlari TTSga berilmaydi. Ilovada ishlab chiquvchining Google Cloud TTS, fal.ai yoki ElevenLabs API kalitlari bilan ovoz yaratilmaydi. Ovoz nomlari yoki ishlab chiqish namunalari bu bulut APIlari ilovada ishlashini anglatmaydi.

## 5. Reklama va maxfiylik tanlovlari
Unity versiyasida Unity Ads SDK 4.16.6, Google Mobile Ads SDK 25.5.0 va Google UMP bor. Banner va ixtiyoriy mukofotli reklamada ikkala provayder ishlatiladi. Maxfiylik sharti bajarilib, ikkala SDK tayyor bo‘lsa, dastlabki so‘rov taxminan Unity 80%/Google 20% tanlanadi; yuklash xatosida boshqa tayyor provayderga bir marta o‘tilishi mumkin. Bittasi tayyor bo‘lsa faqat o‘sha ishlatiladi. Bu ko‘rsatilgan reklama nisbati kafolati emas; eski versiyada faqat Google bo‘lishi mumkin.
SDK va hamkorlar reklama, o‘lchash, suiiste’moldan himoya uchun IP, taxminiy umumiy joylashuv, qurilma/reklama IDsi, o‘zaro ta’sir va diagnostikani qayta ishlashi mumkin. GPS, kontaktlar yoki foto kutubxonasi so‘ralmaydi. UMP rozilik ma’lumotini so‘raydi, reklama so‘rash mumkinligi natijasi SDKni boshlashni boshqaradi. Unity ishlab chiquvchi rozilik bayroqlari false; shaxsiylashtirilgan Unity reklamaga rozilik bildirildi deb hisoblanmaydi. UMP talab qilsa sozlamada reklama maxfiylik tanlovi chiqadi; shakllar Google sozlamasi/hududga bog‘liq. Android reklama ID sozlamalari ham bor. Banner tanaffusi barcha SDK jarayonlari to‘xtashini kafolatlamaydi.
Olingan ixtiyoriy mukofot bannerni 2 soat to‘xtatadi; boshqa mukofot qo‘shimcha dars to‘plamini ochadi. Mahalliy mukofotlar pulli xarid, naqd pul yoki boshqa hisobga o‘tkaziladigan huquq emas; mavjudligi reklama xizmati va muvaffaqiyatli yakunlashga bog‘liq.
Google SDK uzatishida TLS ishlatilishini bildiradi. Google, Unity va hamkorlari o‘z siyosatlariga muvofiq, mamlakatingiz tashqarisida ham qayta ishlashi/saqlashi mumkin; rasmiy havolalar quyida. Ilova mahalliy tarix yoki yozuvlarni reklama so‘roviga qo‘shmaydi. Unity oshkorotida SDK/foydalanuvchi IDlari, xarid tarixi va reklama ta’sirlari ham keltiriladi. Bu ilova ism, email, bank/karta ma’lumotini so‘rashi yoki ichki xarid taklif qilishini anglatmaydi. Ishlab chiquvchi hisob profili yoki xarid hodisalari Unityga yuborilmaydi. Reklama/atributsiya mahalliy o‘quv mukofotidan alohida. Unity ixtiyoriy Acquire Optimization yoqilganda ilovadan foydalanish vaqtini ham tavsiflaydi.

Yangi versiyalarda tasdiqlangan masofaviy sozlamalar reklama provayderlarini yoqishi yoki o‘chirishi mumkin. Dastlab faqat Unity yoqilgan, AdMob o‘chirilgan; 80:20 tanlov faqat ikkalasi yoqilgan va tayyor bo‘lganda amal qiladi. Ilova old planga qaytganda, ko‘pi bilan har 6 soatda bir marta GitHub Pages’dan HTTPS orqali raqamli imzolangan ochiq sozlamalar faylini oladi. Ilova bu so‘rovga o‘quv tarixi, yozuvlar yoki reklama identifikatorlarini qo‘shmaydi; xosting provayderi IP manzil kabi ulanish ma’lumotlarini oladi. Internet bo‘lmaganda oxirgi tasdiqlangan sozlamalar muddatsiz saqlanadi. Reklama diagnostikasi faqat qurilmaning Android jurnaliga yoziladi va ilova tomonidan yuklanmaydi.

## 6. Android zaxirasi va qurilma ko‘chirish
Avtomatik zaxiralash yoqilgan, baza, shared preferences va sozlamalar DataStore kiritilgan. Qurilma/hisob sozlamalariga ko‘ra OS o‘z provayderida o‘quv/sozlama ma’lumotlarini zaxiralashi mumkin. Yozuv papkasi sozlangan bulut zaxirasidan chiqarilgan, lekin qurilmadan qurilmaga ko‘chirishga kiritilgan. Amaliy holat Android, qurilma va provayderga bog‘liq. Alohida bulut sinxronlash yoki qo‘lda o‘quv zaxirasi eksporti yo‘q. Bulut nusxalarini ishlab chiquvchi emas, qurilma/hisob boshqaradi. Mahalliy tozalash eski OS zaxirasini o‘chirishni kafolatlamaydi; qayta o‘rnatish/ko‘chirishda tiklanishi mumkin.

## 7. Saqlash, o‘chirish va xavfsizlik
Ma’lumot tegishli boshqaruvda o‘chirilguncha, almashtirilguncha, xotira tozalanguncha yoki ilova o‘chirilguncha qoladi. Iborani saqlashdan chiqarish faqat karta bog‘lanishini olib tashlaydi, tugallangan mashqlar tarixini emas. Android sozlamalari → Ilovalar → Workplace Korean → Xotira → Xotirani tozalash yoki ilovani o‘chirish orqali mahalliy ma’lumot, ochilish va sozlamalar ketadi; OS tiklashi mumkin. Zaxira/ovoz ma’lumotlarini tegishli provayderda boshqaring. Ishlab chiquvchi faqat qurilmadagi ma’lumotni masofadan ko‘ra yoki o‘chira olmaydi. Android xususiy xotirasi qo‘shimcha end-to-end shifrlash yoki buzilgan qurilma himoyasi kafolati emas. Reklama ma’lumoti saqlanishi/o‘chirilishini reklama xizmatlari boshqaradi.

## 8. Havolalar, ulashish, yordam va auditoriya
Hangul manbalari, siyosatlar, ovoz/yuklash havolalari alohida xizmatlarni ochadi; ular o‘z siyosatida so‘rov/qurilma ma’lumotini olishi mumkin. Sahifalar GitHub Pagesda, GitHub IP va so‘rovlarni o‘z maxfiylik bayonotiga ko‘ra qayta ishlashi mumkin; bu o‘quv serveri emas. Ulashish Android oynasida tanlangan ilovaga tayyor tanishtiruv matnini beradi, yozuv/tarixni qo‘shmaydi. Tanlangan ilova o‘z siyosatiga ko‘ra uzatishi mumkin. Yordam emailida manzil va ixtiyoriy yuborgan ma’lumotingiz javob berish uchun olinadi. Parol yoki keraksiz shaxsiy yozuv yubormang. Ilova katta yoshdagi ish joyi o‘quvchilariga, bolalarga mo‘ljallanmagan; ichki yosh profili yig‘ilmaydi.

## 9. Aloqa va yangilash
Savol, maxfiylik so‘rovi/xatoni yuqoridagi emailga Workplace Korean deb yozib yuboring. Amaliyot o‘zgarsa sana yangilanadi; muhim o‘zgarishlar tegishli ilova yoki reliz ma’lumotida bildiriladi.
