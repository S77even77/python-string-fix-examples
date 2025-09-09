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

![Steven's GitHub stats](https://github-readme-stats.vercel.app/api?username=S77even77&show_icons=true&theme=radical)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=S77even77&layout=compact&theme=radical)

![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=S77even77&theme=radical)

