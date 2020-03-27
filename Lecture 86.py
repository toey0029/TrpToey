import csv

def demo1():
    with open("../CP3_Teerapob_Homdok/saveHomeWork.csv", "w", newline="", encoding="utf8") as f:
        fw = csv.writer(f)
        fw.writerow(["ชื่อเพื่อน", "ภาพยนต์ที่ชอบ", "สัตว์เลี้ยงที่ชอบ"])
        fw.writerow(("นม", "น้องพี่ที่รัก", "หมา"))
        fw.writerow(["เตย", "นายฉุกเฉิน", "หมา"])
        fw.writerow(["กร", "star teak", "หมา"])


demo1()