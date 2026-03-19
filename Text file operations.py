
# --- Phase 1: File Creation and Initial Write ---
# Create a new file (or overwrite if it exists) and populate it with 5 numbered lines.
with open('example.txt', 'w') as f:
    for i in range(1, 6):
        f.write(f'Line {i}\n')

# --- Phase 2: Read Operations ---
# Open the file in read-only mode to load and display the entire content.
with open('example.txt', 'r') as f:
    content = f.read()
    print("Initial File Content:")
    print(content)

# --- Phase 3: Extending the Data ---
# Use append mode ('a') to add new lines without deleting the existing content.
with open('example.txt', 'a') as f:
    for i in range(6, 8):
        f.write(f'Line {i}\n')

# --- Phase 4: Final Verification ---
# Read the file a second time to confirm that it now contains 7 total lines.
with open('example.txt', 'r') as f:
    content = f.read()
    print("Updated File Content (7 lines expected):")
    print(content)