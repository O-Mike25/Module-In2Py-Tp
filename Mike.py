#exercice sur calcul de moyenne
Mike={'ps':[12,12,12] ,'C':[13,13,13],'java':[14,14,14],'mbdd':[15,15,15]}
m_ps=Mike['ps'][0]+Mike['ps'][1]+Mike['ps'][2]/3
m_C=Mike['C'][0]+Mike['C'][1]+Mike['C'][2]/3
m_mbdd=Mike['mbdd'][0]+Mike['mbdd'][1]+Mike['mbdd'][2]/3
m_java=Mike['java'][0]+Mike['java'][1]+Mike['java'][2]/3
m= (m_ps+m_C+m_mbdd+m_java) /4
print("la moyenne de mon dictionnaire est" , m)

#exercice E0
list=[1,2,3,4,5,6,7,8,9,10]
list1=[23,24]
list[0]=list[0]+11
list[1]=list[1]+11
list[2]=list[2]+11
list[3]=list[3]+11
list[4]=list[4]+11
list[5]=list[5]+11
list[6]=list[6]+11
list[7]=list[7]+11
list[8]=list[8]+11
list[9]=list[9]+11 
list.append(22)
list.extend(list1)
L1=list[0:14:2]
L2=list[1:14:2]
print("list:",list)
list.pop(3)
print("L1:",L1)
print("L2:",L2)
print("list:",list)


#exercice E1
d={'nom':'Dupuis','prenom':'Jacque','age':30}

#a) Correction de l'erreur
d['prenom']='Jacques'

#b) Affichage de la liste des cles du dictionnaire
d.keys()

#c) Affichage de la liste des valeurs du dictionnaire
d.values()

#d) Affichage de la liste des paires cle/valeur du dictionnaire
print("nom",d['nom'],"  ", "age",d['age'])

#e) Ecriture de la phrase "Jacques Dupuis a 30 ans"
print(d['prenom'],d['nom'],"a",d['age'],"ans")