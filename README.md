# Testdata-Generater

A testdata generator respository

### 1. Testdata Generater

First, you need to create a folder to save all the files needed for a problem, for example, I created `generator_example\`

Next, you need two files: `Config.py` and `std.cpp`

You need to place them like that:

```
generator_example\
  |- Config.py
  |- std.cpp
```

In `Config.py`, you need to rewrite the method Gen.generater, It should do one of the two things:

    1) Return a str with testdata, for example:

```python
def generater(data_group: int, io: IO) -> str: 
        return '114514'
```

    2) Write testdata to io (which is recommended), for example:

```python
def generater(data_group: int, io: IO) -> None: 
        a = randint(Gen.static.INT_MIN, Gen.static.INT_MAX)
        b = randint(Gen.static.INT_MIN, Gen.static.INT_MAX)
        io.input_writeln(a, b)
```

In `std.cpp`, you just need to write a standard program which can solve the problem

**You don't need to redirect stdin or stdout**

It is optional to have a directory with no `std.cpp` inside and enables `genOut` which is still an experimental function

Then, run the command `python general.py {folder_name}`

Finally, the testdata will be auto generated and zipped, the folder will be looked like:

```
generator_example\
  |- Config.py
  |- std.cpp
  |- std.exe
  |- 1.in
  |- 1.out
  |- 2.in
  |- 2.out
  | ....
  |- generator_example.zip
```


### 2. Comparer

Using the comparer, you can compare the two programs fast