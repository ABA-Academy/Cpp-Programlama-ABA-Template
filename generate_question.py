#!/usr/bin/env python3
"""
C++ Soru Template Generator
500 soru için otomatik template oluşturur
"""

import os
import json
import sys

def create_question_structure(question_number, question_data):
    """Soru klasörü ve dosyalarını oluşturur"""

    # Klasör adı
    folder_name = f"questions/{question_number:03d}-{question_data['slug']}"

    # Klasör oluştur
    os.makedirs(f"{folder_name}/.github/workflows", exist_ok=True)

    # README.md oluştur
    readme_content = f"""# Soru {question_number}: {question_data['title']}

## Zorluk: {question_data['difficulty']}

## Açıklama

{question_data['description']}

## İstenenler

{question_data['requirements']}

## Örnekler

{question_data['examples']}

## İpuçları

{question_data['hints']}

## Puanlama

- ✅ Tüm test durumları: 100 puan
"""

    with open(f"{folder_name}/README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    # main.cpp oluştur
    main_cpp = f"""#include <iostream>
using namespace std;

int main() {{
    // Kodunuzu buraya yazın
    // {question_data.get('hint_comment', 'İpucu: README.md dosyasını okuyun')}

    return 0;
}}
"""

    with open(f"{folder_name}/main.cpp", "w", encoding="utf-8") as f:
        f.write(main_cpp)

    # Test dosyası oluştur
    test_yml = f"""name: Soru {question_number} - {question_data['title']} Test

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  test:
    name: {question_data['title']} Testi
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Derle
      run: |
        g++ -std=c++17 -o program main.cpp
        echo "✅ Derleme başarılı"

{question_data['test_steps']}

    - name: Sonuç
      run: echo "🎉 Tüm testler başarılı!"
"""

    with open(f"{folder_name}/.github/workflows/test.yml", "w", encoding="utf-8") as f:
        f.write(test_yml)

    print(f"✅ Soru {question_number} oluşturuldu: {folder_name}")

def load_questions_from_json(json_file):
    """JSON dosyasından soruları yükler"""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python3 generate_question.py <questions.json>")
        print("Veya: python3 generate_question.py <soru_numarası> (test için)")
        sys.exit(1)

    # Eğer JSON dosyası verilmişse
    if sys.argv[1].endswith('.json'):
        questions = load_questions_from_json(sys.argv[1])
        for i, question in enumerate(questions, start=1):
            create_question_structure(i, question)
        print(f"\n✅ Toplam {len(questions)} soru oluşturuldu!")
    else:
        # Tek soru testi için
        print("Tek soru test modu - henüz implement edilmedi")
        print("Lütfen questions.json dosyası kullanın")

if __name__ == "__main__":
    main()
