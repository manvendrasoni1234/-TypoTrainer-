import time
import random
import pygame

def generate_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is the art of telling another human what one wants the computer to do.",
        "Practice like you've never won. Perform like you've never lost.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "The only way to do great work is to love what you do."
    ]
    return random.choice(sentences)

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def typing_test():
    print("Welcome to the Typing Test!\n")
    time.sleep(1)

    sentence = generate_sentence()
    print("Your task is to type the following sentence:\n")
    print(f'"{sentence}"\n')

    input("Press Enter when you are ready to start typing.")
    start_time = time.time()

    user_input = input("\nType the sentence here: ")
    end_time = time.time()

    # Calculate typing speed
    words_per_minute = (len(user_input.split()) / (end_time - start_time)) * 60

    print(f"\nYour typing speed: {words_per_minute:.2f} words per minute.")

    # Provide feedback with sounds
    if words_per_minute >= 70:
        print("Great job! Your typing speed is excellent.")
        play_sound("cong.mp3")  # Replace with the actual sound file
    elif 40 <= words_per_minute < 70:
        print("Good effort! You can improve your typing speed with more practice.")
        play_sound("announcement.mp3")  # Replace with the actual sound file
    else:
        print("You might need more practice. Focus on accuracy, and speed will come with time.")

if __name__ == "__main__":
    typing_test()

