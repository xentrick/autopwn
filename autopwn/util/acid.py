import logging
import socket

import paramiko

from autopwn import const
from autopwn import exceptions

log = logging.getLogger("autopwn")

def check_services(host):
    """
    Checks if target host is properly configured for SSH
    :param host: target IP address
    :return: True or raise an exception
    """

    ssh = paramiko.SSHClient()

    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=const.ssh.user, password=const.ssh.password)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('service --status-all')
        print(ssh_stdout.readlines())
        print(ssh_stdout.readlines())
    except Exception as e:
        raise exceptions.AcidSSHConfigurationException(f"Acid SSH test failed for {host}: {e}")

    finally:
        try:
            ssh.close()
        except:
            pass


def check_port(host, ports):
    """
    Checks TCP and UDP port, if both are closed raises and exception
    :param port: port list
    :return: None or exception if ports are closed
    """

    log.info("Port Acid test")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for p in ports:
        try:
            log.info(f"Checking TCP port {p} is up")
            s.connect((host, p))
        except Exception as e:
            raise exceptions.AcidTestException(f"Acid port test for {host}: unable to connect to port {p}: {e}" )

        finally:
            try:
                s.close()
            except:
                pass

    log.info("Port acid test succeeded")

def ssh_test(host):
    """
    Run acid test to determine if services are up before checking exploitability
    :param host: target IP address
    :return: True for passed test, False for failure
    """
    log.info("SSH Acid test")
    log.info("Checking services via SSH")
    check_services(host)
    log.info("SSH service check succeeded")
