# DecodeLabs Internship - Week 1 Project
# 1. Knowledge Base
responses = {
    "hello": "Chatbot: Hello! Welcome to DecodeLabs Support. How can I help you today?",
    "hi": "Chatbot: Hi there! How can I assist you with your order?",
    "products": "Chatbot: We sell high-quality Monitors, Phones, Tablets, Chairs, and Printers!",
    "payment": "Chatbot: We accept Credit Card, Debit Card, and Online payments.",
    "status": "Chatbot: Order status can be Shipped, Delivered, Cancelled, or Returned. Please provide your Tracking Number.",
    "help": "Chatbot: You can ask me about our 'products', 'payment' methods, or order 'status'."
}

print("--- DecodeLabs Rule-Based AI Chatbot ---") # [cite: 120]
print("Type 'exit' or 'bye' to close the chatbot.\n")

# 2. Continuous Loop 
while True:
    # 3. Input & Sanitization
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    
    # 4. Exit Strategy 
    if clean_input in ['exit', 'bye']:
        print("Chatbot: Goodbye! Have a great day ahead.")
        break
        
    # 5. Intent Matching & Fallback Mechanism
    reply = responses.get(clean_input, "Chatbot: I am sorry, I do not understand that. Type 'help' for available options.")
    print(reply)
    print("-" * 40)
