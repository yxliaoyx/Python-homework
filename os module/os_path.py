import os

print(os.path.basename('c:\\Python\\Sources\\prog1.py'))
print(os.path.dirname('c:\\Python\\Sources\\prog1.py'))
print(os.path.join('c:\\Python\\Sources', 'prog1.py'))
print(os.getcwd())
os.chdir('c:\\')
print(os.listdir(os.getcwd()))
