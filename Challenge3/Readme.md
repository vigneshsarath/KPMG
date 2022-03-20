# Question3
We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.
Example Inputs:

object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c

object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a

Hints - We would like to see some tests. A quick read to help you along the way. We would expect it in any other language apart from elixir.

## Steps to Execute

1. Install Python3 on the server or system where you execute these python scripts
2. Install pip and install the pytest package to do some testing.
   ```
    sudo apt install python3-pip
    pip3 install pytest
   ```
3. Execute the key.py file which gives the key ouput values of couple of example inputs given in the Question3.
4. Locate the pytest.py file and run that script with test.py as input which has loaded the key values and test against the nested json file. If the answer is correct it shows as test successful.

My local execution ouptut as below, where I have shown the file contents and execution results (Getting the key output and test results):

![image](https://user-images.githubusercontent.com/38080447/159184117-89cd6580-5717-48f5-8929-0065bc785273.png)


