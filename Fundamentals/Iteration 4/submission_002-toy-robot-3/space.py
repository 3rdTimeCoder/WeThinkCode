def h(item, **kwargs):
    print('first item:', item)
    if kwargs['juice']:
        print(kwargs['juice'])
        
h('item 1', juice='testing juices...')