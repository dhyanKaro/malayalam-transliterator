T='l̥̄'
S='r̥̄'
N='a'
M='au'
L='ന'
K='ൌ'
J='ോ'
I='ൊ'
H='ൗ'
D='േ'
C='ം'
B='ാ'
E=len
A='െ'
import unicodedata as O
U=['അ','ആ','ഇ','ഈ','ഉ','ഊ','ഋ','എ','ഏ','ഐ','ഒ','ഓ','ഔ',C]
P={'ൺ':'ṇ','ൻ':'n','ർ':'ṟ','ൽ':'l','ൾ':'ḷ','ൿ':'k'}
Q={(A,B):I,(B,A):I,(D,B):J,(B,D):J,(A,H):K,(H,A):K,(A,A):'ൈ'}
F={B:'ā','ി':'i','ീ':'ī','ു':'u','ൂ':'ū','ൃ':'r̥','ൄ':S,'ൢ':'l̥','ൣ':T,A:'e',D:'ē','ൈ':'ai',I:'o',J:'ō',K:M,H:M,'അ':N,'ആ':'ā','ഇ':'i','ഈ':'ī','ഉ':'u','ഊ':'ū','ഋ':'r̥','ൠ':S,'ഌ':'l̥','ൡ':T,'എ':'e','ഏ':'ē','ഐ':'ai','ഒ':'o','ഓ':'ō','ഔ':M,'ക':'k','ഖ':'kh','ഗ':'g','ഘ':'gh','ങ':'ṅ','ച':'c','ഛ':'ch','ജ':'j','ഝ':'jh','ഞ':'ñ','ട':'ṭ','ഠ':'ṭh','ഡ':'ḍ','ഢ':'ḍh','ണ':'ṇ','ത':'t','ഥ':'th','ദ':'d','ധ':'dh',L:'n','പ':'p','ഫ':'ph','ബ':'b','ഭ':'bh','മ':'m','റ':'ṟ','റ്റ':'ṯ','ഩ':'ṉ','ഴ':'ḻ','യ':'y','ര':'r','ല':'l','ള':'ḷ','വ':'v','ശ':'ś','ഷ':'ṣ','സ':'s','ഹ':'h',C:'ṁ','൦':'0','൧':'1','൨':'2','൩':'3','൪':'4','൫':'5','൬':'6','൭':'7','൮':'8','൯':'9'}
V=set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
W=set(' \t\n\r\x0b\x0c')
R=V.union(W)
X=chr(8204)
R.add(X)
def G(char):
	if char==C:return False
	A=O.category(char);return A.startswith('M')
def transliterate(text):
	I='്';B=text;D='';A=0
	while A<E(B):
		C=B[A]
		if(C==L or C=='റ')and A+2<E(B)and B[A+1:A+3]=='്റ':
			if C==L:D+='nṯ'
			else:D+='ṯṯ'
			H=B[A+3]if A+3<E(B)else None
			if H and not G(H)and H!=I:D+=N
			A+=3
		elif A+1<E(B)and(C,B[A+1])in Q:D+=F[Q[C,B[A+1]]];A+=2
		elif C in F:
			D+=F[C]
			if not G(C)and C not in U and(A+1==E(B)or not G(B[A+1])and B[A+1]!=I):D+=N
			A+=1
		elif C in P:D+=P[C];A+=1
		elif C==I:
			if A==E(B)-1 or B[A+1]in R or O.category(B[A+1]).startswith('Z'):D+='ŭ'
			A+=1
		else:D+=C;A+=1
	return D