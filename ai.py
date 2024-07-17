from transformers import GPT2Tokenizer, GPT2LMHeadModel

# نام مدل و توکنایزر مربوط به آن
model_name = "distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# متن ورودی برای تولید
input_text = "two plus two is   "

# توکن‌های متن ورودی
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# تولید متن جدید با استفاده از مدل
outputs = model.generate(input_ids, max_length=50, num_return_sequences=3, num_beams=5, temperature=0.7)

# چاپ متن‌های تولید شده
for i, output in enumerate(outputs):
    print(f"Generated text {i+1}: {tokenizer.decode(output, skip_special_tokens=True)}")
