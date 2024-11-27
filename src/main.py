import client.client as c
import utils.helpers as h
import time

def main():
    inputs = h.handle_inputs()
    HOST = inputs["host"]
    id = inputs["id"]

    try:
        data = c.client_connection(HOST, "MC", id, "")
        seed = int(data["seed"])
        exp_rand = int(data["rand"])
        poly = h.create_poly_array(data["poly"])
    except:
        print("error while connecting to the server.")
        exit(1)

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
        exit(1)

    if valid:
        print(f"### {counter} time units. ###")
        print(f"process took {time.time()-start_time:.2f} seconds to complete.") 
    else:
        print("something went wrong.")

if __name__ == "__main__":
    main()