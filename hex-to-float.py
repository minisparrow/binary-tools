import struct
import sys
import numpy as np
import bfloat16ext
"""
pip install bfloat16ext==1.1.9
"""

def hex_to_fp32(h):
    return struct.unpack('<f', struct.pack('<I', int(h, 16)))[0]

def hex_to_fp16(h):
    return struct.unpack('<e', struct.pack('<H', int(h, 16)))[0]

def hex_to_bf16(hex_string):
    # Convert hex string to int
    int_value = int(hex_string, 16)
    bfloat16_hex = struct.pack('<H', int_value)
    bfloat16_value = np.frombuffer(bfloat16_hex, dtype=bfloat16ext.bfloat16)[0]
    return bfloat16_value

# === receive a number from terminal ===###


if len(sys.argv) == 3:
    hex = str(sys.argv[2])
    if str(sys.argv[1]) == "fp32" or str(sys.argv[1]) == "FP32":
        print(hex_to_fp32(hex))
    elif str(sys.argv[1]) == "bf16" or str(sys.argv[1]) == "BF16":
        print(hex_to_bf16(hex))
    elif str(sys.argv[1]) == "fp16" or str(sys.argv[1]) == "FP16":
        print(hex_to_fp16(hex))
else:
    print("> FP32:    s|e8      |m23                    |")
    print("           s|--------|-----------------------|")
    print("> BF16:    s|e8      |m7     |")
    print("           s|--------|-------|", )
    print("> FP16:    s|   e5   |m10       |")
    print("           s|   -----|----------|", )

    hex = str(sys.argv[1])
    print("FP32:\n", hex_to_fp32(hex))
    print("BF16:\n", hex_to_bf16(hex))
    print("FP16:\n", hex_to_fp16(hex))
