import os


path = r"C:\Users\jacky-lin\Desktop\0127 to Elsa"

files = os.listdir(path) #獲取資料夾路徑

serial_number = r"I3-220222"


print("開始重新命名檔案...\n")

for files in files: # 迭代输出所有文件和文件夹
    
    file_path = path + "\\" + files #檔案全路徑名稱
    
    root, extension = os.path.splitext(files) #分割檔名+副檔名

    file_name = root.split()[0].replace(".","")

    new_file_name = f"{serial_number}-{file_name}{extension}"

    new_file_path = path + "\\" + new_file_name


    if serial_number not in file_path and os.path.isfile(file_path) and extension != ".db":
        os.rename(file_path,new_file_path)
        print(f"原檔名為:{files}\n更新為:{new_file_name}\n")

        
    else:
        print("此檔案變更檔名異常或檔案不存在")


print("\n檔案名稱已全部變更完畢...")
  

    
    

    
