def converter(angka, pembilang):
    
    result = []
    hasilAngka = ""
    
    loop = True    
    while loop:
        if angka >= pembilang:
            result.append(angka)
            sisa = angka % pembilang
            angka = angka // pembilang
            if sisa > 9:
                huruf = library(sisa)
                hasilAngka += huruf
                sisa = "{0} = {1}".format(sisa, huruf)
            else:
                hasilAngka += str(sisa)
            divid = "{0}------  {1}".format(pembilang, sisa)
            result.append(divid)
        else:
            if angka > 9:
                angka = library(angka)
            hasilAngka += str(angka)
            result.append(angka)
            loop = False
            break
        result.append("")
    
    hasilAngka = "".join(reversed(hasilAngka))

    return (result, hasilAngka)

def library(angka):
    if angka == 10:
        return "A"
    elif angka == 11:
        return "B"
    elif angka == 12:
        return "C"
    elif angka == 13:
        return "D"
    elif angka == 14:
        return "E"
    elif angka == 15:
        return "F"
    elif angka == 16:
        return "G"

angka = int(input("Masukkan bilangan untuk dikonversi : "))

biner, hasilBiner = converter(angka, 2)
octal, hasilOctal = converter(angka, 8)
hexa, hasilHexa = converter(angka, 16)

print("")
print("==============================================================")
print("Binner : ", hasilBiner)
print("Octal  : ", hasilOctal)
print("Hexa   : ", hasilHexa)