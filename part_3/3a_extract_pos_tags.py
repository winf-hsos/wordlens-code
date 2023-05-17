import gzip
import csv
import spacy

nlp = spacy.load("en_core_web_sm")

csv_file = "data/ted_talks_2021/transcript_data.csv.gz"
data = []

# Read the source data and store each line (talk) as an element in an array
with gzip.open(csv_file, mode='rt', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # skip header row
    for row in csv_reader:
        data.append(row)

pos = []
limit = 100
for i, t in enumerate(data):
  
  # Run the spaCy NLP pipeline
  doc = nlp(t[1])
  
  for token in doc:
  
    # Extract the relevant information
    pos_rec = [ 
      t[0],
      token.text,
      token.pos_,
      token.lemma_,
      token.is_stop
      ]
    
    # Add extracted named entity to result array
    pos.append(pos_rec)
  
  print(f"Parsed talk {i}")

  if i >= limit:
    break

  
# Write result to CSV file
header = ['title', 'token_text', 'token_pos', 'token_lemma', 'is_stop'] 

csv_file = 'data/ted_talks_2021/pos.csv'

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)  # Write the header row
    csv_writer.writerows(pos)  # Write the data rows