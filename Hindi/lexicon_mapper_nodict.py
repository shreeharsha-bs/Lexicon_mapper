import pandas as pd
import sys
import numpy as np
import pdb
def unicode_string(string1):
	return[ord(x) for x in string1]

def string_unicode(unc1):
	return[chr(x) for x in unc1]

lex = pd.read_csv(sys.argv[1],sep='\t',header=None).values
#lex = pd.read_csv(sys.argv[1],header=None).values
#lex_hin = lex[3879:]  # hindi words
lex_hin=lex
#pdb.set_trace()
## chr(2306) = 'ं'; chr(2305) = 'ँ' # unicodes 
lex_nasal_unicode = []
for word in lex_hin[:,0]:
	lex_nasal_unicode += [unicode_string(word)] # list of unicode symbols for each word

nasalised_1 = np.array([ord('ं') in sublist for sublist in lex_nasal_unicode]).astype(int) # find all words which have 'ं'
nasalised_2 = np.array([ord('ँ') in sublist for sublist in lex_nasal_unicode]).astype(int) # find all words which have 'ँ'

list1 = lex_hin[np.where(nasalised_1==1)[0]] # In these,'ं'(unicode=2306) will have to be mapped to "q" phone from IITM set

count = 0


for word in list1:
	#print(count)
	#word=list1[1]
	count+=1
	uni_arr1 = np.array(unicode_string(word[0])).astype(int)
	uni_arr2 = np.array(unicode_string(word[1])).astype(int)
	q_pos_all = np.where(uni_arr1==ord('ं'))[0] # position where 'ं' is 
	sp_pos = np.where(uni_arr2==ord(' '))[0] # Position of spaces found
	uni_arr2_final = np.copy(uni_arr2) # copy where phones will be replaced

	#2325 to 2361 consonants

	for q_pos in q_pos_all:
		if(q_pos == len(uni_arr1)-1):
			#print("Found nasal at end, just appending q at end") # Just append the q (unicode 113) with space (unicode 32) for words like क्यों k y o
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2),ord(' '))
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2)+1,ord('q'))

		elif(q_pos == len(uni_arr1)-2 and uni_arr2[np.where(uni_arr2==32)[0][-1]-1]==ord('n')):
			#print("Found nasal just before end, treating last phone as consonant and replacing n with q it")
			uni_arr2_final[np.where(uni_arr2==32)[0][-1]-1]=ord('q')
		elif(uni_arr2[sp_pos[q_pos-1]+1]==ord('n') and len(np.where(uni_arr2==32)[0])+1 >= len(uni_arr1)): # If n (unicode 110) is found in position X, replace the phone after the Xth space (i.e X+1st) by q
			uni_arr2_final[sp_pos[q_pos-1]+1] = ord('q')
			#print("n found and replaced")

		elif(uni_arr2[sp_pos[q_pos-1]+1]==ord('m')): # If m (unicode 109) is found as in अंबा a m b aa, replace with q
			uni_arr2_final[sp_pos[q_pos-1]+1]= ord('q')
			#print("m found and replaced with q")
		elif(len(np.where(uni_arr2==32)[0])+1 > len(uni_arr1) and uni_arr2[sp_pos[q_pos-1]+3]==ord('m')): 
			uni_arr2_final[sp_pos[q_pos-1]+3]=ord('q')
			#print("m found and replaced with q")



		elif(len(np.where(uni_arr2==32)[0])+1 >= len(uni_arr1)):
			#print("Consonant + vowel combination I found")			
			if((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+3]= ord('q')
			elif((uni_arr1[q_pos] < 2325 or uni_arr1[q_pos] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+3]= ord('q')		
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord(' ') and uni_arr2[sp_pos[q_pos-1]+4]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+4]= ord('q')
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+4]==ord(' ') and uni_arr2[sp_pos[q_pos-1]+5]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+5]= ord('q')


		elif(len(np.where(uni_arr2==32)[0])+1 < len(uni_arr1)):
			#print("Consonant + vowel combination II found")
			if((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]-1]==ord('n')):
				#print("Next phone after space in this combo is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]-1]= ord('q')
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+1]==ord('n')):
				#print("Next phone after space in this combo is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+1]= ord('q')
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]-3]==ord('n')):
				#print("Next phone after space in this combo is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]-3]= ord('q')
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord('n')):
				#print("Next phone after space is nasal, replacing that")				
				uni_arr2_final[sp_pos[q_pos-1]+3]= ord('q')
		else: 				    
			print("####@@@%$$$$%%%% No m or n found, appending q, check for errors ####@@@%$$$$%%%%")


	str2 = string_unicode(uni_arr2_final)
	str1 = ''.join(str2)
	#print(word[0]+'\t'+word[1])
	print(word[0]+'\t'+str1)

