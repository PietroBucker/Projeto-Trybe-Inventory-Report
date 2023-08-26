from datetime import datetime
teste = datetime.strptime('2023-08-24', "%Y-%m-%d").date()
teste2 = datetime.now().date()
print(teste2 - teste)