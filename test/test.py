import horovod.torch as hvd
hvd.init()
print('hello world', hvd.rank(), hvd.size(), 'go')
