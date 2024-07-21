import random

x = 0
y = 0


class Tankas():
    def __init__(self, pirmyn, desinen, atgal, kairen):
        self.pirmyn = pirmyn
        self.desinen = desinen
        self.atgal = atgal
        self.kairen = kairen


    def taikinys (dimension = 2, min_c = -5, max_c = 5):
        return [random.randint(min_c, max_c)for _ in range (dimension)]
    print ("Taikinys: ", taikinys())
    user_input = input("p - pirmyn, a - atgal, k - kairen, d - desinen, suvis, info, end\n")

    def pirmyn (self, user_input, y):
        if user_input == "p":
            y += 1
            return y
    def desinen (self, user_input, x):
        if user_input == "d":
            x += 1
            return x
    def atgal (self, user_input, y):
        if user_input == "atgal":
            y -= 1
            return y
    def kairen (self, user_input, x):
        if user_input == "kairen":
            x -= 1
            return x
    def info (self, user_input):
        if user_input == "info":
            print ("Atlikta suviu: ", )

print (x, y)

#Manto

import random

class Tankas:
    def __init__(self):
        # pradines X,Y koordinates
        self.x = 0
        self.y = 0
        # pradine kryptis
        self.kryptis = "pirmyn"
        self.suviu_sk = {"pirmyn": 0, "atgal": 0, "kairen": 0, "dešinėn": 0}
        self.taikinys_x = random.randint(-5, 5)
        self.taikinys_y = random.randint(-5, 5)
        self.taikinys_numustas = False
        # pradiniai taskai
        self.taskai = 100

    def rodyti_taikini(self):
        red_color = "\033[91m"
        # ANSI escape code to reset text color to default
        reset_color = "\033[0m"
        # Print "Jūsų taikinys yra:" in red color
        print(f"{red_color}Jūsų taikinys yra:{reset_color} x: {self.taikinys_x}, y: {self.taikinys_y}")
    def pirmyn(self):
        if self.kryptis == "pirmyn":
            self.y += 1
            # self.y = min(self.y, 5)
            self.taskai -= 10
            self.taskai_pralaimejai()
            # self.rodyti_taikini()
        elif self.kryptis == "atgal":
            self.x += 1
            self.x = min(self.x, 5)
        elif self.kryptis == "kairen":
            self.y -= 1
            self.y = min(self.y, -5)
        elif self.kryptis == "desinen":
            self.x -= 1
            self.x = min(self.x, -5)
    def atgal(self):
        if self.kryptis == "pirmyn":
            self.y -= 1
            # self.y = min(self.y, -5)
            self.taskai -= 10
            self.taskai_pralaimejai()
            # self.rodyti_taikini()
        elif self.kryptis == "atgal":
            self.x -= 1
        elif self.kryptis == "kairen":
            self.y += 1
        elif self.kryptis == "desinen":
            self.x += 1
    def kairen(self):
        if self.kryptis == "pirmyn":
            self.x -= 1
            self.taskai -= 10
            self.taskai_pralaimejai()
            # self.rodyti_taikini()
            # self.x = min(self.x, -5)
        elif self.kryptis == "atgal":
            self.x += 1
        elif self.kryptis == "kairen":
            self.y -= 1
        elif self.kryptis == "desinen":
            self.x -= 1
    def desinen(self):
        if self.kryptis == "pirmyn":
            self.x += 1
            # self.x = min(self.x, 5)
            self.taskai -= 10
            self.taskai_pralaimejai()
            # self.rodyti_taikini()
        elif self.kryptis == "atgal":
            self.x += 1
        elif self.kryptis == "kairen":
            self.y -= 1
        elif self.kryptis == "desinen":
            self.x -= 1

    def taskai_pralaimejai(self):
        if self.taskai <= 0:
            print("!!!!!!!PRALAIMEJAI PRALAIMEJAI PRALAIMEJAI!!!!!!")
            self.taskai = 100
            self.x = 0
            self.y = 0

    def suvis(self):
        atstumas = ((self.taikinys_x - self.x) ** 2 + (self.taikinys_y - self.y) ** 2) ** 0.5
        # Tikriname, ar taikinys yra pakankamai arti (pvz., atstumas mažesnis nei 2 vienetai)
        if atstumas < 2:
            print("Taikinys numustas!")
            self.taikinys_numustas = True
            self.taskai += 80
            self.taikinys_x = random.randint(-5, 5)
            self.taikinys_y = random.randint(-5, 5)
        else:
            print("Taikinys nepasiekiamas. Turite priarteti arciau taikinio.")
            self.taskai -= 10  # Deduct 10 points for a missed shot
    def informacija(self):
        # print(f'Taikinio koordinates: ({self.taikinys_x}, {self.taikinys_y})')
        green_color = "\033[92m"
        # ANSI escape code to reset text color to default
        reset_color = "\033[0m"
        print(f'{green_color}Tanko koordinates: {reset_color}x: {self.x} y: {self.y}')
        print(" ")
        print(f'Jusu taskai: {self.taskai}')
        # print(f'Jusu taskai: {self.taskai}')

tankas = Tankas()

while True:
    print("\nTanko valdymas:")
    print("1. Pirmyn (+Y) | 2. Atgal (-Y) | 3. Kairen (-X) | 4. Desinen (+X) | 5. Sauti | 6. Informacija | 7. Iseiti")
    tankas.informacija()
    print(" ")
    tankas.rodyti_taikini()
    choice = input("Pasirinkite veiksma: ")
    if choice == "1":
        tankas.pirmyn()
        # tankas.informacija()
    elif choice == "2":
        tankas.atgal()
        # tankas.informacija()
    elif choice == "3":
        tankas.kairen()
        # tankas.informacija()
    elif choice == "4":
        tankas.desinen()
        # tankas.informacija()
    elif choice == "5":
        tankas.suvis()
    elif choice == "6":
        tankas.informacija()
        tankas.rodyti_taikini()
    elif choice == "7":
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kart.")
