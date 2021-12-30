#####################################################
#   Code Wars: MUMBLING
#####################################################

def accum(s):
    output = ""
    for letterIdx in range( len(s) ) :
        for idx in range( letterIdx+1 ) :
            # print ( s[letterIdx] )
            ltr = s[letterIdx]
            print (ltr.upper())
    return output

print ("abcd:", accum("abcd"));