#![allow(dead_code)]  // allow unused code
#![allow(unused_imports)]  // allow unused imports
#![allow(unused_variables)]  // allow unused variables


/*
    Project: {{cookiecutter.project_slug}}
    {{cookiecutter.project_short_description}}
    
    Author: {{cookiecutter.author_name}}
 */


mod components;

mod util;
use util::terminal;

mod config;  // make the config module public
use config::globals::{
    APP_NAME, 
    APP_VERSION,
    APP_AUTHOR
};    


/// App Entry Point
/// 
/// 
fn main() {
    terminal::clear();  // clear and reset the terminal
    println!("\x1b[32m{}\x1b[0m {}\n", APP_NAME, APP_VERSION);

    // code...
}
