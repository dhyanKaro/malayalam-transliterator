# Malayalam Transliterator

The Malayalam Transliterator is a Python program that provides a function to transliterate Malayalam text into a Latin script representation following the ISO-15919 standard. It converts Malayalam characters into their corresponding phonetic Latin script equivalents.

## Features

- Transliteration of Malayalam text into Latin script following ISO-15919
- Support for various diacritic marks and ligatures
- Handles special cases like chillu characters and virama (chandrakkala)

Note: Considers "chandrakkala" at the end of a word as the "half-u" or "samvruthokaram" sound instead of acting as a virama

## Usage

1. Ensure you have Python 3 installed on your machine.

2. Clone this repository to your local machine or download the `transliterator.py` file.

3. Import the `transliterate_malayalam` function from `transliterator.py` into your Python program.

4. Call the `transliterate_malayalam` function and pass the Malayalam text as a parameter. It will return the transliterated text.

   ```python
   from transliterator import transliterate_malayalam

   text = 'കൊള്ളാം, ഞാൻ മലയാളം വായിക്കുകയാണ്'
   transliterated_text = transliterate_malayalam(text)
   print(transliterated_text)
   ```

   Output:
   ```
   kolḷāṁ, ñān malayāḷaṁ vāyikkukayāṇ
   ```

## Contributing

Contributions to improve the Malayalam Transliterator are welcome! If you have any bug fixes, feature enhancements, or suggestions, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code for personal or commercial purposes.

---
