# Unminify
This little program can unminify some code.</br>
**Langage Supported :**</br>
- css WIP
- js
- html WIP
- json WIP
- xml WIP
- sql WIP

## Usage

First of all the program works the same way whether the type of the file.</br>
You can put as arguments a file as input and another as output or just an input and the name of
the output file will therefore be the same as the input one with the file extension that changes.</br>


Of course, if the file exists the result will be written in it, otherwise it will be created in the same location as the input file.

```bash
  ./tools -unmin exemple.min.css
  
  > ls
   exemple.min.css
   exemple.css
```

```bash
  ./tools --unminify file1.min.js file2.js
  
  > ls
   file1.min.js
   file2.js
```

