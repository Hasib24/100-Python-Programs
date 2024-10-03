from colorama import Fore, Style
from utils.terminal_utils import clear_terminal
from utils.retry_utils import retry


def sort_words_program():
    while True:
        clear_terminal()
        print(f"{Fore.GREEN}Welcome to Sorting Words Program{Style.RESET_ALL}")

        try:
            words_list = input(
                f"{Fore.YELLOW}Enter words to sort,\nUse comma(,) to separate words\n: {Style.RESET_ALL}"
            )
            if not words_list:
                raise ValueError("Input cannot be empty")

            words_list = words_list.split(",")

            cleaned_words = [word.strip() for word in words_list]

            sorted_words = sorted(cleaned_words)

            clear_terminal()
            print(f"{Fore.CYAN}\nSorted words:\n{sorted_words}{Style.RESET_ALL}")
            break  # Exit the loop if everything is successful
        except ValueError as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            retry()


if __name__ == "__main__":
    sort_words_program()
