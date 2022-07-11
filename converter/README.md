# Convert
This program can convert lot of thigns.</br>
**Conversion :**</br>

**Number converter :**</br>
    - Decimal</br>
    - Hexadecimal</br>
    - Binary</br>
    - Octave</br></br>

**Audio converter (WIP) :**</br>
    - To mp3</br>
    - To ogg</br>
    - To wav</br>
    - To flac</br>
    - To aiff</br>
    - To m4a</br></br>

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


