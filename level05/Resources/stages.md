1. При запуске выводится сообщение о наличии новой почты
2. По стандартному пути хранения писем /var/mail/ лежит файл level05, который содержит:
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
3. Запись */2 * * * * напоминает формат записи времени в crontab. Соответсвенно скрипт /usr/sbin/openarenaserver видимо выполняется раз в 2 минуты.
https://www.tutorialspoint.com/unix_commands/crontab.htm
5. /usr/sbin/openarenaserver содержит
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done

Из скрипта видно, что при выполнении он подбирает все файлы из /opt/openarenaserver/ и также выполняет их, после этого удаляя
6. Создадим файл /opt/openarenaserver/flag05 с содержимым:
getflag > /tmp/flag05
7. Ожидаем в пределах 2 минут и обнаруживаем в /tmp/flag05 ключ для перехода для level06: viuaaale9huek52boumoomioc
