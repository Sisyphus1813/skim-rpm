# skim-rpm

This repository contains RPM packaging files for [the skim COPR](https://copr.fedorainfracloud.org/coprs/sisyphus1813/skim/) which hosts an unofficial package for skim-rs. 
[skim upstream repository](https://github.com/skim-rs/skim)

## Installation

```bash
sudo dnf copr enable sisyphus1813/skim
sudo dnf install -y skim
```
This installs the skim binary, it's man page, shell completions, and keybindings.
