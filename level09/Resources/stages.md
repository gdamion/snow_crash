1. We are given `level09` binary executable and `token`. Reading token results to this: **f4kmm6p|=�p�n��DB�Du{��**
2. It didn't work as password, so lets try to pass `token` file as parameter
```
$ ./level09 token
tpmhr
```
3. It prints some gibberish, so lets check with `ltace`
```
$ ltrace ./level09 token
__libc_start_main(0x80487ce, 2, 0xbffff6e4, 0x8048aa0, 0x8048b10 <unfinished ...>
ptrace(0, 0, 1, 0, 0xb7e2fe38)                           = -1
puts("You should not reverse this"You should not reverse this
)                      = 28
+++ exited (status 1) +++
```
4. Ok... Not much interesting. You should not reverse what? Passed string, we didn't succed passig token, so let's pass something like this
```
$ ./level09 0000000000
0123456789
```
5. Binary adds to each character its index and prints resulting ASCII character. Let's write our own decoder that will substract index from each character instead of adding.
6. (On outer Linux/MacOS host) Example of decoder in Python2 (it could be smaller, but I decided to process the input file and errors)
``` Python
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
```
! WERY IMPORTANT - GET RID OF \n AT THE END OF INPUT STRING !

7. (On outer Linux/MacOS host) Copy script to VM
``` Bash
scp -P 4242 ./reverse.py level09@<snow_crash VM IP adress>:/tmp/
```
8. Run script with token file passed
``` Bash
python2 /tmp/reverse.py ./token
```
9. Executing of script results to flag09 user password: **f3iji1ju5yuevaus41q1afiuq**
10. Go to flag09 user and get flag:
``` Bash
su flag09
getflag
```
11. Flag for level10: **s5cAJpM8ev6XHw998pRWG728z**
