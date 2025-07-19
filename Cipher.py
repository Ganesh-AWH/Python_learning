#encrypt Function
import string

def cesar(msg, shift, option):
    #check if we want to encode or decode
    if(option == "decode"):
        shift *= -1
    alphabets = list(string.ascii_lowercase)
    res = ""
    for i in msg:
        #get index of the msg letters and shift it  
        point = alphabets.index(i) + shift
        res += alphabets[point%26]
    return res
    
print('''
                                                                                                                   
    //   ) )                                                  //   ) )                                       
   //         ___      ___      ___      ___      __         //        ( )  ___     / __      ___      __    
  //        //   ) ) //___) ) ((   ) ) //   ) ) //  ) )     //        / / //   ) ) //   ) ) //___) ) //  ) ) 
 //        //   / / //         \ \    //   / / //          //        / / //___/ / //   / / //       //       
((____/ / ((___( ( ((____   //   ) ) ((___( ( //          ((____/ / / / //       //   / / ((____   //        
''')

while(True):
    option = input("Type 'encode' to encrypt and 'decode' to decrypt or Type 'exit' to end the program: ")
    if option == "exit":
        break
    text = input("Type your message: ").lower()
    shift = int(input("Type shift number: ")) 

    if option == "encode":
        enc_res = cesar(text, shift, option)
        print(enc_res)
    elif option == "decode":
        dec_res = cesar(text, shift, option)
        print(dec_res)
    else:
        print("Invalid text")