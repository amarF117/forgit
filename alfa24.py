a = "hello world"   # daje velika slova.
print(a.upper())

c = "HELLO WORLD"   # daje mala slova.
print(c.lower())

d = " Hello, World "  # brice razmake.
print(d.strip())

e = "Hello, world"         #mjenja slovo ili rjeci.
print(e.replace("H","j"))

t = "Hello, world"        # stavlja rjeci u zagrade []
print(t.split(","))

a = " Hello "           # spaja 
b = " World "
c = a + b
print(c)

a = "Hello"             
b = "World"
c = a + " "+b
print(c)

"""String format
Kao što smo saznali u poglavlju Python Variables, ne možemo kombinirati nizove i brojeve poput ovog:
age = 36 
txt = "My name is  Jhon I am "+ age
print(txt)"""

age = 36 
txt = "My name is Jhon I am {}"
print(txt.format(age))

#Metoda format () uzima neograničen broj argumenata i stavlja se u odgovarajuća rezervirana mjesta:
quantity = 3
itemno = 567
price = 49.95
myorder = " I want {} pieces of  item {} for {} dollars"
print(myorder.format(quantity,itemno,price))

quantity = 3   #Možete koristiti indeksne brojeve {0} da biste bili,
itemno = 567   # sigurni da su argumenti postavljeni u ispravna rezervirana mjesta:
price = 49.95
myorder = "I wont to pay {2} dollars for {0} pieces of item {1} "
print(myorder.format(quantity,itemno,price))

#Da biste riješili taj problem, upotrijebite znak za bijeg \ ":Primjer
#Znak za bijeg omogućuje vam upotrebu dvostrukih navodnika kada vam obično nije dopušteno:
#ili obrisi navodnike "Vikings"
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#Code	Result	
# \'	    Single Quote.	 Jedan navodnik.
# \\	    Backslash.	     Kosa kosa crta.
# \n	    New Line.	     Nova linija.
# \r	    Carriage Return. Povrat prtljage.
# \t	    Tab.	         Tab.
# \b	    Backspace.	     Povratni prostor.
# \f        Form Feed.	     Ulaganje obrasca.
# \ooo	    Octal value.	 Oktalna vrijednost.
# \xhh	    Hex value.       Hex vrijednost.

