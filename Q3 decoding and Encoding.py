letters='abcdefghijklmnopqrstuvwxyz1234567890 )'
dictionary=letters[-1] + letters[0:-1] + 'prmac'
endict=dict(zip(letters,dictionary))
dedict=dict(zip(dictionary,letters))
mes=input('Please enter a msg ')
typee=input('E for encoding , D for decoding ')
if typee=='E':
    msg=''.join([endict[let] for let in mes.lower()])
elif typee=='D':
    msg=''.join([dedict[let] for let in mes.lower()])
else:
    print('please try again ')
print(msg)