def ip_to_int32(ip):
    result = 0
    a = 24
    for x in range(4):
        result += int((ip.split("."))[x]) << a
        a -= 8
    return result
def ip(x):
    addr = x.split(".")
    res = int(addr[0]) <<24
    res += int(addr[1]) << 16
    res += int(addr[2]) << 8
    res += int(addr[3]) << 0
    return res
print(ip_to_int32("128.114.17.104"))
print(ip_to_int32("128.114.17.104") == 2154959208, "wrong integer for ip: 128.114.17.104")
print(ip_to_int32("0.0.0.0") == 0, "wrong integer for ip: 0.0.0.0")
print(ip_to_int32("128.32.10.1") == 2149583361, "wrong integer for ip: 128.32.10.1")