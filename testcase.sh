echo -e  "\nAnagram:"
echo "cat tac tic"|./mapper_anagram.py|sort|./reducer_anagram.py 

echo -e  "\nDNA Same:"
echo -e "user1 ACGT\nuser3 ATGC\nuser2 ACGT"|./mapper_dna_seq.py|sort|./reducer_dna_seq.py 

echo -e "\nDNA Miror Seq:"
echo -e "user1 ACGT\nuser3 ATGC\nuser2 ACGT\nuser4 TGCA"|./mapper_dna_mirror.py |sort|./reducer_dna_mirror.py 

