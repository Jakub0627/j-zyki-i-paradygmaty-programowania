'''
Zadanie 1. Analiza Tekstu i Transformacje Funkcyjne
Napisz program, który przyjmuje długi tekst (np. artykuł, książkę) i wykonuje kilka złożonych operacji
analizy tekstu:
• Zlicza liczbę słów, zdań, i akapitów w tekście.
• Wyszukuje najczęściej występujące słowa, wykluczając tzw. stop words (np. "i", "a", "the").
• Transformuje wszystkie wyrazy rozpoczynające się na literę "a" lub "A" do ich odwrotności (np.
"apple" → "elppa").
Wskazówka: Użyj map(), filter(), i list składanych, aby przeprowadzać transformacje na tekście.
'''
import re
from collections import Counter

with open('tekst.txt', 'r', encoding='utf-8') as file:
    tekst = file.read()


def zadanie1(tekst):
    paragraph = tekst.strip().split('\n\n')
    numParagraphs = len(paragraph)

    zdania = re.split(r'[.!?]+', tekst)
    numZdania = len([s for s in zdania if s.strip()])

    slowa = tekst.split()
    slowaNum = len(slowa)

    stop_words = ['a', 'w', 'i', 'o', 'u', 'z']
    filter_words = list(filter(lambda slowo: slowo.lower() not in stop_words, slowa))
    filter_wordsNumber = Counter(filter_words)

    print(f"Liczba akapitów: {numParagraphs}")
    print(f"Liczba zdań: {numZdania}")
    print(f"Liczba słów: {slowaNum}")
    print(f"Najczęściej występujące słowa (bez stop words): {filter_wordsNumber.most_common(10)}")

zadanie1(tekst)