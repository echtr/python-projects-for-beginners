m=[[[ 25, 36, 62],[ 28, 38, 64],[ 30, 40, 67]],[[ 1, 27, 56],[ 1, 25, 55],[ 2, 21, 51]]]

"""
_ = []
for i in m:
    for k in i:
        for l in k:
            _.append(l)
"""

print(
    [l for i in m for k in i for l in k]
    )
"""
mantigi su: en son l'yi yazdigim icin(for l in k) l'yi basa yaziyorum sonra 
for dongusunu aynen yaziyorum
"""
