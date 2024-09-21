import tkinter as tk
from tkinter import ttk
import nltk
from nltk.corpus import indian
from nltk.tag import tnt
import string


class HindiPOSTaggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hindi POS Tagger")
        
        self.label_input = ttk.Label(self.root, text="Enter Hindi sentence:")
        self.label_input.pack()

        self.entry_input = ttk.Entry(self.root, width=50)
        self.entry_input.pack()

        self.button_tag = ttk.Button(self.root, text="Tag Sentence", command=self.tag_sentence)
        self.button_tag.pack()

        self.label_output = ttk.Label(self.root, text="POS tags:")
        self.label_output.pack()

        self.text_output = tk.Text(self.root, height=5, width=50)
        self.text_output.pack()

        self.pos_tagger_hindi = self.train_hindi()

    def train_hindi(self):
        tagged_set = "hindi.pos"
        word_set = indian.sents(tagged_set)
        count = 0
        for sen in word_set:
            count += 1
            sen = "".join(
                [
                    " " + i if not i.startswith("'") and i not in string.punctuation else i
                    for i in sen
                ]
            ).strip()

        train_perc = 0.9
        train_rows = int(train_perc * count)
        test_rows = train_rows + 1

        data = indian.tagged_sents(tagged_set)
        train_data = data[:train_rows]

        pos_tagger = tnt.TnT()
        pos_tagger.train(train_data)
        return pos_tagger

    def tag_sentence(self):
        sentence_to_tag = self.entry_input.get()
        tagged_sentence = self.tag_hindi(self.pos_tagger_hindi, sentence_to_tag)
        self.display_output(tagged_sentence)

    def tag_hindi(self, pos_tagger, sentence_to_be_tagged):
        tokenized = nltk.word_tokenize(sentence_to_be_tagged)
        return pos_tagger.tag(tokenized)

    def display_output(self, tagged_sentence):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, str(tagged_sentence))


if __name__ == "__main__":
    root = tk.Tk()
    app = HindiPOSTaggerApp(root)
    root.mainloop()
