import horovod.torch as hvd
hvd.init()
print('hello', hvd.rank(), hvd.size(), 'go')
