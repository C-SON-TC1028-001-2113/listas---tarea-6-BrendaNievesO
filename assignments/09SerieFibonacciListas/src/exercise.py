
def main():
    lista=[0,1]
    a=0
    b=1
    v=int(input(''))
    c=v-2
    if v==1:
        lista.remove(1)
        print(lista)
    if v==2:
        print(lista)
    if v>2:
        for x in range(c):
            lista.append(a+b)
            s=a+b
            a=b
            b=s
        print(lista)

if __name__=='__main__':
    main()
