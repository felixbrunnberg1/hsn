import ping 
import send_mail
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

hosts = [(h.strip(), True) for h in config["OPTIONS"]["hosts"].split(",")] #Create tuples with host IP's and a bool which represents up status.
delay = config["OPTIONS"]["delay"]

while True:
    i = 0
    for host in hosts:
        result = ping.ping_host(host[0])
        if result != host[1]:
            if host[1]:
                send_mail.send_mail(host[0], "DOWN")
                hosts[i] = (host[0], False)
                print(host[0], "is down")
                print(hosts)
            else:
                send_mail.send_mail(host[0], "UP")
                hosts[i] = (host[0], True)
                print(host[0], "is up")
                print(hosts)
        i +=1
    time.sleep(10)
    