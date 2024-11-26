import client.client as c
import utils.helpers as h
import time

BIT_LENGTH_24 = 0xFFFFFF

def main():
    inputs = h.handle_inputs()
    HOST = inputs["host"]
    id = inputs["id"]

    try:
        data = c.client_connection(HOST, "MC", id, "")
    except:
        print("error while connecting to the server.")

    seed = int(data["seed"])
    exp_rand = int(data["rand"])
    poly = h.create_poly_array(data["poly"])

    rand = 0
    state = seed
    counter = 0

    start_time = time.time()
    print("### calculating. this may take a while... ###")

    while True:
        if rand == exp_rand:
            break
        elif counter > 2**24:
            print("### not found ###")
            exit(1)

        xor_bit = h.get_xor(state, poly)

        state = (state >> 1) | (xor_bit << 23)
        rand = (rand >> 1) | (xor_bit << 31) 

        counter += 1

    try:
        valid = c.client_connection(HOST, "MCV", id, str(counter))
    except:
        print("error while connecting to the server.")

    print(f"### {counter} time units. ###\nprocess took {time.time()-start_time:.2f} seconds to complete.") if valid else print("### something went wrong. ###")

if __name__ == "__main__":
    main()