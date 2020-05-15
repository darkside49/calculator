
while print:
#pengenalan
	print("Selamat datang di operasi arithmatika dua bilangan")
	print('')
	print('='*50)
	print('Author	: Handika Putra')
	print('Fb	: Handika Putra')
	print('Ig	: @handika811')
	print('='*50)
	print('')
	print('Rules:')
	print('Ini adalah operasi dua bilangan saja, kalau lebih dari dua bilangan maka bukan disini tempatnya.')
	print('Disini ada operasi perkalian, pembagian, pangkat2, penjumlahan, dan pengurangan')
	print('kalo ingin operasi perkalian tekan	1')
	print('kalo ingin operasi pembagian tekan	2')
	print('kalo ingin operasi penjumlahan tekan	3')
	print('kalo ingin operasi pengurangan tekan	4')
	print('='*50)
	kode = input('masukan kode:\n1 untuk perkalian\n2 untuk pembagian\n3 untuk penjumlahan\n4 untuk pengurangan\n:')

#operasi perkalian
	if kode == '1':
		print('selamat datang di operasi perkalian dua bilangan')
		kali1 = input('masukan angka pertama:')
		kali2 = input('masukan angka kedua:')
		kali3 = (int(kali1)) * (int(kali2))
		print('hasil perkalian dari', kali1 ,"dikali", kali2 ,"=", kali3)
#operasi pembagian
	elif kode == '2':
		print('selamat datang di operasi pembagian dua bilangan')
		bagi1 = input('masukan angka pertama:')
		bagi2 = input('masukan angka kedua:')
		bagi3 = (int(bagi1)) / (int(bagi2))
		print('hasil pembagian dari', bagi1 ,'dibagi',bagi2 ,'=', bagi3)
	
#operasi penjumlahan
	elif kode == '3':
		print('selamat datang di operasi penjumlahan dua bilangan')
		tambah1 = input('masukan angka pertama:')
		tambah2 = input('masukan angka kedua:')
		tambah3 = (int(tambah1)) + (int(tambah2))
		print('hasil penjumlahan dari', tambah1, 'ditambah', tambah2 ,'=', tambah3)
	
#operasi pengurangan
	elif kode == '4':
		print('selamat datang di operasi pengurangan dua bilangan')
		kurang1 = input('masukan angka pertama:')
		kurang2 = input('masukan angka kedua:')
		kurang3 = (int(kurang1)) - (int(kurang2))
		print('hasil pengurangan dari', kurang1, 'dikurangi', kurang2, '=', kurang3)
	
	else:
		print('maaf', kode,'tidak merupakan kode dalam daftar')


		
		
		
		
	

	
