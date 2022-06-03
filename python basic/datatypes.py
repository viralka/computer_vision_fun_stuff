import time
print("------------Data type in Python------------")
print()


print("     Text type in Python   ")
print('string type: Hi -> type(\'hi\') = ', end='')
print(type('hi'))
print()
print("     Numeric type in Python ")
print('integer type: 26 -> type(\'26\') = ',end='')
print(type(20))
print()
print('float type: 26.00 -> type(\'26.00\') = ', end='')
print(type(20.00))
com = complex(3,4)
print(f'complex type: {com} -> type(\'{com}\') = ', end='')
print(type(com))
print()


print("     Sequence type in Python ")
a = ["hi", "hi", "hi", "hi", "hi", "hi"]
print(f'list type: {a} -> type(\'{a}\') = ', end='')
print(type(a))

a= (1,2,3,4,5)
print(f'Tupel type: {a} -> type(\'{a}\') = ', end='')
print(type(a))
print('difference: between tupel and list')
print('Tuple is immutable, list is mutable') 

print()
start_time = time.time()
b_list = list(range(10000000))
end_time = time.time()
print("Instantiation time for LIST:", end_time - start_time)

start_time = time.time()
b_tuple = tuple(range(10000000))
end_time = time.time()
print("Instantiation time for TUPLE:", end_time - start_time)

start_time = time.time()
for item in b_list:
  aa = b_list[20000]
end_time = time.time()

print("Lookup time for LIST: ", end_time - start_time)
start_time = time.time()
for item in b_tuple:
  aa = b_tuple[20000]
end_time = time.time()

print("Lookup time for TUPLE: ", end_time - start_time)

P = {'A': 'A', 'B': 'B', 'C': 'C'}
print('     Mapping type',)
print(f'dictionary : {P} -> type', end='')
print(type(P))
print()

print('     Set type', )



print("   Binary data type ") 
e = bytes(4)
print(f'Byte data type: {e} -> type', end='')
print(type(e))
print("bytes is immutable")
data = bytes(b'\xff\xff\xff\xff\x0f\xff\xff')
print(data)
print()

mutable_bytes = bytearray(b'\xff\xff\xff\xff')
print(f'Bytearray data type: {mutable_bytes} -> type', end='')
print(type(mutable_bytes))








print()
print('END')