# https:/github.com/C0derByM4H6301

a = "hello  serdar   anam"
def comand_check(text):
  cmd_list = []
  print(text.split(" "))
  for i in text.split(" "):
    if i != "" and i and " " and i != '' and i != ' ':
      cmd_list.append(i)
  print(cmd_list)
comand_check(a)
