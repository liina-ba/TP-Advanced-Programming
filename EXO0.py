
def calculateTaxis():
    people = int(input("How many people need a ride? "))
    taxiCapacity = int(input("How many people fit in one taxi?"))

    nbTaxis = people//taxiCapacity
    rmd = people % taxiCapacity

    if rmd>0 :
        nbTaxisTotal = nbTaxis + 1
    else:
        nbTaxisTotal = nbTaxis

    print(f"Number of taxis needed: {nbTaxisTotal}")

calculateTaxis()



