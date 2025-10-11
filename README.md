# Codeforces Solutions

A collection of my solutions to competitive programming problems from [Codeforces](https://codeforces.com/).

## Repository Structure

Each problem is organized in its own directory following the naming convention:
```
{N}-{ProblemID}-{ProblemName}/
├── problem.md       # Problem statement and examples
├── solution.py      # Solution implementation
└── input.txt        # Sample input for testing
```

Where:
- `{N}` is the sequential solve number (1, 2, 3...)
- `{ProblemID}` is the official Codeforces problem ID (e.g., 4A, 71A, 231A)
- `{ProblemName}` is a descriptive name for the problem

## Current Solutions

| # | Problem ID | Problem Name | Difficulty | Category |
|---|------------|--------------|------------|----------|
| 1 | [4A](https://codeforces.com/problemset/problem/4/A) | Watermelon | 800 | Math |
| 2 | [71A](https://codeforces.com/problemset/problem/71/A) | Way Too Long Words | 800 | Strings |
| 3 | [231A](https://codeforces.com/problemset/problem/231/A) | Team | 800 | Implementation |

## Getting Started

### Prerequisites
- Python 3.x installed on your system
- Basic understanding of competitive programming concepts

### Running Solutions

To test a specific solution:
```bash
python3 {problem_directory}/solution.py < {problem_directory}/input.txt
```

Example:
```bash
python3 1-4A-watermelon/solution.py < 1-4A-watermelon/input.txt
```

### Testing All Solutions

Run this script to test all solutions at once:
```bash
for dir in */; do
    if [[ -f "$dir/solution.py" && -f "$dir/input.txt" ]]; then
        echo "Testing $dir:"
        python3 "$dir/solution.py" < "$dir/input.txt"
        echo "---"
    fi
done
```

## Adding New Problems

1. Create a new directory:
   ```bash
   mkdir {next_number}-{problem_id}-{problem_name}
   cd {next_number}-{problem_id}-{problem_name}
   ```

2. Create the required files:
   ```bash
   touch problem.md solution.py input.txt
   ```

3. Add the problem statement to `problem.md` (include the Codeforces URL at the top)
4. Implement your solution in `solution.py`
5. Add sample input from the problem to `input.txt`
6. Test your solution before committing

## Solution Approach

All solutions follow these principles:
- **Language**: Python 3 for readability and quick implementation
- **Input/Output**: Standard input/output using `input()` and `print()`
- **Style**: Clean, readable code optimized for competitive programming
- **Testing**: Each solution includes sample input for verification

## Problem Categories

- **Mathematical**: Number theory, divisibility, modular arithmetic
- **String Processing**: Manipulation, parsing, pattern matching  
- **Implementation**: Logic, simulation, basic algorithms
- **Data Structures**: Arrays, lists, basic operations

## Contributing

This is a personal learning repository, but feel free to:
- Suggest optimizations to existing solutions
- Point out edge cases or bugs
- Discuss alternative approaches

## Resources

- [Codeforces](https://codeforces.com/) - The main platform
- [Codeforces Problemset](https://codeforces.com/problemset) - Browse problems
- [CP-Algorithms](https://cp-algorithms.com/) - Algorithm reference

## License

This project is open source and available under the [MIT License](LICENSE).