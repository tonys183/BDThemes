import re

pattern = re.compile(
    r'\.(?P<underscore>_)?(?P<hash>[a-f0-9]+)-(?P<name>[a-zA-Z0-9_-]+)'
)

def replace_class(m):
    hash_part = m.group("hash")
    name_part = m.group("name")
    return f".{name_part}__{hash_part[:5]}" if m.group("underscore") else f".{name_part}_{hash_part[:6]}"

with open("build/midnight-zerotwo.css", "r", encoding="utf-8") as f:
    css = f.read()

css = pattern.sub(replace_class, css)

with open("regex/output.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Done")