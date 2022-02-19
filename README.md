# xremap-my-eucalyn

Generate an xremap config with [xremap-python](https://github.com/xremap/xremap-python).

This config remaps the 109 keyboard to a customized Eucalyn layout.

## Install xremap

You need to install [xremap](https://github.com/k0kubun/xremap). If you are on Arch Linux and X11, you can install [xremap-x11-bin](https://aur.archlinux.org/packages/xremap-x11-bin) from AUR.

```bash
yay -S xremap-x11-bin
```

## Usage

Install xremap-python in the Python virtual environment using poetry.

```bash
poetry install
```

Generate an xremap config(`config.yml`).

```bash
make generate
```

Apply xremap config.

```bash
sudo xremap config.yml
```
