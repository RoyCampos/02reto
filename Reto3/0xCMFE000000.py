print("Welcome .........")
import random as rd

base = "0B98M54321"

# olvide la seed, solo se que tenia  5 cifras
# y terminaba en 0

f = ("".join([rd.choice(base) for x in range(10)]))
print(f)
if f[0:2] == "18" and f[-2:] == "M3":
        print("flag{flag_ctf_%s}"  % f)