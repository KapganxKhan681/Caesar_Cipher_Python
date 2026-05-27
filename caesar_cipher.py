# --- STEP 1: Getting inputs from the user ---
# --- ADIM 1: Kullanıcıdan girdileri alıyoruz ---

operation = input("Type 'E' to Encrypt, 'D' to Decrypt: ").upper()
message = input("Enter your message: ")
key = int(input("Enter shift amount (a number between 1-25): "))

# Variable to store the final result
# Sonucu içine kaydedeceğimiz boş bir string değişkeni
new_message = ""

# --- STEP 2: Loop through each character in the message ---
# --- ADIM 2: Mesajdaki her bir karakteri tek tek dönüyoruz ---

for character in message.upper():
    
    # Check if the character is a letter (ignores spaces/numbers)
    # Karakterin harf olup olmadığını kontrol ediyoruz (boşluk ve sayıları atlar)
    if character.isalpha():
        
        # Get the ASCII value of the character (e.g., A = 65, Z = 90)
        # Karakterin sayısal ASCII değerini alıyoruz (Örn: A = 65, Z = 90)
        char_code = ord(character)
        
        # If the operation is ENCRYPTION, shift forward
        # Eğer işlem ŞİFRELEME ise harfi ileri kaydırıyoruz
        if operation == 'E':
            new_code = char_code + key
            
            # If the code goes past 'Z' (90), wrap around to the beginning
            # Eğer yeni kod 'Z' harfini (90) geçerse, alfabenin başına dön
            if new_code > 90:
                new_code = new_code - 26
                
        # If the operation is DECRYPTION, shift backward
        # Eğer işlem ÇÖZME ise harfi geri kaydırıyoruz
        elif operation == 'D':
            new_code = char_code - key
            
            # If the code goes below 'A' (65), wrap around to the end
            # Eğer yeni kod 'A' harfinin (65) altına düşerse, alfabenin sonuna dön
            if new_code < 65:
                new_code = new_code + 26
        
        # Convert the new ASCII code back to a character and append it
        # Bulduğumuz yeni sayısal kodu tekrar harfe çevirip mesaja ekliyoruz
        new_message += chr(new_code)
        
    else:
        # If it's not a letter (space, punctuation), keep it as it is
        # Eğer karakter harf değilse (boşluk, nokta vb.) hiç dokunmadan aynen ekle
        new_message += character

# --- STEP 3: Print the final result ---
# --- ADIM 3: Sonucu ekrana yazdırıyoruz ---

print(f"\nResult / Sonuç: {new_message}")