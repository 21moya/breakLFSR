BIT_LENGTH_24 = 0xFFFFFF

def get_xor(state, poly):
    xor = 0
    for p in poly:
        xor ^= ((state >> p - 1) & 1)
    return xor

def main():
    seed = 8897124
    rand = 0
    state = seed
    poly = [2, 4, 5, 7, 8, 10, 11, 14, 16, 18, 21, 24]

    counter = 0

    while True:

        print(f"{counter}: {state:024b}")
        print(f"{rand:032b}")

        xor_bit = get_xor(state, poly)

        new_state = ((state << 1) | xor_bit) & BIT_LENGTH_24

        rand_and = xor_bit << 31
        rand = (rand >> 1) | rand_and

        state = new_state
        counter += 1

        if rand == 576159165:
            break

    print(f"### {counter} Zeiteinheiten. ###")

if __name__ == "__main__":
    main()