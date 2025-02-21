# Module Lab: Caesar Cipher Program Bug #1

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

# Get a message to encrypt
def getMessage():
    return input("Please enter a message to encrypt: ")

# Get a cipher key
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return int(shiftAmount)  # Convertendo para inteiro

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  # Corrigido: Removida atribuição desnecessária
    
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        if currentCharacter in alphabet:
            newPosition = position + cipherKey
            encryptedMessage += alphabet[newPosition]  # Usa o alfabeto dobrado corretamente
        else:
            encryptedMessage += currentCharacter  # Mantém caracteres não encontrados

    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -cipherKey  # Já é inteiro, não precisa de conversão
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(f'Message: {myMessage}')
    
    myCipherKey = getCipherKey()
    print(f'Cipher Key: {myCipherKey}')
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Executa o programa
runCaesarCipherProgram()