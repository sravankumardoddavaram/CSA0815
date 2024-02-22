def find_lsd_msd(number):
    number_str = str(number)
    lsd = int(number_str[-1])
    msd = int(number_str[0])
    return lsd,msd

intput_number = 1010101
lsd,msd=find_lsd_msd(intput_number)
print("Input:",intput_number)
print("MSD:",msd)
print("LSD:",lsd)