
# Program untuk menentukan suhu dalam derajat Celsius
print("Program Menentukan Suhu dalam Derajat Celsius")
suhu = float(input("Masukkan suhu dalam derajat Celsius: "))
print("Suhu yang Anda masukkan adalah:", suhu, "derajat Celsius")

# belajar kondisi untuk menentukan suhu
suhu_n = float(input("Masukkan suhu dalam derajat Celsius untuk penilaian: "))
if suhu_n < 15:
    print("Suhu sangat dingin")
elif 15 <= suhu_n < 25: 
    print("Suhu sejuk") 
elif 25 <= suhu_n < 30:
    print("Suhu hangat")   
elif 30 <= suhu_n < 50:
    print("Suhu panas")
else:
    print("Suhu sangat panas")
# Program untuk menentukan suhu dalam derajat
