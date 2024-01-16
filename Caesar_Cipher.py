alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Scrie 'encode' ca sa encriptezi si 'decode' ca sa decriptezi:\n")
text = input("Mesaj: ").lower()
shift = int(input("Nr pt shift: "))
def encrypt(text, shift):
    cipher_text=""
    for letter in text:
        position = int(alphabet.index(letter))
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"Textul criptat este {cipher_text}")
def decrypt(text,shift):
    cipher_text =""
    for letter in text:
        position = int(alphabet.index(letter))
        new_position = position - shift
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"Your decoded text is {cipher_text}")
ans=True
while ans:
    if direction == 'encode':
        encrypt(text = text,shift = shift)
        break
    elif direction == 'decode':
        decrypt(text = text,shift = shift)
        break
    else:
        break