#Method	Description
#  capitalize()	   Converts the first character to upper case.  Pretvara prvi znak u velika slova.
#  casefold()      Converts string into lower case. Pretvara niz u mala slova.
#  center()	       Returns a centered string. Vraća centrirani niz.
#  count()	       Returns the number of times a specified value occurs in a string. Vraća broj pojavljivanja određene vrijednosti u nizu.
#  encode()	       Returns an encoded version of the string. Vraća kodiranu verziju niza.
#  endswith()	   Returns true if the string ends with the specified value. Vraća true ako niz završava navedenom vrijednošću.
#  expandtabs()	   Sets the tab size of the string. Postavlja veličinu kartice niza.
#  find()	       Searches the string for a specified value and returns the position of where it was found. Pretražuje niz za navedenu vrijednost i vraća položaj mjesta na kojem je pronađen.
#  format()	       Formats specified values in a string. Formatira određene vrijednosti u nizu.
#  format_map()	   Formats specified values in a string. Formatira određene vrijednosti u nizu.
#  index()	       Searches the string for a specified value and returns the position of where it was found. Pretražuje niz za navedenu vrijednost i vraća položaj mjesta na kojem je pronađen.
#  isalnum()	   Returns True if all characters in the string are alphanumeric. Vraća True ako su svi znakovi u nizu alfanumerički.
#  isalpha()	   Returns True if all characters in the string are in the alphabet.Vraća True ako su svi znakovi u nizu u abecedi
#  isdecimal()	   Returns True if all characters in the string are decimals. Vraća True ako su svi znakovi u nizu decimale.
#  isdigit()	   Returns True if all characters in the string are digits. Vraća True ako su svi znakovi u nizu znamenke.
#  isidentifier()  Returns True if the string is an identifier. Vraća True ako je niz identifikator 
#  islower()	   Returns True if all characters in the string are lower case. Vraća True ako su svi znakovi u nizu malim slovima.
#  isnumeric()	   Returns True if all characters in the string are numeric. Vraća True ako su svi znakovi u nizu numerički.
#  isprintable()   Returns True if all characters in the string are printable. Vraća True ako su svi znakovi u nizu za ispis.
#  isspace()	   Returns True if all characters in the string are whitespaces. Vraća True ako su svi znakovi u nizu razmaci.
#  istitle()	   Returns True if the string follows the rules of a title. Vraća True ako niz slijedi pravila naslova.
#  isupper()	   Returns True if all characters in the string are upper case. Vraća True ako su svi znakovi u nizu velika slova.
#  join()	       Joins the elements of an iterable to the end of the string. Spaja elemente iterabilnog s krajem niza.
#  ljust()	       Returns a left justified version of the string. Vraća poravnatu lijevu verziju niza.
#  lower()	       Converts a string into lower case. Pretvara niz u mala slova.
#  lstrip()	       Returns a left trim version of the string.Vraća lijevu izrezanu verziju niza.
#  maketrans()	   Returns a translation table to be used in translations. Vraća prijevodnu tablicu koja će se koristiti u prijevodima.
#  partition()	   Returns a tuple where the string is parted into three parts.Vraća korijen gdje je niz podijeljen u tri dijela.
#  replace()	   Returns a string where a specified value is replaced with a specified value. Vraća niz gdje se navedena vrijednost zamjenjuje navedenom vrijednošću.
#  rfind()	       Searches the string for a specified value and returns the last position of where it was found.Pretražuje niz za zadanu vrijednost i vraća posljednju poziciju mjesta na kojem je pronađen.
#  rindex()	       Searches the string for a specified value and returns the last position of where it was found.Pretražuje niz za zadanu vrijednost i vraća posljednju poziciju mjesta na kojem je pronađen.
#  rjust()	       Returns a right justified version of the string.Vraća ispravljenu verziju niza.
#  rpartition()	   Returns a tuple where the string is parted into three parts.Vraća korijen gdje je niz podijeljen u tri dijela.
#  rsplit()	       Splits the string at the specified separator, and returns a list.Dijeli niz na navedenom razdjelniku i vraća popis.
#  rstrip()	       Returns a right trim version of the string.Vraća ispravljenu verziju niza.
#  split()	       Splits the string at the specified separator, and returns a list. Dijeli niz na navedenom razdjelniku i vraća popis.
#  splitlines()	   Splits the string at line breaks and returns a list. Dijeli niz na prijelomu retka i vraća popis.
#  startswith()    Returns true if the string starts with the specified value.Vraća true ako niz započinje navedenom vrijednošću.
#  strip()	       Returns a trimmed version of the string.Vraća skraćenu verziju niza.
#  swapcase()	   Swaps cases, lower case becomes upper case and vice versa.Mijenja slučajeve, mala slova postaju velika i obrnuto.
#  title()	       Converts the first character of each word to upper case. Pretvara prvi znak svake riječi u velika slova.
#  translate()	   Returns a translated string. Vraća prevedeni niz.
#  upper()         Converts a string into upper case. Pretvara niz u velika slova.
#  zfill()	       Fills the string with a specified number of 0 values at the beginning. Ispunjava niz navedenim brojem od 0 vrijednosti na početku.

# Boolean  daje True ili false vrjednost.
print(10 > 9)    #True
print(10 == 9 )  #False
print( 10 < 9 )  #False

#Ispišite poruku na temelju toga je li uvjet Tačno ili Netačno:
a = 200
b = 33
if a > b :
    print("a is greater then b ")
else:
    print("A in not greater then b")

# Procijenite vrijednosti i varijable Funkcija bool () omogućuje vam procjenu bilo koje vrijednosti i zauzvrat vam daje True ili False,
print(bool("Hello"))  #True
print(bool(15))       #True

# Procijenite dvije varijable:
x = "Hello"
b = 15
print(bool(x))    #True
print(bool(b))    #True

#Većina vrijednosti su istinite
#Gotovo svaka vrijednost procjenjuje se na True ako ima nekakav sadržaj.
#Bilo koji niz je True, osim praznih nizova.
#Bilo koji broj je True, osim 0.
#Bilo koji popis, skup, skup i rječnik su True, osim praznih.Primjer
#Sljedeće će vratiti True:
bool("abc")
bool(123)
bool(["apple,banana,cherry"])

#Još jedna vrijednost, ili objekt u ovom slučaju, procjenjuje se na False, a to je ako imate objekt izrađen iz klase s funkcijom __len__ koja vraća 0 ili False:
class myclass:
    def __len__(self):   #True
        return 0
myobj = myclass
print(bool(myobj))

