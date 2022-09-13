from config import *
from analytics import Research

if __name__ == '__main__':
    research = Research(file)
    result = research.file_reader()
    counts = research.calculator.counts()
    fractions = research.calculator.fractions(counts[0], counts[1])
    predict_random = research.analytics.predict_random(3)
    predict_last = research.analytics.predict_last()
    random_tails = sum([tail[0] for tail in predict_random])
    random_heads = sum([head[1] for head in predict_random])
    text_report = report.format(len(result), counts[0], counts[1], fractions[0], fractions[1], num_of_step, random_heads, random_tails)
    research.analytics.save_file(text_report, save_file)