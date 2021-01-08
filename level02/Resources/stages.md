1. Командой ls обнаруживаем в исходной директории файл level02.pcap
2. .pcap - формат для записи логов в программе для аналитики сетевого потока WireShark
3. Копируем файл с VM на свой хост (выполняется с хоста):
4. Меняем права доступа на чтение файла (выполняется с хоста):
chmod 777 ./level02.pcap
5. Запускаем WireShark, подав ему данный файл
chmod 777 ./level02.pcap
6. Видим лог передачи информацинных пакетов. Чтобы цельно увидеть, какую информацию они передавали, нажимаем на любой пакет правой кнопкой мыши -> Follow -> TCP Stream, получаем такой вывод:

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

7. В выводе выше обнаруживаем потенциальный пароль
ft_wandr...NDRel.L0L
Но при попытке подать его в flag02, ничего не получается
Тогда проходим по всем пакетам, формирующим посимвольно пароль, и обнаруживаем, что "." - это не точка, а символ 7F в 8-ричной системе. По таблице ASCII видим, что это на самом деле DELETE
8. Переписываем пароль, каждый раз нажимая DELETE вместо точки:
ft_waNDReL0L
9. Пароль подошел, вызываем getflag и получаем флаг для level03: kooda2puivaav1idi4f57q8iq