#Funkcije mogu vratiti logičku vrijednost. Možete stvoriti funkcije koje vraćaju logičku vrijednost:
def myfunction():
    return True
print(myfunction())

# ako je True pisace Yes ako ne  pisace Not. 
def myfunction():
    return True

if myfunction():
    print("Yes!")
else:
    print("Not!")

#Python također ima mnogo ugrađenih funkcija koje vraćaju logičku vrijednost, poput funkcije isinstance (), 
# koja se može koristiti za određivanje je li objekt određene vrste podataka:
x = 200                   # True
print(isinstance(x,int))  

#Aritmetički operatori koriste se s numeričkim vrijednostima za izvođenje uobičajenih matematičkih operacija:
print(2+3) #5          sabiranje.
print(5-1) #4          Oduzimanje.
print(5*10) #50        Množenje.
print(6/3) #2.0        Podjela.
print(10%100) #10      Modulus postotak.
print(100**2) #1000    Pojačavanje. 
print(5//4)  #1        Podna podjela. 

# Operatori dodjele koriste se za dodjeljivanje vrijednosti varijablama:
"""
=	    x = 5	x = 5	
+=    	x += 3	x = x + 3	
-=   	x -= 3	x = x - 3	
*=  	x *= 3	x = x * 3	
/=	    x /= 3	x = x / 3	
%=	    x %= 3	x = x % 3	
//=	    x //= 3	x = x // 3	
**=	    x **= 3	x = x ** 3	
&=	    x &= 3	x = x & 3	
|=	    x |= 3	x = x | 3	
^=	    x ^= 3	x = x ^ 3	
>>=	    x >>= 3	x = x >> 3	
<<=	    x <<= 3	x = x << 3"""

# Operatori usporedbe koriste se za usporedbu dviju vrijednosti.
# ==	Equal	x == y.
# !=	Not equal	x != y.	
# >	    Greater than	x > y.	
# <	    Less than	x < y.	
# >=	Greater than or equal to	x >= y.	
# <=	Less than or equal to	x <= y.	

# Logički operatori koriste se za kombiniranje uvjetnih izraza:
#   and 	Returns True if both statements are true	x < 5 and  x < 10.	
#   or	    Returns True if one of the statements is true	x < 5 or x < 4.	
#   not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10).

# Python operateri identiteta.
# Operatori identiteta koriste se za usporedbu objekata, 
# ne ako su jednaki, već ako su zapravo isti objekt, s istim memorijskim mjestom:
#     is 	    Returns True if both variables are the same object	x is y.	
#     is not	Returns True if both variables are not the same object	x is not y.

# Operateri članstva u Pythonu.
# Operatori članstva koriste se za ispitivanje je li sekvenca predstavljena u objektu:
#     in 	    Returns True if a sequence with the specified value is present in the object	x in y.	
#     not in	Returns True if a sequence with the specified value is not present in the object	x not in y.

#Python bitovni operateri
#Bitni operatori koriste se za usporedbu (binarnih) brojeva:
#     & 	AND	Sets each bit to 1 if both bits are 1.
#     |	    OR	Sets each bit to 1 if one of two bits is 1.
#     ^	    XOR	Sets each bit to 1 if only one of two bits is 1.
#     ~ 	NOT	Inverts all the bits.
#     <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off.
#     >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off. 

#Da biste utvrdili koliko stavki ima popis, upotrijebite funkciju len ():
thislist = ["apple", "banana", "cherry ","apple,","cherry"]  # 5
print(len(thislist))

#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered and changeable. No duplicate members.
#When choosing a collection type, it is useful to understand the properties of that type. 
# Choosing the right type for a particular data set could mean retention of meaning, 
# and, it could mean an increase in efficiency or security.


#Ovaj primjer vraća stavke od početka na, ali NE uključujući "kiwi":
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4])

