import tiktoken

encoder  = tiktoken.encoding_for_model("gpt-4o")

print("Vocab Size",encoder.n_vocab)

print (encoder.encode("Hello, world!"))