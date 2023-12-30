# Scripts

Collection of my scripts.

## Installation

If you want to use these scripts, remember to adapt them for your own needs as some are refined to my configurations. 

To install simply clone the repository and move theses scripts to somewhere in your $PATH, e.g.:

```console

git clone https://github.com/caprilesport/scripts 
mv scripts ~                                            # Location to move the folder, I use it in ~
echo 'export PATH=$PATH:$HOME/scripts' >> ~/.bashrc     # Or ~/.zshrc if you use zsh

```

Most scripts are self describing. `csync` and `qsub` deserve a little more atention.

`gdrive` is used to synchronize files with google drive, the [original](https://github.com/lmiq/tips/blob/master/GoogleDrive/gdrive) was made by [Prof. Leandro Martinez](https://github.com/lmiq).

Inspired by it I wrote [`csync`](./cluster/csync), which syncs files with remote servers. 

## `csync`

`csync` uses rsync to synchorize data between a local folder and a remote one. 

To use this, the remote servers are entered inside the script itself. You can use aliases defined in .ssh/config.
If you dont, just take care with flags to specify ports and etc.

A .remoteignore file is also supported (such as a .gitignore file) for ignoring files and/or extensions you dont want synced, the script
searches for it inside your current directory.

Use it as follows:

```console
  
csync push/pull         #to copy files
csync push/pull sync    #to synchronize (be careful not to lose anything)
csync push/pull check   #to check differences
    
```

Push and pull operations override files if they have the same name. Also, the sync options removes local/remote files that are not present in source directory. Be careful when using.

## `qsub`

`qsub` submits jobs in a remote location from your local computer. 
It pushes the current directory with `csync` and then submits the job. As it uses `csync`, be careful when running multiple jobs at the same folder.  

Use it as follows (using aliased servers in ~/.ssh/config):

```console
qsub gauss file.com
qsub jup   file.inp
```

For each server there is a different routine to submit a job. Right now they are hardcoded inside the scripts, change 
them to suit your needs.

## License

```
MIT License

Copyright (c) 2023 Vinicius Capriles Port <caprilesport@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

