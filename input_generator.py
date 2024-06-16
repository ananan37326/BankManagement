import random
import os


def generate_input_for_task1(file_path, initial_reserve, num_transactions, num_queries):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as file:
        file.write(f"{initial_reserve} {num_transactions} {num_queries}\n")

        timestamps = sorted(random.sample(range(1, 10**6), num_transactions))

        for i in range(num_transactions):
            transaction_type = random.choice(["Deposit", "Withdraw"])
            amount = random.randint(1, 10**4)
            file.write(f"{timestamps[i]} {transaction_type} {amount}\n")

        for i in range(num_queries):
            start_time = random.choice(timestamps)
            end_time = random.choice(timestamps)
            if start_time > end_time:
                start_time, end_time = end_time, start_time

            file.write(f"Query {start_time} {end_time}\n")


def generate_input_for_task2(file_path, initial_reserve, num_transactions, num_queries):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as file:
        file.write(f"{initial_reserve}\n")

        timestamps = sorted(
            random.sample(range(1, 10**6), num_transactions + num_queries)
        )

        data = []
        for i in range(num_transactions):
            t_type = random.choice(["Deposit", "Withdraw"])
            amount = random.randint(1, 10000)
            data.append(f"{timestamps[i]} {t_type} {amount}\n")

        for i in range(num_queries):
            start_time = random.choice(timestamps)
            end_time = random.choice(timestamps)
            if start_time > end_time:
                start_time, end_time = end_time, start_time
            end_time += random.randint(1, 1000)
            data.append(f"Query {start_time} {end_time}\n")

        random.shuffle(data)

        file.writelines(data)


def generate_inputs():
    input_dir = "input_files"
    task_1_dir = f"{input_dir}/task1"
    task2_dir = f"{input_dir}/task2"
    input_file_names = [
        "input_1.txt",
        "input_2.txt",
        "input_3.txt",
        "input_4.txt",
        "input_5.txt",
    ]
    initial_reserves = [1000, 5000, 10000, 20000, 50000]
    num_transactions = [10, 100, 1000, 10000, 100000]
    num_queries = [10, 20, 50, 100, 100000]

    test_cases_vars_task1 = [
        (
            f"{task_1_dir}/{input_file_names[i]}",
            initial_reserves[i],
            num_transactions[i],
            num_queries[i],
        )
        for i in range(5)
    ]

    test_cases_vars_task2 = [
        (
            f"{task2_dir}/{input_file_names[i]}",
            initial_reserves[i],
            num_transactions[i],
            num_queries[i],
        )
        for i in range(5)
    ]

    for (
        file_path,
        initial_reserve,
        num_transactions,
        num_queries,
    ) in test_cases_vars_task1:
        generate_input_for_task1(
            file_path, initial_reserve, num_transactions, num_queries
        )
        print(f"Generated input for {file_path} for task 1")

    for (
        file_path,
        initial_reserve,
        num_transactions,
        num_queries,
    ) in test_cases_vars_task2:
        generate_input_for_task2(
            file_path, initial_reserve, num_transactions, num_queries
        )
        print(f"Generated input for {file_path} for task 2")


if __name__ == "__main__":
    generate_inputs()
