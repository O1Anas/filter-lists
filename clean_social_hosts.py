#!/usr/bin/env python3

def clean_hosts_file():
    # Read the input file
    with open('social-only.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Process each line
    cleaned_lines = []
    for line in lines:
        # Remove "0.0.0.0 " from the beginning of the line if it exists
        if line.startswith('0.0.0.0 '):
            cleaned_line = line[8:]  # Remove the first 8 characters (0.0.0.0 + space)
            cleaned_lines.append(cleaned_line)
        else:
            cleaned_lines.append(line)
    
    # Write the cleaned content back to the file
    with open('social-only-NIP.txt', 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)

if __name__ == '__main__':
    clean_hosts_file()
    print("File cleaning completed successfully!") 