# Marc Vannucci
# CS 161 HW 2

# Step 1

value = 31

print(value, bin(value), hex(value))

# value = 18.5
# ERROR: 31 0b11111 0x1f
value = 18

bin = 0b1011
# 11
hex = 0xA3
# 163
print(bin, hex)


combine = value + bin + hex

print(f"The sum is {combine}")
# 192

original_size = 240
dicttionary_size = 25
compressed_text_size = 148
total = dicttionary_size + compressed_text_size

precent_of_compression = 1 - ((compressed_text_size + dicttionary_size) / original_size)
precent = precent_of_compression * 100

print("  Compressed text size:", str(compressed_text_size), "characters")
print("  Dictionary size:", str(dicttionary_size), "characters")
print("  Total:", str(total), "characters")
print("  Compression:", str(precent), "%")


# This does not convert to 2's compliment correctly, I attempted to use bin but for some reason was not letting me call it on a int type.
user_num = input("Enter a number for conversion: ")
int_convert = int(user_num)
binary = format(int_convert, "b")
print(f"Your converted number is {int_convert}\nand is {binary} in binary")
