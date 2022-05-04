import os


path = r"C:\Users\jacky-lin\Desktop\新增資料夾"
path = input("請輸入要變更名稱之目錄完整路徑:\n")

files = os.listdir(path) #獲取資料夾路徑

serial_number = r"CMD-220317"

serial_number  = input("請輸入要變更之序列號:\n")

count = 1
fail_count = 1
file_name_count = 1

print("開始重新命名檔案...\n")

for files in files: # 迭代输出所有文件和文件夹
    
    file_path = path + "\\" + files #檔案全路徑名稱
    
    root, extension = os.path.splitext(files) #分割檔名+副檔名

    file_name = root.split()[0].replace(".","")

    new_file_name = f"{serial_number}-{file_name}{extension}"

    new_file_path = path + "\\" + new_file_name

    new_file_path_2 = path + "\\" + f"{serial_number}-{file_name} ({file_name_count}){extension}"

    
    if os.path.exists(new_file_path):
        print(f"{count}.變更檔案名稱重複")
        print(f"  更改名稱為:{serial_number}-{file_name} ({file_name_count}){extension}\n")
        os.rename(new_file_path,new_file_path_2)

        file_name_count += 1

        count +=1
        
    if serial_number not in file_path and os.path.isfile(file_path) and extension != ".db":
        
        os.rename(file_path,new_file_path)
        
        print(f"{count}. 原檔名為:{files}\n    更新為: {new_file_name}\n")
        count += 1
        
    else:
        print(f"{fail_count}. 此檔案變更檔名異常或檔案不存在")
        fail_count += 1

print("\n檔案名稱已全部變更完畢...")

input("請點擊任意鍵關閉程式:\n")


  

    
    


