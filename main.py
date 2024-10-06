import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukan nama kamu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 #INI TETAP HARUS KOSONG

goa = goa_kosong.copy() #INI ADALAH TEMPAT BARU UNTUK SI CUYPY

goa[cuypy_position - 1] = "|0_0|"

print(f'''
Hello {nama_user}! Coba perhatikan goa dibawah ini
{goa_kosong}
''')

pilihan_user = int(input ("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
confirm_answer = input(f"Apakah kamu yakin jawabanya adalah {pilihan_user}? [y/n]: ")

if confirm_answer == "n":
    print("progran dihentikan!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == cuypy_position:
        print(f"{goa}, \n Selamat Kamu Menang!")
    else:
        print(f"{goa}, \n Maaf kamu kalah!")
else:
    print("Silahkan ulangi programnya!")
    exit()
