# Cluster scripts

This file holds some information regarding my workflow with the scripts 
I wrote to submit computational chemistry jobs in some supercomputers I use here [@geem-lab](https://github.com/geem-lab). 

If you want to use any of them just download/clone the repository and put the scripts in your $PATH.

## csync

**csync** uses rsync to synchorize data between a local folder and your user in the remote cluster. 

To use this I have an alias configured in .ssh/config, so I just use it directly in the script. 
To use this script you've got to have your remote locations inside the script, so after cloning the repo you should change it.

A .remoteignore file is also supported (such as a .gitignore file) for ignoring files and/or extensions you dont want synced. 

Use it as follows:

```console
  
csync push/pull         #to copy files
csync push/pull sync    #to synchronize (be careful not to lose anything)
csync push/pull check   #to check differences
    
```

Push and pull operations override files if they have the same name. Also, the sync options removes local/remote files that are not present in source directory. Be careful when using.

# qsub

**qsub** submits jobs in the cluster from your local computer. 
It pushes the current directory with **csync** and then submits the job. As it uses **csync**, be careful when running multiple jobs at the same folder.  

To use it I just specify the supercomputer I'm using and the job to run, e.g.:

```console

qsub gauss file.com
qsub jup   file.inp

```

Those remote locations are defined inside the script and in ~/.ssh/config

For each supercomputer there is a different routine to submit the job. 
For example, in the gauss cluster I need a .job file, so it is generated before syncing and submitting.

If you want to use this, first check your needs and adapt this script as needed.

## cinfo

**cinfo** prints some information about the cluster, for now we have available:

Temperature: ```cinfo -t```

Memory: ```cinfo -m```

Node information: ```cinfo -n job/free/busy```

For more help just do ```cinfo -h```

