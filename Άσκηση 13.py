# Excersize 13
# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου, το χωρίζει σε λέξεις και εμφανίζει
# τα ζευγάρια λέξεων όπου το συνολικό τους μήκος χαρακτήρων είναι 20. Κάθε ζευγάρι φεύγει από το σύνολο και το πρόγραμμα
# τελειώνει όταν εξαντληθούν τα ζευγάρια.

import string
z = string.ascii_letters

print(z)

alBet = [' ']
for i in range(len(z)):
    alBet.append(z[i])

print(alBet)
   

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []
eleven = []
twelve = []
thirteen = []
fourteen = []
fifteen = []
sixteen = []
seventeen = []
eighteen = []
nineteen = []


with open("DEMO 4.txt" , "r") as f:    #read_ASCII  #read_me  # DEMO 9  # DEMO 4 # two_cities.txt
    d = f.readlines()

#print(d)            ############

splt = []

for i in range(len(d)):           # split.
    for j in range(len(d[i])):
        splt.append(d[i][j])

#print(splt)        ############

clean = []                        # Λίστα χωρίς σύμβολα π.χ (!@#*,....)

for i in range(len(splt)):
    if splt[i] in alBet:
        clean.append(splt[i])
#print(clean)                     # Χωρίς σύμβολα π.χ (!@#*,....)  

mrg = ''.join(clean)              # Συνένωση σε string.

#print (mrg)                      # LIST = mrg.split()  # Το string σε λίστα.

LIST = mrg.split()   

cnt_LIST = len(LIST)


for word in LIST:                 # Διαλογή λέξεων που έχουν μήκος από 1 έως και 19, σε λίστες.
    if len(word) == 1:
        one.append(word)
    elif len(word) == 2:
        two.append(word)
    elif len(word) == 3:
        three.append(word)
    elif len(word) == 4:
        four.append(word)
    elif len(word) == 5:
        five.append(word)
    elif len(word) == 6:
        six.append(word)
    elif len(word) == 7:
        seven.append(word)
    elif len(word) == 8:
        eight.append(word)
    elif len(word) == 9:
        nine.append(word)
    elif len(word) == 10:
        ten.append(word)
    elif len(word) == 11:
        eleven.append(word)
    elif len(word) == 12:
        twelve.append(word)
    elif len(word) == 13:
        thirteen.append(word)
    elif len(word) == 14:
        fourteen.append(word)
    elif len(word) == 15:
        fifteen.append(word)
    elif len(word) == 16:
        sixteen.append(word)
    elif len(word) == 17:
        seventeen.append(word)
    elif len(word) == 18:
        eighteen.append(word)
    elif len(word) == 19:
        nineteen.append(word)




def merge(A,B):         # Συνάρτηση για την δημιουργία ζευγάρια λέξεων όπου το συνολικό τους μήκος χαρακτήρων τους είναι 20. 
    LISTA = []                         # L = []
                                 
    while A!=[] and B!=[]:
        L = []
        if len(A) < len(B):
            for i in range(1):         # len(A)       
                L.append(A.pop(0))     # L.append(A.pop(0))
                L.append(B.pop(0))     # L.append(B.pop(0))
            LISTA.append(L)
        elif len(B) < len(A):
            for i in range(1):         # len(B)
                L.append(A.pop(0))
                L.append(B.pop(0))
            LISTA.append(L)
                      
        else:
            for i in range(1):         # len(A)
                L.append(A.pop(0))
                L.append(B.pop(0))
            LISTA.append(L)        
    return LISTA


def listTen(A):                        # Αφορά την λίστα με μήκος χαρακτήρων 10. OK!
    LISTA = []
    while A != [] and len(A) > 1 :    # [] ??????????????????????????
        L = []
        if len(A)%2 == 0:
            for i in range(2):             # len(A)
                L.append(A.pop(0))
            LISTA.append(L)    

        else:
            if len(A) >= 3:        
                for i in range(2):         # len(A)-1
                    L.append(A.pop(0))
                LISTA.append(L)
    return LISTA