list2 = lex_hin[np.where(nasalised_2==1)[0]] # In these, 'ँ'(unicode=2305) will have to be mapped to "mq" phone from IITM set, # Not yet tested

for word in list2:
	#print(count)
	#word=list2[25]
	count+=1
	uni_arr1 = np.array(unicode_string(word[0])).astype(int)
	uni_arr2 = np.array(unicode_string(word[1])).astype(int)
	q_pos_all = np.where(uni_arr1==ord('ँ'))[0] # position where 'ँ' is 
	sp_pos = np.where(uni_arr2==ord(' '))[0] # Position of spaces found
	uni_arr2_final = np.copy(uni_arr2) # copy where phones will be replaced

	#2325 to 2361 consonants

	for q_pos in q_pos_all:
		if(q_pos == len(uni_arr1)-1):
			#print("Found nasal at end, just appending mq at end") # Just append the q (unicode 113) with space (unicode 32) for words like क्यों k y o
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2),ord(' '))
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2)+1,ord('m'))
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2)+2,ord('q'))

		elif(q_pos == len(uni_arr1)-2 and not (uni_arr2[np.where(uni_arr2==32)[0][-1]-1]==ord('n'))):
			#print("Found nasal just before end, just appending mq before end") # Just append			
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2)-2,ord(' '))
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2)-1,ord('m'))
			uni_arr2_final = np.insert(uni_arr2_final,len(uni_arr2),ord('q'))


		elif(q_pos == len(uni_arr1)-2 and uni_arr2[np.where(uni_arr2==32)[0][-1]-1]==ord('n')):
			#print("Found nasal just before end, treating last phone as consonant and replacing n with q it")
			uni_arr2_final[np.where(uni_arr2==32)[0][-1]-1]=ord('m')
			uni_arr2_final = np.insert(uni_arr2_final,np.where(uni_arr2==32)[0][-1],ord('q'))
		elif(uni_arr2[sp_pos[q_pos-1]+1]==ord('n')): # If n (unicode 110) is found in position X, replace the phone after the Xth space (i.e X+1st) by q
			uni_arr2_final[sp_pos[q_pos-1]+1] = ord('m')
			uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+2,ord('q'))
			#print("n found and replaced")

		elif(uni_arr2[sp_pos[q_pos-1]+1]==ord('m')): # If m (unicode 109) is found as in अंबा a m b aa, insert q after m to get mq
			uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+2,ord('q'))
			#print("m found and replaced with mq")
		elif(len(np.where(uni_arr2==32)[0])+1 > len(uni_arr1) and uni_arr2[sp_pos[q_pos-1]+3]==ord('m')): # If m (unicode 109) is found as in अंबा a m b aa, insert q after m to get mq
			uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+4,ord('q'))
			#print("m found and replaced with mq")



		elif(len(np.where(uni_arr2==32)[0])+1 >= len(uni_arr1)):
			#print("Consonant + vowel combination I found")			
			if((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+3]= ord('m')
				uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+4,ord('q'))
			elif((uni_arr1[q_pos] < 2325 or uni_arr1[q_pos] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+3]= ord('m')
				uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+4,ord('q'))
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord(' ') and uni_arr2[sp_pos[q_pos-1]+4]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+4]= ord('m')
				uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+5,ord('q'))
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+4]==ord(' ') and uni_arr2[sp_pos[q_pos-1]+5]==ord('n')):
				#print("Next phone after space is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]+5]= ord('m')
				uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+6,ord('q'))
		elif(len(np.where(uni_arr2==32)[0])+1 < len(uni_arr1)):
			#print("Consonant + vowel combination II found")
			if((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]-1]==ord('n')):
				#print("Next phone after space in this combo is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]-1]= ord('m')
				uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1],ord('q'))
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]-3]==ord('n')):
				#print("Next phone after space in this combo is nasal, replacing that")
				uni_arr2_final[sp_pos[q_pos-1]-3]= ord('m')
				uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]-2,ord('q'))
			elif((uni_arr1[q_pos-1] < 2325 or uni_arr1[q_pos-1] > 2357) and uni_arr2[sp_pos[q_pos-1]+3]==ord('n')):
				#print("Next phone after space is nasal, replacing that")				
				uni_arr2_final[sp_pos[q_pos-1]+3]= ord('m')
				uni_arr2_final = np.insert(uni_arr2_final,sp_pos[q_pos-1]+4,ord('q'))
		else: 				    
			print("####@@@%$$$$%%%% No m or n found, appending q, check for errors ####@@@%$$$$%%%%")



	str2 = string_unicode(uni_arr2_final)
	str1 = ''.join(str2)
	#print(word[0]+'\t'+word[1])
	print(word[0]+'\t'+str1)

