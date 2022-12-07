import xml.etree.ElementTree as ET

def des(order, ll):
	i=0
	while order[1][1]<=ll[i][1][1]:
		i+=1
	ll.insert(i,order)

def asc(order, ll):
	i=0
	while order[1][1]>=ll[i][1][1]:
		i+=1
	ll.insert(i,order)

def bb(order, ll):
	while (order[1][0]>0) & (len(ll)>0) & (order[1][1]>=ll[0][1][1]):
		v1 = order[1][0]
		v2 = ll[0][1][0]
		if v1==v2:
			ll.pop(0)
			return None
		elif v1>v2:
			order[1][0] = v1-v2
			ll.pop(0)
		else:
			ll[0][1][0] = v2-v1
			return None
	return order

def ss(order, ll):
	while (order[1][0]>0) & (len(ll)>0) & (order[1][1]<=ll[0][1][1]):
		v1 = order[1][0]
		v2 = ll[0][1][0]
		if v1==v2:
			ll.pop(0)
			return None
		elif v1>v2:
			order[1][0] = v1-v2
			ll.pop(0)
		else:
			ll[0][1][0] = v2-v1
			return None
	return order

def buy(order,b,s):
	if b[0][1][1]>=order[1][1]:
		des(order,b)
	else:
		by = bb(order,s)
		if by!=None:
			b.insert(0,order)

def sell(order,b,s):
	if s[0][1][1]<=order[1][1]:
		asc(order,b)
	else:
		sy = ss(order,b)
		if sy!=None:
			s.insert(0,order)

def delete(n,b):
	for o in b[0]:
		if o[0]==n:
			b[0].remove(o)
			return None

	for o in b[1]:
		if o[0]==n:
			b[1].remove(o)
			return None

books = [[],[],[]]

tree = ET.parse('orders.xml')
root = tree.getroot()


for child in root:
	if child.tag=='AddOrder':
		oid = int(child.attrib['orderID'])
		bid = int(child.attrib['book'].split('-')[1])
		price = float(child.attrib['price'])
		volume = int(child.attrib['volume'])
		if child.attrib['operation']=="SELL":
			sell((oid,[volume,price]),books[bid][0],books[bid][1])
		elif child.attrib['operation']=="BUY":
			buy((oid,[volume,price]),books[bid][0],books[bid][1])

	elif child.tag=='DeleteOrder':
		oid = int(child.attrib['orderID'])
		n = int(child.attrib['book'].split('-')[1])
		delete(oid,books[n])
