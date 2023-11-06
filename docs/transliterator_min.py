# This file exists because I spent an hour trying to import from the parent directory
# and then decided to do this instead
I='l̥̄'
D='r̥̄'
H='a'
B='au'
G='ന'
A='ം'
E=len
import unicodedata as J
N=['അ','ആ','ഇ','ഈ','ഉ','ഊ','ഋ','എ','ഏ','ഐ','ഒ','ഓ','ഔ',A]
K={'ൺ':'ṇ','ൻ':'n','ർ':'ṟ','ൽ':'l','ൾ':'ḷ','ൿ':'k'}
L={'ാ':'ā','ി':'i','ീ':'ī','ു':'u','ൂ':'ū','ൃ':'r̥','ൄ':D,'ൢ':'l̥','ൣ':I,'െ':'e','േ':'ē','ൈ':'ai','ൊ':'o','ോ':'ō','ൌ':B,'ൗ':B,'അ':H,'ആ':'ā','ഇ':'i','ഈ':'ī','ഉ':'u','ഊ':'ū','ഋ':'r̥','ൠ':D,'ഌ':'l̥','ൡ':I,'എ':'e','ഏ':'ē','ഐ':'ai','ഒ':'o','ഓ':'ō','ഔ':B,'ക':'k','ഖ':'kh','ഗ':'g','ഘ':'gh','ങ':'ṅ','ച':'c','ഛ':'ch','ജ':'j','ഝ':'jh','ഞ':'ñ','ട':'ṭ','ഠ':'ṭh','ഡ':'ḍ','ഢ':'ḍh','ണ':'ṇ','ത':'t','ഥ':'th','ദ':'d','ധ':'dh',G:'n','പ':'p','ഫ':'ph','ബ':'b','ഭ':'bh','മ':'m','റ':'ṟ','റ്റ':'ṯ','ഩ':'ṉ','ഴ':'ḻ','യ':'y','ര':'r','ല':'l','ള':'ḷ','വ':'v','ശ':'ś','ഷ':'ṣ','സ':'s','ഹ':'h',A:'ṁ'}
O=set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
P=set(' \t\n\r\x0b\x0c')
M=O.union(P)
Q=chr(8204)
M.add(Q)
def F(char):
	if char==A:return False
	B=J.category(char);return B.startswith('M')
def transliterate(text):
	J='്';B=text;D='';A=0
	while A<E(B):
		C=B[A]
		if(C==G or C=='റ')and A+2<E(B)and B[A+1:A+3]=='്റ':
			if C==G:D+='nṯ'
			else:D+='ṯṯ'
			I=B[A+3]if A+3<E(B)else None
			if I and not F(I)and I!=J:D+=H
			A+=3
		elif C in L:
			D+=L[C]
			if not F(C)and C not in N and(A+1==E(B)or not F(B[A+1])and B[A+1]!=J):D+=H
			A+=1
		elif C in K:D+=K[C];A+=1
		elif C==J:
			if A==E(B)-1 or B[A+1]in M:D+='ŭ'
			A+=1
		else:D+=C;A+=1
	return D