import os

path = r"C:\Users\jacky-lin\Desktop\韓文修改測試檔案"

files = os.listdir(path)

count = 1
file_name_count = 1
fail_count = 1
new_file_name = ""

for files in files:# 迭代输出所有文件
     file_path = path + "\\" + files #檔案全路徑名稱
     file_name = file_path.split('\\')[-1]
     old_file_name = file_name
     file_name = file_name.split()

     for word in file_name:
         
         if  word.isalpha():
             new_word = word
             file_name.remove(new_word)
     
     for x in file_name:
         
         if x.isalpha():
             new_x = x
             file_name.remove(new_x)
     
     for new_x in file_name:

          if new_x.isalpha():
               new_y = new_x
               file_name.remove(new_y)
             
     new_file_name = ' '.join(file_name)
     new_file_path = path + "\\" + new_file_name
     old_file_path =  path + "\\" + old_file_name
     new_file_path_2 = path + "\\" + new_file_name  +" "+"("+str(file_name_count)+")"


     if os.path.exists(new_file_path):
         print(f"{count}.變更檔案名稱重複")
##         print(f"  更改名稱為:{new_file_name} ({file_name_count})\n")
##         os.rename(new_file_path,new_file_path_2)

         file_name_count += 1

         count += 1

     elif os.path.isdir(old_file_path):
        os.rename(old_file_path,new_file_path)
        print(f"{count}. 原檔名為:{old_file_name}\n    更新為: {new_file_name}\n")
        count += 1

     else:
        print(f"{fail_count}. 此檔案變更檔名異常或檔案不存在")
        fail_count += 1

print("\n檔案名稱已全部變更完畢...")

