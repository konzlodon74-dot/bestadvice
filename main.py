import os

# The Best Advice I Ever Got — one original sentence, written for this bounty.
ENTRY = "My grandmother said, 'If you can't explain why you're angry in one sentence, you're not angry about that thing' — and it's saved me from sending a hundred messages I couldn't take back."

def main():
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry length must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(text.encode("utf-8"))

if __name__ == "__main__":
    main()
