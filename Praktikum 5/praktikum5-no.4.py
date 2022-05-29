# function which return reverse of a string

def palindrom(s):
	return s == s[::-1]


# Driver code
s = "sugus"
ans = palindrom(s)

if ans:
    print ("Kalimat: ", s)
    print("Kalimat", s, "adalah palindrom")
else:
    print (s)
    print("Kalimat", s, "bukanlah palindrom")

