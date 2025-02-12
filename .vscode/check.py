import ollama
import requests

def get_research(topic):
    url = f"https://api.duckduckgo.com/?q={topic}&format=json"
    response = requests.get(url)
    data = response.json()
    research = data.get("AbstractText", "No research found.")
    return research

def generate_script(topic, research):
    prompt = f"Write a viral Instagram Reels script on {topic}. Use engaging storytelling and a hook at the start.\n\nResearch: {research}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def generate_script(topic, research):
    prompt = f"Write a viral Instagram Reels script on {topic}. Use engaging storytelling and a hook at the start.\n\nResearch: {research}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def main():
    topic = input("Enter your topic: ")
    research = get_research(topic)
    script = generate_script(topic, research)
    print("\nGenerated Script:\n", script)

if __name__ == "__main__":
    main()

