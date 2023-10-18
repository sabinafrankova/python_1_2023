import json
with open("ukol_3_body.json", "r") as soubor: seznam_studentu = json.load(soubor)

hodnoceni = {}
for student, body in seznam_studentu.items():
    hodnoceni[student] = "Prosel" if body > 59 else "Neprosel"

with open('ukol_3_hodnoceni.json', 'w') as soubor: json.dump(hodnoceni, soubor)
print("PROVEDENO")

#nevím si rady s tím, že se mi diakritika v tom ukol_3_hodnoceni.json mění na jakési podivné "kódy" :((