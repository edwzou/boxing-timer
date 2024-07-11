import time
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')

my_time = int(input("Enter a time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")
pygame.mixer.music.play()

start_time = time.time()
while time.time() - start_time < 5:  # stops after 5 seconds
    if not pygame.mixer.music.get_busy():
        break
    time.sleep(0.1)

pygame.mixer.music.stop()
pygame.quit()
