from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base", device_map="auto")


def prompting():
    input_text = input("Enter your question ? :")
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

    outputs = model.generate(input_ids)
    gen_text = tokenizer.decode(outputs[0])

    return gen_text

count =0
while(1):
    choice = input("Enter Y for Prompt and N for Exit : ")
    if (choice == "Y" or choice == "y"):
        print(f"prompts : {count}")
        count = count+1
        gen_text = prompting()
        print(gen_text)
    elif (choice == "N" or choice == "n"):
        break
    else:
        print("Enter a valid choice (Y/N)")