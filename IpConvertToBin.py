class IpConvertToBin:
    """Operation convert of ASCI in bits"""

    __slots__ = ("ip_address", "mask")

    def __init__(self, ip_address):
        self.ip_address = ip_address.split("/")[0]
        self.mask = int(ip_address.split("/")[1])
        if not (all(map(lambda a: 255 >= a > 0, list(map(int, self.ip_address.split(".")))))
                and 32 >= self.mask > 0):
            raise TypeError("Invalid ip address format")

    def __str__(self):
        return f"{IpConvertToBin.__name__}"

    def mask_convert_to_bits(self):
        lst_mask = [["0"]*8 for _ in range(4)]
        cnt = 0
        for octet in range(len(lst_mask)):
            for bit_in_octet in range(len(lst_mask[octet])):
                if lst_mask[octet][bit_in_octet] == "0" and cnt != int(self.mask):
                    lst_mask[octet][bit_in_octet] = "1"
                    cnt += 1
        return IpConvertToBin.convert_octet_to_str(lst_mask)

    def ip_convert_to_bits(self):
        lst_ip = []
        for octet in self.ip_address.split("."):
            lst_ip.append(str(bin(int(octet)))[2:])
        for octet in range(len(lst_ip)):
            if len(lst_ip[octet]) < 8:
                lst_ip[octet] = ("0" * (8 - len(lst_ip[octet]))) + lst_ip[octet]
        return lst_ip

    # запись октета в виде строки(бит)
    @staticmethod
    def convert_octet_to_str(lst_ip_bin):
        new_lst = []
        for octet in range(len(lst_ip_bin)):
            new_lst.append("".join(lst_ip_bin[octet]))
        return new_lst
