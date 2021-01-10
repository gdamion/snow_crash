1. We are given `level06` binary executable and PHP `level06.php` file
``` PHP
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
```
2. Code takes filename as input, loads containing of this file, changing it and outputs to console
3. After short search, `preg_replace()` [revealed](https://medium.com/@isharaabeythissa/command-injection-preg-replace-php-function-exploit-fdf987f767df) to be vulnerable when used with `/e` modifier: before changing input string, string is executed as PHP-code
4. Create `/tmp/php_exploit`. Containing of this file will be string that after PHP modification `\[x (.*)\]` will result `getflag` shell command. Needed string is ``[x (`getflag`)]`` (backticks are needed to launch it as shell command)
5. Launching `./level06 /tmp/php_exploit` results to flag for level07: **wiok45aaoguiboiki2tuin6ub**
