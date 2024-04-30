import os, logging, sys

logging.basicConfig(level=logging.INFO)
''
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def downnumbers(i):
    number=0
    number=input(f"Podaj skadnik {i}:")
    number=float(number)
    return number

def downlist():
    list=[]
    number=0
    i=1
    while True:
        number=input(f"Podaj skadnik {i}:")
        if number!='x':
            list+=[float(number)]
            i+=1
        else: break
    return list

def addlist(list):
    return sum(list)

def multilist(list):
    x=1
    for number in list:
        x=x*number
    return x



if __name__ == "__main__":
    os.system('clear')

    action=input("Podaj działanie, posługując się odpowiednią liczbą:\n1-Dodawanie\n11-Dodawanie kilku liczb\n2-Odejmowanie\n3-Mnożenie\n31-Mnożenie kilku liczb\n4-Dzielenie\n:")

    if action=='1':
        a=downnumbers(1)
        b=downnumbers(2)
        logging.info(f"Dodaje {a} i {b}")
        print(f"Wynik to {add(a,b)}")
    elif action=='11':
        print("Podaj liczby (wpisz x aby zakonczyc)")
        list=downlist()
        result=addlist(list)
        listsing=[str(i) for i in list]
        sing=' ,'.join(listsing)
        logging.info(f"Dodaje {sing}")
        print(f"Wynik to {result}")
    elif action=='2':
        a=downnumbers(1)
        b=downnumbers(2)
        logging.info(f"Odejmuje {a} i {b}")
        print(f"Wynik to {sub(a,b)}")
    elif action=='3':
        a=downnumbers(1)
        b=downnumbers(2)
        logging.info(f"Mnoze {a} i {b}")
        print(f"Wynik to {multi(a,b)}")
    elif action=='31':
        print("Podaj liczby (wpisz x aby zakonczyc)")
        list=downlist()
        result=multilist(list)
        listsing=[str(i) for i in list]
        sing=' ,'.join(listsing)
        logging.info(f"Mnoze {sing}")
        print(f"Wynik to {result}")
    elif action=='4':
        a=downnumbers(1)
        b=downnumbers(2)
        if b==0:
            logging.error("Dzielenie przez 0 jest niemozliwe")
            sys.exit(0)
        logging.info(f"Dziele {a} i {b}")
        print(f"Wynik to {div(a,b)}")
    else:
        logging.info("Niepoprawinie wybrana funkcja")

