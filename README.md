# exd
Portable tool to dump any file to hex and retrieve file hex to original file. (Windows/Linux)

## Usage

**Linux** ;
```bash
chmod +x exd_x86-64_lin.elf

# Dump the hex from the original file
./exd_x86-64_lin.elf -f test.bin > test.hex

# Retrieve the file from hexdump
./exd_x86-64_lin.elf -d test.hex > executable.elf

# Or specify outputfile -o
./exd_x86-64_lin.elf -d test.hex -o executable.elf
```

Same for **Windows** with `exd_x86-64_win.exe`
