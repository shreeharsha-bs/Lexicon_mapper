import pandas as pd
import sys
import numpy as np

def unicode_string(string1):
	return[ord(x) for x in string1]

def string_unicode(unc1):
	return[chr(x) for x in unc1]

lex = pd.read_csv(sys.argv[1],sep='\t').values

lex_hin = lex[3879:]  # hindi words

## chr(2306) = 'ं'; chr(2305) = 'ँ' # unicodes 

dev2phone = {'अ':'a',
'आ':'aa',
'इ':'i',
'ई':'ii',
'उ':'u',
'ऊ':'uu',
'ए':'ee',
'ऐ':'ee',
'ऎ':'ee',
'ऄ':'ee',
'ऍ':'ei',
'ॲ':'ei',
'ओ':'o',
'ऒ':'o',
'औ':'ou',
'ऑ':'ou',
'ं':'q',
'ः':'H',
'ँ':'mq',
'ऋ':'r u',
'ऌ':'l r u',
'क':'k',
'ख':'kh',
'ग':'g',
'घ':'gh',
'ङ':'n g',
'च':'c',
'छ':'ch',
'ज':'j',
'झ':'jh',
'ञ':'n j',
'ट':'tx',
'ठ':'txh',
'ड':'dx',
'ढ':'dxh',
'ण':'nx',
'त':'t',
'थ':'th',
'द':'d',
'ध':'dh',
'न':'n',
'प':'p',
'फ':'ph',
'ब':'b',
'भ':'bh',
'म':'m',
'य':'y',
'र':'r',
'ऱ':'r',
'ल':'l',
'ळ':'l',
'व':'w',
'श':'sh',
'ष':'sh',
'स':'s',
'ह':'h',
'़':'',
'ऽ':'',
'ा':'aa',
'ि':'i',
'ी':'ii',
'ु':'u',
'ू':'uu',
'ृ':'r u',
'ॄ':'r uu',
'ॅ':'ei',
'ॆ':'ee',
'े':'ee',
'ै':'ee',
'ॉ':'ou',
'ॊ':'o',
'ो':'o',
'ौ':'ou',
'ॏ':'ou',
'्':'',
'‍':'',
'ॐ':'o m',
'॔':'r',
'ॕ':'ou',
'क़':'k',
'ख़':'kh',
'ग़':'g',
'ज़':'z',
'ड़':'dx',
'ढ़':'dxh',
'फ़':'f',
'य़':'y',
'ॠ':'r uu',
'ॡ':'l r uu',
'ॢ':'l r u',
'ॣ':'l r uu',
'।':'',
'॥':'',
'-':''}

lex_nasal_unicode = []
for word in lex_hin[:,0]:
	lex_nasal_unicode += [unicode_string(word)] # list of unicode symbols for each word

nasalised_1 = np.array([ord('ं') in sublist for sublist in lex_nasal_unicode]).astype(int) # find all words which have 'ं'
nasalised_2 = np.array([ord('ँ') in sublist for sublist in lex_nasal_unicode]).astype(int) # find all words which have 'ँ'

list1 = lex_hin[np.where(nasalised_1==1)[0]] # In these,'ं'(unicode=2306) will have to be mapped to "q" phone from IITM set

# list2 = lex_hin[np.where(nasalised_2==1)[0]] # In these, 'ँ'(unicode=2305) will have to be mapped to "mq" phone from IITM set, # Not yet tested

#for word in list1:
word = list1[7] # testing for अंडटेकिंग	a n dx a tx ee k i n g : a q dx a tx ee k i q g
word = list1[-6] # testing for त्यांनी	t y aa n n ii
uni_arr1 = np.array(unicode_string(word[0])).astype(int)
uni_arr2 = np.array(unicode_string(word[1])).astype(int)
q_pos_all = np.where(uni_arr1==ord('ं'))[0] # position where 'ं' is 

uni_arr2_final=[]

for unic in uni_arr1:
	print(unic)
	uni_arr2_final+=dev2phone[chr(unic)]
	uni_arr2_final+=[' ']


str2 = uni_arr2_final
str1 = ''.join(str2)
print(word[0]+' 	'+word[1])
print(word[0]+' 	'+str1)
