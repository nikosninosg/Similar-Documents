#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import math
import os,sys
import itertools
from os import listdir
from os.path import isfile, join
from collections import Counter
import collections
from operator import itemgetter  

print("Kαλωσήρθες στο πρόγραμμα για την ομοιότητα κειμένων.")
print("Βάλε στο φάκελο TxtDocs τα κείμενα σου και μετά πάτα ENTER για να συνεχίσεις.")


while True:
 input("")
 break


N=int(input("Δώσε τον αριθμό των αρχείων του φακέλου TxtDocs: N="))
K=int(input("Δώσε τον αριθμό που θέλεις να εμφανίσεις για τα Κ πιο όμοια κείμενα του φακέλου TxtDocs. K="))
print("\n")

#files into myList
myList = [f for f in listdir("TxtDocs") if isfile(join("TxtDocs", f))]



#sinartisi gia ta pairs ths listas
def pairsList(lista):
 result = []
 for L1 in range(len(lista)):
  for L2 in range(L1+1,len(lista)):
   result.append([lista[L1],lista[L2]])
 return result

pairingsList=[]
pairingsList = pairsList(myList) #pairs into list
#print("%d pairingsList" % len(pairingsList)) #arithmos pairs



def omoiot_sinimit(Doc_1,Doc_2):

 #----diaxorismos(Doc_1)----
 text=open(Doc_1).read().split()
 #lower() giati mporei na yparxoun kefalaia stin idia leji kai den 8a tairiazoun
 values1=[word.lower() for word in text]
 #metritis omoiwn lexewn
 Dic_1=Counter(values1)
 #print(Dic_1)


 #----diaxorismos(Doc_2)----
 text=open(Doc_2).read().split()
 #lower() giati mporei na yparxoun kefalaia stin idia leji kai den 8a tairiazoun
 values2=[word.lower() for word in text] 
 Dic_2=Counter(values2)
 #print(Dic_2)


 #dic_1 * dic_2 -> dic_1
 #polaplasiasmos values() me idio key() kai kataxwrisi sto Dic_1
 multi_dic1={k: Dic_1[k]*Dic_2[k] for k in Dic_1}
 
 #lista timwn tou lexikou Dic_1
 val1=Dic_1.values()
 


 #---omoiws gia to Dic_2
 multi_dic2={k: Dic_1[k]*Dic_2[k] for k in Dic_2}
 val2=Dic_2.values()
 

 #ginomeno dianysmatwn d1*d2
 athrisma=sum(Dic_1[k]*Dic_2[k] for k in Dic_1)
 #print("athrisma={}".format(athrisma))


 #norm_d1
 D1=[a*a for a,a in zip(val1,val1)] #polaplasiasmow stoixeiwn
 norm_d1=(sum(D1))**(0.5) #norma=prosthesi stoixeiwn + riza
 
 #norm_d2
 D2=[a*a for a,a in zip(val2,val2)]  
 norm_d2=(sum(D2))**(0.5)

 
 z=(athrisma/(norm_d1*norm_d2)) #z=cos(d1,d2)
 #print("cos(d1,d2)={:.3} or {:.3}%".format(z,z*100))
 
 Docs=Doc_1+"-"+Doc_2
 return Docs,z



#----main----


#to programma mpainei sto fakelo TxtDocs gia na vlepei ta arxeia
os.chdir('TxtDocs')

dictionary={}
pososta_list=[]

#gia ka8e stoixio tis listas(poy ta stoixia einai zeugh) kalese th sinartisi:
for pair in pairingsList:
 documents,pososta=omoiot_sinimit(pair[0],pair[1])
 dictionary[documents]=pososta

counter=0

print("Οι {} πρώτοι συνδυασμοί όμοιων αρχείων είναι:".format(K))
#tajinomisi lexikoy me basi thn timh
for key, value in sorted(dictionary.items(), key = itemgetter(1), reverse = True):
 while counter<K:
  print("Τα κείμενα: {}, με ποσοστό ομοιότητας={:.3}%".format(key, value*100))
  counter+=1
  break