#!/home/vinicp/.pyenv/shims/python
########################
# Input Generator for ADF (ETS-NOCV analisys)
# Input the .xyz files of fragments optmized by AVOGADRO or CHEMCRAFT
########################
# Usage: the script takes three inputs, the first is the "bonded frags" and the other two must be the isolated frags within the geometry of interactions
########################

import sys

# def input script
def input(arquivoinp):
    with open(arquivoinp, "w") as f1:
        f1.write(
            "AMS_JOBNAME=eda $AMSBIN/ams <<eor\n\nTask SinglePoint\n\nEngine adf\n\ttitle frag1frag2\n\n\tETSNOCV\n\t\tRHOKmin 1e-3\n\t\tEKmin 0.5\n\t\tENOCV 0.01\n\tend\n\n\tprint ETSLOWDIN\n\n\teprint\n\t\tsfo eig ovl\n\tend\n\n\tRelativity\n\t\tFormalism ZORA\n\t\tLevel scalar\n\tend\n\n\tBasis\n\t\ttype ZORA/TZ2P\n\t\tCORE none\n\tend\n\n\tSymmetry NoSYM\n\n\tXC\n\t\tDispersion Grimme3 BJDAMP\n\t\tHybrid PBE0	\n\tend\n\n\tBeckegrid\n\t\tquality verygood\n\tend\n\n\tfragments\n\t\tfrag1 ./frag1.results/adf.rkf\n\t\tfrag2 ./frag2.results/adf.rkf\n\tend\nEndEngine\n\nSystem\n\tatoms\n"
        )
        # introduzir fragmentos pelo mesmo argumento da func xyztoin
        C = []
        w = 1
        for t in range(2, len(sys.argv)):
            C.append(sys.argv[t])
        for c in C:
            D = []
            for f in c:
                D.append(f)
            D.pop(-1)
            D.pop(-1)
            D.pop(-1)
            D.append("r")
            D.append("k")
            D.append("f")
            frag = "".join(D)
            with open(arquivoinp, "a") as f101:
                f101.write(str(w) + " " + frag + "\n")
            w += 1

        Charge = 0
        for w in range(1, len(sys.argv)):
            Charge += 1.0
        with open(arquivoinp, "a") as f2:
            f2.write("\tend\n\nEndEngine\n\nSystem\n\tatoms\n")
    for g in range(2, len(sys.argv)):
        with open(sys.argv[g], "r") as f3:
            A = f3.readlines()
        A.pop(0)
        A.pop(0)
        B = []
        for j in A:
            B.append(j.strip())
        with open(arquivoinp, "a") as f4:
            for i in B:
                f4.write(i + " adf.f=frag" + str(g - 1) + "\n")

    with open(arquivoinp, "a") as f17:
        f17.write("\tend\n\t\tCharge 3\n\tend\n\neor\n")


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


#######
infile = xyztoin(sys.argv[1])

input(infile)
