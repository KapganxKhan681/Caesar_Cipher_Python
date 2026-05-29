# TR: Kullanıcıdan operasyon türünü alıyoruz ve doğru girdi girene kadar döngüde tutuyoruz (Girdi Doğrulaması).
# EN: Get the operation type and enforce valid input using a while loop (Input Validation).
operation = input("Type 'E' to Encrypt, 'D' to Decrypt: ").upper()
while operation not in ['E', 'D']:
    print("Invalid choice! / Geçersiz seçim! Please type 'E' or 'D'.")
    operation = input("Type 'E' to Encrypt, 'D' to Decrypt: ").upper()

# TR: Operasyon türü garanti altına alındıktan sonra diğer girdileri alıyoruz.
# EN: Proceed with other inputs only after a valid operation is secured.
message = input("Enter your message: ")
key = int(input("Enter shift amount (a number between 1-25): "))

# TR: Kullanıcı 25'ten büyük girdiğinde algoritmanın alfabe dışına taşmasını önlemek için mod 26 alıyoruz.
# EN: Apply modulo 26 to handle shift amounts greater than 25 safely.
key = key % 26

new_message = ""

# TR: 'isalpha()' fonksiyonu Türkçe karakterlerde True döndürüp ASCII hesabını bozduğu için,
# kontrolü doğrudan İngiliz alfabesinden oluşan sabit bir string ile yapıyoruz.
# EN: Since 'isalpha()' returns True for non-English characters and breaks ASCII calculations,
# we validate characters directly using a fixed English alphabet string.
ALFABE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# TR: Mesajdaki her bir karakteri tek tek dönerek şifreleme/çözme işlemini başlatıyoruz.
# EN: Loop through each character in the message to perform encryption or decryption.
for character in message.upper():
    
    if character in ALFABE:
        # TR: Harfin alfabedeki mevcut indeksini buluyoruz (0-25 arası).
        # EN: Find the current index of the character in the alphabet (0-25).
        mevcut_indeks = ALFABE.index(character)
        
        if operation == 'E':
            # TR: Şifreleme için harfi ileri kaydır ve alfabe sınırını aşarsa başa dönmesi için mod 26 uygula.
            # EN: Shift forward for encryption and apply modulo 26 to wrap around the alphabet.
            new_indeks = (mevcut_indeks + key) % 26
                
        elif operation == 'D':
            # TR: Çözme için harfi geri kaydır ve negatif indeksleri yönetmek için mod 26 uygula.
            # EN: Shift backward for decryption and apply modulo 26 to handle negative indices.
            new_indeks = (mevcut_indeks - key) % 26
        
        new_message += ALFABE[new_indeks]
        
    else:
        # TR: Karakter İngiliz alfabesinde yoksa (boşluk, sayı, Türkçe karakter), yapısını aynen koru.
        # EN: If the character is not in the English alphabet (space, digit, punctuation), preserve it.
        new_message += character

print(f"\nResult / Sonuç: {new_message}")
