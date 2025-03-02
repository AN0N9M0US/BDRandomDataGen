import random
import time
import sys
import itertools
import os

def animate_text(text, color_code="\033[92m"):
    for char in text:
        sys.stdout.write(color_code + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_logo():
    logo = """
  _____                 _                   _____        _        
 |  __ \               | |                 |  __ \      | |       
 | |__) |__ _ _ __   __| | ___  _ __ ___   | |  | | __ _| |_ __ _ 
 |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \  | |  | |/ _` | __/ _` |
 | | \ \ (_| | | | | (_| | (_) | | | | | | | |__| | (_| | || (_| |
 |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_| |_____/ \__,_|\__\__,_|

    """
    colors = ["\033[91m", "\033[92m"]
    for color in itertools.cycle(colors):
        clear_console()
        animate_text(logo, color)
        time.sleep(0.2)
        break

def generate_bd_phone_number():
    prefixes = ["013", "014", "015", "016", "017", "018", "019"]
    return [random.choice(prefixes) + "".join([str(random.randint(0, 9)) for _ in range(8)]) for _ in range(20)]

def generate_random_gmail():
    names = ["rakib", "mehedi", "sumaiya", "arif", "tanha", "hasib", "tasnim", "jahid"]
    return [random.choice(names) + str(random.randint(100, 999)) + "@gmail.com" for _ in range(20)]

def generate_bd_name(category):
    male_names = [
        "Rakib", "Arif", "Hasib", "Jahid", "Mehedi", "Shakib", "Nayeem", "Samiul", "Rahat", "Arafat",
        "Sabbir", "Nadim", "Tareq", "Farhan", "Mahmud", "Ashraf", "Tuhin", "Sajid", "Ehsan", "Imran",
        "Kamrul", "Shamim", "Habib", "Sohag", "Tanvir", "Shihab", "Shahin", "Zubair", "Fahim", "Hafiz",
        "Sami", "Fuad", "Bashir", "Kabir", "Omar", "Asif", "Sifat", "Shuvo", "Fardin", "Riyad",
        "Tahmid", "Kawsar", "Aminul", "Shahriar", "Touhid", "Anis", "Milon", "Hasan", "Zakir", "Nashir"
    ]

    female_names = [
        "Sumaiya", "Tanha", "Tasnim", "Nusrat", "Jannat", "Maliha", "Sadia", "Raisa", "Sanji", "Lamia",
        "Mim", "Farzana", "Samira", "Ritu", "Tania", "Afia", "Nafisa", "Afsana", "Tithi", "Nabila",
        "Sharmin", "Faria", "Anika", "Joya", "Puja", "Moushumi", "Mahjabin", "Ayesha", "Shila", "Sanjida",
        "Lubna", "Nasrin", "Sultana", "Ruba", "Sadia", "Mehjabin", "Jui", "Sakila", "Shaila", "Marufa",
        "Nargis", "Rupali", "Tasfia", "Mahi", "Sanjana", "Dipa", "Khadija", "Humayra", "Rizwana", "Zerin"
    ]

    if category == "male":
        return [random.choice(male_names) for _ in range(20)]
    elif category == "female":
        return [random.choice(female_names) for _ in range(20)]
    else:
        return [random.choice(male_names + female_names) for _ in range(20)]

# Animated Logo
animated_logo()

# Category selection
animate_text("\n===== Welcome to the Random Data Generator =====", "\033[92m")
animate_text("Developed By TG: @SecureStacksNetwork", "\033[92m")
print("\nSelect a category:")
print("1. 20 Random Bangladeshi Phone Numbers")
print("2. 20 Random Gmail Addresses")
print("3. 20 Random Bangladeshi Names")

category = input("\nEnter category (1, 2, 3): ")

if category == "1":
    animate_text("Generating 20 Random Bangladeshi Phone Numbers...", "\033[92m")
    print("\033[91m" + "\n".join(generate_bd_phone_number()) + "\033[0m")
elif category == "2":
    animate_text("Generating 20 Random Gmail Addresses...", "\033[92m")
    print("\033[91m" + "\n".join(generate_random_gmail()) + "\033[0m")
elif category == "3":
    gender = input("Enter gender (male/female/any): ").strip().lower()
    animate_text("Generating 20 Random Bangladeshi Names...", "\033[92m")
    print("\033[91m" + "\n".join(generate_bd_name(gender)) + "\033[0m")
else:
    animate_text("Invalid category selection! Please try again.", "\033[92m")
