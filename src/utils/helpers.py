def get_xor(state, poly):
    xor = 0
    for p in poly:
        xor ^= ((state >> (24 - int(p))) & 1)
    return xor

def create_poly_array(poly):
    arr = []
    for p in poly:
        if p.split(" ")[0] != "[]" or not p.split(" ")[0]:
            arr.append(p.split(" ")[0])
    arr.pop(0)
    return arr

def handle_inputs():
    while True:
        choice = input("local (1) or HS network (2)? ")
        if choice == "1":
            HOST = "localhost"
            break
        elif choice == "2":
            HOST = "10.32.31.18"
            break
        else:
            print("wrong input detected.")

    while True:
        id = input("please enter your student ID: ")
        if len(id) > 7 or len(id) < 6:
            print("student ID has to be 6 or 7 digits long.")
            continue
        else: 
            break

    return {"host": HOST, "id": id}