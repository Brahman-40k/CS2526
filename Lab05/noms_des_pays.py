uio = input("Enter the name of the country (in french): ")
result = ""
vowels = "aieouAIEOU"
exceptions = "belize cambodge mozambique zaire zimbabwe"

if uio[0] in vowels:
    result = result + "L'" + uio
    print(result)
    # feminine nations end with e
if uio[-1] == "e" and uio.lower() not in exceptions:
    result = result + "La " + uio
    print(result)
if uio.lower() == "etats-unis" or uio.lower() == "pays-bas":
    result = result + "Les " + uio
    print(result)
if uio.lower() in exceptions:
    print("le " + uio)
else:
    result = result + "Le " + uio