#Ovaj primjer vraća stavke iz "trešnje" na kraj:
thislist = ["apple","Banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])

#Ovaj primjer vraća stavke iz "narančaste" (-4) u, ali NE uključujući "mango" (-1):
thislist = ["apple","Banana","cherry","orange","kiwi","melom","mango"]
print(thislist[-4:-1])

#Provjerite je li na popisu prisutna "jabuka":
thislist = list(("apple", "banana", "cherry","orange","kiwi","melon","mango")) 
if "apple" in thislist:
    print("Yes apple is in fruits this list ")

#Promijenite vrijednost predmeta
#Da biste promijenili vrijednost određene stavke, pogledajte indeksni broj:
thislist = ["apple","Banana","Cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Promijenite vrijednosti "banana" i "trešnja" s vrijednostima "crni ribiz" i "lubenica":
thislist = ["apple","Banana","Cherry","orange","kiwi","malon","mango"]
thislist = ["blackcurrant","watermalon"]
print(thislist[1:3])

#Promijenite drugu i treću vrijednost zamjenom s jednom vrijednošću:
thislist = ["apple","banana","cherry",]
thislist[1:3] = ["watermelon"]
print(thislist)

#Umetnite "lubenica" kao treću stavku:
thislist = ["apple","Banana","Cherry"]
thislist.insert(2,"watermalon")
print(thislist)

#Korištenje metode append () za dodavanje stavke: 
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

#Metoda insert () ubacuje stavku s navedenim indeksom:
thislsit = ["apple","banana","cherry"]
thislsit.insert(1,"orange")
print(thislsit)

#Da biste dodali elemente s drugog popisa trenutnom popisu, upotrijebite metodu extend().
thislist = ["apple","banana","cherry"]
tropical = ["mango","pinepple","papaya"]
thislist.extend(tropical)
print(thislist)

#extend() metoda ne mora dodavati popise, možete dodati bilo koji iterabilni objekt(tuples, sets, dictionaries etc.)
thislist = ["apple","banana","cherry"]
thistuple = ("orange","kiwi")
thislist.extend(thistuple)
print(thislist)

#remove() uklanja navedenu stavku.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Uklonite navedeni indeks
#Metoda pop () ako nekazes koji indeks hoces da se obrise on ce obrisati zadnji sam od sebe.
thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)

# del brise indekse [apple, banana, cherry]
thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)

#del Izbrišite cijeli popis:
thislist = ["apple", "banana", "cherry"]
del thislist

#clear() metoda prazni popis.Popis i dalje ostaje, ali nema sadržaja.
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)

#Ispišite sve stavke na popisu, jednu po jednu: 
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)

#Upotrijebite funkcije range () i len () da biste stvorili prikladan iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Ispišite sve stavke pomoću petlje while za prolazak kroz sve indeksne brojeve.
thislist = ["apple","banana","cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i +1

#Kratka petlja za petlju koja će ispisati sve stavke na popisu:
thislist = ["apple","banana","cherry"]
[print(x) for x in thislist]

#Na temelju popisa voća želite novi popis koji sadrži samo plodove sa slovom "a" u nazivu.
#Bez razumijevanja popisa morat ćete napisati izjavu for s uvjetnim testom unutar:
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) 

#S razumijevanjem popisa sve to možete učiniti sa samo jednim retkom koda:
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 

#Prihvaćajte samo predmete koji nisu "jabuka": 
newlist = [x for x in fruits if x != "apple"]

#Pomoću funkcije range () možete stvoriti iterable:
#newlist = [x for x in (range[10])]  # daje gresku 

#Prihvatite samo brojeve niže od 5:
newlist = [x for x in range(10) if x <5 ]
print(newlist)

#Objekti popisa imaju metodu sort () koja će prema zadanim postavkama sortirati popis alfanumerički, uzlazno: Primjer
#Poredaj popis po abecedi: 
thislist = ["apple","orange","banana","kiwi","pineapple"]  
thislist.sort()    # Ako stavimo velika slvova sort() ce ih poreedati po velicini.
print(thislist)

#Poredaj popis numerički:
thislist = [100,50,65,82,23]
thislist.sort()                # daje rezultat 23 50 65 82 100
print(thislist)

#Poredaj silazno.Da biste sortirali silazno, upotrijebite argument ključne riječi reverse = True:
thislist = ["ornage","mango","kiwi","pineapple","banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100,50,65,82,23]     #daje obratni rezultata 100 65.82 50 23
thislist.sort(reverse = True)
print(thislist)

#Ovaj kod  sortira broj koji ukucas  i poreda postujece broje   koje si ti ukuco.
def myfunc(n):              #Ako stavis 10 on ce poredati brojeve koje su naj blize tom broju.
    return abs(n -50)

thislist = [100,50,65,82,23]  
thislist.sort(key = myfunc)
print(thislist)

#Ovaj kod  ispise prvo mala slova pa onda velika.
thislist = ["Apple","Kivi","banana","Mango","Orange"]
thislist.sort(key = str.lower)
print(thislsit)

#Ovaj kod cita od zadnjeg  elementa a ne od prvog.
thislist = ["apple","banana","Kiwi","Orange","cherry"]
thislist.reverse()
print(thislist)

#Kopirajte popis
#Popis ne možete kopirati jednostavnim upisivanjem list2 = list1, jer: 
#lista2 bit će samo referenca na listu1, a promjene izvršene na listi1 automatski će se izvršiti i na listi2.
thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist)

