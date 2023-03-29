###########################Funkcje break i continue
#funkcja break jest używana do zakończenia pętli for i while,
#podczas gdy funkcja continue pozwala opuścić blok instrukcji niżej i wrócić do nagłówka pętli.

## Przykład 1
## Program wypisuje tylko liczby 0 1 2 3 4

# lista =[0,1,2,3,4,5,6,7,8,9]


# for i in lista:
#     print(i)
#     if  i  > 5:
#         break   # przerwij działanie pętli
# print('#######################################')
# # Przykład 2
# # Program wypisuje tylko liczby nieparzyste - 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Sprawdz, czy x jest parzyste
#         continue
#     print(x)


# if type(n) == 'str':
#     print('zmienna string')

#################Instrukcje sterujące tj. instrukcje warunkowe i pętle  Teoria
################# 1. Instrukcja warunkowa "MATCH"#########struktura
# match zmienna:
# case wartość zmiennej 1:
#     blok instrukcji
# case wartość zmiennej 2:
#     blok instrukcji
# ....
# case wartość zmiennej n:
#     blok instrukcji

## Przykład 2
# ## Program liczy  liczba jest większa od zera

# dane_osobowe = input('Wpisz "imie" albo "nazwisko"'))
# match dane_osobowe:
#    case "imie":
#        print('Ala')
# case "imie":
#    print('Kowalska')







    
#############Zadania do wykonania##############################
############Blok obowiązkowy############################
#Zadanie 1
#Użytkownik podaje trzy liczby, sprawdź, która z nich jest największa, wynik wydrukuj na ekranie. 

# n1 = int(input(" 2 "))
# n2 = int(input(" 7 "))
# n3 = int(input(" 5 "))

# if n1 > n2 and n1 > n3:
#     print(n1)
# elif n2 > n3 and n2 > n1:
#     print(n2)
# elif n3 > n2 and n3 > n1:
  
#     print(n3)







#Zadanie 2
#Napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
#a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
#program kończy działanie jeżeli trafi na cyfrę 0.



#Zadanie 3
# Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
# właściwe hasło (hasło jest przechowywane w zmiennej)




#Zadanie 4
#Utwórz dowolną listę złożoną z 10 liczb całkowitych parzystych i nieparzystych
# wypisz wszystkie liczby parzyste z tablicy




#Zadanie 5
# Zapytaj użytkownika o wiek, w zależności od wieku 16, 18 lat poinformuj użytkownika o jego prawach np.:
#  czy może legalnie obejrzeć film w kinie (tytuł),
#  kupić alkohol i papierowsy,
# ma prawa wyborcze itd
# w zadaniu użyj conajmnie 2 warunki


# wiek = input('podaj wiek: ')
# if wiek < 16:
#   pass
# elif wiek > 16 and wiek < 18:
#   pass
# else:
#   pass

# age = int(input("Podaj swój wiek: "))

# if age < 16:
#     print("Jesteś zbyt młody, aby legalnie obejrzeć większość filmów w kinie.")
# elif age >= 16 and age < 18:
#     print("Możesz legalnie obejrzeć filmy oznaczone symbolem 16+.")
# elif age >= 18:
#     print("Możesz legalnie obejrzeć wszystkie filmy.")

# if age < 18:
#     print("Nie możesz kupić alkoholu ani papierosów.")
# elif age >= 18:
#     print("Możesz legalnie kupić alkohol i papierosy.")

# if age < 18:
#     print("Nie masz prawa głosować w wyborach.")
# elif age >= 18:
#     print("Masz prawo głosować w wyborach.")





#Zadanie 6
#Oblicz w pętli sumę liczb od 1 do 100


#Zadanie 7
#Pytaj użytkownika o imię i je wyświetlaj aż do momentu gdy wpisze wyraz stop



#Zadanie 8
#Korzystając z pętli for oblicz średnią z 4 liczb







#Zadanie 9
#Korzystając z pętli while oblicz średnią z 4 liczb

n = 4
i = 1
suma = 0
ile = 0
while i < n+1:
  suma = suma + i
  i = i + 1
  ile = ile + 1
  print(suma)
print(ile)





# Zadanie 10
#  Napisz skrypt, w ktorym w zaleznosci od wybranej przez uzytkownika liczby
#  calkowitej z zakresu od 1, 2 lub3, wykonane zostana nastepujace działania:
#  dla wpisanej liczby 1  zostanie obliczona wartosc sin(x)
#  dla liczby 2 obliczona cos(x)  oraz dla liczby 3 obliczony tan(x),

############Blok nadobowiązkowy############################
#Zadanie 1
# Rozbuduj program z Zadania 3: 2różne hasła - 2 różne dane



#Zadanie 2
# Wylosuj liczbę, napisz program w którym użytkownik probuje zgadnąć tą liczbę może to jednak zrobić maksymalnie 10 razy
# do wylosowania liczby użyj poniższych metod z biblioteki random
#import random
#print(random.random())
# wylosowana_liczba = random.choice([1,2,3,4,5])



#Zadanie 3
#Utwórz dowolną listę złożoną z 10 liczb całkowitych parzystych i nieparzystych
# wypisz wszystkie liczby parzyste z tablicy liczby, następnie wypisz posortowane od najmniejszej do największej