# Initale Variablen
steuersatz = ""

# Versuche eine Float-Eingabe
try:
    preis = float(input("Preis: "))
except:
    # Die Umwandlung in einen Float hat nicht geklappt
    print ("Das war keine Zahl")
    exit()

umsatz_reduziert = input("Nehmen Sie das Essen mit nach Hause? (J/N): ")

# Verarbeitung
if umsatz_reduziert == "J" or umsatz_reduziert == "j":
    netto = preis / 1.07
    steuersatz = "7%"
elif umsatz_reduziert == "N" or umsatz_reduziert == "n":
    netto = preis / 1.19
    steuersatz = "19%"
else:
   print("Fehler bei der Eingabe")

# Ausgabe
if steuersatz != "":
    print(f"Netto {netto:.2f} Euro bei einem Steuersatz von {steuersatz}")
