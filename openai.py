import openai
import tkinter as tk
from tkinter import scrolledtext

# Set your OpenAI API key
openai.api_key = "your-api-key-here"

def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def send_message():
    user_input = user_entry.get()
    if not user_input.strip():
        return
    
    chat_history.insert(tk.END, "You: " + user_input + "\n", "user")
    user_entry.delete(0, tk.END)
    
    response = get_openai_response(user_input)
    chat_history.insert(tk.END, "Bot: " + response + "\n", "bot")
    chat_history.yview(tk.END)

# Create GUI window
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("500x500")

chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.NORMAL, width=60, height=20)
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("bot", foreground="green")
chat_history.pack(pady=10)

user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()