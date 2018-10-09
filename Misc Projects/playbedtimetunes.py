#! usr/bin/python3


from selenium import webdriver
import time



musicSelection = [['Lofi Relaxation', 'https://www.youtube.com/watch?v=hHW1oY26kxQ'],
				 ['Classical', 'https://www.youtube.com/watch?v=rLMHGjoxJdQ'],
				 ['Indie Rock', 'https://www.youtube.com/watch?v=JdWvHnZUJIA'],
				 ['Jazz', 'https://www.youtube.com/watch?v=Vls4h1GAP-c'],
				 ['Water Sounds', 'https://www.youtube.com/watch?v=Ev1CWj7ZhcQ'],
				 ['Jazz and Guitar', 'https://www.youtube.com/watch?v=2ccaHpy5Ewo']]



def playBedTimeTunes(lengthofPlay, musictoPlay):
	browser = webdriver.Firefox()
	browser.get(musictoPlay)
	time.sleep(lengthofPlay)
	browser.close()



print('input the length of time you want music to play in minutes.')
minutesofPlay = int(input())
print('input the number corresponding to the playlist you want to hear:')
for i in range(len(musicSelection)):
	print(str(i) + ' ' + musicSelection[i][0])
desiredMusic = int(input())
playBedTimeTunes(minutesofPlay * 60, musicSelection[desiredMusic][1])