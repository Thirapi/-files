import time

lyrics_and_times = [
    "Udara mana kini yang kau hirup?",
    "Hujan dimana kini yang kau peluk?",
    "Dimana pun kau kini",
    "Rindu tentangmu 'tak pernah pergi",
    "Udara mana kini yang kau hirup?",
    "Hujan dimana kini yang kau peluk?",
    "Dimana pun kau kini",
    "Rindu tentangmu 'tak pernah pergi",
    "Rindu tentangmu 'tak pernah pergi"
]

delays = [7, 7, 7, 7, 7, 7, 7, 7]  #ini delay

def print_lyrics_with_timing():
    start_time = time.time()
    
    for i, line in enumerate(lyrics_and_times):
        print(line)
        if i < len(delays):
            time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics_with_timing()
