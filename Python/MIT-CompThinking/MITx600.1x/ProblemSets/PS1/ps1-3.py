#!usr/bin/python
# _*_ coding = utf-8 _*_

''' check each charter one by one and compare all the following charcters 
    which satify the requirement with the counts.  keep the largest 
    counts and retunr it '''

#s = 'azcbobobegghakl'
#   Longest substring in alphabetical order is: beggh
#s = 'ktkkrnyobdbingjyggvmgqmp'
#   Longest substring in alphabetical order is: kkr   
#s = 'pweuykwpdfgixvtidhee'
#   Longest substring in alphabetical order is:  dfgix
#s = 'shiwqmcavduonpc'
#   Longest substring in alphabetical order is:  hiw
#s = 'wwirxbywqjvxq'
#   Longest substring in alphabetical order is: irx     
#s = 'dtcilzkavcuatpbuxcyq'
#   Longest substring in alphabetical order is:  cilz
#s = 'ygwpuwsflrsgosmcjdh'
#   Longest substring in alphabetical order is:  flrs
#s = 'gervriojujrlwng'
#   Longest substring in alphabetical order is:  erv
#s = 'abcdefghijklmnopqrstuvwxyz'
#   Longest substring in alphabetical order is: abcdefghijklmnopqrstuvwxyz 
#s = 'ptaaiwsrdhpupbyksyiadgzj'
#   Longest substring in alphabetical order is:  aaiw
#s = 'siztexrrjvxrl'
#   Longest substring in alphabetical order is: jvx    
#s = 'aecxueeshscwqipr'
#   Longest substring in alphabetical order is: ees 
#s = 'zyxwvutsrqponmlkjihgfedcba'
#   Longest substring in alphabetical order is: z 
#s = 'tunvzcelxl'
#   Longest substring in alphabetical order is:  celx       
#s = 'rutgfodnqekdpfra'
#   Longest substring in alphabetical order is: dnq 
#s = 'sttnftrfhljdxqdgslvbbml'
#   Longest substring in alphabetical order is:  stt
#s = 'ideuecpbcjfmkjoicufdwfji'
# Longest substring in alphabetical order is:  deu
#s = 'ofjmocpdz'
#   Longest substring in alphabetical order is:  fjmo
#s = 'ragnabjhdcvxfaeyyccwcvkl'
#   Longest substring in alphabetical order is: aeyy        x
#s = 'csojaqpytpc'
#   Longest substring in alphabetical order is:  cs
#s = 'gctdsjpjelnxeoqtogfcim'
#   Longest substring in alphabetical order is:  elnx

record = ''

for idx1 in range(len(s)):
    cntCur = 1
    for idx2 in range(len(s)-idx1-1):
#        print 'idx1=', idx1, ' char =', s[idx1+idx2], 'next =', s[idx1+idx2+1], 'curCnt =', cntCur
        if s[idx1+idx2] <= s[idx1+idx2+1]:
            cntCur += 1
        else:
            break

    if cntCur > len(record):
        record = s[idx1:idx1+cntCur]
#    print 'cntCur =', cntCur, 'record =', record, '\n'

print 'Longest substring in alphabetical order is: ', record

