import matplotlib.pyplot as plt
from collections import Counter
import re


def load_article(filename):
    with open(filename, 'r') as file:
        return file.read()


def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    stopwords = set([
        'and', 'the', 'to', 'of', 'in', 'a', 'is', 'it', 'with', 'as', 'for', 'on',
        'are', 'was', 'by', 'this', 'that', 'at', 'from', 'or', 'but', 'be', 'an'
    ])
    keywords = [word for word in words if word not in stopwords]
    return keywords


def extract_designers(text, designers):
    designer_counts = Counter()
    for designer in designers:
        count = text.lower().count(designer.lower())
        designer_counts[designer] = count
    return designer_counts


def analyze_and_plot(keywords, designer_counts):
    keyword_counts = Counter(keywords)

    # Debugging: Print keyword and designer counts
    print("Keyword Counts:", keyword_counts)
    print("Designer Counts:", designer_counts)

    # Plot keywords
    plt.figure(figsize=(10, 5))
    plt.bar(*zip(*keyword_counts.most_common(10)))
    plt.title("Top Keywords in Summer Trends Article")
    plt.xlabel("Keywords")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()

    # Plot designers
    plt.figure(figsize=(10, 5))
    designers, counts = zip(*designer_counts.items())
    plt.bar(designers, counts, color='purple')
    plt.title("Top Designers in Summer Trends Article", fontsize=16, fontweight='bold', fontname='Arial')
    plt.xlabel("Designers", fontsize=14, fontweight='bold', fontname='Arial')
    plt.ylabel("Frequency", fontsize=14, fontweight='bold', fontname='Arial')
    plt.xticks(rotation=45, fontsize=12, fontname='Arial')
    plt.yticks(fontsize=12, fontname='Arial')
    plt.show()


if __name__ == "__main__":
    text = load_article("Summertrends.txt")
    keywords = extract_keywords(text)

    # Define a subset of designers to focus on
    designers_list = [
        "Balenciaga", "Chloe", "Dior", "Loewe", "Alaia", "Chanel", "The Row", "Miu Miu", "Prada", "Peter Do"
    ]

    designer_counts = extract_designers(text, designers_list)
    analyze_and_plot(keywords, designer_counts)



