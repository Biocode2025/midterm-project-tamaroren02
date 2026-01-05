import random
Halobacterium_salinarum=open('data/Halobacterium_salinarum','r')#פתיחת הקבצים של כל האורגניזמים
Halobacterium_noricense=open('data/Halobacterium_noricense','r')
Haloarcula_vallismortis=open('data/Haloarcula_vallismortis','r')
Thermus_thermophilus=open('data/Thermus_thermophilus','r')
Thermus_aquaticus=open('data/Thermus_aquaticus','r')
Shewanella_oneidensis=open('data/Shewanella_oneidensis','r')
Shewanella_violacea=open('data/Shewanella_violacea','r')
#פונקציות#
#פונקציה שמעבירה את תוכן הקובץ לרשימה#
def from_file_to_list (file):
  file_list=[]
  for line in file:
    if line.startswith(">"):#מדלג על השורה הראשונה
      continue
    else:
      for i in line:
        file_list.append(i)
  return file_list
  
#פוקציה שסופרת כמה פעמים מופיעה כל אחת מחומצות האמינו ברצפי החלבונים#
def aminoacid_counter (protein):
  aminoacid_total=len(protein)
  counter = {}
  for i in protein:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
  precent={}
  for a in counter:
    precent_calculation= (counter[a]/aminoacid_total)*100
    precent[a] = precent_calculation
  return precent
#פונקציה שמדפיסה את התוצאות הסופיות#
def printing(name,precent):
  Organism_name=name
  first_line= "Organism name" + "\t"
  second_line= Organism_name
  for i in precent:
    first_line += i + "\t"
    precentage=precent[i]
    second_line += f"  {precentage:.1f}%  "
  print(first_line)
  print(second_line)
  return first_line , second_line
#תוכנית ראשית#
#שימוש בפונקציות עבור כל אורגניזם#
#Halobacterium salinarum#
Halobacterium_salinarum_list = from_file_to_list(Halobacterium_salinarum)
Halobacterium_salinarum_precent = aminoacid_counter(Halobacterium_salinarum_list)
Halobacterium_salinarum_name = "Halobacterium salinarum"
print_Halobacterium_salinarum=printing(Halobacterium_salinarum_name,Halobacterium_salinarum_precent)
print()
print("-----------------------------------------------------------------------------------")
print()

#Halobacterium_noricense#
Halobacterium_noricense_list=from_file_to_list(Halobacterium_noricense)
Halobacterium_noricense_precent=aminoacid_counter(Halobacterium_noricense_list)
Halobacterium_noricense_name="Halobacterium noricense"
print_Halobacterium_noricense=printing(Halobacterium_noricense_name,Halobacterium_noricense_precent)
print()
print("-----------------------------------------------------------------------------------")
print()

#Haloarcula_vallismortis#
Haloarcula_vallismortis_list=from_file_to_list(Haloarcula_vallismortis)
Haloarcula_vallismortis_precent=aminoacid_counter(Haloarcula_vallismortis_list)
Haloarcula_vallismortis_name="Haloarcula vallismortis"
print_Haloarcula_vallismortis=printing(Haloarcula_vallismortis_name,Haloarcula_vallismortis_precent)
print()
print("-----------------------------------------------------------------------------------")
print()

#Thermus_thermophilus#
Thermus_thermophilus_list=from_file_to_list(Thermus_thermophilus)
Thermus_thermophilus_precent=aminoacid_counter(Thermus_thermophilus_list)
Thermus_thermophilus_name="Thermus thermophilus"
print_Thermus_thermophilus=printing(Thermus_thermophilus_name, Thermus_thermophilus_precent)
print()
print("-----------------------------------------------------------------------------------")
print()

#Thermus_aquaticus#
Thermus_aquaticus_list=from_file_to_list(Thermus_aquaticus)
Thermus_aquaticus_precent=aminoacid_counter(Thermus_aquaticus_list)
Thermus_aquaticus_name="Thermus aquaticus"
print_Thermus_aquaticus=printing(Thermus_aquaticus_name,Thermus_aquaticus_precent)
print()
print("-----------------------------------------------------------------------------------")
print()

#Shewanella_oneidensis#
Shewanella_oneidensis_list=from_file_to_list(Shewanella_oneidensis)
Shewanella_oneidensis_precent=aminoacid_counter(Shewanella_oneidensis_list)
Shewanella_oneidensis_name="Shewanella oneidensis"
print_Shewanella_oneidensis=printing(Shewanella_oneidensis_name,Shewanella_oneidensis_precent)
print()
print("-----------------------------------------------------------------------------------")
print()

#Shewanella_violacea#
Shewanella_violacea_list=from_file_to_list(Shewanella_violacea)
Shewanella_violacea_precent=aminoacid_counter(Shewanella_violacea_list)
Shewanella_violacea_name="Shewanella violacea"
print_Shewanella_violacea=printing(Shewanella_violacea_name,Shewanella_violacea_precent)

#סגירת הקבצים#
Halobacterium_salinarum.close()
Halobacterium_noricense.close()
Haloarcula_vallismortis.close()
Thermus_thermophilus.close()
Thermus_aquaticus.close()
Shewanella_oneidensis.close()
Shewanella_violacea.close()
