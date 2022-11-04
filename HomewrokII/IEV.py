def dom_off(x):
    my_input = (1*x[0] + 1*x[1] + 1*x[2] + 0.75*x[3] + 0.5*x[4] + 0*x[5]) * 2
    return my_input

if __name__ == "__main__":
    with open("/Users/lorenzopossanzini/Desktop/Rosalind/rosalind_iev.txt", "r") as my_sample:
        x = [float(el) for el in my_sample.readline().strip().split(" ")]
    print(dom_off(x))