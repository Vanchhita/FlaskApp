#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask


# In[1]:


from flask import Flask


# In[ ]:


app=Flask(__name__)#create flask object
@app.route('/')
def test():
    return "Test code working!!!!!!!"
@app.route('/next')
def next():
    return "Showing the next page"
if __name__=='__main__':
    app.run()


# In[ ]:




