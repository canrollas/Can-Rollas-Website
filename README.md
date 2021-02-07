### Features

- Basic html bootstrap design and python flask usage
- 8 html pages
- 1 python main file
- Responsive bootstrap design
- Usage of javascript
- Connected with local database file with used structed query language
- Includes settings of Vscode

### Which types of algorithms/patterns used in this basic project
**Table of Contents**


## Get redirect post pattern

- Basic knowledge of internet protocol reqires get redirect post pattern to get rid of resubmit error
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/PostRedirectGet_DoubleSubmitSolution.png/350px-PostRedirectGet_DoubleSubmitSolution.png)

- Basically when back button pressed it can be annoying to resubmitting form.

## POST/GET patterns with python knowledge

- Basic knowledge of get/post form is applied with sql database language

```flow
st=>start:Mail registiration
op=>operation: GET method with http 200
cond=>condition: Successful Yes or No?
form=>operation:Data Input and POST request with protocol 3xx
controller=>condition:If data in database Yes or No?
redirect1=>end:Error you have already submitted
redirect2=>end:Congrats you submitted mail
crash=>Internet protocol error

st->op->cond
cond(yes)->form
form->controller
controller(yes)->redirect1
controller(no)->redirect2
cond(no)->crash

```



## 

