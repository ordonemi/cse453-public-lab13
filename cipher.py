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
        self.row_length = ''
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
        return "citation"

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):

        # The encrypt pseudocode
        pc = "encrypt(plaintext,password)\n" \
             "   rowLength <- len(password)\n" \
             "   IF rowLength >= len(plaintext)\n" \
             "      rowLength <- len(password)\n" \
             "   FOR col <- 0...rowLength\n" \
             "      WHILE p < len(plaintext)\n" \
             "         ciphertext[col] <- plaintext[p]\n" \
             "         p <- p + rowLength\n" \
             "   RETURN " 

        # The decrypt pseudocode
        pc += "decrypt(cipherText,password)\n" \
              "   numRows = -(-len(cipherText) // len(password)\n" \
              "   colOrder <- getColOrder(password,len(password))\n" \
              "   colLengths <- getColLengths(ciphertext,len(password))\n" \
              "   FOR col is all values of colOrder\n" \
              "      FOR row <- 0...len(numRows)\n" \
              "         IF row < colLengths[col]\n" \
              "            plaintext[row * num_cols + col] = ciphertext[idx]\n"\
              "            idx <- idx + 1\n" \
              "   return plaintext"

        return pc

    ##########################################################################
    # ENCRYPT
    #  Arranges the characters of the plaintext into columns based on the password,
    #  it then concatenates the characters from these columns to generate the ciphertext.
    ##########################################################################
    def encrypt(self, plaintext, password):
        
        self.row_length = len(password)

        if self.row_length >= len(plaintext):
            self.row_length = len(password) / 2

        self._ciphertext = [''] * self.row_length

        for col in range(self.row_length):
            p = col

            while p < len(plaintext):
                self._ciphertext[col] += plaintext[p]
                p += self.row_length

        
        return ''.join(self._ciphertext)

    ##########################################################################
    # DECRYPT
    # Uses the provided password to rearrange the characters of the ciphertext 
    # into their original order by iterating through columns and rows based on 
    # the sorted column order.
    ##########################################################################
    def decrypt(self, ciphertext, password):
        # Get the number of rows and columns
        cols = len(password)
        rows = -(-len(ciphertext) // cols)  
        plaintext = [''] * len(ciphertext)

        # Sorts the columns
        colOrder = self._get_col_order(password,cols)

        # Computes the length of each column
        colLengths = self._get_col_lengths(ciphertext,cols)
        idx = 0

        # Iterate through the columns based on the sorted column order
        for col in colOrder:
            # Iterate through the rows
            for row in range(rows):
                # Check if the current row is within range
                if row < colLengths[col]:
                    # Assign the ciphertext character to the plaintext position
                    plaintext[row * cols + col] = ciphertext[idx]
                    idx += 1

        return ''.join(plaintext)
    
    ##########################################################################
    # GET COL ORDER
    # Sorts the indices based on the characters in the password using a simple sort.
    ##########################################################################
    def _get_col_order(self,password, num_cols):
        col_order = list(range(num_cols))

        # Sorts the indices using a bubble sort algorithm
        for i in range(num_cols - 1):
            for j in range(0, num_cols - i - 1):
                if password[col_order[j]] > password[col_order[j + 1]]:
                    col_order[j], col_order[j + 1] = col_order[j + 1], col_order[j]

        return col_order
    
    ##########################################################################
    # GET COL LENGTHS
    #  Computes the length of each column in the ciphertext by slicing it 
    #  based on the number of columns.
    ##########################################################################
    def _get_col_lengths(self,ciphertext, cols):
        col_lengths = []

        # Computes the length of each column by slicing the ciphertext
        for i in range(cols):
            length = len(ciphertext[i::cols])
            col_lengths.append(length)
        
        return col_lengths
