import math

def encrypt(s):
    s = s.replace(" ", "")
    L = len(s)
    row = math.floor(math.sqrt(L))
    col = row

    if col * row < L:
        col += 1
    
    m = []
    for i in range(row):
        cur_row = []
        for j in range(col):
            if i * col + j < L:
                cur_row.append(s[i * col + j])
            else:
                cur_row.append("")
        m.append(cur_row)
    
    res_text = ""
    for j in range(col):
        for i in range(row):
            res_text += m[i][j]
        res_text += " "
    res_text = res_text[:-1] # remove the last additional " "
    return res_text

s = "if manwas meant to stay on the ground god would have given us roots"
res = encrypt(s)
print(res)