jmeno = input("zadejte jmeno:")
prijmeni = input("zadejte prijmeni:")

jmeno_upper = jmeno.upper()
jmeno_lower = jmeno.lower()
jmeno_title = jmeno.title()

prijmeni_upper = prijmeni.upper()
prijmeni_lower = prijmeni.lower()
prijmeni_title = prijmeni.title()

print(jmeno_upper + " " + prijmeni_upper)
print(jmeno_lower + " " + prijmeni_lower)
print(jmeno_title + " " + prijmeni_title)
print(f"{jmeno_upper [0]}. {prijmeni_upper [0]}.")

jmeno_length = len(jmeno)
if jmeno_length > 5:
    print(f"{jmeno_upper [0]}. {prijmeni_title}")
else: 
    print(f"{jmeno_title} {prijmeni_title}")