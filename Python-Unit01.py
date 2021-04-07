msg = [" Python was created in the 1890's by Guido van Rossum. "," Python is maintained as an 'open source' project by a group that is called the Python Software Foundation. "," He is affectionately known as Python's \"Benevolent Dictator for Life\". "]
msg[0] = msg[0].replace("1890", "1990")
for i in range(len(msg)): msg[i] = msg[i].lstrip(" ")
print(msg[0] + msg[2] + msg[1])