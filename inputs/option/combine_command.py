import os

def combine(set1,set1_name, set2, set2_name):
    set_out=[]
    set_out_name=[]
    for i in range(len(set1)):
        set_out.append(set1[i])
        set_out_name.append(set1_name[i])
        for j in range(len(set2)):
            set_out.append(set1[i]+" "+set2[j])
            set_out_name.append(set1_name[i]+"_"+set2_name[j])
    for j in range(len(set2)):
        set_out.append(set2[j])
        set_out_name.append(set2[j])

    return set_out, set_out_name


# Liste pour stocker les noms de fichiers .txt
fichiers_txt = []
# Parcourir le dossier donné
for fichier in os.listdir("."):
    if fichier.endswith('.txt'):
        fichiers_txt.append(fichier)
print(fichiers_txt)

final_set = []
final_set_name = []
for name_fichier in fichiers_txt:
    with open(name_fichier, "r") as f:
        content = f.read()
    line_content = content.splitlines()
    set1=[x.split("/")[0] for x in line_content]
    set1_name=[x.split("/")[1] for x in line_content]
    final_set, final_set_name = combine(set1, set1_name, final_set, final_set_name)
    print(name_fichier)
to_write="option;option_name\n;only\n"
with open("options.csv", "w") as f:
    f.write(to_write)
    for i in range(len(final_set)):
        f.write(final_set[i]+";"+final_set_name[i]+"\n")
