import os
import re
import googletrans
import requirement

location_documents = r"/home/r0h8n/Desktop/Test/sample/Documents"
ls2 = []
os.chdir("Documents/")
l = os.listdir()
for ls in l:
    a = os.path.splitext(ls)
    if a[1] == ".pdf":
        a = "".join(a)
        ls2.append(a)
        # requirement.check_dir(a)
for items in ls2:    
    if requirement.check_dir(items) == False:    
        i = 1
        with open("txt23.txt", "r") as f:
            for line in f:
                if "نوع الخدمة" in line:
                    line = line.split()
                    seven = line[3]
                    three = " ".join(line[6::])
                if "اسم الشارع" in line:
                    line1 = line.split()
                    eight = " ".join(line1[2::])
                if "درجة الأهمية" in line:
                    line2 = line.split()
                    nine = line2[2]
                if "اسم المقاول" in line:
                    ten = line  
                if "أمخالفة تشوه بصري" in line:
                    line3 = line.split()
                    twelve = " ".join(line3[1::])
                if "الزيارة الميدانية" in line:
                    eleven = line
                if "ملاحظات المهندس المشرف / المراقب" in line:
                    thirteen = line.split()
                    thirteen = " ".join(thirteen[5::])
                    if len(thirteen) == 0:
                        thirteen = "الموقع تابع لكم حسب الاختصاص"
                if "المراقب الميداتي" in line:
                    fourteen = line.split()
                    fourteen = " ".join(fourteen[3::])
                if "التاري" in line:
                    line = line.split(":")
                    line = line[0].split(" ")
                    zero = []
                    for e in line:
                        if e != "التاريخ":
                            zero.append(e)
                        else:
                            break
                    zero1 = " ".join(zero)
                i+=1
            four = "هبوط ترنش خدمات"
        f.close()
        with open("txt23_eng.txt", "r") as t:
            cont = t.read()
            patt1 = re.compile(r"\d{2}-\d{2}-\d{4}")
            matches = patt1.finditer(cont)
            i = 0
            for item in matches:
                if i != 0:
                    break
                one = item.group(0)
                i+=1
            patt2 = re.compile(r"\b\d{12} ")
            matches1 = patt2.finditer(cont)
            for item in matches1:
                two = item.group(0)
            patt3 = re.compile(r"(\d{2}-\d{2}-\d{4}) (\d{6})")
            matches3 = patt3.finditer(cont)
            for item in matches3:
                six = item.group(2)
            patt4 = re.compile(r"N:(\d{2}\.\d*) [_ ]*E:(\d{2}.\d*)")
            matches4 = patt4.finditer(cont)
            for item in matches4:
                five_a = item.group(2)
                five_b = item.group(1)
            patt5 = re.compile(r"900\d{4}")
            matches5 = patt5.finditer(cont)
            for item in matches5:
                fifteen = item.group(0)
        t.close()
        lst_to_append = [
            ['Content', requirement.get_trans(zero1), one, two, requirement.get_trans(three), requirement.get_trans(four), 'site location', five_a, five_b, six, requirement.get_trans(seven), requirement.get_trans(eight), 
            requirement.get_trans(nine), requirement.get_trans(ten), requirement.get_trans(eleven), requirement.get_trans(twelve), requirement.get_trans(thirteen), requirement.get_trans(fourteen), fifteen]
        ]
        requirement.append_csv(lst_to_append)
        requirement.append_txt(items)
        os.chdir(f"{location_documents}")




