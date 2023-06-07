temperatura=int(input("Introdu temperatura de afara: "))

if temperatura <=-40 or temperatura<=-10:
    print(f"Vreme extrem de rece!")
if  temperatura <=-10 or temperatura<=0:
        print(f"Vreme foarte rece!")
if temperatura <=0 or temperatura <=10:
        print(f"Vreme rece!")
elif temperatura <=10 or temperatura<=20:
            print(f"Vreme normala")
elif temperatura <=20 or temperatura<=30:
                print(f"Vreme calda")
elif temperatura <=30 or temperatura <=40:
    print(f"Este foarte cald")
if temperatura>=40:
        print(f"Este extrem de cald")