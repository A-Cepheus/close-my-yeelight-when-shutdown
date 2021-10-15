import re
import json
import socket
import requests


def sentOff(address):
    
    message = {
        "id": 1,
        "method": "bg_set_power",
        "params": ["off", "smooth", 500]
    }
    message = json.dumps(message) + "\r\n"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((address[0], 55443))

    print('[+]  链接成功')

    print(message.encode())
    client.send(message.encode())

    


def main():
    mcastAddr = "239.255.255.250"
    udp_port = 1982

    datagram = "M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1982\r\nMAN: \"ssdp:discover\"\r\nST: wifi_bulb"

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    s.setblocking(False)
    s.sendto(datagram.encode(), (mcastAddr, udp_port))

    while True:
        try:
            data, address = s.recvfrom(2048)
        except Exception as e:
            try:
                s.sendto(datagram.encode(), (mcastAddr, udp_port))
            except Exception as e:
                pass
            pass
        else:
            print(address)
            print(data.decode())
            sentOff(address)
            break


main()
