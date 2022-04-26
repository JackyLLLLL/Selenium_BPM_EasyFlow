import openpyxl
from openpyxl import load_workbook

file_path = r"C:\Users\jacky-lin\Dropbox\Elsa+Kevin\terminator 备品报价单(1)220414.xlsx"

wb = load_workbook(file_path)
sheet = wb['Sheet1']


component = sheet["B3:B17"]
package = sheet["E3:E17"]
part_number = sheet["D3:D17"]

subject = [] #流程主旨
components = [] 
part = []
product_description = [] #產品描述
part_num = []
customer_notice = [] #客戶要求生產注意事項填寫

for component in component:
    for value in component:
        
        result= value.value
        components.append(result)
        result = f"COUGAR電競椅 Terminator 備品-{result}料號申請"
        subject.append(result)

for package in package:
    for value in package:
        
        result = value.value
        part.append(result)

for i in range(len(part)):
    
    product_description.append(f"COUGAR電競椅 Terminator 備品-{components[i]}{part[i]} 單個報價 COUGAR")


for part_number in part_number:
    for value in part_number:

        result = value.value
        part_num.append(result)

for i in range(len(part)):
    
    customer_notice.append(f"此為{product_description[i]}(洪晟)\n備品料號申請\n請編為{part_num[i]}\n")



for i in range(len(part)):
    x = (f"{subject[i]}\n\n{product_description[i]}\n\n{customer_notice[i]}\n")
    print(x)
