print("="*40)
judulAnime = [
  'Naruto',
  'One piece',
  'Kimetsu no yaiba',
  'Jujutsu kaisen',
  'Black clover'
]

pemeranUtama = [
  'Uzumaki naruto',
  'Monkey D. luffy',
  'Kamado tanjiro',
  'Yuji itadori',
  'Asta'
]

# enumerate
for i, Anime in enumerate(judulAnime):
  print(i,Anime)

# zip (menggabungkan list)
for Anime, pemeran in zip(judulAnime, pemeranUtama):
  print(Anime , "Pemeran utama\t:",pemeran)

print("="*40)
#set 
favorite_anime ={
  'naruto',
  'one piece',
  'black clover',
  'jujutsu kaisen',
  'attack on titan'
}
for f in sorted(favorite_anime):
  print(f)

# dictionary
print('='*100)

favorite_character ={
  'Kitagawa Marlin': 'My Dress-Up Darling',
  'Nezuko Kamado'  : 'Demon Slayer: Kimetsu no Yaiba',
  'Raphtalia'      : 'The Rising of The Shield Hero',
  'Iroha Igarashi' : '3D Kanojo: Real Girl'
}

for i, v in favorite_character.items():
    print(i, 'Girl Favorite :', v)

for i in reversed(range(1, 10, 1)):
    print(i)
