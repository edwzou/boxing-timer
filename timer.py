import time
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sound.mp3')


def countdown_timer(duration_seconds):
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        current_time = duration_seconds - (time.time() - start_time)
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        print(f"Time remaining: {minutes:02}:{seconds:02}")
        time.sleep(1)
    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    start_sound_time = time.time()
    while time.time() - start_sound_time < 5:
        if not pygame.mixer.music.get_busy():
            break
        time.sleep(0.1)
    pygame.mixer.music.stop()


warmup_time = int(input("Enter time of warmup in seconds: "))
num_sets = int(input("Enter number of working sets: "))
work_duration_minutes = int(input("Enter time per working set in minutes: "))
rest_duration_minutes = int(input("Enter time per rest set in minutes: "))


print("Warmup Time")  # warmup period
countdown_timer(warmup_time)

for set_num in range(1, num_sets + 1):  # working and resting sets
    print(f"Working Set {set_num}")
    countdown_timer(work_duration_minutes * 60)

    if set_num < num_sets:
        print(f"Rest Set {set_num}")
        countdown_timer(rest_duration_minutes * 60)

pygame.quit()
