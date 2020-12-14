# Alfred Roman Numerals

![GitHub Workflow Status (branch)](https://github.com/shmulvad/alfred-roman-numerals/workflows/CI/badge.svg)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/shmulvad/alfred-roman-numerals)
[![GitHub issues](https://img.shields.io/github/issues/shmulvad/alfred-roman-numerals)][issues]
![Languages supported](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)
[![GitHub license](https://img.shields.io/github/license/shmulvad/alfred-roman-numerals)][license]
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)][makeAPullRequest]

A simple [Alfred][alfred] workflow for converting between roman numerals and arabic integers written in Python.

## Installation
1. Install [alfred-roman-numerals][release] workflow.
2. All further updates are handled automatically.

## Usage
In Alfred, type `rn` and enter either your roman numeral or arabic integer. Selected result is copied to your clipboard.

<p align="center">
  <img src="images/arabic_to_roman.png?raw=true" alt="Arabic to Roman" />
  <img src="images/roman_to_arabic.png?raw=true" alt="Roman to Arabic" />
</p>

The expression is being evaluated as you type it. If the expression cannot be evaluated, for example if you are using illegal characters, user will be notified about that.

<p align="center">
  <img src="images/gibberish.png?raw=true" alt="Gibberish" />
</p>


## Note
The workflow doesn't support incorrectly written roman numerals, i.e. `"IC"`, and will also notify user about this:

<p align="center">
  <img src="images/invalid_roman.png?raw=true" alt="Invalid Roman" />
</p>

## Credits
The workflow makes use of [OneUpdater][oneUpdater] by vitorgalvao to focus on the implementation of the conversion between the number systems rather than code related to updating.

[license]: https://github.com/shmulvad/alfred-roman-numerals/blob/master/LICENSE
[issues]: https://github.com/shmulvad/alfred-roman-numerals/issues
[release]: https://github.com/shmulvad/alfred-roman-numerals/releases/latest
[makeAPullRequest]: https://makeapullrequest.com
[alfred]: https://www.alfredapp.com/
[oneUpdater]: https://github.com/vitorgalvao/alfred-workflows/tree/master/OneUpdater