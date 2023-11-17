
# Malayalam Transliterator

The Malayalam Transliterator is a Python program that provides a function to transliterate Malayalam text into a Latin script representation following the ISO-15919 standard. It converts Malayalam characters into their corresponding phonetic Latin script equivalents.

## Try It Online

You can try out the Malayalam Transliterator online by visiting our web app. Simply go to the following URL:

[Malayalam Transliterator Web App](https://dhyankaro.github.io/malayalam-transliterator/)

## Features

- Transliteration of Malayalam text into Latin script following the ISO-15919 standard
- Support for various diacritic marks and ligatures
- Handles special cases like chillu characters and virama (chandrakkala)
- Ignores archaic characters which probably no one will notice
Note: Considers "chandrakkala" at the end of a word as the "half-u" or "samvruthokaram" sound instead of acting as a virama

## Usage

If you prefer to use the Malayalam Transliterator as a Python library, you can follow these steps:

1. Ensure you have Python 3 installed.

2. Clone this repository to your local machine or download the `malayalam_transliterator.py` file.

3. Import the `transliterate` function from `malayalam_transliterator.py` into your Python program.

4. Call the `transliterate` function and pass the Malayalam text as a parameter. It will return the transliterated text.

   ```python
   from malayalam_transliterator import transliterate

   text = 'കൊള്ളാം, ഞാൻ മലയാളം വായിക്കുകയാണ്'
   transliterated_text = transliterate(text)
   print(transliterated_text)
   ```

   Output:
   ```
   koḷḷāṁ, ñān malayāḷaṁ vāyikkukayāṇŭ
   ```

## Contributing

Contributions to improve the Malayalam Transliterator are welcome! If you have any bug fixes, feature enhancements, or suggestions, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code for personal or commercial purposes.

---