# Minify

**Langage Supported :**</br>
- css
- js
- html
- json
- xml
- sql

Of course this little piece of code can be easily integrated for your website to minify your program each time you update it.

## Usage

First of all the program works the same way whether the type of the file.</br>
You can put as arguments a file as input and another as output or just an input and the name of
the output file will therefore be the same as the input one with the file extension that changes.</br>


Of course, if the file exists the result will be written in it, otherwise it will be created in the same location as the input file.

```bash
  ./tools min exemple.css
  
  > ls
   exemple.css
   exemple.min.css
```

```bash
  ./tools min file1.js file2.min.js
  
  > ls
   file1.js
   file2.min.js
```

## API

This program use the API from www.toptal.com for css, js and html langages.
