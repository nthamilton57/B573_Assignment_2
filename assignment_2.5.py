#Read the complete sequence from the file
with open("chr1_GL383518v1_alt.fa", "r") as fasta:
    #store the first line as the header
    header = fasta.readline()
    # Read the sequence replacing each new line with nothing
    sequence = (fasta.read().replace("\n", "")).upper()

#Create an empty dictionary that will be the final product
my_dict = {}

#Convert the sequence string to a list of each base
bases = list(sequence)

#Use for loop that creates dictionaries within the main dictionary that will create a dictionary for each 1000 base
for n in range(0,len(sequence),1000):
    #within each dictionary for each 1000 base, there will be another dictionary with keys for each base and 0 for their initial count
    my_dict[n] = {'G':0, 'C':0, 'T':0, 'A':0}

#loops through each 1000th number in the length of the sequence
for n in range(0,len(sequence),1000):
    #loops through each group of 1000 bases
    for base in bases[n:n+1000]:
        #for each base, updates the count by 1 when the base occurs
        if base == "A":
            my_dict[n]["A"] += 1
        if base == "T":
            my_dict[n]["T"] += 1
        if base == "G":
            my_dict[n]["G"] += 1
        if base == "C":
            my_dict[n]["C"] += 1

#prints each dictionary within the main dictionary
for n in range(0,len(sequence),1000):
    #labels the dictionary with every 1000 bases
    if len(bases[n:n+1000]) == 1000:
        print(f"The base count for {n} to {n+10000}: {my_dict[n]}")
    else:
        #prints the last group of bases with the proper ending value
        print(f"The base count for {n} to {len(sequence)}: {my_dict[n]}")