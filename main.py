print('Welcome to supplyManage8 by MS9\nFor help go the README.')
initcmd = input('$$: ')
chain = []
products = []
destinations = []
shipping = []
nl = '\n'
while True:
  if initcmd == 'new':
    print('Creating New Chain.')
    newchain_temp = input('Name: ')
    chain.append(newchain_temp)
    products = []
    destinations = []
    shipping = []
    print(f'Chain {newchain_temp} was made.')
    initcmd = input('$$: ')
  elif initcmd == 'add':
    newproduct_temp = input('Name: ')
    newdestination_temp = input('Destination: ')
    newshipping_temp = input('Shipping Type: ')
    products.append(newproduct_temp)
    destinations.append(newdestination_temp)
    shipping.append(newshipping_temp)
    print(f'Product {newproduct_temp} was made.')
    initcmd = input('$$: ')
  elif initcmd == 'del':
    delproduct_t = input('What to del: ')
    try:
      index_temp = products.index(delproduct_t)
      products.pop(index_temp)
      destinations.pop(index_temp)
      shipping.pop(index_temp)
      print('Product Removed.')
      initcmd = input('$$: ')
    except:
      initcmd = input('$$: ')
  elif initcmd == 'find':
    findproduct_temp = input('Product: ')
    index_temp2 = products.index(findproduct_temp)
    print(products[index_temp2],nl, destinations[indextemp_2], nl,shipping[indextemp_2])
    initcmd = input('$$: ')
  elif initcmd == 're':
    reproduct_temp = input('Product: ')
    index3 = products.index(reproduct_temp)
    re1 = input('New Name: ')
    re2 = input('New Destination: ')
    re3 = input('New Shipping: ')
    products[index3] = re1
    destinations[index3] = re2
    shipping[index3] = re2
    print("Product Updated")
    initcmd = input('$$: ')
  elif initcmd == 'massdel':
    break
  elif initcmd == 'export':
    print('Exporting Chain Into A Data File.')
    textfile = open("data.txt", "w")
    for element in products, destinations, shipping:
      textfile.write(str(element) + '\n')
    textfile.close()
    print(Fore.GREEN + 'Done.')
    initcmd = input("$$: ")
  elif initcmd == 'import':
    try:
      with open('data.txt', 'r') as filetype:
        datax = filetype.read()
        initcmd = input(Fore.RED + "$$: ")      
    except FileNotFoundError:
      print("No exported data file found.")
      g = False
      initcmd = input(Fore.RED + "$$: ")