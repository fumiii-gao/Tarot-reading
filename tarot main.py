import random
import datetime
import Tarot_cards 
from Tarot_cards import Tarotcard
import Tarotdeck
from Tarotdeck import Deck



def yes_no_reading():
    print('\nYES / NO Reading')
    while True:
        pick = input('Enter lucky number (0-79): ')
        if not pick.isdigit() or not (0 <= int(pick) <= 79):
            print('Invalid request.')
        else:
            break
    card = random.choice(Deck)
    card.display_YoN()
    
restore_today = []
def daily_tarot():
    print('\nDaily Tarot')
    today = str(datetime.date.today())
    for r in restore_today:
        if r[0] == today:
            print("\nYou already chose today's card: ")
            print(f'Daily card: {r[1]}')
            return 
    print(f'Today: {today}')
    daily_deck = [card for card in Deck if card.yes_or_no.strip().lower() == 'yes']
    card = random.choice(Deck)
    card.display_Daily()
    restore_today.append([today,card.name])

restore_cus = []
def custom_question():
    print('\nCustom 3-Card Reading')   
    while True:
        question = input('Enter your question title: ').strip()
        if question:
            break
        print('Please enter a title.')

    prep = input('Shuffle or Pick? ').strip().lower()
    if prep == 'shuffle':
        print('(Cards shuffled...)')  
    else:
        print('(Proceeding to pick...)')

    print('Please pick your three cards.')
    chosen_cards = []
    while len(chosen_cards) < 3:
        try:
            pick = int(input(f'Enter number {len(chosen_cards)+1} (1-79): '))
            if not (1 <= pick <= 79):
                raise ValueError
            card = random.choice(Deck)
            if card not in chosen_cards:
                card.orientation = random.choice(['Upright', 'Reversed'])
                chosen_cards.append(card)
            else:
                print('Card already chosen. Try again.')
        except ValueError:
            print('Invalid input. Please enter a number from 1 to 79.')

    today = str(datetime.date.today())
    for card in chosen_cards:
        card.display_cus()
    restore_cus.append([today, question] + [(c.name, c.orientation) for c in chosen_cards])

    while True:
        option = input('\n1.Check restore | 2.Ask for professional help | 3.Menu : ')
        if option == '1':
            print('\nLast 3-card reading:')
            print(restore_cus[-1])
            break
        elif option == '2':
            print('\nPlease contact wechat: Alnannn')
            break
        elif option == '3':
            break
        else:
            print('Invalid request. Please enter 1, 2, or 3.')

def card_meanings():
    search_mode = input("Search by name or number? (name/number): ").strip().lower()

    if search_mode == "name":
        name_input = input("Enter the name of the card (case insensitive): ").strip().lower()
        for card in Deck:
            if card.name.lower() == name_input:
                card.display_show()
                return
        print("Card not found.")
        return
    elif search_mode == "number":
        while True:
            pick_arcana = input('Major arcana | Minor arcana: ').strip().lower()
            if pick_arcana in ['major arcana', 'major']:
                print("Available Major Arcana:")
                for card in Deck:
                    if card.suit == "major":
                        print(f"{card.suit_number}. {card.name}")

                while True:
                    try:
                        pick_number = int(input('Enter a number (0-21): '))
                        break
                    except ValueError:
                        print('Invalid number.')

                for card in Deck:
                    if card.suit == 'major' and card.suit_number == pick_number:
                        card.display_show()
                        return
                print('Card not found.')
                return

            elif pick_arcana in ['minor arcana', 'minor']:
                valid_suits = ['cups', 'pentacles', 'swords', 'wands']
                pick_suit = input('Cups | Pentacles | Swords | Wands: ').strip().lower()
                if pick_suit not in valid_suits:
                    print('Invalid suit.')
                    continue

                print(f"Available cards in {pick_suit.title()}:")
                for card in Deck:
                    if card.suit == pick_suit:
                        print(f"{card.suit_number}. {card.name}")

                try:
                    pick_number = int(input("Enter number (1-14): "))
                except ValueError:
                    print('Invalid number.')
                    return

                for card in Deck:
                    if card.suit == pick_suit and card.suit_number == pick_number:
                        card.display_show()
                        return
                print('Card not found.')
                return
            else:
                print('Invalid request.')
    else:
        print('Invalid request.')
    

username = None
def main_menu():
    global username
    if username is None:
        username = input('Enter your name: ')
        print(f'\n{username}, welcome!')
    while True:
        print("\n===== Moon and rose =====")
        print('1. HELP')
        print('2. Function')
        print('3. Tarot meaning')
        print('4. Restore')
        print('5. Exit')
        choice = input("Choose an option: ")

        if choice == "1":
            print('\nMoon and rose is an interesting tarot reading system, it can help you quickly find your path. It prepares 3 different functions for you to choose.')
            print('Function one: Yes/No question. You can ask a question and receive a result.')
            print('Function two: Daily tarot. The tarot card of your day. ')
            print("Function three: three cards. It's the simplest way to know your need.")
            print('You can also find what you read in Restore.')
        elif choice == "2":
            print('1. Yes/No question')
            print('2. Daily tarot')
            print('3. three cards')
            cho = input('Choose an option: ')
            if cho == '1':
                yes_no_reading()
            elif cho == '2':
                daily_tarot()

            elif cho == '3':
                custom_question()
            else:
                print('Invalid request.')

        elif choice == "3":
            card_meanings()

            
        elif choice == '4':
            while True:
                record_cho = input('1. Daily record | 2. Custom record: ')
                if record_cho == '1':
                    print('\nDaily record: ')
                    print(restore_today)
                    break
                elif record_cho == '2':
                    print('\nCustom record: ')
                    for i in restore_cus:
                        print(i)
                    break
                else:
                    print('Invalid request. Please enter 1 or 2.')


    
        elif choice == "5":
            print('Exit')
            break
        else:
            print('Invalid option. Try again.')

if __name__ == "__main__":
    main_menu()