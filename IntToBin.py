from stack import Stack

def convert_int_to_bin(dec_num):
  s = Stack()
  while (dec_num != 0):
    num = dec_num%2
    s.push(num)
    dec_num = dec_num//2
  string = ""
  while (not s.is_empty()):
    string = string + str(s.pop())
  return string


d = convert_int_to_bin(93)
print(d)