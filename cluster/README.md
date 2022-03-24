# Cluster scripts

This folder holds some of the scripts I wrote using our cluster in @geem-lab. 

## cinfo


## csync

This script uses rsync to synchorize data between a local folder and your user in the remote cluster. 

In order for you to use this script you've got to have your remote registered in your .ssh/config file (see https://linuxize.com/post/using-the-ssh-config-file/). 

A .remoteignore file is also supported (such as a .gitignore file) for ignoring files and/or extensions you dont want synced. 

Use it as follows:

```console
  
clustersync push/pull         #to copy files
clustersync push/pull sync    #to synchronize (be careful not to lose anything)
clustersync push/pull check   #to check differences
    
```

The sync options removes local/remote files that are not present in source directory. Be careful when using.
