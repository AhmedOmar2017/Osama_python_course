#----------------- Numbers ------------------


# integer

print(type(1))
print(type(-1))
print(type(100))
print(type(-10))

# float


print(type(1.5000))
print(type(100.99))
print(type(-10.99))
print(type(-10.54))


#Complex number

print(type(5+6j))


complex_number = 5+6j
print(f"Real part is: {complex_number.real}, Imaginary part is: {complex_number.imag}")




# [1] You can convert from int to or complex
# [2] You can convert from float to or complex
# [3] complex can't convert to any type


print(100)              # integer
print(float(100))       # float
print(complex(100))     # complex


print(12.0)             # float
print(int(12.0))        # int
print(complex(12.0))    # complex

