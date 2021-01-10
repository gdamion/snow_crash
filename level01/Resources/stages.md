1.  Check file with info about users
``` Bash
cat /etc/passwds
```
2. Every user here have it's password stored in `/etc/shadow` (`x` character means it), but user flag01 stores its password here
```
...
flag00:x:3000:3000::/home/flag/flag00:/bin/bash
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
flag02:x:3002:3002::/home/flag/flag02:/bin/bash
...
```
3. **42hDRfypTqqnw** not applies as password for flag01. Maybe it's encrypted.
4. (On outer Linux/MacOS host) Let's copy string with ecrypted password from VM's `/etc/passwds` to file `pwd_tmp`
5. (On outer Linux/MacOS host) Install John program and use it
``` Bash
john ./pwd_tmp --show
```
6. John cracked this password: **abcdefg**
7. Go to flag01 user and get flag:
``` Bash
su flag01
getflag
```
7. Flag for level02: **f2av5il02puano7naaf6adaaf**
