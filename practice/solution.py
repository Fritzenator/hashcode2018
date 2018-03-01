def main():
    with open("example.in") as input:
        row_count, column_count, min_ingridient, max_area = tuple(
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