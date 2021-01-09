1. Find any files owned bu user flag00
```
find / -user flag00
```
2. We barely can find anything in search ouput because of dispalying files with restricted access, so lets put their output into a "black hole"
```
find / -user flag00 2>/dev/null
```
3. Search gave us 2 files: `/usr/sbin/john`, `/rofs/usr/sbin/john`. Every file contains list of sybols: **cdiiddwpgswtgt**. But unfortunately it's not a flag. Maybe it's encrypted/
4. Go to https://www.dcode.fr/ (this website is recommended to use in intra video about snow_crash)
5. Use 1-st decoder in list for text - for Caesar cipher. We get our flag: **nottoohardhere**
6. Go to flag00 user and get flag:
```
su flag00
getflag
```
7. Flag for level01: **x24ti5gi3x0ol2eh4esiuxias**
