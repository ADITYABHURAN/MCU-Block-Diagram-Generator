#!/usr/bin/env python3
"""
MCU Block Diagram Generator
Generates a simple PNG block diagram from a JSON configuration file.
"""

import json
import argparse
from PIL import Image, ImageDraw, ImageFont


class DiagramGenerator:
    def __init__(self, config_path):
        """Initialize the diagram generator with a config file."""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        # Diagram styling parameters
        self.img_width = 800
        self.img_height = 600
        self.bg_color = (255, 255, 255)
        self.box_color = (70, 130, 180)  # Steel blue
        self.peripheral_color = (100, 180, 100)  # Light green
        self.text_color = (255, 255, 255)
        self.line_color = (50, 50, 50)
        self.line_width = 2
        
        # Box dimensions
        self.board_box_width = 300
        self.board_box_height = 80
        self.peripheral_box_width = 200
        self.peripheral_box_height = 60
        
        # Spacing
        self.vertical_spacing = 100
        self.peripheral_spacing = 80
        
    def _get_font(self, size):
        """Get font for text rendering."""
        try:
            # Try to use a nice font
            return ImageFont.truetype("arial.ttf", size)
        except:
            # Fallback to default font
            return ImageFont.load_default()
    
    def _draw_box(self, draw, x, y, width, height, color, text):
        """Draw a box with centered text."""
        # Draw rectangle
        draw.rectangle(
            [(x, y), (x + width, y + height)],
            fill=color,
            outline=self.line_color,
            width=2
        )
        
        # Draw text
        font = self._get_font(16)
        
        # Get text bounding box for centering
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        text_x = x + (width - text_width) // 2
        text_y = y + (height - text_height) // 2
        
        draw.text((text_x, text_y), text, fill=self.text_color, font=font)
    
    def _draw_line(self, draw, x1, y1, x2, y2):
        """Draw a connecting line."""
        draw.line([(x1, y1), (x2, y2)], fill=self.line_color, width=self.line_width)
    
    def generate(self, output_path="diagram.png"):
        """Generate the block diagram."""
        board_name = self.config.get("board_name", "MCU Board")
        peripherals = self.config.get("peripherals", [])
        
        # Calculate required height based on number of peripherals
        total_peripheral_height = len(peripherals) * self.peripheral_box_height + \
                                  (len(peripherals) - 1) * (self.peripheral_spacing - self.peripheral_box_height)
        
        required_height = self.board_box_height + self.vertical_spacing + total_peripheral_height + 100
        self.img_height = max(self.img_height, required_height)
        
        # Create image
        img = Image.new('RGB', (self.img_width, self.img_height), self.bg_color)
        draw = ImageDraw.Draw(img)
        
        # Draw board box (centered at top)
        board_x = (self.img_width - self.board_box_width) // 2
        board_y = 50
        self._draw_box(
            draw,
            board_x,
            board_y,
            self.board_box_width,
            self.board_box_height,
            self.box_color,
            board_name
        )
        
        # Calculate board center point for connections
        board_center_x = board_x + self.board_box_width // 2
        board_bottom_y = board_y + self.board_box_height
        
        # Draw peripheral boxes
        peripheral_start_y = board_y + self.board_box_height + self.vertical_spacing
        
        for i, peripheral in enumerate(peripherals):
            peripheral_x = (self.img_width - self.peripheral_box_width) // 2
            peripheral_y = peripheral_start_y + i * self.peripheral_spacing
            
            # Draw peripheral box
            self._draw_box(
                draw,
                peripheral_x,
                peripheral_y,
                self.peripheral_box_width,
                self.peripheral_box_height,
                self.peripheral_color,
                peripheral
            )
            
            # Draw connecting line from board to peripheral
            peripheral_center_x = peripheral_x + self.peripheral_box_width // 2
            peripheral_top_y = peripheral_y
            
            self._draw_line(
                draw,
                board_center_x,
                board_bottom_y,
                peripheral_center_x,
                peripheral_top_y
            )
        
        # Save the image
        img.save(output_path)
        print(f"✓ Diagram generated successfully: {output_path}")
        print(f"  Board: {board_name}")
        print(f"  Peripherals: {len(peripherals)}")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Generate MCU block diagrams from JSON configuration"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.json",
        help="Path to the JSON configuration file (default: config.json)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="diagram.png",
        help="Path for the output PNG file (default: diagram.png)"
    )
    
    args = parser.parse_args()
    
    try:
        generator = DiagramGenerator(args.config)
        generator.generate(args.output)
    except FileNotFoundError:
        print(f"✗ Error: Config file '{args.config}' not found")
        return 1
    except json.JSONDecodeError:
        print(f"✗ Error: Invalid JSON in config file '{args.config}'")
        return 1
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
