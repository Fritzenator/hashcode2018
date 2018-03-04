import time
from solution import solve

def run_benchmark(example_name, input_dataset, output_file):
    print('Processing Example {name}'.format(name = example_name))

    start_time = time.perf_counter()
    solve(input_dataset, output_file)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print('Example {name} took {elapsed_time}s'.format(
        name = example_name,
        elapsed_time = elapsed_time
        ))


def main():
    run_benchmark('A', 'input_data/a_example.in', 'output_data/a_example.out')
    run_benchmark('B', 'input_data/b_should_be_easy.in', 'output_data/b_should_be_easy.out')


if __name__ == '__main__':
    main()