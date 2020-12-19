try:
	import PyPDF2
	import time
	import itertools

	characters = input(str("[*] Characters To Use: "))
	min_length = int(input("[*] Min lenght of combinations: "))
	max_length = int(input("[*] Max lenght of combinations: "))
	filename = input(str("[*] File name/path To Crack: "))
	f = open(filename, mode='rb')
	reader = PyPDF2.PdfFileReader(f)
	if min_length >= max_length:
		print("[x] Please `min_length` must smaller than `max_length`")
		exit(1)

	start_time = time.time()

	for n in range(min_length, max_length + 1):
		for xs in itertools.product(characters, repeat=n):
			password = ''.join(xs)
			print(f"[~] INFO: Trying {password}")

			try:
				if reader.isEncrypted:
				  reader.decrypt(password)
				  print(f"Number of page: {reader.getNumPages()}")
				  print("\n[✓] Password Found!")
				  print(f"[✓] Password is {password}")
				  print(f"[✓] Total Time Taken {int(time.time() - start_time)} Seconds")
				  exit(0)
			except PyPDF2.utils.PdfReadError as e:
				continue

	print("[x] All Combinations in the given criteria were\ntried, but password was not found")
	exit(0)
except KeyboardInterrupt:
	print("\n[x] Ctrl + C Detected")
	exit(0)
except ImportError:
	print("\n[x] Required Module(s) Was Not Found")
	exit(1)
except Exception as e:
	print(f"\n{e}")
	exit(1)
