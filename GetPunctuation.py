import re

# List of input files
input_files = ["MRData.txt",'XrayData.txt','CTData.txt']

# Set to store unique characters
unique_chars = set()

# Loop through each input file
for file in input_files:
    # Open the file for reading
    with open(file, "r",encoding='utf-8') as f:
        # Read the contents of the file
        contents = f.read()

        # Find all non-Chinese, non-English, non-digit characters
        non_alnum_chars = re.findall(r"[^\u4e00-\u9fff\w\d]", contents)

        # Add the non-alphanumeric characters to the set
        unique_chars.update(non_alnum_chars)

# Open the output file for writing
with open("output.txt", "w",encoding='utf-8') as f:
    # Write the unique characters to the output file
    f.write("\", \"".join(unique_chars))