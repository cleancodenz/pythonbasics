
import os.path

filename = os.path.join('tmp','source.txt')
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
try:
                
    # w for writing and t for text 
    file = open(filename, mode='w')
    file.write('This is some content, ')
    file.write('this is some more content, ')
    file.write('good bye for now.')
   
except IOError as e:
    print('Eoor: {0}'.format(e))
finally:
    print("Trying to close file...")
    try:
        file.close()
        print("File is closed.")
    except UnboundLocalError as rule:
         print('Could not close file: {0}'.format(ule))
    


#using keywords

try:
    with open(filename, mode='wt') as file:
         file.write('This is some content, ')
         file.write('this is some more content, ')
         file.write('good bye for now.')
         # no need to close file
except IOError as e:
    print('Eoor: {0}'.format(e))      
        
        
#read from file 

try:
    with open(filename, mode='rt') as file:
         source_lines = file.readlines()
         print source_lines        
         # no need to close file
except IOError as e:
    print('Eoor: {0}'.format(e))      
        