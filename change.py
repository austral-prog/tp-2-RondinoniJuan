def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    
    print("Vuelto")
    
    print("Pesos:")
    print(int((money - expense) - 0.25))
    print("Centavos:")
    print(int(((money - expense) - (int((money - expense) - 0.25))) * 100))
