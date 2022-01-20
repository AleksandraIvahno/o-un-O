text = input("Ievadi tekstu:")
def replace0 (text):
  if text.count("o")>0 or text.count("O")>0:
    text = text.replace("o","%")
    text = text.replace("O","%")
  else:
    text = "nav burtu O vai o"
  return text
print(replace0(text)) 