n,m,a = map(int, raw_input().split())
num_flags_x = n / a + (0 if n % a == 0 else 1)
num_flags_y = m / a + (0 if m % a == 0 else 1)
print(num_flags_x*num_flags_y)