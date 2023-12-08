##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, Emilio Ordonez Guerrero
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        self._ciphertext = ''

    def get_author(self):
        return "Emilio Ordonez Guerrero"

    def get_cipher_name(self):
        return "Transposition Cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        citation = "Simmons, Gustavus J.. \"transposition cipher\". Encyclopedia Britannica, 10 May. 2011,"\
                    "https://www.britannica.com/topic/transposition-cipher. Accessed 6 December 2023."
        return citation

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):

        # The encrypt pseudocode
        pc = "encrypt(plaintext,password)\n" \
             "   columns <- len(password)\n" \
             "   IF more columns than len(plaintext)\n" \
             "      columns <- len(password) / 2\n" \
             "   WHILE len(plaintext) \%\ columns\n" \
             "      add space to end of plaintext\n" \
             "   FOR col 0...columns\n" \
             "      p <- col\n" \
             "      WHILE p < len(plaintext)\n" \
             "         ciphertext[col] <- ciphertext[col] + plaintext[p]\n" \
             "         p <- p + columns\n" \
             "   return ciphertext\n\n" 

        # The decrypt pseudocode
        pc += "decrypt(cipherText,password)\n" \
              "   columns <- len(password)\n" \
              "   rows <- -(len(ciphertext) // columns)\n" \
              "   FOR outer 0...len(rows)\n" \
              "      FOR array is all values of self._ciphertext\n" \
              "         plaintext <- plaintext + array[outer]\n" \
              "   return plaintext\n"

        return pc

    ##########################################################################
    # ENCRYPT
    #  Arranges the characters of the plaintext into columns based on the password,
    #  it then concatenates the characters from these columns to generate the ciphertext.
    ##########################################################################
    def encrypt(self, plaintext, password):
        # Get the number of columns
        columns = len(password)

        # Make sure there are less columns than characters in plaintext
        if columns >= len(plaintext):
            columns = len(password) / 2

        # Make sure every columns will have the same amount of characters
        while len(plaintext) % columns:
            plaintext += " "
        
        self._ciphertext = [''] * columns
        
        # Iterate through the columns
        for col in range(columns):
            p = col

            # Iterate through plaintext characters
            while p < len(plaintext):
                # Add the character to the current column fo the cipher
                self._ciphertext[col] += plaintext[p]
                p += self._columns # Move to the next character in the same column

        return ''.join(self._ciphertext)

    ##########################################################################
    # DECRYPT
    # Uses the provided password to rearrange the characters of the ciphertext 
    # into their original order by iterating through columns and rows based on 
    # the sorted column order.
    ##########################################################################
    def decrypt(self, ciphertext, password):
        # Get the number of rows and columns
        columns = len(password)
        rows = -(-len(ciphertext) // columns)  
        plaintext = ''

        # Iterate through the _ciphertext array
        for outer in range(rows):
            # Iterate through each character in the array
            for array in self._ciphertext:
                # Add the character to the plaintext
                plaintext += array[outer]

        return plaintext.strip()
    