L1_19 = merge(one,nineteen)            # Κάλεσμα συνάρτησης για την δημιουργία των αντίστοιχων ζευγαριών σε λίστες. 
L2_18 = merge(two,eighteen)
L3_17 = merge(three,seventeen)
L4_16 = merge(four,sixteen)
L5_15 = merge(five,fifteen)
L6_14 = merge(six,fourteen)
L7_13 = merge(seven,thirteen)
L8_12 = merge(eight,twelve)
L9_11 = merge(nine,eleven)
L_10 = listTen(ten)

z = f"Ζευγάρια λέξεων με μήκος 1 και 19 : {L1_19}"     ###### Ζευγάρια λέξεων
print(z)
z = f"Ζευγάρια λέξεων με μήκος 2 και 18 : {L2_18}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 3 και 17 : {L3_17}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 4 και 16 : {L4_16}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 5 και 15 : {L5_15}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 6 και 14 : {L6_14}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 7 και 13 : {L7_13}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 8 και 12 : {L8_12}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 9 και 11 : {L9_11}"
print(z)
z = f"Ζευγάρια λέξεων με μήκος 10 και 10 : {L_10}"
print(z)

count = 0
                            
if L1_19 != []:                     # Θα διαγράψει τα ζευγάρια λέξεων από το σύνολο!!!
    for i in range(len(L1_19)):              
        LIST.remove(L1_19[i][0])    
        LIST.remove(L1_19[i][1])
        count += 2


if L2_18 != []:
    for i in range(len(L2_18)):              
        LIST.remove(L2_18[i][0])    
        LIST.remove(L2_18[i][1])
        count += 2

    
    
if L3_17 != []:
    for i in range(len(L3_17)):              
        LIST.remove(L3_17[i][0])    
        LIST.remove(L3_17[i][1])
        count += 2

    
    
if L4_16 != []:
    for i in range(len(L4_16)):              
        LIST.remove(L4_16[i][0])    
        LIST.remove(L4_16[i][1])
        count += 2

    
    
if L5_15 != []:
    for i in range(len(L5_15)):              
        LIST.remove(L5_15[i][0])    
        LIST.remove(L5_15[i][1])
        count += 2

    
    
if L6_14 != []:
    for i in range(len(L6_14)):              
        LIST.remove(L6_14[i][0])    
        LIST.remove(L6_14[i][1])
        count += 2

    
    
if L7_13 != []:
    for i in range(len(L7_13)):              
        LIST.remove(L7_13[i][0])    
        LIST.remove(L7_13[i][1])
        count += 2

    
    
if L8_12 != []:
    for i in range(len(L8_12)):              
        LIST.remove(L8_12[i][0])    
        LIST.remove(L8_12[i][1])
        count += 2

    
    
if L9_11 != []:
    for i in range(len(L9_11)):              
        LIST.remove(L9_11[i][0])    
        LIST.remove(L9_11[i][1])
        count += 2

    
    
if L_10 != []:
    for i in range(len(L_10)):              
        LIST.remove(L_10[i][0])    
        LIST.remove(L_10[i][1])
        count += 2

    

text = ''
for i in range (len(LIST)):
    text += LIST[i]
    if LIST[i] != LIST[-1]:
        text += ' '

z = f"Το σύνολο των λέξεων του αρχείου ASCII ήταν : {cnt_LIST}"    
print(z)

z = f"Το σύνολο (ζευγάρια λέξεων με συνολικό μήκος χαρακτήρων 20) που αφαιρέθηκαν είναι : {count}"    
print(z)

z = f"Ο αριθμός των λέξεων του καινούργιου κειμένου είναι :  {len(LIST)}"    
print(z)

z = f"Το καινούργιο αρχείο είναι : {text}"
print(z)



