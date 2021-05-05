class NonlocalKeyword:
    
    x = 4
    def my_function():
        x = 3
        
        def innner():
            nonlocal x
            print(x)
        innner()
    my_function()

if __name__ == '__main__':
    NonlocalKeyword()