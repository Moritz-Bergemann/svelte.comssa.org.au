# `svelte.comssa.org.au`
A redesign of the ComSSA website in Svelte with usability improvements!

## Environment Setup
This guide will assume you are using a Linux environment. If on Windows, we recommend [WSL](https://learn.microsoft.com/en-us/windows/wsl/install). If you'd like to stick to windows, most of the below will work though you'll need to explore some [alternatives](https://github.com/coreybutler/nvm-windows).

First, install [NPM](https://www.npmjs.com/) LTS, preferably via [NVM](https://github.com/nvm-sh/nvm). Skip this step if you already have the correct NPM version setup!

```bash
# First, install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# Refresh your bash to activate it (or restart your terminal)
source ~/.bashrc

# Install and activate LTS version of NPM 
nvm install --lts
nvm use --lts
```

Then, clone the repository and install all dependencies to build/run the app locally.
```bash
git clone $THE_URL_OF_THE_REPOSITORY

# Navigate to the repository root folder.

npm install
```

You can now run a development server!

```bash
npm run dev
```