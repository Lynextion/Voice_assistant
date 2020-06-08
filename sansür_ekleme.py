def delete():
    secim = 1
    lst_yasakli_kelimeler = []

    while secim != 0:
        secim = input("Please enter the word(s) that you want to remove in text enter '0' when you want stop:")
        lst_yasakli_kelimeler.append(secim)


    text = input("Please enter the text:")
    str_sansurlu_yazi = ""
    lst_sansurlenmis_yazi = []
    lst_parcali_yazi = text.split()

    for parca in lst_parcali_yazi:
        if parca not in lst_yasakli_kelimeler:
            lst_sansurlenmis_yazi.append(parca)
        else:
            lst_sansurlenmis_yazi.append("#?@!?")

    str_sansurlu_yazi = " ".join(lst_sansurlenmis_yazi)
    print("Sansur oncesi :")
    print(text)
    print("Sansur sonrasi :")
    print(str_sansurlu_yazi)
