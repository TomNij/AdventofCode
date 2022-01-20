with open('../Input_files/16.txt') as file:
    input = file.readlines()


bin_input = [bin(int(line.strip(), 16))[2:] for line in input]

def parse_payload(bin_str):
    #chop string in sections of 5
    check = bin_str[0:5]
    bin_str = bin_str[5:]
    ans = ''
    nchunks = 0
    while check[0] != '0':
        ans += check[1:]
        nchunks += 1
        check = bin_str[0:5]
        bin_str = bin_str[5:]
    #check of 0 should still be processed
    ans += check[1:]
    return ans,nchunks,bin_str

tot_version = 0
for packet in bin_input:
    packet = '00111000000000000110111101000101001010010001001000000000'
    version = packet[0:3]
    tot_version += int(version,2)
    type_id = packet[3:6]
    if type_id == '100':
        val,nchunks,remainder = parse_payload(packet[6:])
    else:
        len_type = packet[6]
        if len_type == '0':
            bit_len = int(packet[7:7+15],2)
            val,nchunks,bin_str = parse_payload(packet[22:22+bit_len])
        else:
            packet_len = int(packet[7:7+11],2)