import os

pdf = dict()
mp4 = dict()
txt = dict()
print(os.walk("D:\Masaüstü"))

for road, file_list, dosya_list in os.walk("D:\Masaüstü"):
    for i in dosya_list:
        if i.endswith(".pdf"):

            pdf[i] = road

        elif i.endswith(".py"):

            mp4[i] = road

        elif i.endswith(".txt"):

            txt[i] = road

with open("pdf_dosyalari.txt", "w", encoding="utf-8") as file:
    for i, j in pdf.items():
        file.write("Dosya Direction {} Dosya Ismi: {}\n".format(j, i))

with open("txt_dosyalari.txt", "w", encoding="utf-8") as file1:
    for i, j in txt.items():
        file1.write("Dosya Direction {} Dosya Ismi: {}\n".format(j, i))

with open("mp4_dosyalari.txt", "w", encoding="utf-8") as file2:
    for i, j in mp4.items():
        file2.write("Dosya Direction {} Dosya Ismi: {}\n".format(j, i))