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
            println!("{}", number*complement)
        }
        input_data.insert(number);
    }

    Ok(())
}