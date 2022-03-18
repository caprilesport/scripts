# disks must be mounted beforehand

sudo apt update && sudo apt upgrade

sudo apt install tmux python3-venv python-dev python3-dev python3-pip python3-neovim ranger zathura zsh fzf hledger

mkdir /home/vinicip/Repos
mkdir /home/vinicip/software
rm -rf /home/vinicp/Documents
rm -rf /home/vinicp/Downloads
rm -rf /home/vinicp/Pictures

ln -s /mnt/media/Documents/ /home/vinicp/
ln -s /mnt/media/Cult /home/vinicp/
ln -s /mnt/media/Downloads /home/vinicp/
ln -s /mnt/media/Frances/ /home/vinicp/
ln -s /mnt/media/nutricao/ /home/vinicp/
ln -s /mnt/media/physics /home/vinicp/
ln -s /mnt/media/Pictures/ /home/vinicp/
ln -s /mnt/media/Programming/ /home/vinicp/

git clone https://github.com/caprilesport/scripts
git clone https://github.com/caprilesport/dotfiles /home/vinicp/Repos/dotfiles

curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

#github cli
sudo apt update
sudo apt install gh vim

#rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# julia 
curl -fsSL https://install.julialang.org | sh

#alacritty
sudo apt install cmake pkg-config libfreetype6-dev libfontconfig1-dev libxcb-xfixes0-dev libxkbcommon-dev python3
git clone https://github.com/alacritty/alacritty.git /home/vinicp/software
cd /home/vinicp/software/alacritty
cargo build --release
sudo tic -xe alacritty,alacritty-direct extra/alacritty.info
sudo cp target/release/alacritty /usr/local/bin # or anywhere else in $PATH
sudo cp extra/logo/alacritty-term.svg /usr/share/pixmaps/Alacritty.svg
sudo desktop-file-install extra/linux/Alacritty.desktop
sudo update-desktop-database
sudo mkdir -p /usr/local/share/man/man1
gzip -c extra/alacritty.man | sudo tee /usr/local/share/man/man1/alacritty.1.gz > /dev/null
gzip -c extra/alacritty-msg.man | sudo tee /usr/local/share/man/man1/alacritty-msg.1.gz > /dev/null


#zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

#npm and node 
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
nvm install node

#nvim
sudo add-apt-repository ppa:neovim-ppa/unstable
sudo apt update
sudo apt install neovim
cargo install --locked code-minimap
npm i -g bash-language-server

#tmux
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# lsd
cargo install lsd

