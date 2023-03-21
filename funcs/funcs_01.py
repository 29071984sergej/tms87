#Написать функцию, которая получает на вход имя и выводит строку вида:
# “Hello, {name}”. Создать список из 5 имен.
# Вызвать функцию для каждого элемента списка в цикле.
def my_funct(name):
    print(f"hello {name}")
def main():
    arr = ["Boris", "Toni", "Vasj","Max","Ivan"]
    for name in arr:
        my_funct(name)
if __name__ == '__main__':
   main()
