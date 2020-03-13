# autopwn

This was used to run a reverse CTF in the Defcon 27 Blue Team Village. 

It attacked known vulnerable services in metasploitable VMs and reported if the target was vulnerable or patched. It also reached out to CTFd to give the teams points if services were secure.

Cool idea. Maybe someone will have a use for this

## Nmap Ubuntu

PORT     STATE  SERVICE     REASON       VERSION
21/tcp   open   ftp         syn-ack      ProFTPD 1.3.5
22/tcp   open   ssh         syn-ack      OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open   http        syn-ack      Apache httpd 2.4.7 ((Ubuntu))
445/tcp  open   netbios-ssn syn-ack      Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
631/tcp  open   ipp         syn-ack      CUPS 1.7
3000/tcp closed ppp         conn-refused
3306/tcp open   mysql       syn-ack      MySQL (unauthorized)
3500/tcp open   http        syn-ack      WEBrick httpd 1.3.1 (Ruby 2.3.8 (2018-10-18))
6697/tcp open   irc         syn-ack      UnrealIRCd
8181/tcp open   http        syn-ack      WEBrick httpd 1.3.1 (Ruby 2.3.8 (2018-10-18))

# Exploits

Unreal - 6697 - 2010-2075 - Figure out listener?
ProFTPd - 80/21 - 2015-3306 - Working Exploit
Drupal - 80 "/drupal" working exploit
payrollapp - 80 - wrote exploit working.
webrick -3500 - dir trav - 1.1.1.1:3500/readme?os=../../../../ working
phpmyadmin - exploited with sql database default creds
ruby - 8181 vuln cookie - ahrd because i have to marshall a ruby serialized payload
mysql - m
samba - Working
Chat - Working


# Solutions

Payroll - add `mysql_real_escape_string` to user/pass post input
Chat - add `escapeshellcmd` around `$text` data in `stripslashes` (post.php)


## Ports

* HTTP(S)
* FTP
* IMAP
* SMB / NetBios
* SSH
* SNMP
* MySQL

## Services

## Credentials
* U: vagrant P: vagrant
* U: leah_organa P: help_me_obiw@n
* U: luke_skywalker P: use_the_f0rce
* U: han_solo P: sh00t-first
* U: artoo_detoo P: beep_b00p
* U: c_three_pio P: pr0t0c0l
* U: ben_kenobi P: thats_no_moon
* U: darth_vader P: d@rk_sid3
* U: anakin_skywalker P: yipp33!!
* U: jarjar_binks P: mesah_p@ssw0rd
* U: lando_calrissian P: b@ckstab
* U: boba_fett P: mandalorian1
* U: jabba_hutt P: not-a-slug12
* U: greedo P: hanShotFirst!
* U: chewbacca P: rwaaaaawr5
* U: kylo_ren P: daddy_issues1
