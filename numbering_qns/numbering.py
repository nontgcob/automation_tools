def number_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        question_number = 1
        for line in infile:
            # Check if the line starts with "คำตอบ:"
            if line.strip().startswith("คำตอบ:"):
                # Write the answer directly without numbering
                outfile.write(line)
                # Ensure to add a blank line for separation
                outfile.write("\n")
            elif line.strip() == "":
                continue
            else:
                # Number the questions
                outfile.write(f"{question_number}. {line}")
                question_number += 1

# Specify the file paths
input_file = './numbering_qns/input.txt'
output_file = './numbering_qns/output.txt'

number_lines(input_file, output_file)