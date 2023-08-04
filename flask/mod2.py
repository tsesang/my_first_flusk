import mod1       # here this line execute first from another file that is executing another file inside the main file
print(__name__,'mod2')

#if you execute any file directly  then __name__ variable value will be __main__
#if you execute any file indirectly  then __name__ variable value will be module name