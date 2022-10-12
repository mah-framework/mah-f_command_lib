# https:/github.com/C0derByM4H6301

#a = "hello  serdar   anam"
a = " set  "
def comand_check(text):
  cmd_list = []
  print(text.split(" "))
  for i in text.split(" "):
    if i != "" and i and " " and i != '' and i != ' ':
      cmd_list.append(i)
  print(cmd_list)
  print(len(cmd_list))
  len_list = len(cmd_list)
  if len_list < 1:
    print("boş string")
  if len_list == 1:
    print("birinci komut")
    if cmd_list[0] == "set":
      print("set fonksiyonuşimdi çalışacak")
      if len_list < 2:
        print("değişken yok")
comand_check(a)
