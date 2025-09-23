import random
import time

x = random.randint(0, 4) 
life = 3 

emoticon = (":)", ":(", ":O", ":p", ":3") 
emoticon_meaning = ("smiling", "sad", "shocked", "tongue out", "silly") 

emoticon_random = emoticon[x] 
emoticon_meaning_random = emoticon_meaning[x] 

while life != 0: 
	emoticon_guess = input("The emoji description is *" + emoticon_meaning_random + "*, Can you guess which emoji it is? ") 
	if emoticon_guess == emoticon_random:  
		break 
	else: 
		life -= 1 
		print("oh no.. that was wrong") 
if life == 0:
	print("good luck next time!")
else:
	print("good job on getting that!")
time.sleep(2)
quit()

