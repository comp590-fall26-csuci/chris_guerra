#!/bin/bash

# this script reads a txt file containing unsorted passwords, sorts them, prints them out to the console,
# then creates a file for each password containing the password text

# function to read the contents of the file and sort them
sort_file() {
	local input_file="$1"
	mapfile -t sorted_strings < <(sort "$input_file")
}

# function to iterate through the sorted strings and process each string
file_loop() {
	# store argument in local variable
	local -n strings="$1"

	# iterate through strings and process each one
	for i in "${!strings[@]}"; do

		# create a filename to store the password
		filename=$(printf "password_%d.txt" "$((i + 1))")

		# print string and write to file
		proc_string "${strings[$i]}" "$filename"
	done
}

# function to take a string and filename and process it
# prints the string to console and creates a new file containing the string
proc_string() {
	local text="$1" # the text to write
	local filename="$2" # the file to write to
	echo "$text"
	echo "$text" > "$filename"
}

# first argument is the txt file containing passwords
sort_file "$1"

# iterate through strings and process each one
file_loop sorted_strings



