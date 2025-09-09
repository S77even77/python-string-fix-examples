# Python String Handling Bug Fix Examples

This repository demonstrates common **string handling bugs** in Python and how to fix them.

## Example: Unwanted Whitespace and Newlines

**Buggy Code**
```python
name = "  Steven\n"
print("Hello " + name + "!")
Hello   Steven
!


Fixed Code

name = "  Steven\n"
cleaned = name.strip()
print(f"Hello {cleaned}!")
Output
Hello Steven!

License

MIT
