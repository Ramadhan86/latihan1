# Program untuk belajar menentukan kondisi suhu panas, sejuk, dan dingin
def cek_suhu(suhu):
    if suhu < 20:
        return "Suhu Dingin"
    elif 20 <= suhu <= 30:
        return "Suhu Sejuk"
    else:
        return "Suhu Panas"

def main():
    try:
        suhu = float(input("Masukkan suhu dalam derajat Celsius: "))
        hasil = cek_suhu(suhu)
        print(hasil)
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
if __name__ == "__main__":
    main()
