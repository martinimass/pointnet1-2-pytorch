import os, glob

base_path = "../data/arch-original/"    # Folder containing original data
out_path = "../data/arch-conv/"         # Folder for converted data
meta_path = "../data_utils/meta_arch/"  # "meta" folder for the converted data

os.makedirs(out_path,exist_ok=True)
os.makedirs(meta_path,exist_ok=True)

labels = ["arc",
    "column",
    "moulding",
    "floor",
    "door-window",
    "wall",
    "stairs",
    "vault",
    "roof",
    "other" ]

scenes = [
    "Training/1_TR_cloister.txt",
    "Training/2_TR_church.txt",
    "Training/3_VAL_room.txt",
    "Training/4_CA_church.txt",
    "Training/5_SMV_chapel_1.txt",
    "Training/6_SMV_chapel_2to4.txt",
    "Training/7_SMV_chapel_24.txt",
    "Training/8_SMV_chapel_28.txt",
    "Training/9_SMV_chapel_10.txt",
    "Training/10_SStefano_portico_1.txt",
    "Training/11_SStefano_portico_2.txt",
    "Training/12_KAS_pavillion_1.txt",
    "Training/13_KAS_pavillion_2.txt",
    "Training/14_TRE_square.txt",
    "Training/15_OTT_church.txt",
    "Test/A_SMG_portico.txt",
    #"Test/B_SMV_chapel_27to35.txt"     # I have to choose only one test scene
    ]

mapping = []
annotations = []

print("Founded {} scenes...".format(len(scenes)))
for i,scena in enumerate(scenes):
    base = os.path.basename(scena)
    name = "Area_"+str(i+1)
    mapping.append((base,name))
    dizio={}
    folder_path = out_path + name + "/"
    os.makedirs(folder_path,exist_ok=True)
    folder_path = folder_path + name + "/"
    os.makedirs(folder_path, exist_ok=True)

    print(name,"-",base)
    print(" - Loading...")
    with open(base_path+scena,"r") as fr:
        for l in fr:
            x, y, z, r, g, b, label, _, _, _ = l.strip().split(" ")
            if label not in dizio:
                dizio[label] = []
            dizio[label].append([x,y,z,r,g,b])

    annotations_path = folder_path + "Annotations/"
    os.makedirs(annotations_path, exist_ok=True)
    annotations.append("{}/{}/{}".format(name, name, "Annotations"))
    print(" - Saving...")
    with open(folder_path+name+".txt", "w") as ftot:

        for k in sorted(dizio.keys()):
            print("   -"+labels[int(k)])
            label_path = annotations_path + labels[int(k)]+"_1.txt"
            with open(label_path, "w") as fl:
                points = dizio[k]
                for p in points:
                    row = "{} {} {} {} {} {}\n".format(p[0],p[1],p[2],p[3],p[4],p[5])
                    fl.write(row)
                    ftot.write(row)

# Mapping between original scenes and created Areas
print("\nMapping:")
with open(out_path+"mapping.txt", "w") as fw:
    for m,n in mapping:
        fw.write("{} {}\n".format(m,n))
        print("{} {}\n".format(m,n))



# meta/anno_paths.txt
with open(meta_path+"anno_paths.txt", "w") as fanno:
    for a in annotations:
        fanno.write(a+"\n")

# meta/class_names.txt
with open(meta_path+"class_names.txt","w") as fw:
    for l in labels:
        fw.write("{}\n".format(l))

print("Done")

