from IpCalculate import *
from keyboard import read_key


def convert_from_bin_to_asci(lst_ip):
    new_lst_ip = []
    for octet in lst_ip:
        new_lst_ip.append(str(int(octet, 2)))
    return ".".join(new_lst_ip)


if __name__ == '__main__':
    while True:

        print("Формат ввода, пример: 192.168.1.1/24, где /24 маска")
        try:
            ip_add = input("Введите ip: ")
            ip_calculate = IpCalculate(ip_add)
            print(f"Маска подсети: {convert_from_bin_to_asci(ip_calculate.mask_convert_to_bits())}")
            print(f"Номер сети: {convert_from_bin_to_asci(ip_calculate.network_num_calculation())}")
            print(f"Широковещательный адрес: {convert_from_bin_to_asci(ip_calculate.broadcast_calculation())}")
        except:
            print("Неправельный формат ввода, введите как указано в примере")
        print("--Нажмите esc, чтобы выйти--")
        if read_key("esc"):
            break
