import json
import PyPDF2
import re

def analyze_transcript(text):
    
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip()) > 10]
    
    resumo = ". ".join(sentences[:3])
    
    words = text.lower().split()
    stop_words = ['a', 'o', 'e', 'de', 'da', 'do', 'em', 'para', 'com', 'um', 'uma', 'que']
    words = [w for w in words if len(w) > 3 and w not in stop_words]
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    topicos = sorted(word_count, key=word_count.get, reverse=True)[:5]
    
    ganchos = []
    for sentence in sentences:
        lower_sent = sentence.lower()
        if "dica" in lower_sent or "nunca" in lower_sent:
            ganchos.append(sentence)
            if len(ganchos) >= 3:
                break
    
    if len(ganchos) < 3:
        long_sentences = sorted(sentences, key=len, reverse=True)
        for sentence in long_sentences:
            if sentence not in ganchos:
                ganchos.append(sentence)
                if len(ganchos) >= 3:
                    break
    
    return {
        "resumo": resumo,
        "topicos": topicos,
        "ganchos": ganchos[:3]
    }

with open("transcription.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

result = analyze_transcript(text)

print(json.dumps(result, ensure_ascii=False, indent=2))

with open("resultado.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)