#Kopiranje pomocu list():
thislist = ["apple","banana","cherry"]
mylist = list(thislist)
print(mylist)

#Ovako spajam liste u novu list.
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

#Spajanja pomocu append()
list1 = ["a","b","c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)
print(list1) 

#Metoda extend() spaja dvije liste.
list1 = ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2)
print(list1) 

#Metode popisa. Python ima skup ugrađenih metoda koje možete koristiti na popisima.
# append()   Dodaje element na kraju popisa.
# clear()    Uklanja sve elemente s popisa.
# copy()     Vraća kopiju popisa.
# count()    Vraća broj elemenata s navedenom vrijednošću.
# extend()   Dodajte elemente popisa (ili bilo kojeg ponovljivog teksta) na kraj trenutnog popisa.
# index()    Vraća indeks prvog elementa s navedenom vrijednošću.
# insert()   Dodaje element na navedenom položaju.
# pop()      Uklanja element na navedenom položaju.
# remove()   Uklanja element na navedenom položaju.
# reverse()  Obrne redoslijed popisa.
# sort()     Sortira popis

#Korijeni se koriste za pohranu više predmeta u jednu varijablu.
#Tuple je jedna od 4 ugrađene vrste podataka u Pythonu koje se koriste za pohranu zbirki podataka, 
# ostale 3 su List, Set, i Dictionary, sve s različitim kvalitetama i upotrebom.
#Tuple je zbirka koja je uređena i nepromjenjiva.
#Tuple su napisane okruglim zagradama.

thistuple = ("apple","banana","cherry")
print(thistuple)   # Ako dodamo len() dobicemo broj koliko se nalazi u zagradi.

# Tuple moze biti biti bilo koji podatak String, int i boolean vrste podataka:
tuple1 = ("apple","banana","cherry")
tuple2 = (1,5,7,9,3)
tuple3 = (True,False,False,)
tuple = ("abc",34,True,40,"male")

#Tuple se nemoze promjeniti ali sa ovim kodo moze.
X = ("apple","banana","kiwi") 
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Pretvorite tuple u list, dodajte "narančasto" i pretvorite ih natrag u tuple:
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)

#Uklonite stavke
#Napomena: Ne možete ukloniti stavke u Tuple.
#Tuple su nepromjenjive, pa iz njih ne možete ukloniti stavke, 
#ali možete upotrijebiti isto zaobilazno rješenje kao i mi za promjenu i dodavanje tuple stavki:
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(y)

#Ako zelim mozemo skroz obrisati tuple sa del:
thistuple =  ("apple","banana","cherry")
del thistuple
print(thistuple) 

