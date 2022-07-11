# Convert
This program can convert lot of thigns.</br>
**Conversion :**</br>

**Number converter**
    - Decimal
    - Hexadecimal
    - Binary
    - Octave</br>

**Audio converter (WIP)**
    - To mp3
    - To ogg
    - To wav
    - To flac
    - To aiff
    - To m4a</br>

## Usage

```bash
  ./tools convert bin 01001111
  
  > result:
    Hexadecimal : 0x4f
    Octal : 0o117
    Decimal : 79
  
```
Tips : You can do the same for other conversion by replacing bin with **hex, oct, dec**</br>


This example below will convert a file.ogg to a file.mp3</br>
```bash
  ./tools convert audio mp3 file.ogg

  > ls
   file.ogg
   file.mp3
```

