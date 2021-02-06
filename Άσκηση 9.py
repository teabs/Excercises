# Excersize 9
# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα 
# στον αντίστοιχο αριθμό ASCII και κρατάει τους μονούς. Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με “μπάρες” 
# χρησιμοποιώντας το χαρακτήρα *, όπου κάθε * αντιστοιχεί σε 1%. Η στρογγυλοποίηση θα γίνει προς τα πάνω.

splt = []                               # split
ascii_nums = []
per_asc = []                            

with open ("two_cities_ascii.txt" , "r") as f:    # DEMO 9.txt    # read_ASCII.txt     #two_cities
    d = f.readlines()                   # Δημιουργεί το αρχείο σε λίστα.

#print (d)

for i in range(len(d)):
    for j in range(len(d[i])):
        splt.append(d[i][j])            #π.χ['T', 'o', 'd', 'a', 'y', 'i', 's', 't', 'h', 'e', 'b', 'e', 's', 't', 'd', 'a', 'y', 'o', 'f', 'm', 'y', 'l', 'i', 'f', 'e', '!']

#print (splt)
splt.sort()                      

for i in range(len(splt)):              # Convert to ascii numbers.
    ascii_nums.append(ord(splt[i]))     #π.χ [84, 111, 100, 97, 121, 105, 115, 116, 104, 101, 98, 101, 115, 116, 100, 97, 121, 111, 102, 109, 121, 108, 105, 102, 101, 33]
    
print (ascii_nums)    

for i in range(len(ascii_nums)):        # Συλλογή των περιττών χαρακτήρων.
    if ascii_nums[i] % 2 != 0:
        per_asc.append(ascii_nums[i])   #π.χ [111, 97, 121, 105, 115, 101, 101, 115, 97, 121, 111, 109, 121, 105, 101, 33]

#print (per_asc) 
#print (len(per_asc))

ASC = []                                # Λίστα περριτών μιας εγγραφής!!!!!! 
TIMES = []                              # Λίστα εμφάνισης των περριτών.

                                        
for i in range(len(per_asc)):           # ΠΡΟΣΟΧΗ ΕΡΩΤΗΣΗ!!!!!!!!          
    if per_asc[i] not in ASC:           ############################################################
        cnt = 0                         ############################################################
        x = per_asc.count(per_asc[i])
        cnt = x  
        ASC.append(per_asc[i])
        TIMES.append(cnt)

print (ASC)
print (TIMES)

suma = 0                                # Ο συνολίκος αριθμός όλων των περιττών χαρακτήρων του αρχείου ASCII,  
                                        # όπου βάση αυτού θα υπολογιστεί το ποσοστό του κάθε γράμματος !!!!!!!!

for i in range(len(TIMES)):             #  ΠΡΟΣΟΧΗ ΕΡΩΤΗΣΗ!!!!!!!!
    suma += TIMES[i]

z = f"Ο συνολίκος αριθμός όλων των περιττών χαρακτήρων του αρχείου : {suma}"
print(z)


POS = []

for i in range(len(TIMES)):
    x = (TIMES[i]*100)/suma            # Όπου suma: συνολίκος αριθμός όλων των περριτών χαρακτήρων του αρχείου ASCII.
    POS.append(x)

#print (POS)                            # Λίστα εμφάνισης ποσοστού κάθε γράμματος.

for i in range(len(POS)):              # Στρογγυλοποίηση προς τα πάνω.
    if POS[i] == int(POS[i]):
        POS[i] = POS[i]
    elif POS[i] < 1:
        POS[i] = 1
    elif POS[i]%int(POS[i]) <= 0.5 :
        POS[i] = int(POS[i]) + 1
    else:
        POS[i] = round(POS[i])      
#print (POS)

alpha = ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m']
ALPHA = ['A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']

per_alpha = []
per_ALPHA = []

for i in range(len(alpha)):            # Λίστα περιττών πεζών χαρακτήρων.
    if ord(alpha[i])%2 != 0:
        per_alpha.append(alpha[i])

for i in range(len(ALPHA)):            # Λίστα περιττών κεφαλαίων χαρακτήρων.
    if ord(ALPHA[i])%2 != 0:
        per_ALPHA.append(ALPHA[i])

#print(per_alpha)
#print(per_ALPHA)

for i in range(len(POS)):
    if chr(ASC[i]) in per_alpha or chr(ASC[i]) in per_ALPHA:
        print ((str(ASC[i])+ ' - ' + chr(ASC[i]) + ": " + "*"*POS[i] + ' ' + str(POS[i]) + '%')) # Στατιστικά εμφάνισης του κάθε γράμματος επί του συνόλου των περριτών  
                                                                                                # χαρακτήρων.
