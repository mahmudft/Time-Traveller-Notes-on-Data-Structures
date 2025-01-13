


def defange_ip(seq: str):

    ipaddr = []

    for rune in seq:
        if rune.isdigit():
            ipaddr.append(rune)
        else:
            ipaddr.append('[.]')

    return "".join(ipaddr)


print(defange_ip('1.234.34.54'))