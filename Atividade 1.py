
# coding: utf-8

# In[1]:


#Slide 18 da apresentação python_lectures_7


# In[2]:


import numpy
a = numpy.arange(4.0) 
b = a * 23.4 
c = b/(a+1) 
c += 10 
print (c)  

arr = numpy.arange(100, 200) 
select = [5, 25, 50, 75, -5] 
print(arr[select])  # can use integer lists as indices  

arr = numpy.arange(10, 20 )
div_by_3 = arr%3 == 0  # comparison produces boolean array 
print(div_by_3) 

print(arr[div_by_3])  # can use boolean lists as indices 


arr = numpy.arange(10, 20) . reshape((2,5))


# In[3]:


#Plotar gráficos


# In[4]:


import numpy as np
import matplotlib.pyplot as pl
x = np.linspace(0, 15, num = 2)
y = np.linspace(2, 17, num = 2)
z = np.linspace(0, 20, num = 2)
pl.plot(x)
pl.plot(y)

pl.title("Retas paralelas")
pl.show()
pl.title("Retas concorrentes")

pl.plot(y)
pl.plot(z)
pl.show()


# In[5]:


import numpy as np
import matplotlib.pyplot as pl
x = np.linspace(0, 15, num = 2)
y = np.linspace(2, 17, num = 2)
z = np.linspace(0, 20, num = 2)
pl.plot(x)
pl.plot(y)

pl.title("Retas paralelas")
pl.show()
pl.title("Retas concorrentes")

pl.plot(y)
pl.plot(z)
pl.show()


# In[6]:


#Converter decimal para binário


# In[7]:


# Precisão das casas decimais (em bits)
precisao = 8

def convert_d(d):
    if d == 1:
        return '1'
    if d == 0:
        return '0'
    else:
        return convert_d(int(d/2)) + str(d%2)

def convert_f(f, i):
    dobro = f * 2
    if dobro == 1.0:
        return '1'
    if i == precisao - 1:
        if dobro < 1.0:
            return '0'
        else:
            return '1'
    else:
        return str(int(dobro)) + convert_f(dobro - int(dobro), i+1)

def convert(num):
    inteiro = int(num)
    fracionario = num - inteiro
    return convert_d(inteiro) + '.' + convert_f(fracionario, 0)


entrada = float(input('Informe um número decimal: '))
print('Decimal: ', entrada)
print('Binário: ', convert(entrada))

