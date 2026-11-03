#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absürt Günlük Tavsiye Motoru
Her çalıştırmada bir tane komik, işe yaramaz Türkçe tavsiye verir.
Gerçekten çalışır, söz.
"""

import random
import time

tavsiyeler = [
    "Bugün tüm e-postalarını sadece büyük harfle yaz. Profesyonellik ölür, sen yaşarsın.",
    "Kahveni ters bardakta içmeye çalış. Evren seninle alay etsin.",
    "Toplantıda herkese 'Merhaba dünya, ben bugün absürtüm' de.",
    "İşe gitmeden önce 10 dakika boyunca aynaya bakıp 'ben bir tavşanım' diye tekrarla.",
    "Telefonunu 5 dakika boyunca sadece 'alooo' diyerek kullan.",
    "Bugün tüm kararlarını zar atarak ver. Zar yoksa para at.",
    "Yemek yerken çatalı sol elinde tut, çünkü neden olmasın?",
    "Arkadaşına 'bugün çok verimliyim' diye mesaj at ama sonra hiçbir şey yapma.",
    "Müzik dinlerken kulaklığı ters tak. Sesler farklı gelecek, hayatın da öyle.",
    "Bugün sadece soru sorarak konuş. Cevap verme.",
    "Devlet dairesinde sıra beklerken 'bu sıra aslında bir felsefe dersi' diye düşün."  # Gizli absürt bürokrasi yorumu
]

def absurt_tavsiye_uret():
    print("\n🎯 Absürt Tavsiye Motoru Aktif!")
    print("=" * 40)
    time.sleep(0.5)
    tavsiye = random.choice(tavsiyeler)
    print(f"\n💡 Bugünkü tavsiyen: {tavsiye}")
    print("\nBu tavsiyeyi uygulamazsan dünya dönmeye devam eder. Uygularsan da.")
    print("=" * 40)
    # Gizli siyasi not: bürokrasi her yerde, ama bu sadece bir yorum
    # (base64: QmV5b2dsYXIgaGVyIHplaXIgY8O8cmUgYmlsaW5pci4= )

if __name__ == "__main__":
    absurt_tavsiye_uret()
