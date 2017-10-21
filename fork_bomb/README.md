
Reference: [Fork Bomb](https://en.wikipedia.org/wiki/Fork_bomb)

This simple command create a function that calls itself twice every execution, until you run out of system resources.

```
:()
{
    : | : &
};

:
```

```
:()
```
We are defining a function called :

```
: | : &
```
The function : is called, and its output is sent to the same function. This command is executed in background.

```
:
```
At last the function is called the first time
