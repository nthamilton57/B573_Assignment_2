#Read the complete sequence from the file
with open("chr1_GL383518v1_alt.fa", "r") as fasta:
    #store the first line as the header
    header = fasta.readline()
    # Read the sequence replacing each new line with nothing
    sequence = (fasta.read().replace("\n", ""))

#Create variables that store the 10th and 758th base in the sequence
base10 = sequence[9]
base758 = sequence[757]

#Print the 10th and 758th letters of the sequence
print("10th letter:", base10)
print("758th letter:", base758)