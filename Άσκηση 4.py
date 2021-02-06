# Άσκηση 4. Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και να το κόβει σε
# συνεχόμενες τριάδες λέξεων (όλες τις δυνατές). Στην συνέχεια, διαλέγει τυχαία μια τριάδα και προσπαθεί να συντάξει ένα
# τυχαίο κείμενο από αυτό, χρησιμοποιώντας τις δυο τελευταίες λέξεις και επιλέγοντας μια τριάδα που να ξεκινάει από αυτές
# τις δυο. Το πρόγραμμα ολοκληρώνεται, όταν γράψει 200 λέξεις ή δεν μπορεί να επιλεγχεί άλλη τριάδα λέξεων.


import string
z = string.ascii_letters

#print(z)

alBet = [' ']
for i in range(len(z)):
    alBet.append(z[i])

#print(alBet)


with open("read_ASCII.txt", "r") as f:  # read_me  # DEMO 4 # DEMO 9 # read_ASCII  # read_me  # two_cities_ascii
          d = f.readlines()          

#print(d)

splt = []

for i in range(len(d)):              # split.
    for j in range(len(d[i])):
        splt.append(d[i][j])

print(splt)        

clean = []                           # Λίστα χωρίς σύμβολα π.χ (!@#*,....)

for i in range(len(splt)):
    if splt[i] in alBet:
        clean.append(splt[i])
#print(clean)                        # Χωρίς σύμβολα π.χ (!@#*,....)  

mrg = ''.join(clean)                 # Συνένωση σε string.

#print (mrg)                         # Το string σε λίστα.
L = mrg.lower()                      # Όλοι οι χαρακτήρες γίνονται πεζοί.
#print (L)
LIST = L.split()                     # LIST = mrg.split()

#print(LIST)                      

LIST_3 = []
L_3 = []
cnt = 0

for i in range(len(LIST)-2):
    for j in range(cnt,cnt+3):
        L_3.append(LIST[j])
    cnt +=1
    LIST_3.append(L_3)               # Λίστα με λίστες από, ['τριάδες', 'λέξεων', 'κειμένου']
    L_3 = []
    
#print(LIST_3)                   

############################################################################################################################

NEW = []                             # ΛΊΣΤΑ για να φτιάξουμε το κείμενο.
import random
random.shuffle(LIST_3)               # Για την επιλογή μίας τυχαίας τριάδας από την ΛΙΣΤΑ. 

for i in range(1):                                  
    x =  LIST_3[i]                                

z = f"Η τυχαία τριάδα (x) είναι : {x}"
print(z)

for word in x:                       # Εγγραφή της τυχαίας τριάδας.
    NEW.append(word)
    
#################################################################################################

found = False

while len(NEW) < 200 and not found:  # (and not found) : ή δεν μπορεί να επιλεγχεί άλλη τριάδα λέξεων.
    temp = [] 
    for i in range(len(LIST_3)):
        if (x[1] == LIST_3[i][0] and x[2] == LIST_3[i][1]):
                temp.append(LIST_3[i])
    #z = f"H temp είναι: {temp}"            
    #print(z)
    
    if temp != []:
        random.shuffle(temp)         # τυχαία επιλογή απο τις τριάδες.
        for i in range(1):
            x = temp[i]
            #z = f"Η καινούργια τυχαία τριάδα είναι : {x}"
            #print(z)
            NEW.append(x[2])
            temp = []
            found = False
    else:
        found = True
        
            
##################################################################################################


z = f"Το μήκος του κειμένου είναι : {len(NEW)}"
print(z)

text = ''

for i in range(len(NEW)):
    text += NEW[i]
    if NEW[i] != -1:
        text += ' '

z = f"Εμφάνιση του κειμένου : {text}"        
print(z)                            # Εμφάνιση του κειμένου.
        









