import os
import re

def extract_cards_from_js_array(js_file_path, output_dir="ascii_cards"):
    if not os.path.exists(js_file_path):
        print(f"❌ File not found: {js_file_path}")
        return

    os.makedirs(output_dir, exist_ok=True)

    with open(js_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 适配你给出的结构：name: 'Card Name', card: `ascii\n...`
    pattern = r"name:\s*'([^']+)',\s*card:\s*`([\s\S]*?)`"
    matches = re.findall(pattern, content)

    print(f"🔍 Found {len(matches)} cards.")
    if not matches:
        print("❌ No matches found. Please check the format.")
        return

    for name, art in matches:
        filename = name.replace(" ", "_").replace("/", "_") + ".txt"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(art.strip() + "\n")
        print(f"✅ Saved: {filepath}")

# 🖥️ 替换为你的本地路径（例如桌面）
js_path = "/Users/gaotianqi/Desktop/tarot cards/cards.js"
output_dir = "/Users/gaotianqi/Desktop/tarot cards/ascii_cards"

extract_cards_from_js_array(js_path, output_dir=output_dir)

print(f"📁 Output directory: {os.path.abspath(output_dir)}")