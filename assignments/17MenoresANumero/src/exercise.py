def main():
    a=int(input(''))
    b=int(input(''))
    c=a*b
    i=0
    lista=[]
    while i<c:
        i=i+1
        v=int(input(''))
        if v<10:
            lista.append(v)
    print(lista)

if __name__=='__main__':
    main()
