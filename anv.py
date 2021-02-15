förnamn = "Oskar"
efternamn = "Forsgren"

anvnamn = ""

anvrätt = "okrfrn"

anvnamn += förnamn[0]
anvnamn += förnamn[2]
anvnamn += förnamn[-1]
anvnamn += efternamn[0]
anvnamn += efternamn[2]
anvnamn += efternamn[-1]

anvnamn = anvnamn.lower()



if (anvrätt == anvnamn):
    print ("Jag är bäst och klarade uppgiften")
else:
    print("Jag får inte gå hem")