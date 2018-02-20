# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.

ipAddress = input("Please enter an IP address: ")
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
# character = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in the string was a . then we haven't printed the last segment
# if character != '.':
#     print("segment {} contains {} characters".format(segment, segment_length))
