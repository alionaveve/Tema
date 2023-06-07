parola=str(input("Introdu parola:"))
valid_parola=True
if len(parola)<8:
    print(f"Parola este scurta,introduceti alta parola sa contina 8 caractere:")
if  parola.islower():
    print(f"Parola este slaba")
    if parola.isupper():
        print(f"Parola este slaba")
        if parola==valid_parola:
            print(f"Parola puternica")