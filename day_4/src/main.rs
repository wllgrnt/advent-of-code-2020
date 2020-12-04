/*
The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

 passports are key:value pairs separated by whitespace.
 passports are separated by newlines   
*/
// Get the number of passports with all fields barring cid
use std::error::Error;
use std::fs;
use std::process;
use std::collections::HashSet;

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

    let lines: Vec<&str> = contents.split(|c| c == '\n' || c == ' ').collect();
    
    let required_fields: HashSet<&str> = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].iter().cloned().collect();
    let mut valid_passports = 0;
    let mut found_fields: HashSet<&str> = HashSet::new();
    for line in &lines {
        // iterate over these key:value pairs. If you see an empty line, clear the hashset.
        // If you see all the fields, valid passport += 1
        let mut key = line.split(|c| c == ':').next().unwrap();
        if key == "" {
            found_fields.clear();
        }
        else if required_fields.contains(&key) {
            found_fields.insert(&key);
        }
        if found_fields == required_fields {
            valid_passports += 1;
            found_fields.clear();

        }
    }

    println!("{} valid passports", valid_passports);

    Ok(())
}
