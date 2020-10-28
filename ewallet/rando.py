import random
import string

test = random.choice(string.ascii_uppercase + string.digits)
size = 10
N = 15

ref_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
print(''.join(random.choice(test) for _ in range(size)))

print(ref_id)