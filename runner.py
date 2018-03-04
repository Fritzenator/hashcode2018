import time
from solution import solve

def run_benchmark(example_name, input_dataset, output_file):
    print('Processing dataset {name}'.format(name = example_name))

    start_time = time.perf_counter()
    solve(input_dataset, output_file)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    result_string = 'Dataset {name} took {elapsed_time}s'.format(
        name = example_name,
        elapsed_time = elapsed_time
        )
    print(result_string)
    with(open('output_data/benchmark_results.out', 'a')) as bench:
        bench.write(result_string)
        bench.write('\n')


def main():
    run_benchmark('A', 'input_data/a_example.in', 'output_data/a_example.out')
    run_benchmark('B', 'input_data/b_should_be_easy.in', 'output_data/b_should_be_easy.out')
    run_benchmark('C', 'input_data/c_no_hurry.in', 'output_data/c_no_hurry.out')
    run_benchmark('D', 'input_data/d_metropolis.in', 'output_data/d_metropolis.out')
    run_benchmark('E', 'input_data/e_high_bonus.in', 'output_data/e_high_bonus.out')


if __name__ == '__main__':
    main()