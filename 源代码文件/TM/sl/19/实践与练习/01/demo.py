# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 任务：网络嗅探器

import socket
import os
import struct
from ctypes import *

host="192.168.1.41"

class IP(Structure):
    _fields_=[
        ("ihl",     c_ubyte,4),
        ("version", c_ubyte,4),
        ("tos",     c_ubyte),
        ("len",     c_ushort),
        ("id",      c_ushort),
        ("offset",  c_ubyte),
        ("ttl",     c_ubyte),
        ("protocol_num", c_ubyte),
        ("sum",     c_ushort),
        ("src",     c_ulong),
        ("dst",     c_ulong)
        ]

    def __new__(self,socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self,socket_buffer=None):
        self.protocol_map={1:"ICMP",6:"TCP",17:"UDP"}
        self.src_address=socket.inet_ntoa(struct.pack("<L",self.src))
        self.dst_address=socket.inet_ntoa(struct.pack("<L",self.dst))
        try:
            self.protocol=self.protocol_map[self.protocol_num]
        except:
            self.protocol=str(self.protocol_num)


if os.name=="nt":  # WIN平台
    socket_protocol=socket.IPPROTO_IP
else:
    socket_protocol=socket.IPPROTO_ICMP


sniffer=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)

sniffer.bind((host,0))

sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

# 在WIN平台上，需要设置IOCTL以启用混杂模式
if os.name=="nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

try:
    while True:
        raw_buffer=sniffer.recvfrom(65565)[0]
        ip_header=IP(raw_buffer[0:20])
        print ("Protocol:%s %s -> %s" % (ip_header.protocol,ip_header.src_address,ip_header.dst_address))
except KeyboardInterrupt:
    if os.name=="nt":
        sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

