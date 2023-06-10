import board
import busio
import e5

appkey = "your appkey"
appeui = "your appeiu"

# Set UART Pins

uart = busio.UART(board.GP4, board.GP5, baudrate=9600)
lora_module = e5.LoRaModule(uart)

lora_module.show_information()
lora_module.setup_and_join_otaa(appkey, appeui)

lora_module.send_hex("01234567")
