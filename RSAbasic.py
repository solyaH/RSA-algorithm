import math
alphabet = "abcdefghijklmnopqrstuvwxyz"

def EuclidAlgorithm(a,b):#a>=b
    d=0; x=1; y=0
    if b==0:
        return(d,x,y)
    x2=1; x1=0; y2=0; y1=1
    while b>0:
        q=a//b
        r=a-q*b
        x=x2-q*x1
        y=y2-q*y1
        a=b; b=r; x2=x1; x1=x; y2=y1; y1=y
    d=a; x=x2; y=y2
    return (d,x,y)

def intToBit(letterNumb,bitLength):    
    return '{0:0b}'.format(letterNumb).zfill(bitLength)

def RSA(text,p,q,e,action):   
    n=p*q
    phi=(p-1)*(q-1)
    smt,u,v=EuclidAlgorithm(phi,e)
    bitLength=int(math.log(len(alphabet), 2))+1
    maxBitIntervalLength=int(math.log(n-1, 2))
#    print("bitLength=",bitLength)
#    print("maxBitIntervalLength=",maxBitIntervalLength)
    if action=='e':
        bitStr=''
        for letter in text:
            letterNumb = alphabet.find(letter)+1
#            print("letterNumb=",letterNumb)
            bitStr=bitStr+intToBit(letterNumb,bitLength)
#        print("bitStr = ",bitStr)
        C=[]
        lengthOfCipher=len(bitStr)//maxBitIntervalLength+1
        for i in range(lengthOfCipher):
#            print("numbBit=",bitStr[maxBitIntervalLength*i:maxBitIntervalLength*(i+1)])
            M=int(bitStr[maxBitIntervalLength*i:maxBitIntervalLength*(i+1)],2)
#            print("M = ",M)
            C.append((M**e)%n)
        return(C)
    elif action=='d':
        d=v%phi
        M=[]
        for code in text:
            M.append((code**d)%n)
#        print("M = ",M)    
        bitStr=''
        for i in range(len(M)):
            if i==len(M)-1:
                length=int(maxBitIntervalLength*(len(M)-1)/bitLength)+1
#                print("length=",length)
#                print("numbBit=",intToBit(M[i],length*bitLength-len(bitStr)))
                bitStr=bitStr+intToBit(M[i],length*bitLength-len(bitStr))
            else:
#                print("numbBit=",intToBit(M[i],maxBitIntervalLength))
                bitStr=bitStr+intToBit(M[i],maxBitIntervalLength)
#        print("bitStr = ",bitStr)
        decodedText=''
        lengthOfCipher=len(bitStr)//bitLength
#        print("lengthOfCipher=",lengthOfCipher)
        for i in range(lengthOfCipher):
            letterNumb=int(bitStr[bitLength*i:bitLength*(i+1)],2)
#            print("letterNumb=",letterNumb)
            decodedText+=alphabet[letterNumb-1]
        return decodedText
    
def main():   
    text='wonderfull'
#    text=[358, 262, 486, 384, 43, 24]
#    text='download'
#    text=[195, 194, 93, 44, 147, 82]
    action='e'
    p=17#17 13
    q=31# 31 23
    e=7#7 5
    print(RSA(text,p,q,e,action))
    
#main()
