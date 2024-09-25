def retry():
    ret_inp = input("Do you want to retry ? (y/q) : ").lower()
    if ret_inp != "y":
        quit()
    else: True