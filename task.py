import os


def parse_input(file_path, random_query=False):
    with open(file_path, "r") as file:
        lines = file.readlines()

    if random_query:
        initial_reserve = int(lines[0].strip())
    else:
        initial_reserve, num_transactions, num_queries = map(
            int, lines[0].strip().split()
        )
    transactions = []
    queries = []
    transactions_count = 0

    for line in lines[1:]:
        parts = line.strip().split()
        if parts[0] == "Query":
            if random_query:
                queries.append((int(parts[1]), int(parts[2]), transactions_count))
            else:
                queries.append((int(parts[1]), int(parts[2])))

        else:
            transactions.append((int(parts[0]), parts[1], int(parts[2])))
            transactions_count += 1

    return initial_reserve, transactions, queries


def process_transactions(transactions, initial_reserve):
    reserve = initial_reserve
    # Declined transactions
    declined = []

    # Process each transaction
    for timestamp, t_type, amount in transactions:
        # Check if the transaction is a deposit
        if t_type == "Deposit":
            # Add the amount to the reserve
            reserve += amount

        # Check if the transaction is a withdraw
        elif t_type == "Withdraw":
            # Check if the reserve is greater than or equal to the amount
            if reserve >= amount:
                reserve -= amount
            else:
                declined.append((timestamp, t_type, amount))

    # Return the final declined transactions
    return declined


def handle_query_for_task1(transactions, start_time, end_time, initial_reserve):
    # Transactions before the query start time
    pre_query_transactions = [t for t in transactions if t[0] < start_time]

    # Transactions within the query time frame
    in_range_transactions = [t for t in transactions if start_time <= t[0] < end_time]

    # Actual order of transactions up until end_time
    upto_end_time_transactions = [t for t in transactions if t[0] <= end_time]

    # Process transactions before the query to get the previously declined transactions
    declined_pre_query = process_transactions(pre_query_transactions, initial_reserve)

    # Separate the deposits and withdraws from the in_range_transactions
    deposits = [t for t in in_range_transactions if t[1] == "Deposit"]
    withdraws = [t for t in in_range_transactions if t[1] == "Withdraw"]

    # Remove the declined_pre_query transactions from the pre_query_transactions
    pre_query_transactions = [
        t for t in pre_query_transactions if t not in declined_pre_query
    ]

    # Reorder the transactions such that we can process any previously declined transactions after we get the deposits
    reordered_transactions = (
        pre_query_transactions + deposits + declined_pre_query + withdraws
    )

    # Process the reordered transactions to get the final declined transactions
    declined = process_transactions(reordered_transactions, initial_reserve)

    # process the transaction in order to get the previous declined transactions
    declined_previous = process_transactions(
        upto_end_time_transactions, initial_reserve
    )

    # Calculate the difference between the declined transactions from the previous transactions and the declined transactions from the reordered transactions
    reprocessed_count = len(declined_previous) - len(declined)

    return reprocessed_count


def handle_query_for_task_2(
    transactions, start_time, end_time, initial_reserve, transactions_count
):
    # Get the timestamp of the last transaction before index transactions_count and find the effective end time
    # +1 to include the last transaction in the query
    effective_end_time = min(transactions[transactions_count - 1][0] + 1, end_time)

    # Transactions before the query start time
    pre_query_transactions = [t for t in transactions if t[0] < start_time]

    # Transactions within the query time frame, up to the effective end time
    in_range_transactions = [
        t for t in transactions if start_time <= t[0] < effective_end_time
    ]

    # Actual order of transactions up until the effective end time
    upto_end_time_transactions = [t for t in transactions if t[0] < effective_end_time]

    # Process transactions before the query to get the previously declined transactions
    declined_pre_query = process_transactions(pre_query_transactions, initial_reserve)

    # Separate the deposits and withdraws from the in_range_transactions
    deposits = [t for t in in_range_transactions if t[1] == "Deposit"]
    withdraws = [t for t in in_range_transactions if t[1] == "Withdraw"]

    # Remove the declined_pre_query transactions from the pre_query_transactions
    pre_query_transactions = [
        t for t in pre_query_transactions if t not in declined_pre_query
    ]

    # Reorder the transactions such that we can process any previously declined transactions after we get the deposits
    reordered_transactions = (
        pre_query_transactions + deposits + declined_pre_query + withdraws
    )

    # Process the reordered transactions to get the final declined transactions
    declined = process_transactions(reordered_transactions, initial_reserve)

    # Process the transaction in order to get the previous declined transactions
    declined_previous = process_transactions(
        upto_end_time_transactions, initial_reserve
    )

    # Calculate the difference between the declined transactions from the previous transactions and the declined transactions from the reordered transactions
    reprocessed_count = len(declined_previous) - len(declined)

    return reprocessed_count


def main(input_file, output_file, random_query=False):
    # Parse the input file
    initial_reserve, transactions, queries = parse_input(input_file, random_query)

    # Process each query
    results = []

    if random_query:
        for query in queries:
            start_time, end_time, transactions_count = query
            result = handle_query_for_task_2(
                transactions, start_time, end_time, initial_reserve, transactions_count
            )
            results.append(result)
    else:
        for query in queries:
            start_time, end_time = query
            result = handle_query_for_task1(
                transactions, start_time, end_time, initial_reserve
            )
            results.append(result)

    # Write the results to the output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as file:
        for result in results:
            file.write(f"{result}\n")


if __name__ == "__main__":
    input_dir, output_dir = "input_files", "output_files"

    task1_subdir, task2_subdir = "task1", "task2"

    tasks = [
        {"subdir": task1_subdir, "random_query": False},
        {"subdir": task2_subdir, "random_query": True},
    ]

    input_files = [
        "input_1.txt",
        "input_2.txt",
        "input_3.txt",
        "input_4.txt",
        "input_0.txt",
    ]
    output_files = [
        "output_1.txt",
        "output_2.txt",
        "output_3.txt",
        "output_4.txt",
        "output_0.txt",
    ]

    # input_5 contains the largest input size, and it takes a while to generate the output, so we will skip it for now
    # if needed, you can uncomment the line below to generate the output for input_5

    # input_files.append("input_5.txt")
    # output_files.append("output_5.txt")

    for task in tasks:
        for i in range(len(input_files)):
            input_file = f"{input_dir}/{task['subdir']}/{input_files[i]}"
            output_file = f"{output_dir}/{task['subdir']}/{output_files[i]}"
            main(input_file, output_file, task["random_query"])
            print(f"Generated output for {input_file} for {task['subdir']}!")

    print("All outputs generated successfully!")
