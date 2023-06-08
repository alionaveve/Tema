temperatura=int(input("Introdu temperatura de afara: "))

if temperatura <=-40 and temperatura<=-10:
    print(f"Vreme extrem de rece!")
elif  temperatura <=-10 and temperatura<=0:
        print(f"Vreme foarte rece!")
elif temperatura <=0 and temperatura <=10:
        print(f"Vreme rece!")
elif temperatura <=10 and temperatura<=20:
            print(f"Vreme normala")
elif temperatura <=20 and temperatura<=30:
                print(f"Vreme calda")
elif temperatura <=30 and temperatura <=40:
    print(f"Este foarte cald")
if temperatura>=40:
        print(f"Este extrem de cald")