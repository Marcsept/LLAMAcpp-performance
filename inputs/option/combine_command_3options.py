import os

def combine(set1,set1_name, set2, set2_name):
    set_out=[]
    set_out_name=[]
    for i in range(len(set1)):
        for j in range(len(set2)):
            set_out.append(set1[i]+" "+set2[j])
            set_out_name.append(set1_name[i]+"_"+set2_name[j])
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
for i in range(len(fichiers_txt)):
    with open(fichiers_txt[i], "r") as f:
        content = f.read()
        line_content = content.splitlines()
        set1=[x.split("/")[0] for x in line_content]
        set1_name=[x.split("/")[1] for x in line_content]
    f.close()
    
    for j in range(len(fichiers_txt)):
        if(j>i):
            with open(fichiers_txt[j], "r") as f:
                content = f.read()
                line_content = content.splitlines()
                set2=[x.split("/")[0] for x in line_content]
                set2_name=[x.split("/")[1] for x in line_content]
                f.close()
            combine2_set, combine2_set_name = combine(set1, set1_name, set2, set2_name)
            #final_set, final_set_name = final_set + combine2_set, final_set_name + combine2_set_name 
            for k in range(len(fichiers_txt)):
                if(k>j):
                    with open(fichiers_txt[k], "r") as f:
                        content = f.read()
                        line_content = content.splitlines()
                        set2=[x.split("/")[0] for x in line_content]
                        set2_name=[x.split("/")[1] for x in line_content]
                        f.close()
                    combine3_set, combine3_set_name = combine(combine2_set, combine2_set_name, set2, set2_name)
                    final_set, final_set_name = final_set + combine3_set, final_set_name + combine3_set_name 

    #final_set, final_set_name = final_set +  set1, final_set_name + set1_name 
    
    print(fichiers_txt[i])
to_write="option;option_name\n ;only\n"
with open("options.csv", "a") as f:
    f.write(to_write)
    for i in range(len(final_set)):
        f.write(final_set[i]+";"+final_set_name[i]+"\n")
