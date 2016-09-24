# DiceParser

Just a simple dice parser for a coding challenge.

## Usage

Input an expression as a single string (i.e. put quotes around it). Whitespace is ignored.

```bash
$ ./dice_parser "1d6 + 2d4 - 2"
7
$ ./dice_parser "1d% >= 75"
Success
```

## Project Roadmap

- Allow parentheses.
- Allow just "d#" as shorthand for "1d#".
- Allow Fudge dice: "dF", "dF.1", "dF.2"
- Allow keep/drop highest/lowest.
- Clean up the code extensively.
- Accept prefix and postfix notations.
- Accept expression as multiple arguments (i.e. without surrounding quotes).
- Make it a Slack bot.
