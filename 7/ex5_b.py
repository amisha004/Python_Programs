dobin = input ("Enter the birth date: ")
doblist = dobin.split("/")
dob = '-'.join(doblist)
mydob = {"Birthday": dob}
if 'Birthday' in mydob:
    print (mydob['Birthday'])
