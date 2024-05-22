from pathlib import Path
import json

# numbers=list(range(21))
# path=Path('numbers.json')
# contents=json.dumps(numbers)
# path.write_text(contents)

path=Path('numbers.json')
contents=path.read_text()
print(contents)
#numbers=json.loads(contents)

#print(numbers)