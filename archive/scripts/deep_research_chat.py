import os
import openai
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
google_cse_id = os.getenv("GOOGLE_CSE_ID")

client = openai.OpenAI(api_key=openai_api_key)

def search_google(query, num_results=3):
    """Google Custom Search API használata gazdasági kereséshez."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': google_api_key,
        'cx': google_cse_id,
        'q': query,
        'num': num_results
    }
    response = requests.get(url, params=params)
    results = response.json()

    snippets = []
    if 'items' in results:
        for item in results['items']:
            snippets.append(item['snippet'])

    return snippets


def generate_deep_research_answer(prompt, context):
    """Válasz generálása OpenAI API-val, kiegészítve a gazdasági keresési eredményekkel."""
    combined_prompt = (
        f"Készíts egy részletes, szakmai gazdasági választ az alábbi kérdésre, "
        f"figyelembe véve a következő gazdasági háttérinformációkat is:\n\n"
        f"Gazdasági háttérinformációk:\n{context}\n\n"
        f"Kérdés: {prompt}\n\nRészletes gazdasági válasz:"
    )

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": combined_prompt}],
        temperature=0.5,
        max_tokens=1000,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    user_prompt = input("Adj meg egy gazdasági kérdést vagy promptot: ")

    print("\n[1/2] Gazdasági webes keresés folyamatban...")
    research_context = search_google(user_prompt)
    research_text = "\n---\n".join(research_context)

    print("\n[2/2] OpenAI gazdasági elemzés generálása...")
    answer = generate_deep_research_answer(user_prompt, research_text)

    print("\nGazdasági elemzés válasz:\n")
    print(answer)

    # Mentés fájlba
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    output_dir = "../docs/reports/deep_research"
    os.makedirs(output_dir, exist_ok=True)
    output_path = f"{output_dir}/{timestamp}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Gazdasági Deep Research válasz ({timestamp})\n\n")
        f.write(f"## Kérdés:\n{user_prompt}\n\n")
        f.write(f"## Gazdasági háttérinformációk:\n{research_text}\n\n")
        f.write(f"## Válasz:\n{answer}\n")

    print(f"\nMentve: {output_path}")