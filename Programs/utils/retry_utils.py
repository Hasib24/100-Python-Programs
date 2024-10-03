from colorama import Fore, Style
def retry():
    ret_inp = input(f"Do you want to retry ? ({Fore.GREEN}y{Style.RESET_ALL}/q) : ").lower()
    if ret_inp != "y":
        quit()
    else: True