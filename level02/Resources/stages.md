1. We are given file `level02.pcap`
2. pcap - net trafic log format for WireShark
3. (On outer Linux/MacOS host) Copy pcap file to outer host and change access rules
``` Bash
scp -P 4242 level02@<snow_crash VM IP adress>:/home/user/level02/level02.pcap .
chmod 777 ./level02.pcap
```
4. (On outer Linux/MacOS host) Run WireShark with this file
``` Bash
wireshark ./level02.pcap
```
5. We see log of TCP packages. To see what text message they transported, do *right click on any packages -> Follow -> TCP Stream*, then this output occurs
```
..%..%..&..... ..#..'..$..&..... ..#..'..$.. .....#.....'........... .38400,38400....#.SodaCan:0....'..DISPLAY.SodaCan:0......xterm.........."........!........"..".....b........b....	B.
..............................1.......!.."......"......!..........."........"..".............	..
.....................
Linux 2.6.38-8-generic-pae (::ffff:10.1.1.2) (pts/10)

..wwwbugs login: l.le.ev.ve.el.lX.X
..
Password: ft_wandr...NDRel.L0L
.
..
Login incorrect
wwwbugs login:
```
6. The most interesting part - potential password: **ft_wandr...NDRel.L0L**. But it didin't work.
7. So we check each TCP package containing chars of password and see that `.` is not a normal symbol of dot, but a `7F` octal sybol. According to ASCII table it's `7F is DELETE`.
8. Rewrite password using DELETE instead of each dot: **ft_waNDReL0L**
9. Go to flag02 user and get flag:
``` Bash
su flag02
getflag
```
10. Flag for level03: **kooda2puivaav1idi4f57q8iq**
