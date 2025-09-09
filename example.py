# Buggy Code
name = "  Steven\n"
print("Hello " + name + "!")  # Extra spaces and newline cause messy output


# Fixed Code
name = "  Steven\n"
cleaned = name.strip()
print(f"Hello {cleaned}!")  # "Hello Steven!"
