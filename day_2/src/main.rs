// Get the number of passwords valid according to the password policy.
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
    let mut valid_passwords: usize = 0;
    let mut part_two_valid_passwords: usize = 0;
    // let mut input_data = vec![];
    for line in lines {
        // Part 1:
        // Format is e.g 1-3 <char>: <password> where the range is the number of occurences of char
        let split_line: Vec<&str> = line.trim().split(|c| c == ':' || c == '-'  || c == ' ').collect();

        let lower_bound: usize = split_line[0].parse::<usize>()?;
        let upper_bound: usize = split_line[1].parse::<usize>()?;
        let character: &str = split_line[2];
        let password: &str = split_line[4];

        // Part 1
        // Count the number of occurrences of the character in the password.
        let num_occurrences: usize = password.matches(character).count();

        if (lower_bound <= num_occurrences) && (num_occurrences <= upper_bound) {
            valid_passwords += 1;
        }

        // Part 2
        // 1-3 <char> describes two positions: char must occur exactly once in one of those positions.
        let password_char_one = password.chars().nth(lower_bound-1).unwrap();
        let password_char_two = password.chars().nth(upper_bound-1).unwrap();
        if (password_char_one == character.chars().nth(0).unwrap() )
         ^ (password_char_two == character.chars().nth(0).unwrap() ) {
            part_two_valid_passwords += 1;
        }


    }

    println!("{} valid passwords", valid_passwords);
    println!("{} part two valid passwords", part_two_valid_passwords);

    Ok(())
}