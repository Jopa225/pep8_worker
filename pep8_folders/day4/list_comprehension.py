
demo_list = [
                [10, "20", "45"],
                [35, 42, 20],
                [10],
                (0, 133, (45, 10))
            ] 
print(demo_list)


demo_list = [int(y) for x in demo_list for y in x if x.index(y) == 1]

# demo_list[0] = (int)demo_list[0]
print(demo_list)
print(sum(demo_list))