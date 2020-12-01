// For each element, add the number x to the set.
// Check if 2020-x is in the set. If True, return x*(2020-x)
// Otherwise, continue
use std::collections::HashSet;
use std::error::Error;
use std::fs;
use std::process;

fn main() {
    let input_filename = "input.txt";
    if let Err(e) = run(input_filename) {
        println!("Application error: {}", e);
        process::exit(1);
    }
}

fn run(filename: &str) -> Result<(), Box<dyn Error>> {
    // Parse into a vector of ints
    let contents = fs::read_to_string(filename)?;

    let lines = contents.lines();
    let mut input_data = HashSet::new();
    for line in lines {
        let number = line.trim().parse::<i64>()?;
        let complement = 2020-number;
        if input_data.contains(&complement) {
            println!("Part 1: {}", number*complement);
        }
        input_data.insert(number);
    }

    // Now we need to find three numbers that sum to 2020.
    // As before, but double-iterating.
    'outer: for number_one in &input_data {
        for number_two in &input_data {
            let sum = number_one + number_two;
            let complement = 2020-sum;
            if input_data.contains(&complement) {
                println!("Three numbers are {}, {}, and {}", number_one, number_two, complement);
                println!("Multiplied, its {}", number_one*number_two*complement);
                break 'outer;
            }

        }
    }


    Ok(())
}