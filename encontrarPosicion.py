m = [[1,2,3,4],[9,11,5,7],[6,3,2,1]]
l = [4,3,19]
def encontrarPosicion(lista,nums):
    i = 0
    pos = []
    while i < len(nums):
        num = nums[i]
        j = 0
        enLista = False
        bk = False
        while j < len(lista):
            k = 0
            if bk == True:
                bk = False
                break
            else: 
                while k < len(lista[j]):
                    if lista[j][k] == num:
                        enLista = True
                        temp = [j,k]
                        pos.append(temp)
                        bk = True
                        break
                    if k == len(lista[j]) - 1:
                        if enLista == False:
                            pos.append(None)
                            bk = True
                            break
                    k = k + 1
                j = j + 1
        i = i + 1
    return pos
position = encontrarPosicion(m,l)
print(position)
