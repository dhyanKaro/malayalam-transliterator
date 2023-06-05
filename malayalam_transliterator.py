import string
import unicodedata

# Define the transliteration mappings

vowels_exclude = ['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ', 'ം']

chillu = {
    'ൺ': 'ṇ',
    'ൻ': 'n',
    'ർ': 'ṟ',
    'ൽ': 'l',
    'ൾ': 'ḷ',
    'ൿ': 'k',
}

transliteration_mappings = {
    'ാ': 'ā',
    'ി': 'i',
    'ീ': 'ī',
    'ു': 'u',
    'ൂ': 'ū',
    'ൃ': 'r̥',
    'ൄ': 'r̥̄',
    'ൢ': 'l̥',
    'ൣ': 'l̥̄',
    'െ': 'e',
    'േ': 'ē',
    'ൈ': 'ai',
    'ൊ': 'o',
    'ോ': 'ō',
    'ൌ': 'au',
    'ൗ': 'au',
    'അ': 'a',
    'ആ': 'ā',
    'ഇ': 'i',
    'ഈ': 'ī',
    'ഉ': 'u',
    'ഊ': 'ū',
    'ഋ': 'r̥',
    'ൠ': 'r̥̄',
    'ഌ': 'l̥',
    'ൡ': 'l̥̄',
    'എ': 'e',
    'ഏ': 'ē',
    'ഐ': 'ai',
    'ഒ': 'o',
    'ഓ': 'ō',
    'ഔ': 'au',
    'ക': 'k',
    'ഖ': 'kh',
    'ഗ': 'g',
    'ഘ': 'gh',
    'ങ': 'ṅ',
    'ച': 'c',
    'ഛ': 'ch',
    'ജ': 'j',
    'ഝ': 'jh',
    'ഞ': 'ñ',
    'ട': 'ṭ',
    'ഠ': 'ṭh',
    'ഡ': 'ḍ',
    'ഢ': 'ḍh',
    'ണ': 'ṇ',
    'ത': 't',
    'ഥ': 'th',
    'ദ': 'd',
    'ധ': 'dh',
    'ന': 'n',
    'പ': 'p',
    'ഫ': 'ph',
    'ബ': 'b',
    'ഭ': 'bh',
    'മ': 'm',
    'റ': 'ṟ',
    'റ്റ': 'ṯ',
    'ഩ': 'ṉ',
    'ഴ': 'ḻ',
    'യ': 'y',
    'ര': 'r',
    'ല': 'l',
    'ള': 'ḷ',
    'വ': 'v',
    'ശ': 'ś',
    'ഷ': 'ṣ',
    'സ': 's',
    'ഹ': 'h',
    'ം': 'ṁ',
}

punctuation_set = set(string.punctuation)
whitespace_set = set(string.whitespace)
word_end_markers = punctuation_set.union(whitespace_set)


def is_diacritic(char):
    if char == '\u0D02':
        return False
    category = unicodedata.category(char)
    return category.startswith('M')


def transliterate_malayalam(text):
    transliterated_text = ''
    i = 0
    while i < len(text):
        char = text[i]

        # Check for the ligatures "ന്റ" and "റ്റ"
        if (char == 'ന' or char == 'റ') and i + 2 < len(text) and text[i + 1:i + 3] == '്റ':
            if char == 'ന':
                transliterated_text += 'nṯ'
            else:
                transliterated_text += 'ṯṯ'

            next_char = text[i + 3] if i + 3 < len(text) else None
            if next_char and not is_diacritic(next_char) and next_char != '\u0D4D':
                transliterated_text += 'a'
            i += 3

        elif char in transliteration_mappings:
            transliterated_text += transliteration_mappings[char]
            # a ...
            if not is_diacritic(char) and char not in vowels_exclude and (
                    i + 1 == len(text) or not is_diacritic(text[i + 1]) and text[i + 1] != '\u0D4D'):
                transliterated_text += 'a'

            i += 1

        elif char in chillu:
            transliterated_text += chillu[char]
            i += 1

        # Check for chandrakkala (virama)
        elif char == '\u0D4D':
            if i == len(text) - 1 or text[i + 1] in word_end_markers:  # saṁvr̥tōkāram
                transliterated_text += 'ŭ'
            i += 1

        else:
            transliterated_text += char
            i += 1

    return transliterated_text
