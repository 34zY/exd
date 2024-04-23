# =========================================
# Title      : EXD
# Descr   : Portable tool to exfiltrate data offline
# OS        : Windows/Linux
# Author : 34zY
# Date     : 04/23/24
# =========================================

import argparse, sys

def main(args):

	# More arguments needed in case argparse script doesn't need same arguments 
	if not (args.filename or args.dump or args.dump and args.fileoutput):
		parser.error('More arguments needed.')

	ORIGINAL_FILE = args.filename
	DUMP_FILE = args.dump
	FINAL_FILE = args.fileoutput

	if ORIGINAL_FILE:

		with open(ORIGINAL_FILE, 'rb') as f:
			content = f.read()
		f.close()
		#print(type(content))
		#print(content.hex())
		hex_content = content.hex()
		print(hex_content) # display hexdump

	if DUMP_FILE:
		#print('[+] Reverse the procedure ... ')
		# Retrieve -d
		with open(DUMP_FILE, 'r') as tmp_file:
			tmp_hex = tmp_file.read()
		tmp_file.close()
		# string to hex
		retrieved_bytes = bytes.fromhex(tmp_hex) 
		# Redirect stdout
		#print(type(retrieved_bytes))

		if 	FINAL_FILE:
			with open(FINAL_FILE, 'wb') as final_file:
				final_file.write(retrieved_bytes)
			final_file.close()
		else:
			#print(type(retrieved_bytes))
			# print binary file directly to stdout
			sys.stdout.buffer.write(retrieved_bytes)
			exit(0)

		print('[+] File successfully retrieved as %s ' % FINAL_FILE)

if __name__ == '__main__':
	msg = """FILE TO DUMP HEX : exd.exe -f Document.rtf | FROM DUMP HEX TO FILE : exd -d Document.hex > Document.rtf"""
	
	# Initialize parser
	parser = argparse.ArgumentParser(description = msg)
	parser.add_argument("-f", "--filename", help = "Input file name to dump hex", required=False)
	parser.add_argument("-d", "--dump", help = "Input dump file to get the original data", required=False)
	parser.add_argument("-o", "--fileoutput", help = "Output original filename", required=False)
	args = parser.parse_args()

	main(args)