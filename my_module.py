# Pendefinisian objek
PI = 22/7

# Pendefinisian function
def luasLingkaran(radius) :
    return PI * radius ** 2

def kelilingLingkaran(radius) :
    return 2 * PI * radius

def kabisat(tahun) :
    return (tahun % 100 == 0 and tahun % 400 == 0 ) or (tahun % 100 != 0 and tahun % 4 == 0)

