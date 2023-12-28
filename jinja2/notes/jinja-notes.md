**Title**: Jinja2 Note

**Author**: รศ.ดร. โชติพัชร์ ภรณวลัย

**Rights**:  Copyright 2023 - ใช้เป็นการภายในคณะเทคโนโลยีสารสนเทศ สจล. เท่านั้น

**Language**: th-TH

**Date**: 27 มกราคม 2566

---

# JINJA2

This lecture will talk about Jinja2

## Introduction

### What is Jinja2?

- a templating language

### Why?

- Command
- Command arguments
- Command Options

## Variable Substitution

- {{ name }}
- jinja01.py - template and data are in the python file. Each data is stored in a variable. Not convinient.
- jinja02.py - similar to jinja01.py but data is now stored in a dict.
- Both jinja01.py and jinja02.py use Template from jinja2 because template is already stored in the file.
- jinja03.py - we have to use FileSystemLoader and Environment. FileSystemLoader is used to load template file from the Filesystem. Once template file is loaded, it is used by Environment to create a environment. And environment is called with get_template to get the template.

#### cat

```
$ cat filename
$ cat filename1 filename2 ...
$ cat -n filename
$ cat -t filename
/* display tab as ^I */
$ cat > filename
line1
line2
^d
$ cat << EOF > filename
line1
line2
EOF
$ cat -s filename
/* squeeze multiple adjacent blank line to one blank line */
```

## References

1. <https://learnbyexample.gitbooks.io/linux-command-line/content/Command_Line_Introduction.html>
2. <https://blog.balthazar-rouberol.com/discovering-the-terminal>
