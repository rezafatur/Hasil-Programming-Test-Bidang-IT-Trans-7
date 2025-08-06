# fungsi untuk menghilangkan spasi dan mengubah huruf menjadi lowercase
def is_palindrome(teks):
    teks_bersih = teks.replace(" ", "").lower()
    return teks_bersih == teks_bersih[::-1]

# fungsi untuk menghitung jumlah huruf konsonan dan vocal
def hitung_konsonan_vocal(teks):
    vocal_set = set("aiueo")
    konsonan = vocal = 0
    for huruf in teks.lower():
        if huruf.isalpha():
            if huruf in vocal_set:
                vocal += 1
            else:
                konsonan += 1
    return vocal, konsonan

# simulasi input kalimat
kalimat = input("INPUT: ")

# cek palindrome
palindrome = is_palindrome(kalimat)
vocal, konsonan = hitung_konsonan_vocal(kalimat)

# hasil
if palindrome:
    print(f'Kalimat "{kalimat}" termasuk palindrome')
else:
    print(f'Kalimat "{kalimat}" tidak termasuk palindrome')
print(f"Jumlah konsonan: {konsonan}")
print(f"Jumlah vocal: {vocal}")
