# Scripts

Collection of my scripts.

gdrive is used to synchronize files with google drive the [original](https://github.com/lmiq/tips/blob/master/GoogleDrive/gdrive)) was made by [Prof. Leandro Martinez](https://github.com/lmiq), I just copied it.

The [csync](./cluster/csync) script is heavily inspired by it. For instructions on how to use click [here](./CLUSTER.md). 

I have some scripts I use to work on remote clusters (while keeping everything in my local machine). To see a more detailed description of how I use these please check out the [CLUSTER.md](./CLUSTER.md) file. 

## Installation

If you want to use these scripts, remember to adapt them for your own needs as some are refined to my configurations. 

To install simply clone the repository and move theses scripts to somewhere in your $PATH, e.g.:

```console

git clone https://github.com/caprilesport/scripts 
mv scripts ~                                            # Location to move the folder, I use it in ~
echo 'export PATH=$PATH:$HOME/scripts' >> ~/.bashrc     # Or ~/.zshrc if you use zsh

```
