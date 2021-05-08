import re
result = re.match(r"hello", "hello world")
result.group()
re.match(r"hello", "hello world").group()
re.match(r"hello world\d", "hello world66").group()
re.match(r"hello world[123456789]", "hello world66").group()
re.match(r"hello world[1-57-9]", "hello world66123").group()
re.match(r"你好\d", "你好123").group()
re.match(r"你好[1-9a-zA-Z]", "你好a ").group()
re.match(r"你好\w", "你好杯 ").group()
re.match(r"你好 \d", "你好 1").group()
re.match(r"你好\s\d", "你好 1").group()
re.match(r"你好.", "你好#").group()


