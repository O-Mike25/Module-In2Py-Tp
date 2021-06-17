Mike={'ps':[12,12,12] ,'C':[13,13,13],'java':[14,14,14],'mbdd':[15,15,15]}
m_ps=Mike['ps'][0]+Mike['ps'][1]+Mike['ps'][2]/3
m_C=Mike['C'][0]+Mike['C'][1]+Mike['C'][2]/3
m_mbdd=Mike['mbdd'][0]+Mike['mbdd'][1]+Mike['mbdd'][2]/3
m_java=Mike['java'][0]+Mike['java'][1]+Mike['java'][2]/3
m= (m_ps+m_C+m_mbdd+m_java) /4
print("la moyenne de mon dictionnaire est" , m)