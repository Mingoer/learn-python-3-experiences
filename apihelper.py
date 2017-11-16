def info(object,spaceing=10,collapse):
    ( """print methods and doc strings .

    takes module ,class, list, dictionary,or string.""")
    methodList=[method for mathod in dir(object) if callable(getattr(object,method))]
    processFunc=collapase and (lambda s:"".join(s.split()))or(lambda s:s)
    print("\n".join(["%s%s"%(method.ljust(spaceing),
                             processFunc(str(getaattr(object,method).__doc__)))
                     for method in methodList])
          

if __name__== '__main__':
          print( "info.__doc__")
          
