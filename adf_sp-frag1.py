#!/home/vinicp/.pyenv/shims/python
########################
# Input Generator for ADF
# Input the .xyz file optmized by AVOGADRO or CHEMCRAFT
########################

import sys

# def input script
def inp(argv, arquivoinp):
    with open(arquivoinp, "w") as f5:
        f5.write(
            "AMS_JOBNAME=frag1 $AMSBIN/ams <<eor\n\nTask SinglePoint\n\nEngine ADF\n\ttitle frag1\n\n\tRelativity\n\t\tFormalism ZORA\n\t\tLevel scalar\n\tEnd\n\n\tBASIS\n\t\tTYPE ZORA/TZ2P\n\t\tCreateOutput yes\n\tend\n\n\tSymmetry NoSym\n\t\tDependency\n\tend\n\n\tXC\n\t\tHybrid PBE0\n\t\tDispersion Grimme3 BJDAMP\n\tend\n\n\tBeckegrid\n\t\tQuality verygood\n\tend\n\nEndEngine\n\n"
        )
    with open(argv, "r") as f1:
        A = f1.readlines()
    A.pop(0)
    A.pop(0)
    B = []
    for j in A:
        B.append(j.strip())
    with open(arquivoinp, "a") as f2:
        f2.write("System\n\tatoms\n")
    with open(arquivoinp, "a") as f3:
        for i in B:
            f3.write(i + "\n")
    with open(arquivoinp, "a") as f4:
        f4.write("\tend\n\t\tCharge 4\n\tend\n\neor\n")


# def transformation of .xyz in .in
def xyztoin(argv):
    A = []
    for c in argv:
        A.append(c)
    A.pop(-1)
    A.pop(-1)
    A.pop(-1)
    A.append("r")
    A.append("u")
    A.append("n")
    return "".join(A)


cont = 1
while cont < len(sys.argv):
    infile = xyztoin(sys.argv[cont])
    inp(sys.argv[cont], infile)
    cont += 1
