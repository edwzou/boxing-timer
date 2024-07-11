import time
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')


def countdown_timer(duration_seconds):
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        current_time = duration_seconds - (time.time() - start_time)
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        print(f"Time remaining: {minutes:02}:{seconds:02}")
        time.sleep(1)
    pygame.mixer.music.play()
    time.sleep(5)  # Play alarm for 5 seconds


num_sets = int(input("Enter number of working sets: "))
work_duration_minutes = int(input("Enter time per working set in minutes: "))
rest_duration_minutes = int(input("Enter time per rest set in minutes: "))


for set_num in range(1, num_sets + 1):
    print(f"Working Set {set_num}")
    countdown_timer(work_duration_minutes * 60)

    if set_num < num_sets:
        print(f"Rest Set {set_num}")
        countdown_timer(rest_duration_minutes * 60)

pygame.quit()
