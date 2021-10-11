def gemiddeldeSNelheid(afstand,tijd):
   return afstand/tijd

#done --> is voor gemakkelijker te zien waar de functie stopt

def Verschil_A_B(A,B):
   return A - B

#done

def gemSnelheden(TijdList, PositieList):
   FirstObject = 0
   secondobject = 1
   GemiddeldeSnelheidsLIST = []
   TijdGemSnelLIST = []

   for Eind_tijd, Eind_pos in zip(TijdList[secondobject:len(TijdList)], PositieList[secondobject:len(PositieList)]):
       Begin_tijd = TijdList[FirstObject]
       Begin_positie = PositieList[FirstObject]
       GemiddeldeSnelheidsLIST.append(
           gemiddeldeSNelheid(
               Verschil_A_B(Eind_pos,Begin_positie),Verschil_A_B(Eind_tijd,Begin_tijd)))
       TijdGemSnelLIST.append((Eind_tijd+Begin_tijd)/2)
       FirstObject += 1

   return GemiddeldeSnelheidsLIST, TijdGemSnelLIST

#done

def versnelling(TijdLIST, PositieLIST):
   GemiddeldeSnelheidsLIST , TijdGemSnelLIST = gemSnelheden(TijdLIST,PositieLIST)

   FirstObject = 0
   SecondObject = 1

   VersnellingsLIST = []
   TijdVersLIST = []
   for Eind_tijd,Eind_snelheid in zip(TijdGemSnelLIST[SecondObject:len(TijdGemSnelLIST)],GemiddeldeSnelheidsLIST[SecondObject:len(GemiddeldeSnelheidsLIST)]):
       Begin_tijd = TijdGemSnelLIST[FirstObject]
       Begin_snelheid = GemiddeldeSnelheidsLIST[FirstObject]
       VersnellingsLIST.append(
           gemiddeldeSNelheid(
               Verschil_A_B(Eind_snelheid,Begin_snelheid),Verschil_A_B(Eind_tijd,Begin_tijd)))
       TijdVersLIST.append((Eind_tijd+Begin_tijd)/2)
       FirstObject += 1

   return  VersnellingsLIST,TijdVersLIST

#done

def StriktMeesten(TijdLIST, PositieLIST):
    Snelheden , tijd = gemSnelheden(TijdLIST, PositieLIST)
    negatieven = 0

    for snelheid in Snelheden:
        if snelheid < 0:
            negatieven += 1

    if negatieven > (len(Snelheden)/2):
        return True
    else:
        return False

#done

def Valversnelling(TijdLIST, PositieLIST):
    versnellingen, tijden = versnelling(TijdLIST, PositieLIST)
    return [snel for snel in versnellingen if abs(snel) > 9.81]

#testcode begint hier

TijdLIST = [1,2,3,4,5]
PostitieLIST = [1,2,15,50,100]


#testcommand
print(Valversnelling(TijdLIST, PostitieLIST))
