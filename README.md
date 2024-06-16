# Bank Management

## Overview

This repository contains the solution to the problem of processing transactions and handling queries in a randomized order. The project includes code for both Task 1 and Task 2, along with an input generator to create sample input files. The solution is dockerized for easy setup and execution.

## Table of Contents

- [Bank Management](#bank-management)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Running Locally](#running-locally)
  - [Running Dockerized Application](#running-dockerized-application)
  - [Clarifying Assumptions](#clarifying-assumptions)
  

## Prerequisites

- Docker Desktop
- Git
- Python 

## Setup

1. Clone the repository
```bash
git clone https://github.com/ananan37326/BankManagement.git
```

2. Change directory to the project folder
```bash
cd BankManagement
```

## Running Locally

1. Run the following command to generate sample input files
```bash
python3 input_generator.py
```

2. Run the following command to run the application and generate the output for both task1 and task2
```bash
python3 task.py
```

## Running Dockerized Application

1. Build the docker image
```bash
docker-compose build
```

2. Run the input generator to generate a sample input file
```bash
docker-compose run input_generator
```

3. Run the application to generate the output for both task1 and task2
```bash
docker-compose up
```

## Clarifying Assumptions

1. For task1, the declined transactions before the end_time of each query are considered for reprocessing. Transactions before and after reorganization are compared by length. For example, if there were 3 declined transactions before reorganization and 2 declined transactions after reorganization, the output will be 1. the declined transactions after the end_time of a query are not considered for reprocessing. Negative output means after reorganization, the number of declined transactions increased.

2. For task2, the transactions before each query are considered. If the end_time of a query is later than the latest transaction timestamp before that query, the effective end time is considered, which is the earliest of the end_time of the query and the latest transaction timestamp before that query. The transactions after the end_time of a query are not considered. 

3. The sample output for task2 looks like a wrong one. The correct output should be
```
0
1
1
2
```

