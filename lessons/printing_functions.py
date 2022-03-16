# module code meant to show the print design of paper. Ment to import into 8-15
def print_designs(print_begin, done_designs):

    while print_begin:
        design = print_begin.pop()

        # Simulate creating a 3d print from the design.
        print(f"Design- {design}")
        done_designs.append(design)


def show_done(done_designs):
    print("-----Printed------")
    for done_design in done_designs:
        print(done_design)

# commented test code.
#print_begin = ['Logo', 'Text', 'Picture']
#done_designs = []

#print_designs(print_begin, done_designs)
#show_done(done_designs)





