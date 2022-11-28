import os
import googletrans
import time
import csv


trans = googletrans.Translator()
dirs = []

def get_trans(a):
    b = trans.translate(a, dest ='en')
    return b.text

def run_command(name_pdf):
    os.chdir(r"/home/r0h8n/Desktop/Test/sample")
    os.system(fr"pdftoppm -jpeg ~/Desktop/Test/sample/Documents/{name_pdf} new12")
    time.sleep(1)
    os.system(r"tesseract new12-1.jpg txt23 -l ara --dpi 600")
    time.sleep(1)
    os.system(r"tesseract new12-1.jpg txt23_eng -l eng --dpi 600")

def append_csv(rown):
    os.chdir(r"/home/r0h8n/Desktop/Test/sample")
    with open("Book-v2.csv", "a+") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(rown)
        # for line in reader:
            # print(line)
    file_csv.close()
# append_csv()

def check_dir(fl_name):
    os.chdir("/home/r0h8n/Desktop/Test/sample/Documents")
    with open("list.txt", "r") as tx:
        for line in tx:
            dirs.append(line[:-1])
        # print(dirs)
        if fl_name in dirs:
            print(f"{fl_name}  in directory")
            return True
        else:
            run_command(fl_name)
            # translate_main()
            # lst_to_append = [
                # ['Content', requirement.get_trans(zero1), one, two, requirement.get_trans(three), requirement.get_trans(four), 'site location', five_a, five_b, six, requirement.get_trans(seven), requirement.get_trans(eight), 
                # requirement.get_trans(nine), requirement.get_trans(ten), requirement.get_trans(eleven), requirement.get_trans(twelve), requirement.get_trans(thirteen), requirement.get_trans(fourteen), fifteen]
                # ]
            tx.close()
            # append_csv(lst_to_append)
            # append_txt(fl_name)
            return False

def append_txt(name):
    os.chdir("/home/r0h8n/Desktop/Test/sample/Documents")
    with open("list.txt", "a") as txe:
        txe.write(f"\n{name}")



