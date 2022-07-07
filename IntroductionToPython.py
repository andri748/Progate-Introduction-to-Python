# 1.LIST
fruits = ['apel', 'pisang', 'jeruk']

# Tambahkan 'anggur' ke 'fruits'
fruits.append('anggur')

# Cetak 'fruits'
print(fruits)

# 2.DICTIONARY 
# # Tetapkan dictionary ke variable fruits
fruits = {'apel':'apple','jeruk':'orange'}

# Cetak nilai dengan kunci 'jeruk'
print (fruits['jeruk'])

# 3.FOR LOOP
fruits = ['apel', 'pisang', 'jeruk']

# Dapatkan element fruits menggunakan loop for, dan cetak 'Saya suka ___'
for fruits in fruits:
  print('Saya suka ' + fruits)

# loop while
x = 10

# Buat loop while yang diulang selama x lebih besar dari 0
while x > 0:
    # Cetak variable x
    print(x)
    # Kurangi 1 dari variable x
    x -= 1

# 4.CONDITION
money = 20
items = {'apel': 2, 'pisang': 4, 'jeruk': 6}
for item_name in items:
    print('--------------------------------------------------')
    print('Anda memiliki ' + str(money) + ' dolar di dompet Anda')
    print('Harga setiap ' + item_name + ' ' + str(items[item_name]) + ' dolar')

    input_count = input('Mau berapa ' + item_name + '?:')
    print('Anda akan membeli ' + input_count + ' ' + item_name)

    count = int(input_count)
    total_price = items[item_name] * count
    print('Harga total adalah ' + str(total_price) + ' dolar')

    if money >= total_price:
        print('Anda telah membeli ' + input_count + ' ' + item_name)
        money -= total_price

        if money == 0:
            print('Dompet Anda kosong')
            break
    else:
        print('Uang Anda tidak mencukupi')
        print('Anda tidak dapat membeli ' + item_name + ' sebanyak itu')
print('Uang Anda tinggal ' + str(money) + ' dolar')

# 5. PERMAINAN GUNTTING, KERTAS DAN BATU
# Mendapatkan Masukkan
# Tambahkan nilai default untuk name
def print_hand(hand, name='Tamu'):
    print(name + ' memilih: ' + hand)

# Tambahkan argument ke print_hand
print_hand('Batu')

""""""
# Memilih tangan
def print_hand(hand, name='Tamu'):
    # Tetapkan list hands ke variable hands
    hands = ['Batu', 'Kertas', 'Gunting']

    # Memperbarui dengan menggunakan element dari variable hands
    print(name + ' memilih: ' + hands[hand])


print('Memulai Permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')
# Cetak 'Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)'
print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')

# Dapatkan input, ubah, dan tetapkan ke variable player_hand
player_hand = int(input('Masukkan nomor (0-2):'))

# Ubah argument pertama ke player_hand
print_hand(player_hand, player_name)

""""""
# Nilai return
# Definisikan function validate
def validate(hand):
    # Tambahkan control flow berdasarkan nilai hand
    if hand < 0 or hand > 2:
      return False
    else:
      return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('masukkan nomor (0-2): '))

# Tambahkan control flow berdasarkan nilai return dari function validate
if validate(player_hand):
  print_hand(player_hand, player_name)
else:
  print('Mohon masukkan nomor yang benar')
print_hand(player_hand, player_name)

""""""
# Return
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    # Hapus else dan perbaiki indentasi
    return True

def print_hand(hand, name='Tamu'):
    hands = ['Batu', 'Kertas', 'Gunting']
    print(name + ' memilih: ' + hands[hand])

print('Memulai permainan Batu Kertas Gunting!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if validate(player_hand):
    print_hand(player_hand, player_name)
else:
    print('Mohon masukkan nomor yang benar')

# 6.INIT METHOD
class MenuItem:
    # Definisikan method __init__
    def __init__(self):
      print('Instance dari class MenuItem telah di ciptakan!')

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'Roti Lapis'
menu_item1.price = 5

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('Total harga adalah $' + str(result))