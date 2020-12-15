# How to add bin/ directory to the system PATH variable?

```bash
echo 'export PATH="'$(pwd)':$PATH"' >> <shell-configuration-file>
```

Notes
- You MUST replace the `<shell-configuration-file>` with the shell configuration file specific for your computer. For Mac users, the default path to the shell configuration file is ~/.zshrc (for Z Shell, aka zsh.)
- `$(pwd)` prints the absolute directory path of the bin/ directory. Feel free to replace `'$(pwd)'` with your desired path for the bin/ directory.
