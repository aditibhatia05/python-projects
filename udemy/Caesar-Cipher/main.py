alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_decrypt(text, shift, direction):
  list_of_char=list(text)
  length_text=len(list_of_char)
  for i in range(0,length_text):
    for j in range(0, len(alphabet)):
      if(list_of_char[i]==alphabet[j]):
        if(direction=='encode'):
          key=(j+shift)%len(alphabet)
        else:
          if(direction=='decode'):
            key=(j-shift)%len(alphabet)
        list_of_char[i]=alphabet[key]
        i=i+1
        break
      else:
        j=j+1
  cipher=''.join(list_of_char)
  print(f"Result text is: {cipher}")

choice='y'
while (choice=='y'):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if(direction != 'encode' and direction != 'decode'):
    print("Invalid input. Try again")
    continue
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if(shift<0):
    print("Invalid input. Try again")
    continue
  encrypt_decrypt(text, shift, direction)
  
  choice=input("Do you want to continue? (y/n) ").lower()