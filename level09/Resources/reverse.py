
#!/usr/bin/env python
import sys

def get_path(args):
	if len(args) == 1:
		print("You should pass the token file path")
		return ""
	elif len(args) > 2:
		print("You should pass ONLY the token file path as script argument")
		return ""
	path = args[1]
	return(path)

def reverse(token):
	token_rev = ""
	decrypt = 0
	for c in token:
		decrypted = ord(c) - decrypt
		if decrypted < 0:
			decrypted += 256
		elif decrypted >= 256:
			decrypted -= 256
		token_rev += chr(decrypted)
		decrypt += 1
	return token_rev

def main():
	path = get_path(sys.argv)
	if not path:
		return
	token = ""
	try:
		token_file = open(path, 'r')
		token = token_file.read()
		token_file.close()
	except:
		print("Couln't open " + path + " file")
		return
	print("Input token: " + token)
	token_rev = reverse(token.rstrip())
	print("Reversed token: " + token_rev)

if __name__ == "__main__":
	main()
