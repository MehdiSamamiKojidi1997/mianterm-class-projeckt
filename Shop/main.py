import json
import sqlite3
cnt = sqlite3.connect('myshop.db')
# class cars:
#     def __init__(self,colour,company):
#         self.colour=colour
#         self.company=company
#     def showdata(self):
#         print(f"company:{self.company},colour:{self.colour}")
#
#
#
# #--------------------------------------
# car1=cars("red","BMW")
# car1.showdata()
# class files:
#     def __init__(self,filename):
#         self.filename=fn
#     def fwrite(self):
#         text=input("enter a text:")
#         with open(self.filename,"w") as f:
#             f.write(text)
#             print("saved!")
# #-------------------------
# f1=files("doc.txt")
# class A:
#     def f1(self):
#         print("f1 is running...")
# with open("sample.json","w") as f:
#     x=json.dump({"5":"ali"},f)

# ID = 5
# dct={}
# sql = f'''SELECT pid,number FROM cart WHERE uid={ID}'''
# lst = (cnt.execute(sql)).fetchall()
# for item in lst:
#     dct[f"{item[0]}"]="sample"
# for k,v in dct.items():
#     v = 0
#     for item in lst:
#         if item[0]==int(k):
#             v+=item[1]
#             dct[k]=v
#
# print(dct)
# print(lst)


