import os

path = "english"
files = os.listdir(path)
os.makedirs("simp_chinese")

for file in files :
    target = open("simp_chinese/"+file.replace("english", "simp_chinese"), 'w', encoding = "utf_8_sig")
    source = open("english/"+file, encoding = "utf_8_sig")

    lines = source.readlines()
    for line in lines :
        target.writelines(line.replace("l_english", "l_simp_chinese"))

    target.close()
    source.close()
