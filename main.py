import personnummer

persnr = input("\nMata personnummer: ")

if (len(persnr) == 10):
    pnr = personnummer.Personnummer(persnr)
    slutsiffra = pnr.getKontrollSiffra()
    print("\nBeräknad slutsiffra: " + str(slutsiffra))

    inputkontrollsiffra = persnr[+9 : ]

    if (inputkontrollsiffra == str(slutsiffra)):
        print("Kontrollsifffran stämmer \n")

    else: 
        print("Ogiltigt personnummer\n")

else:
    print("\n Fel Format")
