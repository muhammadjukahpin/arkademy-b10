import json
ariandy = {}
ariandy.update({'name':'Ariandy'})
ariandy.update({'address':'Pipit Raya Street, G5, 75119'})
ariandy.update({'hobbies':['Reading about Philosophy', 'Playing with a cat']})
ariandy.update({'is_married':False})

hs  = {'highSchool':'SMKN 7 Samarinda'}
uni = {'university':'STMIK Widya Cipta Dharma'}
ariandy.update({'school':[hs,uni]})

nameVal = ['Python', 'Arduino', 'Discrete Math']
scoreVal = ['6','6','6']

ariandy.update({'skills':[{'name':nameVal},{'score':scoreVal}]})

def return2json():
	py2json = json.dumps(ariandy)
	print(py2json)

return2json()