#Ali, u Pythonu nam je također dopušteno izvući vrijednosti natrag u varijable. To se naziva "raspakiranje":
fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#Ako stavim * zvjezdicu  sve ostale ce  biti red koje nisu  definisane.
fruits = ("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red) = fruits
print(green,yellow,red)

#Ovo  nesto radi nemam blage sta? 
fruits = ("apple","mango","papaya","pineapple","cherry")
(Green, *Tropical, red) = fruits
print(Green,Tropical,red)

# spajanje dvije vrjednosti sa operatorom +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Ako želite umnožiti sadržaj tupe određeni broj puta, možete upotrijebiti * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits *2
print(mytuple)

#Set se kreira sa viticastim zagradama {} set se nemoze promjeniti kad ga jednom napravite. 
#Ali i set  ne dozvolava duple varijable na primjer zadnji  dupli apple se nece printati  bice  ignoriran.
#Nece racunati zadnji apple.
#Set moze biti bilo koji podatak set,int,boolen.
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
thisset = {"apple","cherry","banana","apple"}
print(len(thisset))
#Ovo je prebaciti iz jednog u set ako definisem.
thisset = set (("apple", "banan", "cherry"))
print(thisset)
# Ako stavim thisset  = set("apple") dacemi  rezultat {'e', 'l', 'p', 'a'}?
# Ako stavim thisset = tuple("apple") dacemi rezultat ('a', 'p', 'p', 'l', 'e')?

#Pored ih  uspravno.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Ako hocu da vidim dali postoji rjec u listi  ako postoji dacemi rezultat True:
thisset = {"apple","banana","cherry"}
print("banana" in thisset)

#Da dodam u rjecnik 
thisset = {"apple","banana","cherry"}
thisset.add ("orange")
print(thisset)

# Ovako spajam  dvije strane rjecnika:
# Sa metodom Update() mogu spojiti bilo koji iteraciju podatak Tuples,lists,dictionaries, etc.
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

#Zbirke Pythona (nizovi)
#U programskom jeziku Python postoje četiri vrste podataka o kolekciji:
#List je zbirka koja je uređena i promjenjiva. Omogućuje duplicirane članove.
#Tuple je kolekcija koja je uređena i nepromjenjiva. Omogućuje duplicirane članove.
#Set je kolekcija koja je neuređena i indeksirana. Nema dupliciranih članova.
#Dictionary je zbirka koja je neuređena i promjenjiva. Nema dupliciranih članova.
#Pri odabiru vrste zbirke korisno je razumjeti svojstva te vrste. 
# Odabir prave vrste za određeni skup podataka mogao bi značiti zadržavanje značenja, 
# a mogao bi značiti i povećanje učinkovitosti ili sigurnosti.

#Metoda Remove  smacinje dijo koji oznacite.
thisset = {"apple", "banana","cherry"}
thisset.remove("banana")
print(thisset)

#Metoda Discard  smacinje dijo koji  oznacim u zagradama 
thisset = {"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

#Metoda  pop uklanja posnjednu stavku u redu.
#Napomena setovi nisu uredeni pa kada koristite metodu pop ne znate koja ce stavka biti uklonjena.
thisset = {"apple","banana","cherry"}
x = thisset.pop()
print(x)
print(thisset)

#Metoda Clear brise elemente u listi. 
thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset)

#Metoda Del brise cjelu set i daje  eror kad se pusti kroz print.
thisset = {"apple","banana","cherry"}
del thisset
print(thisset)

#Da prelistamo sve elemente.
thisset = {"apple","banana","cherry"}
for x in thisset: 
    print(x)

# Metoda union() vraca novi skup sa stavkama iz oba skupa 
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# Metoda update() ubacuje stavke iz set2 u set1.
# Napomena union(), update() ce iskljuciti bilo koji dubplikat.
set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

# Ostavlja samo duple vrjednosti u  setovima ili listama.
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.intersection_update(y)
print(x)

#Ovako  un uzima samo  pojadinacne  podatke ne duplikate  i staviti ih u novi  set/listu.
x = {"apple","banana","cherry"}
y = {"google","microfost","apple"}
z = x.intersection(y)
print(z)

#Metoda symmetric_difference_update ne uzima duplikate samo pojedinacne i stavnja ih u listu od x.
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.symmetric_difference_update(y)
print(x)

#Sam symmetric_difference uzima pojadinacne  i stavlja ih u novi set 
x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
z = x.symmetric_difference(y)
print(z)

#add()                         Dodaje element skupu.
#clear()                       Uklanja sve elemente iz skupa.
#copy()                        Vraća kopiju skupa.
#difference()                  Vraća skup koji sadrži razliku između dva ili više skupova.
#difference_update()           Uklanja stavke iz ovog skupa koje su također uključene u drugi, navedeni skup.
#discard()                     Uklonite navedenu stavku.
#intersection()                Vraća skup, odnosno presjek dvaju drugih skupova
#intersection_update()         Uklanja stavke iz ovog skupa koje nisu prisutne u drugim navedenim set(s).
#isdisjoint()                  Vraća imaju li dva skupa sjecište ili ne.
#issubset()                    Vraća sadrži li ga drugi skup ili ne.
#issuperset()                  Vraća sadrži li ovaj skup drugi skup ili ne.
#pop()                         Uklanja element iz skupa. 
#remove()                      Uklanja navedeni element.
#symmetric_difference()        Vraća skup sa simetričnim razlikama dvaju skupova.
#symmetric_difference_update() ubacuje simetrične razlike iz ovog i drugog skupa.
#union()                       Vrati skup koji sadrži uniju skupova.
#update()                      Ažurirajte skup ujedinjenjem ovog skupa i ostalih.
