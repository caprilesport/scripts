# Cluster scripts

This folder holds some of the scripts I wrote using our cluster in @geem-lab. 

If you want to use any of them just download/clone the repository and put the scripts in your $PATH.

## cinfo

Prints some information about the cluster, for now we have available:

Temperature: ```cinfo -t```

Memory: ```cinfo -m```

Node information: ```cinfo -n job/free/busy```

For more help just do ```cinfo -h```

## csync

This script uses rsync to synchorize data between a local folder and your user in the remote cluster. 

In order for you to use this script you've got to have your remote registered in your .ssh/config file (see https://linuxize.com/post/using-the-ssh-config-file/). 

A .remoteignore file is also supported (such as a .gitignore file) for ignoring files and/or extensions you dont want synced. 

Use it as follows:

```console
  
csync push/pull         #to copy files
csync push/pull sync    #to synchronize (be careful not to lose anything)
csync push/pull check   #to check differences
    
```

The sync options removes local/remote files that are not present in source directory. Be careful when using.
