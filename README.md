# degender_pronoun

## Introduction

A dependency-free Python package to replace gender pronouns in a given text with gender-neutral pronouns, i.e., a gender pronoun neutralizer.

Built from **hephaest0s/lavenderPy** (https://github.com/hephaest0s/lavenderPy). This package further distinguishes between the objective case and possessive adjective of "her," improves in more contexts, and supports replacing with user-defined pronouns.

Caution: This package does not consider verbs in the sentence, so you will likely see sentences starting with "They is" if you use this package.

## Install

> pip install degender-pronoun

## Example


```python
from degender_pronoun import degenderizer
```

`.getDictionary()` method is used to retrieve the current used pronoun dictionary. It is ordered like [he/she, him/her, his/her, his/hers, himself/herself]. The default dictionary is ['they', 'them', 'their', 'theirs', 'themselves'].


```python
D = degenderizer()
D.getDictionary()
```




    ['they', 'them', 'their', 'theirs', 'themselves']


The main method used to degender pronouns is `.degender()`.

```python
texts = ["She is a girl.",
        "he loves her?",
         "I don't like her as she only cares herself.",
        "WHAT SHE SAYS ABOUT HERSELF?",
        "if he or she wants her candy, take his."
       ]
for text in texts:
    print(D.degender(text))
```

    They is a girl.
    they loves them?
    I don't like them as they only cares themselves.
    WHAT THEY SAYS ABOUT THEMSELVES?
    if they wants their candy, take theirs.
    

You can also set a dictionary you like using `.setDictionary`.


```python
# User-defined dictionary must be like [he/she, him/her, his/her, his/hers, himself/herself]
user_pronouns = ["Xe", "Xem", "Xir", "Xirs", "Xemself"]
D.setDictionary(user_pronouns)
for text in texts:
    print(D.degender(text))
```

    Xe is a girl.
    xe loves xem?
    I don't like xem as xe only cares xemself.
    WHAT XE SAYS ABOUT XEMSELF?
    if xe wants xir candy, take xirs.
    


```python

```
