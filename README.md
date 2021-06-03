# Lexicon mapper from DAPLAB phone set to CMU English Phone set or IITM Hindi phone set. 

The code converts IITB lexicon which contains words and their corresponding IITB phone sequences and converts it into an IITM lexicon with its IITM phone sequences. This process is done via mapping phones from the IITB set to the IITM set. Mappings can be found here: https://docs.google.com/document/d/1ELu035po-i9MJeZaRYRXYaXT_Zpa8Rxi68nS_T2VkpY/


To run the codes in either folder (Hindi or English):

./lexicon_mapper.sh `Input IITB Lexicon File+Path` `Output IITM Lexicon File+Path`

e.g. ./lexicon_mapper.sh IITB/lexicon/global_lexicon.txt global_lexicon_IITM.txt 
