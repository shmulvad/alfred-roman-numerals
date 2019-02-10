# Alfred Roman Numerals
A simple [Alfred 3][1] workflow for converting between roman numerals and arabic integers written in Python.

## Installation
1. Install [alfred-roman-numerals][2] workflow.
2. All further updates are handled automatically.

## Usage
In Alfred, type `rn` and enter either your roman numeral or arabic integer. Selected result is copied to your clipboard.
![arabic to roman](images/arabic_to_roman.png?raw=true "")
![roman to arabic](images/roman_to_arabic.png?raw=true "")

The expression is being evaluated as you type it. If the expression cannot be evaluated, for example if you are using illegal characters, user will be notified about that.
![gibberish](images/gibberish.png?raw=true "")


## Note
The workflow doesn't support incorrectly written roman numerals, i.e. "IC", and will also notify user about this:
![invalid roman](images/invalid_roman.png?raw=true "")

## Credits
The workflow makes use of the following code to focus on the implementation of the conversion between the number systems rather than focusing on a lot of Alfred Workflow related stuff. 

1. [OneUpdater][3] to easily check for updates by vitorgalvao
2. [Alfred Workflow Feedback XML Generation][4] to easily add items by lrrfantasy.

[1]: https://www.alfredapp.com/
[2]: https://github.com/shmulvad/alfred-roman-numerals/releases/latest
[3]: https://github.com/vitorgalvao/alfred-workflows/tree/master/OneUpdater
[4]: https://github.com/lrrfantasy/alfred-feedback-xml-generation