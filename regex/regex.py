import re

pattern = re.compile(
    r'\.(?P<underscore>_)?(?P<hash>[a-f0-9]+)-(?P<name>[a-zA-Z0-9_-]+)'
)

def replace_class(m):
    sep = "__" if m.group("underscore") else "_"
    return f".{m.group('name')}{sep}{m.group('hash')[:6]}"

with open("build/midnight-cloud.css", "r", encoding="utf-8") as f:
    css = f.read()

css = pattern.sub(replace_class, css)

with open("output.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Done")