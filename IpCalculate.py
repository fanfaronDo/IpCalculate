from IpConvertToBin import *


class IpCalculate(IpConvertToBin):
    """Calculate"""

    __slots__ = ()

    def __init__(self, ip_address):
        super().__init__(ip_address)

    def __str__(self):
        return f"{IpCalculate.__name__}"

    def network_num_calculation(self):
        lst_ip = self.ip_convert_to_bits()
        lst_mask = self.mask_convert_to_bits()
        network_num = []
        for octet in range(len(lst_ip)):
            new_lst = []
            for bit in range(len(lst_ip[octet])):
                # конъюнкция ip/mask

                new_lst.append(str(int(lst_ip[octet][bit]) & int(lst_mask[octet][bit])))
            network_num.append(new_lst)
        result_network_num = IpCalculate.convert_octet_to_str(network_num)
        return result_network_num

    def inversion_mask_calculation(self):
        lst_mask = self.mask_convert_to_bits()
        inversion_lst_mask = []
        for octet in range(len(lst_mask)):
            octet_lst = []
            for bit in range(len(lst_mask[octet])):
                # исключающая или 1 ^ 1 = 0, 0 ^ 1 = 1, чтобы получить инверсию
                octet_lst.append(str((int(lst_mask[octet][bit])) ^ 1))
            inversion_lst_mask.append(octet_lst)
        result_inversion_mask = IpCalculate.convert_octet_to_str(inversion_lst_mask)
        return result_inversion_mask

    def broadcast_calculation(self):
        lst_ip = self.ip_convert_to_bits()
        lst_inversion_mask = self.inversion_mask_calculation()
        broadcast_lst = []
        for octet in range(len(lst_inversion_mask)):
            octet_lst = []
            for bit in range(len(lst_inversion_mask[octet])):
                # дизъинкция
                octet_lst.append(str(int(lst_ip[octet][bit]) | int(lst_inversion_mask[octet][bit])))
            broadcast_lst.append(octet_lst)
        result_broadcast = IpCalculate.convert_octet_to_str(broadcast_lst)
        return result_broadcast

