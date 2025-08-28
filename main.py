from dotenv import load_dotenv

load_dotenv()

def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    return len(text)

def main():
    print("Hello from react-langchain!")
    print(get_text_length("Hello, world!"))

if __name__ == "__main__":
    main()
