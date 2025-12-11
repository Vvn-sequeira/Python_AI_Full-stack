
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Vivian Marcel Sequiera "
Tokens = enc.encode(text=text)
print(f"Tokens {Tokens}") # Tokens [25216, 1354, 0, 3673, 1308, 382, 191517, 92485, 1550, 50796, 220]

Decode = enc.decode([25216, 1354, 0, 3673, 1308, 382, 191517, 92485, 1550, 50796, 220])
print(f"Decoder {Decode}")