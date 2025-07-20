import itertools

def generate_passwords(words, min_len=1, max_len=3):
    separators = ['', '_', '-', '.']
    suffixes = ['', '!', '@', '123', '2024', '01']

    combinations = []
    
    for length in range(min_len, max_len + 1):
        for word_combo in itertools.permutations(words, length):
            for sep in separators:
                base = sep.join(word_combo)

                # Add base in multiple case formats
                variants = set()
                variants.add(base)
                variants.add(base.lower())
                variants.add(base.upper())
                variants.add(base.capitalize())

                for variant in variants:
                    for suffix in suffixes:
                        combinations.append(variant + suffix)
    
    return combinations

# Example usage:
words = ['admin', '123', 'user']
password_list = generate_passwords(words)

# Save to file
with open('generated_passwords.txt', 'w') as f:
    for pw in password_list:
        f.write(pw + '\n')

print(f"{len(password_list)} passwords generated.")
