import struct
import ctypes # ctypes in imported to create string buffer 


# Format: h is short in C type 
# Format: l is long in C type 
# Format 'hhl' stands for 'short short long' 
var1 = struct.pack('hhl',5,10,15)
print(var1)


# Format: i is int in C type 
# Format 'iii' stands for 'int int int' 
var2 = struct.pack('iii', 10, 20, 30)
print(var2)


print(struct.unpack('hhl', var1))
print("Size of String representation is {}.".format(struct.calcsize('hhl')))


# '?' -> _BOOL , 'h' -> short, 'i' -> int and 'l' -> long 
var = struct.pack('?hil', True, 2, 5, 445) 
print(len(var)) # 16
print(var) # b'\x01\x00\x02\x00\x05\x00\x00\x00\xbd\x01\x00\x00\x00\x00\x00\x00'


# q -> long long int and f -> float 
var = struct.pack('qf', 5, 2.3) 
print(var) 
tup = struct.unpack('qf', var) 
print(tup) 
print(struct.calcsize('qf'))
print(struct.calcsize('?hil')) 

print('calcsize of the format speicifiers: ')
print('b',struct.calcsize('b')) # 1
print('h',struct.calcsize('h')) # 2
print('i',struct.calcsize('i')) # 4
print('q',struct.calcsize('q')) # 8
print('l',struct.calcsize('l')) # 8
print('f',struct.calcsize('f')) # 4
print('?',struct.calcsize('?')) # 1


# Note: The ordering of format characters may have an impact on size.

var = struct.pack('bi', 56, 0x12131415) 
print('bi',struct.calcsize('bi')) # 8 
print('ib',struct.calcsize('ib')) # 5


# SIZE of the format is calculated using calcsize() 
siz = struct.calcsize('hhl') 
print('siz',siz) 
  
# Buffer 'buff' is created 
buff = ctypes.create_string_buffer(siz) 
  
# struct.pack() returns packed data 
# struct.unpack() returns unpacked data 
x = struct.pack('hhl', 2, 2, 3) 
print(x) # b' \x02\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00
print(struct.unpack('hhl', x)) 
  
# struct.pack_into() packs data into buff, doesn't return any value 
# struct.unpack_from() unpacks data from buff, returns a tuple of values 
struct.pack_into('hhl', buff, 0, 2, 2, 3) 
print(struct.unpack_from('hhl', buff, 0)) 