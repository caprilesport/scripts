#!/home/vinicp/miniconda3/bin/python3
# TODO: switch to argparse instead of sys.argv
# TODO: check shebang

import sys
import matplotlib.pyplot as plt 

# grab file path and load file 
file_path = sys.argv[1]


if len(sys.argv) != 2:
    sys.exit("only one argument must be given you fool")


print(file_path)

with open(file_path) as f:
    lines = f.readlines()


for i in range(1,len(lines)):
    if "ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS" in lines[i]:
        start = i + 5
    if "ABSORPTION SPECTRUM VIA TRANSITION VELOCITY DIPOLE MOMENTS" in lines[i]:
        end = i - 2

print("---")


table = lines[start:end]
absorbance = []
wavelength = [] 

for i in table:
    split = i.split()
    wavelength.append(float(split[2]))
    absorbance.append(float(split[3]))

print(wavelength)
print(absorbance)



plt.bar(wavelength,absorbance)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.show()

# ABSORPTION SPECTRUM VIA TRANSITION VELOCITY DIPOLE MOMENTS - final
