#Read the complete sequence from the file
with open("chr1_GL383518v1_alt.fa", "r") as fasta:
    #store the first line as the header
    header = fasta.readline()
    # Read the sequence replacing each new line with nothing
    sequence = list(fasta.read().replace("\n", "").upper())
    
#Creates a function that will get the complement sequence
def getcomplement(sequence):
    #creates a dictionary that contains the base pairs
    dna_sub = {'G':'C','C':'G','A':'T','T':'A'}
    #Creates an empty list
    complement = []
    #creates the complement string by joining the value for each base as the key from the dictionary. 
    #Prints missing if the key isnt in the dictionary
    complement = ''.join(dna_sub.get(base, 'Missing') for base in sequence)
    #returns the complement as a list
    return list(complement)

#Create a function that will reverse the sequence string
def flip(sequence):
    #Uses reverse to flip the sequence
    sequence.reverse()
    #returns the flipped sequence as a list
    return sequence

#calls both functions on the original sequence and stores the output as a variable
reverse_comp = flip(getcomplement(sequence))

#prints teh 79th base of the reverse complement
print("79th Base of Reverse Complement", reverse_comp[78])

#Prints the 500th base through the 800th basae (including 800th base)
print("500 through 800th Bases of Reverse Complement", reverse_comp[499:800])