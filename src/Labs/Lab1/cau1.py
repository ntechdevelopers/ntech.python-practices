import filehelpers as File

try:
    data = File.ReadFile("cau1.inp")
    print(f"Data {data[0]}")
    File.WriteFile("cau1.out", data[0])

except Exception as ex:
    print(f"Error: {ex}")

