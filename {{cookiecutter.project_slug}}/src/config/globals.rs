// globals is a module that contains global variables that are used throughout the application

// use::std::sync::Mutex;  // Mutex is a type that allows only one thread to access the data at a time
// lazy_static! {  
//     pub static ref GLOBALS: Mutex<Globals> = Mutex::new(Globals::new());
// }

// global variables (constants)
pub const APP_NAME: &str = "{{cookiecutter.project_slug}}";
pub const APP_VERSION: &str = "v0.1";
pub const APP_AUTHOR: &str = "{{cookiecutter.author_name}}";
