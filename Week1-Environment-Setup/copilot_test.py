import re
from typing import Tuple, List


def is_strong_password(password: str) -> Tuple[bool, List[str]]:
	"""Check whether a password is strong.

	Rules enforced:
	- Minimum length 12
	- Contains at least one lowercase letter
	- Contains at least one uppercase letter
	- Contains at least one digit
	- Contains at least one special character (punctuation)
	- No whitespace characters

	Returns (True, []) if strong, otherwise (False, [reasons...]).
	"""
	reasons: List[str] = []
	if len(password) < 12:
		reasons.append("must be at least 12 characters long")
	if not re.search(r"[a-z]", password):
		reasons.append("must include a lowercase letter")
	if not re.search(r"[A-Z]", password):
		reasons.append("must include an uppercase letter")
	if not re.search(r"[0-9]", password):
		reasons.append("must include a digit")
	if not re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?`~]", password):
		reasons.append("must include a special character")
	if re.search(r"\s", password):
		reasons.append("must not contain whitespace")

	return (len(reasons) == 0, reasons)


if __name__ == "__main__":
	# quick manual test
	samples = [
		"Password123!",
		"weakpass",
		"StrongPassw0rd$",
		"Too short1!",
		"Has space 123A!",
	]
	for s in samples:
		ok, reasons = is_strong_password(s)
		print(s, "=>", "STRONG" if ok else "WEAK:", ", ".join(reasons))

