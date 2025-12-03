# MCU Block Diagram Generator

A Python tool that generates clean, professional block diagrams for microcontroller (MCU) projects from simple JSON configuration files.

## Features

- 🎨 **PNG Output** - Generates high-quality PNG diagrams using Pillow
- 📦 **Simple Layout** - Vertical, centered design with board and peripheral boxes
- 🔗 **Visual Connections** - Lines connecting the main board to each peripheral
- ⚙️ **JSON Configuration** - Easy-to-edit configuration files
- 🖥️ **CLI Support** - Command-line interface for automation and scripting
- 🎨 **Color-Coded** - Board and peripherals use distinct colors for clarity

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ADITYABHURAN/MCU-Block-Diagram-Generator.git
cd MCU-Block-Diagram-Generator
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install required dependencies:
```bash
pip install Pillow
```

## Usage

### Basic Usage

Generate a diagram using the default configuration:

```bash
python diagram_generator.py --config config.json
```

### Custom Output

Specify a custom output filename:

```bash
python diagram_generator.py --config config.json --output my_diagram.png
```

### Configuration File Format

Create a JSON file with your board name and peripherals:

```json
{
  "board_name": "STM32F407 Discovery",
  "peripherals": [
    "GPIO - LEDs & Buttons",
    "USART2 - Serial Debug",
    "SPI1 - External Flash",
    "I2C1 - Accelerometer",
    "ADC1 - Analog Sensors",
    "TIM2 - PWM Output",
    "USB OTG - Full Speed"
  ]
}
```

## Example Output

The script generates a block diagram with:
- **Board box** at the top (steel blue)
- **Peripheral boxes** below (light green)
- **Connection lines** linking the board to each peripheral

See `diagram.png` for an example output.

## Command-Line Options

| Option | Default | Description |
|--------|---------|-------------|
| `--config` | `config.json` | Path to the JSON configuration file |
| `--output` | `diagram.png` | Path for the output PNG file |

## Examples

### Arduino Project
```json
{
  "board_name": "Arduino Uno",
  "peripherals": [
    "Digital Pins (D0-D13)",
    "Analog Pins (A0-A5)",
    "Serial (UART)",
    "SPI Interface",
    "I2C Interface",
    "PWM Outputs"
  ]
}
```

### Raspberry Pi Pico
```json
{
  "board_name": "Raspberry Pi Pico",
  "peripherals": [
    "GPIO (26 pins)",
    "UART0 & UART1",
    "SPI0 & SPI1",
    "I2C0 & I2C1",
    "ADC (3 channels)",
    "PWM (16 channels)",
    "USB 1.1"
  ]
}
```

## Requirements

- Python 3.7 or higher
- Pillow library

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Author

Created by Aditya Bhuran

## Acknowledgments

Built with [Pillow](https://python-pillow.org/) - The friendly PIL fork for image processing.
