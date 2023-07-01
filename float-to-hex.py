import struct
import sys
import numpy as np
import bfloat16ext
"""
pip install bfloat16ext==1.1.9
"""
##=== fp16 to hex ===###
def fp16_to_hex(f):
    return hex(struct.unpack('<H', struct.pack('<e', f))[0])

##=== bf16 to hex ===###
def bf16_to_hex(f):
   bf16 = bfloat16ext.bfloat16(f).view(np.uint16)
   print(bf16)
   return hex(bf16)

##=== fp32 to hex ===###
def fp32_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

print("> FP32:    s|e8      |m23                    |")
print("           s|--------|-----------------------|")
print("> BF16:    s|e8      |m7     |")
print("           s|--------|-------|", )
print("> FP16:    s|   e5   |m10       |")
print("           s|   -----|----------|", )


##=== receive a number from terminal ===###
number = float(sys.argv[1])

print("> FP32:\n", fp32_to_hex(number))
print("> BF16:\n", bf16_to_hex(number))
print("> FP16:\n", fp16_to_hex(number))



