# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random
import re

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;\'<>?,./\"")
    print '     is word =', word
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    dict_coder = {}

    # this function use ord() to convert ascii into interger
    # however, space should be handled as an exception due to discontinuity
    # ord('A') = 65, ord('B') = 66, ..., ord('Z') = 90
    # ord('a') = 97, ord('b') = 98, ..., ord('Z') = 122
    # using 65 as the base_shift for upper cases to make these letters align to A 
    # using 97 as the base_shift for lower cases to make these letters align to a
    # i.e. ' ' = 0, 'a' = 1, 'b' = 2, ..., 'z' = 26
    baseC = 65
    baseL = 97
    letter_size = 26

    # dealing with lower cases
    # create mapping with given shift with cyclic buffer
    # dealing with space and letters
    for idx in range(letter_size):
        key = chr(idx+baseL)

        #if (idx+shift) % letter_size == 0:
        #    value = 'z'
        #else:
        #print chr(idx+baseL), chr(((idx+shift) % letter_size) + baseL)
        value =  chr(((idx+shift) % letter_size) + baseL)    
        dict_coder[key] = value

    # dealing with upper cases
    for idx in range(letter_size):
        key = chr(idx+baseC)
        #if (idx+shift) % letter_size == 0:
        #    value = 'Z'
        #else:
            
        #print chr(idx+baseC), chr(((idx+shift) % letter_size) + baseC)
        value = chr(((idx+shift) % (letter_size)) + baseC)
        dict_coder[key] = value

    return dict_coder

#print buildCoder(0)
#print buildCoder(5)
#print buildCoder(24)
#print buildCoder(13)
#print buildCoder(9)

#print buildCoder(3)
#print
#print buildCoder(9)



def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    '''
    create a temporary list to store the encode/decode text, then 
    join them together and return the joined string
    '''
    coded_text = ''
    for idx in range(len(text)):
        if coder.get(text[idx], 0) == 0:
            coded_text += text[idx]
        else: 
            coded_text += coder[text[idx]]

    return coded_text


#print applyCoder('Hello, world!', buildCoder(14))
#   'Vszzc, kcfzr!'
#print applyCoder('Hello, world!', buildCoder(6))
#   'Nkrru, cuxrj!'
#print applyCoder('Hello, world!', buildCoder(0))
#   'Hello, world!'
#print applyCoder('Hello, world!', buildCoder(11))
#   'Spwwz, hzcwo!'
#print applyCoder('The quiz is... hard!', buildCoder(14))
#   'Hvs eiwn wg... vofr!'
#print applyCoder('The quiz is... hard!', buildCoder(6))
#   'Znk waof oy... ngxj!'
#print applyCoder('The quiz is... hard!', buildCoder(0))
#   'The quiz is... hard!'
#print applyCoder('The quiz is... hard!', buildCoder(11))
#   'Esp bftk td... slco!'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(14))
#   '12 xoqyrokg eiwnnsr am gdvwbl!?'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(6))
#   '12 pgiqjgcy waoffkj se yvnotd!?'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(0))
#   '12 jackdaws quizzed my sphinx!?'
#print applyCoder('12 jackdaws quizzed my sphinx!?', buildCoder(11))
#   '12 ulnvolhd bftkkpo xj dastyi!?'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(14))
#   '?DXz4;M8K73UkEpnreOuwZvWg.ILlA'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(6))
#   '?VPr4;E8C73McWhfjwGmoRnOy.ADdS'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(0))
#   '?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM'
#print applyCoder('?PJl4;Y8W73GwQbzdqAgiLhIs.UXxM', buildCoder(11))
#   '?AUw4;J8H73RhBmkobLrtWsTd.FIiX'


#print applyCoder("Hello, world!", buildCoder(3))
#print
#print applyCoder("Khoor, zruog!", buildCoder(23))



def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

#pritn applyShift('Hello, world!', 12)
#   'Tqxxa, iadxp!'
#print applyShift('The quiz is... hard!', 19)
#   'Max jnbs bl... atkw!'
#print applyShift('12 jackdaws quizzed my sphinx!?', 0)
#   '12 jackdaws quizzed my sphinx!?'
#print applyShift('qgboj', 23)
#   'ndylg'
#print applyShift('drmwsnickjxbpo', 20)
#   'xlgqmhcwedrvji'
#



# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    text: string
    returns: 0 <= int < 26
    """
    text_words = text.split(' ')
    max_valid = 0
    best_shift = 0

    for shift in range(26):
        num_valid = 0

        for word in text_words:
            plaintext = applyShift(word, shift)
            if isWord(wordList, plaintext):
                num_valid += 1

        if num_valid > max_valid:
            max_valid = num_valid
            best_shift = shift

    return best_shift

wordList = loadWords()
#s = applyShift('Hello, world!', 8)
#print s
#print findBestShift(wordList, s)
#print applyShift(s, 18)

#print findBestShift(wordList, 'YvccF, nficu!')
#   9
#print findBestShift(wordList, 'Rfc osGx gq... fypb!')
#   2
#print findBestShift(wordList, "Xli xiEgliv'w reqi Mw XefmXle?")
#   22
#print findBestShift(wordList, 'Uv, IbA aOlYl pz h AH uhTlK Hscpu!')
#   19
#print findBestShift(wordList, 'suRyLgh')
#   23
#print findBestShift(wordList, 'weekeND everybodY GrouP cArt 
#   0
#print findBestShift(wordList, 'wplCy xtiefcp Mcfds nstnvpy dsLca lmdpye')
#   15
#print findBestShift(wordList, 'zlrde cxo obixqFlk ixqbiv mOBsbkqflk qfm pmlq pxrzb mboprxpflk nrFZh')
#   3
#print findBestShift(wordList, 'TyijyDwkyIX isudu tyijqDj fhEFuhjo Ixem mhyij cekdjqyd jhkij kdyJo Mehiu jxyda ydlyju Sehhusj ixEej qsheii')
#   10
#print findBestShift(wordList, 'qkeql rNfgfk pccheb')
#   0
#print findBestShift(wordList, "Uif ufbdifs'T obnf jt UbcjUib?")
#   25
#print findBestShift(wordList, 'Kl, yrq qebob fp x QX kXjba Xisfk!')
#   3
#print findBestShift(wordList, "Rfc rcyafcp'q lykc gQ Ryzgrfy?")
#   2
#print findBestShift(wordList, 'KL, Yrq qEbob fp x QX kxJba XiSfk!')
#   3
# print findBestShift(<edX wordList>, 'YvccF, nficu!')
#   
#print findBestShift(wordList, 'Tqxxa, iadxp!')
#   14
#print findBestShift(wordList, 'Nkrru, cuxrj!')
#   20
#print findBestShift(wordList, 'Pda mqev eO... DWnZ!')
#   4
#print findBestShift(wordList, "The teAcher's naMe is TaBitha?")
#   0
#print findBestShift(wordList, 'Za, ngF ftqdq ue m FM zmyqp MXhUz!')
#   14
#print findBestShift(wordList, 'gxfn')
#   23
#print findBestShift(wordList, 'jklup rdszkZFe nyrKvmvi jyvckvi iffK')
#   9
#print findBestShift(wordList, 'yjfhm mjxnYfYnts TwnlnS gJsi bjFymJw htsxHntzx')
#   21
#print findBestShift(wordList, 'iRjm mofbpq ebxa efkaoxkzb pKlT obsBkdb jfih diloV bxpqbok xmmixrPb')
#   3
#print findBestShift(wordList, 'qcbbsQHwcb fib gVih asobkvwzs Gmghsa aoqvwbs cFbOaSbh ibzsgg gwhiOhwcb aobitoQHifs rwqhwcbofm kccrsb gdwHs bwuvh bCHwqs')
#   12
#print findBestShift(wordList, 'oicoj pldedi NaAfcz')
#   0


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    return "Not yet implemented." # Remove this comment when you code the function

#print decryptStory: ('Cdchtcht ldgsh: vgtpi lwxrwtktg vgpkt egtitcs vdas')
#   'Nonsense words: great whichever grave pretend gold'
#print decryptStory: ('Uvuzluzl dvykz: nylha dopjolcly nyhcl wylaluk nvsk')
#   'Nonsense words: great whichever grave pretend gold'
#print decryptStory: ('Nonsense words: great whichever grave pretend gold')
#   'Nonsense words: great whichever grave pretend gold'
#print decryptStory: ('Dediudiu mehti: whuqj mxysxuluh whqlu fhujudt webt')
#   'Nonsense words: great whichever grave pretend gold'
#print decryptStory: ('Yprz Uadgtn xh p bniwxrpa rwpgpritg rgtpits dc iwt hejg du p bdbtci\nid wtae rdktg pc xchjuuxrxtcian eapccts wprz. Wt wph qttc gtvxhitgts\nudg raphhth pi BXI ilxrt qtudgt, qji wph gtedgitsan ctktg ephhts p\nraphh. Xi wph qttc iwt igpsxixdc du iwt gthxstcih du Tphi Rpbejh id\nqtrdbt Yprz Uadgtn udg p utl cxvwih tprw ntpg id tsjrpit xcrdbxcv\nhijstcih xc iwt lpnh, btpch, pcs tiwxrh du wprzxcv.\n')
#   'Jack Florey is a mythical character created on the spur of a moment\nto help cover an insufficiently planned hack. He has been registered\nfor classes at MIT twice before, but has reportedly never passed a\nclass. It has been the tradition of the residents of East Campus to\nbecome Jack Florey for a few nights each year to educate incoming\nstudents in the ways, means, and ethics of hacking.\n'
#print decryptStory: ('Qhjr Msvylf pz h tfaopjhs johyhjaly jylhalk vu aol zwby vm h tvtlua\nav olsw jvcly hu puzbmmpjpluasf wshuulk ohjr. Ol ohz illu ylnpzalylk\nmvy jshzzlz ha TPA adpjl ilmvyl, iba ohz ylwvyalksf ulcly whzzlk h\njshzz. Pa ohz illu aol ayhkpapvu vm aol ylzpkluaz vm Lhza Jhtwbz av\niljvtl Qhjr Msvylf mvy h mld upnoaz lhjo flhy av lkbjhal pujvtpun\nzabkluaz pu aol dhfz, tlhuz, huk laopjz vm ohjrpun.\n')
#   'Jack Florey is a mythical character created on the spur of a moment\nto help cover an insufficiently planned hack. He has been registered\nfor classes at MIT twice before, but has reportedly never passed a\nclass. It has been the tradition of the residents of East Campus to\nbecome Jack Florey for a few nights each year to educate incoming\nstudents in the ways, means, and ethics of hacking.\n'
#print decryptStory: ('Jack Florey is a mythical character created on the spur of a moment\nto help cover an insufficiently planned hack. He has been registered\nfor classes at MIT twice before, but has reportedly never passed a\nclass. It has been the tradition of the residents of East Campus to\nbecome Jack Florey for a few nights each year to educate incoming\nstudents in the ways, means, and ethics of hacking.\n')
#   'Jack Florey is a mythical character created on the spur of a moment\nto help cover an insufficiently planned hack. He has been registered\nfor classes at MIT twice before, but has reportedly never passed a\nclass. It has been the tradition of the residents of East Campus to\nbecome Jack Florey for a few nights each year to educate incoming\nstudents in the ways, means, and ethics of hacking.\n'
#print decryptStory: ('Cdchtcht ldgsh: rpkt lpzt rdbudgi lxiwxc qpht raphhxuxrpixdc wdbtrdbxcv ati htt hrpgrt piitcixkt rwpgvt uxcs qtwpkxdg rdhi')
#   'Nonsense words: cave wake comfort within base classification homecoming let see scarce attentive charge find behavior cost'
#print decryptStory: ('Uvuzluzl dvykz: jhcl dhrl jvtmvya dpaopu ihzl jshzzpmpjhapvu ovtljvtpun sla zll zjhyjl haaluapcl johynl mpuk ilohcpvy jvza')
#   'Nonsense words: cave wake comfort within base classification homecoming let see scarce attentive charge find behavior cost'
#print decryptStory: ('Nonsense words: cave wake comfort within base classification homecoming let see scarce attentive charge find behavior cost')
#   'Nonsense words: cave wake comfort within base classification homecoming let see scarce attentive charge find behavior cost'
#print decryptStory: ('Dediudiu mehti: sqlu mqau secvehj myjxyd rqiu sbqiiyvysqjyed xecusecydw buj iuu isqhsu qjjudjylu sxqhwu vydt ruxqlyeh seij')
#   'Nonsense words: cave wake comfort within base classification homecoming let see scarce attentive charge find behavior cost'
#print decryptStory: ('Cdchtcht ldgsh: atpkt xchjgt gtaxvxdc gdjvw rdbeaxrpixdc ixgt heprt xchtri ltardbt ugn gddb paa vgdl bthhpvt ugttot qphzti zxirwtc exrz qgxvwitc hjrw lxcsdl bdstgpit piitbei rdktg qdn lwtc uxct iwt bthhtcvtg excz wdltktg hpsstc qpgt hbddiw iwxc')
#   'Nonsense words: leave insure religion rough complication tire space insect welcome fry room all grow message freeze basket kitchen pick brighten such window moderate attempt cover boy when fine the messenger pink however sadden bare smooth thin'
#print decryptStory: ('Uvuzluzl dvykz: slhcl puzbyl ylspnpvu yvbno jvtwspjhapvu apyl zwhjl puzlja dlsjvtl myf yvvt hss nyvd tlzzhnl myllgl ihzrla rpajolu wpjr iypnoalu zbjo dpukvd tvklyhal haaltwa jvcly ivf dolu mpul aol tlzzlunly wpur ovdlcly zhkklu ihyl ztvvao aopu')
#   'Nonsense words: leave insure religion rough complication tire space insect welcome fry room all grow message freeze basket kitchen pick brighten such window moderate attempt cover boy when fine the messenger pink however sadden bare smooth thin'
#print decryptStory: ('Nonsense words: leave insure religion rough complication tire space insect welcome fry room all grow message freeze basket kitchen pick brighten such window moderate attempt cover boy when fine the messenger pink however sadden bare smooth thin')
#   'Nonsense words: leave insure religion rough complication tire space insect welcome fry room all grow message freeze basket kitchen pick brighten such window moderate attempt cover boy when fine the messenger pink however sadden bare smooth thin'
#print decryptStory: ('Dediudiu mehti: buqlu ydikhu hubywyed hekwx secfbysqjyed jyhu ifqsu ydiusj mubsecu vho heec qbb whem cuiiqwu vhuupu rqiauj ayjsxud fysa rhywxjud iksx mydtem cetuhqju qjjucfj seluh reo mxud vydu jxu cuiiudwuh fyda xemuluh iqttud rqhu iceejx jxyd')
#   'Nonsense words: leave insure religion rough complication tire space insect welcome fry room all grow message freeze basket kitchen pick brighten such window moderate attempt cover boy when fine the messenger pink however sadden bare smooth thin'

#
# Build data structures used for entire session and run encryption
#
if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()