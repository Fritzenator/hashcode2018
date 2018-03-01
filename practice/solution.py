def main():
    with open("a_example.in") as input:
        row_count, column_count, vehicle_count, ride_count, bonus, steps_count = tuple(
            map(
                int, input.readline().split(' ')
            )
        )
        grid = []
        for line in input:
            grid.append(list(line.rstrip()))
    print(grid)

    

        

if __name__ == '__main__':
    main()