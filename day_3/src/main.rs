// Get the number of passwords valid according to the password policy.
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

    let lines: Vec<&str> = contents.lines().collect();
    let mut current_x_position = 0;
    let mut tree_count = 0;
    // part one - single increment.
    let increment = 3;
    for line in &lines {
        if line.chars().nth(current_x_position).unwrap() == '#' {
            tree_count += 1
        }
        current_x_position = (current_x_position + increment) % (line.chars().count());
    }
    println!("Number of trees for increment {}: {}", increment, tree_count);

    // part one- multiple increments
    let mut part_two_ans = 1;
    for right_increment in [1,3,5,7].iter() {
        part_two_ans *= count_trees(&lines, *right_increment, 1);
    }
    part_two_ans *= count_trees(&lines, 1, 2);
    println!("Part two answer: {}", part_two_ans);
    Ok(())
}

fn count_trees(lines: &Vec<&str>, right_increment: usize, down_increment: usize) -> usize {
    let mut current_x_position = 0;
    let mut tree_count = 0;
    for line in lines.iter().step_by(down_increment) {
        if line.chars().nth(current_x_position).unwrap() == '#' {
            tree_count += 1
        }
        current_x_position = (current_x_position + right_increment) % (line.chars().count());
    }
    println!("Number of trees for right increment {}, down_increment {}: {}", right_increment, down_increment, tree_count);

    tree_count
}
